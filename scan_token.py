#!/usr/bin/env python3
"""
DexMultichain Token Scanner v1.0
Screens Solana tokens via Helius RPC + DexScreener API
Outputs: price, liquidity, holders, volume, risk score, signals
Usage: python3 scan_token.py <contract_address>
"""

import sys
import json
import time
import urllib.request
import urllib.error
import os

# ── CONFIG ──
HELIUS_API_KEY = os.environ.get("HELIUS_API_KEY", "")
HELIUS_RPC = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"
DEXSCREENER_API = "https://api.dexscreener.com/latest"
SOL_MINT = "So11111111111111111111111111111111111111112"

# ── HELPERS ──
def rpc_call(payload: dict) -> dict:
    """Make a Helius RPC call."""
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        HELIUS_RPC,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}

def http_get(url: str, timeout=15) -> dict:
    """Make an HTTP GET request."""
    req = urllib.request.Request(url, headers={"User-Agent": "DxM-Scanner/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}

def format_price(price: float) -> str:
    if price >= 1: return f"${price:.2f}"
    if price >= 0.0001: return f"${price:.6f}"
    return f"${price:.10f}"

def format_num(n: float) -> str:
    if n >= 1e9: return f"${n/1e9:.2f}B"
    if n >= 1e6: return f"${n/1e6:.2f}M"
    if n >= 1e3: return f"${n/1e3:.1f}K"
    if n >= 1: return f"${n:.2f}"
    return f"${n:.8f}"

# ── FETCH METADATA (Helius DAS API) ──
def fetch_token_metadata(mint: str) -> dict:
    """Fetch token metadata via Helius DAS API."""
    # Try getTokenSupply first
    supply_resp = rpc_call({
        "jsonrpc": "2.0", "id": 1, "method": "getTokenSupply",
        "params": [mint]
    })

    # Try getAsset for metadata
    asset_resp = rpc_call({
        "jsonrpc": "2.0", "id": 2, "method": "getAsset",
        "params": {"id": mint}
    })

    # Try getAccountInfo
    account_resp = rpc_call({
        "jsonrpc": "2.0", "id": 3, "method": "getAccountInfo",
        "params": [mint, {"encoding": "jsonParsed"}]
    })

    return {
        "supply": supply_resp,
        "asset": asset_resp,
        "account": account_resp,
    }

# ── FETCH DEX SCREENER ──
def fetch_dexscreener(mint: str) -> dict:
    """Fetch token data from DexScreener."""
    # Try multiple endpoints
    endpoints = [
        f"https://api.dexscreener.com/latest/dex/tokens/{mint}",
        f"https://api.dexscreener.com/latest/dex/search?q={mint}",
    ]
    for url in endpoints:
        data = http_get(url)
        if "error" not in data and data.get("pairs"):
            return data
    return {"pairs": []}

# ── RISK ANALYSIS ──
def analyze_risk(metadata: dict, dexscreener: dict) -> dict:
    """Analyze token risk based on on-chain data."""
    score = 50  # Start at neutral
    signals = []
    details = {}

    pairs = dexscreener.get("pairs", [])
    pair = pairs[0] if pairs else {}

    # Price & liquidity data
    liquidity_usd = pair.get("liquidity", {}).get("usd", 0) if pair else 0
    volume_24h = pair.get("volume", {}).get("h24", 0) if pair else 0
    price_usd = 0
    if pair and pair.get("priceUsd"):
        try:
            price_usd = float(pair["priceUsd"])
        except (ValueError, TypeError):
            price_usd = 0

    # Market cap
    mcap = pair.get("fdv", pair.get("marketCap", 0)) if pair else 0

    # Liquidity analysis
    if liquidity_usd >= 100_000:
        score += 15; signals.append({"type": "good", "text": "✓ Strong liquidity"})
    elif liquidity_usd >= 10_000:
        score += 5; signals.append({"type": "info", "text": "ℹ Moderate liquidity"})
    elif liquidity_usd > 0:
        score -= 10; signals.append({"type": "warn", "text": "⚠ Low liquidity"})
    else:
        score -= 20; signals.append({"type": "bad", "text": "✗ No liquidity found"})

    # Volume analysis
    if volume_24h >= 1_000_000:
        score += 10; signals.append({"type": "good", "text": "✓ High volume 24h"})
    elif volume_24h >= 100_000:
        score += 5
    elif volume_24h > 0:
        pass  # Neutral
    else:
        score -= 5; signals.append({"type": "warn", "text": "⚠ No volume 24h"})

    # Market cap analysis
    if mcap > 0:
        if mcap >= 1_000_000:
            score += 5
        elif mcap <= 10_000:
            score -= 5; signals.append({"type": "warn", "text": "⚠ Very low mcap — high risk"})

    # Check for freeze/mint authority from metadata
    for key in ["supply", "asset"]:
        d = metadata.get(key, {})
        if d.get("result", {}).get("data", {}).get("mintAuthority"):
            score -= 15; signals.append({"type": "bad", "text": "✗ Mint authority active — can print tokens"})
        if d.get("result", {}).get("data", {}).get("freezeAuthority"):
            score -= 10; signals.append({"type": "bad", "text": "✗ Freeze authority active"})

    # Check DexScreener info
    info = pair.get("info", {}) if pair else {}
    if info.get("imageUrl"):
        signals.append({"type": "info", "text": "ℹ Has socials/token image"})

    # Boost for "boost" or "pump" tags
    labels = pair.get("labels", []) if pair else []
    if "pump" in labels:
        signals.append({"type": "info", "text": "ℹ pump.fun token"})
    if "raydium" in labels:
        score += 5; signals.append({"type": "good", "text": "✓ Listed on Raydium"})

    # Cap score
    score = max(0, min(100, score))

    # Risk level
    if score >= 75: risk_level = "LOW"
    elif score >= 50: risk_level = "MEDIUM"
    elif score >= 25: risk_level = "HIGH"
    else: risk_level = "EXTREME"

    return {
        "score": score,
        "risk_level": risk_level,
        "signals": signals,
        "liquidity_usd": liquidity_usd,
        "volume_24h": volume_24h,
        "price_usd": price_usd,
        "mcap": mcap,
        "pair_count": len(pairs),
        "dex": pair.get("dexId", "unknown") if pair else "unknown",
        "pair_address": pair.get("pairAddress", "") if pair else "",
        "token_name": pair.get("baseToken", {}).get("name", "Unknown") if pair else "Unknown",
        "token_symbol": pair.get("baseToken", {}).get("symbol", "???") if pair else "???",
        "created_at": pair.get("pairCreatedAt", 0) if pair else 0,
    }

# ── MAIN SCANNER ──
def scan_token(mint: str) -> dict:
    """Full token scan — metadata + market + risk."""
    start = time.time()

    print(f"🔍 Scanning: {mint[:8]}...{mint[-8:]}")
    print("⏳ Fetching on-chain data...", end="", flush=True)

    metadata = fetch_token_metadata(mint)
    print(" ✅", end="", flush=True)

    print(" Fetching market data...", end="", flush=True)
    dexscreener = fetch_dexscreener(mint)
    print(" ✅", end="", flush=True)

    print(" Analyzing risk...", end="", flush=True)
    risk = analyze_risk(metadata, dexscreener)
    print(" ✅")

    elapsed = time.time() - start

    result = {
        "mint": mint,
        "scan_time_seconds": round(elapsed, 2),
        "timestamp": int(time.time()),
        "token": {
            "name": risk["token_name"],
            "symbol": risk["token_symbol"],
            "dex": risk["dex"],
        },
        "market": {
            "price_usd": risk["price_usd"],
            "price_formatted": format_price(risk["price_usd"]),
            "liquidity_usd": risk["liquidity_usd"],
            "liquidity_formatted": format_num(risk["liquidity_usd"]),
            "volume_24h": risk["volume_24h"],
            "volume_formatted": format_num(risk["volume_24h"]),
            "mcap": risk["mcap"],
            "mcap_formatted": format_num(risk["mcap"]),
            "pair_count": risk["pair_count"],
            "pair_address": risk["pair_address"],
        },
        "risk": {
            "score": risk["score"],
            "level": risk["risk_level"],
            "signals": risk["signals"],
        },
    }

    return result

# ── CLI ──
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scan_token.py <contract_address>")
        print("Example: python3 scan_token.py So11111111111111111111111111111111111111112")
        sys.exit(1)

    mint = sys.argv[1].strip()
    if len(mint) < 30:
        print("❌ Invalid Solana address (too short)")
        sys.exit(1)

    if not HELIUS_API_KEY:
        print("❌ HELIUS_API_KEY not set in ~/.hermes/.env")
        sys.exit(1)

    result = scan_token(mint)

    print("\n" + "="*50)
    print(f"  ◈ {result['token']['symbol']} — {result['token']['name']}")
    print(f"  DEX: {result['token']['dex'].upper()}")
    print("="*50)

    m = result["market"]
    print(f"  Price:     {m['price_formatted']}")
    print(f"  Liq:       {m['liquidity_formatted']}")
    print(f"  MCap:      {m['mcap_formatted']}")
    print(f"  Vol 24h:   {m['volume_formatted']}")
    print(f"  Pairs:     {m['pair_count']}")

    r = result["risk"]
    risk_emoji = {"LOW": "🟢", "MEDIUM": "🟡", "HIGH": "🟠", "EXTREME": "🔴"}
    print(f"\n  Risk Score: {r['score']}/100 {risk_emoji.get(r['level'], '')} {r['level']}")

    print(f"\n  Signals:")
    for s in r["signals"]:
        emoji = {"good": "✅", "warn": "⚠️", "bad": "❌", "info": "ℹ️"}.get(s["type"], "•")
        print(f"    {emoji} {s['text']}")

    print(f"\n  ⏱️  Scan time: {result['scan_time_seconds']}s")
    print("="*50)

    # Also output JSON for piping
    print("\n--- JSON OUTPUT ---")
    print(json.dumps(result, indent=2))
