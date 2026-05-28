# 🚀 QUICK START — Skill Microcap Trade

**First time? Start here.** (5 minutes)

---

## **Step 1: Understand What This Is**

This framework is a **manual trading system** for Solana microcap tokens on PumpFun.  
You provide a **chart screenshot** → AI applies rules → You get an **entry/exit signal**.

**NOT automated.** You execute trades manually.

---

## **Step 2: Get Your Tools Ready**

Have these open when trading:
- **Padre** (Photon) — chart + on-chain data
- **GMGN** — holder analysis
- **ChatGPT** / **Claude** / **Gemini** — paste framework + screenshot
- **Screenshot tool** — Snip, Print Screen, etc.

---

## **Step 3: The Three Scan Types**

### **FULL SCAN** (Default, 3–5 min)
Best for: New token analysis, detailed review  
Command: Just paste screenshot, or say "full scan [TOKEN]"  
Output: Complete verdict, all indicators, Forward Projection

### **QUICK SCAN** (30 sec)
Best for: Fast decision, entry window closing  
Command: "quick scan [TOKEN]"  
Output: Kill Filter check + Triple Lock status + Final Call only

### **MOMENTUM SCAN** (2 min)
Best for: Fresh breakout, volume spike, token < 45m  
Trigger: Auto-detect OR command "momentum scan [TOKEN]"  
Output: Early entry allowed, aggressive sizing

---

## **Step 4: Prepare Your Screenshot**

Make sure visible:
```
✅ Chart (1m or 5m timeframe)
✅ Padre panel (MCap, Liq, Insiders%, Dev%)
✅ Bonding Curve %
✅ Indicators (RSI, MFI, EMA, VWAP visible)
✅ Volume bars + SMA overlay
```

**Don't show**: Private keys, sensitive URLs

---

## **Step 5: Run Your First Scan**

### **Example Prompt for Claude/ChatGPT:**

```
Use the framework in this document: [paste MASTER.md or bagus_v7.md]

FULL SCAN for this Solana token:
[paste screenshot]

Provide: verdict, entry zone, TP levels, SL, confidence, Forward Projection
```

---

## **Step 6: Read the Output**

You'll get back 6 sections:

| Section | What to Look For |
|---------|------------------|
| **Verdict** | 🟢 GREEN (execute) / 🟡 YELLOW (wait) / 🔴 RED (abort) |
| **Entry Zone** | Price range to enter (from Fib 0.618 usually) |
| **TP1 / TP2 / TP3** | Profit targets (when to take partial/full profit) |
| **SL** | Stop-loss level (where you admit you're wrong) |
| **Confidence** | % certainty (higher = better edge) |
| **Forward Projection** | What happens next (Bull/Bear/Trap scenarios) |

---

## **Step 7: Decision Framework**

```
IF Verdict = 🟢 GREEN
  → Size: Check Confidence score
  → Confidence >= 85% → FULL size
  → Confidence 70–84% → 80% size
  → Confidence < 70% → CAUTION (70% size, TP1 only)

IF Verdict = 🟡 YELLOW
  → WAIT minimum
  → Re-check at next candle or price milestone
  → Don't force entry

IF Verdict = 🔴 RED
  → ABORT (or watchlist for re-entry later)
  → Do not trade this token
```

---

## **Step 8: Position Sizing (Half-Kelly)**

Once you get an entry signal:

```
Formula: f* = (Win% × RR − Loss%) / RR × 0.5

Example:
  - Confidence 70% = ~70% win probability
  - R:R = 1:2 (risk 1, make 2)
  - f* = (0.70 × 2 − 0.30) / 2 × 0.5 = 13.75% → cap to 10% (BALANCED)

Position Size:
  - AGGRESSIVE mode: cap 20%, multiplier 1.2×
  - BALANCED mode: cap 10%, multiplier 1.0×
  - DEFENSIVE mode: cap 5%, multiplier 0.6×

Floor rule: f* < 3% → NO TRADE
```

---

## **Step 9: Manage Your Trade**

### **Entry**
1. Set SL at framework-defined level
2. Set TP1 as first exit
3. Enter sized position

### **During Trade**
1. Monitor: If MFI > 80 + BC > 90% → EXIT NOW
2. Check: Every 5 candles (don't obsess)
3. Watch: Dev wallet movements, fresh wallet changes

### **Exit**
- Hit TP1 → Take 30–50%
- Hit TP2 → Take another 30–50%
- Hit TP3 (if aggressive) → Take final 20%
- SL hit → Full exit (this is planned loss)

---

## **Step 10: Common Mistakes (Avoid These)**

| Mistake | What Happens | Fix |
|---------|--------------|-----|
| Entry without SL | Unlimited loss | Framework requires SL always |
| R:R < 1:2 | Bad odds | Reject trade if R:R not met |
| Ignore RED verdict | Lost trade | Trust Kill Filter (F1–F7b) |
| FOMO after +50% | Chase = rug | Use DEW (Dynamic Entry Window) — don't chase |
| No position sizing | Overleveraged | Use Half-Kelly formula |
| Deviate from rules | Emotional bias | Framework = discipline |

---

## **Step 11: Paper Trade First**

**Before real money:**
1. Do 10 FULL SCANs with fake entries
2. Log results in spreadsheet
3. Track: Entry price, TP1, TP2, SL, actual outcome
4. Calculate: Win %, average R:R, profitability
5. Goal: >= 60% win rate before going live

**Paper trading template:**
```
Trade #1: TOKEN_X | Entry $0.050 | TP1 $0.065 | SL $0.040 | Win/Loss
Trade #2: TOKEN_Y | Entry $0.032 | TP1 $0.042 | SL $0.025 | Win/Loss
...
Stats: X/10 wins | Avg R:R | Profit factor
```

---

## **Step 12: Framework Hierarchy (When Confused)**

```
1. Kill Filter (F1–F7b)    → If triggered = RED, STOP
2. Anti-Rugi Checkpoint   → Must pass 5 gates
3. Pre-Entry Defense      → If triggered = cap YELLOW
4. Confidence Score       → >= 70% is GREEN
5. Exit Signal (PL-14)    → Override everything
```

Rule: **Earlier rule always beats later rule.**

---

## **Step 13: Key Terminology**

| Term | Meaning |
|------|---------|
| **Kill Filter** | 9 red flags (DEV RUG, bundle concentration, etc.) |
| **Triple Lock** | 3 entry confirmations (Fib + VWAP + Volume sweep) |
| **Confidence** | % probability setup works (70% = GREEN) |
| **DEW** | Time window to enter (expires as token age increases) |
| **BC** | Bonding Curve % (90%+ = LETHAL = exit) |
| **R:R** | Risk:Reward ratio (must be >= 1:2) |
| **TP** | Take Profit (where you close winners) |
| **SL** | Stop Loss (where you cut losers) |
| **VWAP** | Volume-weighted price (fair value marker) |
| **Fib** | Fibonacci retracement levels (0.618 golden ratio) |

---

## **Step 14: Red Flags to Know**

See these = ABORT:
- 🚨 Insiders + Bundles > 30%
- 🚨 Dev holding = 0% + MCap rising 20%+
- 🚨 Fresh wallets > 30% (coordinated control)
- 🚨 Pump > 300% in < 30 min
- 🚨 LP Unlocked (unless token < 1h old)
- 🚨 Zero social activity but MCap up 500%

---

## **Next Steps**

1. ✅ Read [MASTER.md](../MASTER.md) (80 min full, 10 min skim)
2. ✅ Practice: Run 3 QUICK SCANs on random tokens
3. ✅ Paper trade: 10 full scans with fake entries
4. ✅ Track: Win rate, R:R, profit factor
5. ✅ Go live: Only after >= 60% win rate confirmed

---

## **Need Help?**

- Framework questions → [GitHub Discussions](https://github.com/allinoneacount1-dot/skill-microcap-trade-/discussions)
- Bug/edge case → [Create Issue](https://github.com/allinoneacount1-dot/skill-microcap-trade-/issues)
- Prompt examples → See `/examples` directory

---

**Version**: V8.5 REV.4  
**Last Updated**: May 24, 2026  
**Difficulty**: Intermediate (assumes basic trading knowledge)
