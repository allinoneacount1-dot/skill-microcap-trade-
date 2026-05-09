# Skill Microcap Trade

Advanced Solana PumpFun microcap trading framework focused on detecting high-probability entry points using AI-assisted analysis and technical confluence. only use SCREENSHOT CHART

Designed for:
- ChatGPT
- Claude
- Gemini
- Grok

Compatible with:
- Padre
- GMGN

---

# Objective

Detect:
- Strong entries
- Momentum continuation
- Smart money positioning
- Volume expansion
- Healthy breakout structures
- Risk-efficient trade opportunities

Avoid:
- Fake breakouts
- Exit liquidity traps
- Dev manipulation
- Weak volume setups
- Overextended pumps

---

# Core Philosophy

Microcap trading is probability-based.

The goal is not predicting tops or bottoms.

The goal is identifying:
- High-quality setups
- Strong momentum shifts
- Controlled risk entries
- Favorable risk/reward environments

---

# Main Indicators

## RSI
Relative Strength Index used for:
- Momentum detection
- Reversal signals
- Divergence analysis
- Overbought/oversold conditions

Preferred:
- Recovery from 35–50 range
- Bullish divergence
- Healthy mid-range expansion

Avoid:
- Extreme overheated entries

---

## MFI
Money Flow Index used for:
- Detecting capital inflow
- Accumulation confirmation
- Momentum validation

Preferred:
- Rising MFI with rising volume
- Stable inflow structure

Avoid:
- Sudden inflow collapse

---

## EMA Cross
EMA structure used for:
- Trend confirmation
- Momentum continuation
- Market direction

Preferred:
- Fast EMA crossing above Slow EMA
- Price holding above EMA cluster
- Strong continuation after cross

Avoid:
- Weak sideways movement
- Delayed entries after extension

---

## VPVR
Volume Profile Visible Range used for:
- Support/resistance zones
- Volume acceptance areas
- High-volume nodes

Preferred:
- Price holding major volume node
- Breakout into low-resistance area
- Strong acceptance above value area

Avoid:
- Thin liquidity regions

---

## VWAP
Volume Weighted Average Price used for:
- Fair value positioning
- Momentum confirmation
- Trend validation

Preferred:
- VWAP reclaim
- Successful retest
- Sustained hold above VWAP

Avoid:
- Failed reclaim attempts

---

## Volume SMA
Volume Simple Moving Average used for:
- Detecting abnormal activity
- Momentum confirmation
- Breakout validation

Preferred:
- Volume expansion above average
- Consecutive buy pressure candles

Avoid:
- Single manipulated spikes

---

# Entry Logic

High-quality entries usually include:
- Volume expansion
- VWAP reclaim
- EMA bullish structure
- Rising MFI
- Healthy RSI
- VPVR support hold
- Stable buy pressure

The more confluence present:
- The stronger the setup quality

---

# Aggressive Entry Model

Used for:
- Early breakout capture
- Fast momentum entries

Requirements:
- Fresh volume expansion
- EMA cross confirmation
- VWAP reclaim
- Strong buying pressure

Risks:
- Higher volatility
- Increased fakeout probability

---

# Conservative Entry Model

Used for:
- Safer confirmation entries
- Reduced fakeout exposure

Requirements:
- Retest confirmation
- Stable VWAP hold
- Sustained volume growth
- RSI + MFI alignment

Advantages:
- Higher confirmation quality
- Better structure validation

---

# Trade Quality Checklist

Checklist before entering:
- Volume increasing
- Buyers dominant
- VWAP reclaimed
- EMA structure bullish
- RSI healthy
- MFI rising
- VPVR support confirmed
- Liquidity acceptable
- No obvious manipulation

If multiple conditions fail:
- Skip the trade

---

# Risk Management

Never:
- Full-port one trade
- Chase vertical candles
- Ignore invalidation levels
- Trade emotionally

Always:
- Use stop-loss logic
- Scale positions properly
- Secure partial profits
- Respect risk exposure

---

# AI Workflow

Use AI to:
- Analyze momentum
- Detect manipulation
- Evaluate setup quality
- Assess continuation probability
- Identify risk factors

Recommended workflow:
1. Open chart
2. Check volume
3. Analyze VWAP
4. Validate EMA structure
5. Confirm RSI/MFI
6. Review VPVR zones
7. Assess narrative strength
8. Determine entry quality

---

# Example AI Prompt

```txt
Analyze this Solana PumpFun token chart for entry quality:

CHART: [SCREENSHOT]

Check for:
1. Volume expansion above SMA
2. VWAP reclaim with hold
3. EMA bullish structure
4. RSI healthy range (35-70)
5. MFI rising with volume
6. VPVR support confirmation
7. Smart money accumulation signs

Is this a quality entry? Rate 1-10 and explain risks.
```
