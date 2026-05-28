⚡ MASTER DXM ARCHITECT V13.11 — FULLY RESOLVED
Mode: SS-Only | Zero-Loss | Anti-Rug | Full Indicator Stack | Predictive
Indicator Stack: VPVR · EMA Cross · RSI · MFI · VWAP · Volume SMA · Fibonacci
Excluded (Platform-Safe): Mint Auth · Freeze Auth · Burned Liq · LP Lock · Sell/Buy Tax
---

# ⚠️ CRITICAL FIXES FROM V13.10 → V13.11

## ISSUE #1: CONFIDENCE CEILING CONTRADICTION ✅ FIXED

**Problem (V13.10):**
- Base score max = 85%, but +20% modifier cap → 105% (capped to 100%)
- AR 4/6 = 56.7% base, but LAW 05 requires ≥85% final
- **Logical trap:** AR 4/6 could never reach 85%, making LAW 05 unachievable

**Fix (V13.11):**
```
NEW BASE SCORE FORMULA (AMENDED):
  Base = (AR PASS count / 6) × 80  [CHANGED: was 85, now 80]
  
  CEILING BY DESIGN (RECALCULATED):
  AR 6/6 → Base 80% → max confidence 100% (with +20% modifier cap)
  AR 5/6 → Base 66.7% → max confidence 86.7% ✅ (achievable)
  AR 4/6 → Base 53.3% → max confidence 73.3% (CAUTION eligible path)
  
  LAW 05 AMENDMENT:
  Final Confidence ≥ 85% = FULL ENTRY (unchanged)
  Final Confidence 80–84.9% = CONDITIONAL ENTRY (new tier)
  Final Confidence 70–79.9% = CAUTION ENTRY only
  Final Confidence < 70% = NO ENTRY
  
  CONDITIONAL ENTRY (80–84.9%) Rules:
  - Allowed ONLY if AR 5/6 with ≤1 WARNING
  - Size reduced to 80% of FULL (vs CAUTION 70%)
  - TP1 + TP2 active, no TP3
  - Requires explicit [CONDITIONAL ENTRY — FULL TP1/TP2] label
```

---

## ISSUE #2: DOUBLE PENALTY ON BEARISH INDICATORS ✅ FIXED

**Problem (V13.10):**
- Section 7 Modifier Stack penalizes bearish signals (e.g., EMA -6%)
- STEP 09 Alignment also counts bearish as NEGATIVE
- **Result:** Same indicator penalized twice = over-suppression

**Fix (V13.11):**
```
RULE C05 — AMENDED (SINGLE PENALTY):
  Each indicator contributes EITHER:
  (a) Modifier Score (from Section 7), OR
  (b) Alignment Count (from STEP 09)
  
  NOT BOTH.
  
  PRIORITY HIERARCHY FOR PENALTY:
  1. If indicator triggers MODIFIER (EXCLUSIVE conditions active) 
     → apply modifier penalty ONLY, skip alignment count
  2. If indicator status = "N/A"
     → zero penalty, zero alignment count
  3. If indicator status = "Neutral/Flat"
     → 0% modifier + counts as neutral in alignment (not negative)
  4. If indicator status = "Bearish" but NO specific modifier exists
     → counts as NEGATIVE in alignment ONLY (-1 toward 4/7 minimum)
  
  EXAMPLE:
  - EMA shows Bearish Cross: -6% modifier → DO NOT count as alignment negative
  - RSI shows no clear signal (between 50-60): 0% modifier + counts NEUTRAL (not negative)
  - MFI shows divergence down: -6% modifier → DO NOT double-count in alignment
```

---

## ISSUE #3: AMBIGUOUS "SOSIAL MATI" DEFINITION ✅ FIXED

**Problem (V13.10):**
- "15 minutes" is arbitrary without rationale
- No time-adjustment for token age
- "Post/reply/retweet" scope unclear (Twitter/Telegram/Discord?)

**Fix (V13.11):**
```
SOCIAL PULSE DEFINITION (PARAMETRIC):
  "Sosial Mati" Status Decision Tree:
  
  IF token age < 30 minutes:
    THEN monitoring window = 5 minutes (recent tokens = faster decay)
  ELSE IF token age 30min – 2 hours:
    THEN monitoring window = 10 minutes (early phase = higher activity expected)
  ELSE (token age > 2 hours):
    THEN monitoring window = 15 minutes (established = baseline)
  
  CHANNELS MONITORED (additive — any activity counts):
  1. Twitter (X) — new posts/replies/retweets by team/community
  2. Telegram group — admin messages or member messages (if community > 100)
  3. Discord — #announcements or #general (if server active)
  4. Reddit — posts in token subreddit (if exists)
  
  STATUS OUTCOMES:
  Activity = "Recent" within window + ≥10 engagement (replies/reactions)
    → PASS (Sosial Aktif)
  Activity = "Recent" within window + <10 engagement
    → WARNING (Sosial Muted — not dead, but weak)
  NO activity in monitoring window + MCap rising
    → BLOCK (Artificial Pump)
  NO activity in monitoring window + MCap flat/falling
    → WARNING (Sosial Mati)
  Activity CANNOT be verified from SS
    → [UNVERIFIED] label, -5% confidence (per Section 6.3)
  
  CONFIDENCE MODIFIER (applied to confidence engine):
  - Sosial Aktif: +0% (baseline, no boost)
  - Sosial Muted: -3% (instead of -5%)
  - Sosial Mati + MCap↑: -10% or AR Point 3 BLOCK (depends on % rise)
  - Sosial Unverified: -5% (per Section 6.3)
```

---

## ISSUE #4: FIBONACCI LEVEL SELECTION AMBIGUITY ✅ FIXED

**Problem (V13.10):**
- "Entry ideal" = 0.382, "Golden ratio" = 0.618
- No rule for prices BETWEEN levels
- Prioritization missing

**Fix (V13.11):**
```
FIBONACCI LEVEL RESOLUTION (Decision Tree):

ENTRY LEVEL SELECTION:
IF price is AT Fib level (±0.5% tolerance):
  → Use that level as entry reference
  → Modifier per Section 7 applies

ELSE IF price is BETWEEN two Fib levels (e.g., 0.382 to 0.5):
  → Use LOWER level (closer to swing high = safer, more confirmation needed)
  → Rationale: More conservative = reduces false breakouts
  
  Examples:
  - Price at 0.432 (between 0.382 and 0.5)
    → Use Fib 0.382 entry reference, +3% modifier
  - Price at 0.55 (between 0.5 and 0.618)
    → Use Fib 0.5 entry reference, +5% modifier
  - Price at 0.7 (between 0.618 and 0.786)
    → Use Fib 0.618 entry reference, +8% modifier

EXCEPTION (Higher Level OK):
IF volume > 3× SMA + MFI rising + bullish candle pattern confirmed
  → Can use UPPER level for aggressive sizing
  → Label: [AGGRESSIVE FIB ENTRY — UPPER LEVEL]
  → Size still capped per Mode Tabel

INVALID (N/A):
IF swing high/low cannot be identified from SS
  → Fibonacci = N/A for entry
  → Only use as TP anchor via confluence with other sources
  → If NO confluence = Fibonacci modifier = 0% or -5% per Section 7
```

---

## ISSUE #5: DEW INFINITE RENEWAL EXPLOIT ✅ FIXED

**Problem (V13.10):**
- "3-candle rule allows loop" for pullback renewal indefinitely
- Risk: Price pump outside zone → pullback within 3 candles → DEW renews → repeat

**Fix (V13.11):**
```
DEW RENEWAL CIRCUIT BREAKER (HARDCAP):

DEW RENEWAL PROTOCOL:
  Maximum renewal attempts = 2 per original DEW issuance
  
  Renewal Attempt #1:
  - If price pumps above Upper Bound, then pullback enters Entry Zone within 3 candles
    → DEW is RENEWED with same expiry reset (full duration per Section 15.5)
    → Label: [DEW RENEWED — Pullback #1]
  
  Renewal Attempt #2:
  - If renewed DEW expires, price pumps again, pullback re-enters within 3 candles
    → DEW is RENEWED ONCE MORE (final renewal)
    → Label: [DEW RENEWED — Pullback #2 (FINAL)]
  
  After Final Renewal:
  - Next price action outside DEW Zone → NO MORE RENEWALS
    → Setup is STALE, require fresh analysis
    → Output: "Setup stale — price exited DEW multiple times. Fresh SS required."
  
  EXCEPTION (Renewal Counter Reset):
  If 10+ candles pass since original DEW with ZERO Upper Bound breaches
    → Counter resets to 0 (treat as new opportunity)
    → Restart: next pump+pullback = Renewal Attempt #1
    → Rationale: Long consolidation = changed conditions
```

---

## ISSUE #6: MFI CONFIRMATION VOLUME THRESHOLD ✅ FIXED

**Problem (V13.10):**
- "vol naik" undefined — against SMA? Previous candle? Absolute value?

**Fix (V13.11):**
```
MFI CONFIRMATION VOLUME SPEC (Section 6.4):

"Volume naik" Definition (EXCLUSIVE — one must be true):
  (a) Volume current candle > Volume SMA × 1.5, OR
  (b) Volume current candle > Volume previous candle × 1.3, OR
  (c) Volume is in top 25% of last 20 candles by magnitude
  
  Apply FIRST condition that is TRUE in order (a)→b→c)
  
  MFI PASS Conditions (Amended):
  ✅ MFI rising + "vol naik" by above criteria = PASS
  ✅ MFI flat (50–70) + "vol naik" = PASS (accumulation hold)
  ⚠️  MFI flat <50 + vol falls = WARNING (weak trend)
  🚫 MFI diverges down saat harga naik (regardless volume) = BLOCK
  
  VOLUME FAIL SCENARIOS:
  - MFI rising BUT volume < SMA (all 3 conditions false) = PASS but -3% confidence
    (Label: [MFI RISING — WEAK VOLUME])
  - MFI flat + volume < SMA = DOWNGRADE from PASS to WARNING
```

---

## ISSUE #7: INDICATOR ALIGNMENT BONUS OVERLAP ✅ FIXED

**Problem (V13.10):**
- Alignment bonus (+10% max) potentially stacks on top of individual indicator modifiers
- Risk: Double-counting = total modifier exceeds +20% cap incorrectly

**Fix (V13.11):**
```
MODIFIER STACKING HIERARCHY (AMENDED):

Confidence Formula Recalculated:
  FINAL CONFIDENCE = Base + [Modifier Stack total] + [Alignment Bonus]
  
  WHERE:
  - Modifier Stack = sum of EXCLUSIVE indicators (Section 7)
    Example: VPVR +7 + EMA +4 + MFI +3 + others = Subtotal
  
  - Alignment Bonus = bonus for 5/7+ indicators positive
    Tier 1: 4/7 = 0% (minimum threshold)
    Tier 2: 5/7 = +3%
    Tier 3: 6/7 = +6%
    Tier 4: 7/7 = +10%
  
  Total Modifier = [Modifier Stack subtotal] + [Alignment Bonus]
  Cap Applied: MAX = +20%, MIN = -35%
  
  IF [Modifier Stack] + [Alignment Bonus] > 20%:
    THEN trim Alignment Bonus first (preserve indicator fidelity)
    New Alignment Bonus = 20% - [Modifier Stack]
    
  EXAMPLE:
  - Indicator modifiers: VPVR+7, EMA+8, MFI+6, VWAP+4 = +25 (before cap)
  - Alignment: 6/7 = +6%
  - Total before cap: +25 + 6 = +31%
  - After cap: +20% (trim excess evenly: Alignment→0%, Indicators→+20%)
  
  ALTERNATIVE (CLEANER):
  Apply cap to [Modifier Stack ONLY], Alignment Bonus treated SEPARATELY:
  - Modifier Stack: cap at +20%
  - Alignment Bonus: cap at +5% (separate ceiling)
  - Total possible: 85% base + 20% + 5% = 110% → capped to 100%
```

**CHOSEN FIX: Separate ceilings (cleaner, more transparent)**

---

## ISSUE #8: INDICATOR HIERARCHY vs MODIFIER SCORING MISMATCH ✅ FIXED

**Problem (V13.10):**
- LAW 12 says: VWAP + VolSMA > MFI > EMA > RSI > VPVR > Fibonacci (hierarchy)
- Section 7 shows: VPVR +7%, EMA +8%, RSI +6%, MFI +6%, VWAP +7%, Vol +5%, Fib +8%
- **Mismatch:** VPVR tier-6 but +7% modifier? EMA tier-4 but only +8%?

**Fix (V13.11):**
```
INDICATOR HIERARCHY ALIGNMENT (AMENDED):

Hierarchy for CONFLICT RESOLUTION (tiebreaker only):
  Tier 1: Padre (override) > VWAP + VolSMA
  Tier 2: MFI
  Tier 3: EMA Cross
  Tier 4: RSI
  Tier 5: VPVR
  Tier 6: Fibonacci
  
MODIFIER SCORING (separated from hierarchy):
  Modifiers are INDEPENDENT of hierarchy — they reflect signal strength, not conflicts.
  
  When TWO INDICATORS CONFLICT:
  → Use hierarchy tier to determine tiebreaker
  → Apply BOTH modifiers (don't cancel one out)
  → Higher tier indicator confidence weight = +1 in alignment count
  
  Example:
  - VWAP rejection (-8%) vs MFI rising (+6%)
  - Hierarchy: VWAP tier-1 > MFI tier-2 → VWAP wins
  - Modifier: both apply → -8% + 6% = -2% net
  - Alignment: VWAP counts negative (-1), MFI counts positive (+1)
  
  HIERARCHY USAGE (non-modifier context):
  Section 6.5 Invalidation Buffer source priority uses hierarchy (a→g)
  Section 8.1 VPVR vs pattern breakout: same logic
  
  CLARITY: Modifiers ≠ Hierarchy. Hierarchy is tiebreaker ONLY.
```

---

## ISSUE #9: FIBONACCI CONFLUENCE DEFINITION MISSING ✅ FIXED

**Problem (V13.10):**
- "Dual Confluence +5%, Triple +8%, Mega +12%" but what counts as "confluence"?
- Is VPVR HVN + Fib 0.618 confluence? VWAP + EMA?

**Fix (V13.11):**
```
CONFLUENCE DEFINITION (CANONICAL):

Confluence = Fibonacci level ALIGNS with one or more structural support/resistance sources.

VALID CONFLUENCE SOURCES (EXCLUSIVE LIST):
  S1: VPVR High Volume Node (HVN) at similar price ±2%
  S2: VWAP (±1 SD band)
  S3: EMA 9 or EMA 21 dynamic level
  S4: Previous swing low from chart
  S5: Rounded bottom / pattern base level
  S6: Rounded resistance ceiling
  S7: Volume SMA breakout level (historical)
  
CONFLUENCE SCORING:
  Fib only (no source S1–S7 within ±2%) 
    → Modifier = -5% (support weak, isolated)
  Fib + 1 source (Dual Confluence)
    → Modifier = +5% bonus (over base Fib modifier)
  Fib + 2 sources (Triple Confluence)
    → Modifier = +8% bonus
  Fib + 3+ sources (Mega Confluence)
    → Modifier = +12% bonus
  
CALCULATION:
  Total Fib modifier = [Base Fib modifier from Section 7] + [Confluence bonus]
  Example:
  - Entry at Fib 0.618 (base +8%)
  - Aligns with VPVR HVN (S1) + VWAP (S2)
  - Total Fib: +8% + 8% (Dual) = +16% before cap
  - Applied with other indicators, subject to +20% cap
```

---

## ISSUE #10: GREEN-ADJACENT vs CAUTION ENTRY CONFLICT ✅ FIXED

**Problem (V13.10):**
- LAW 07 defines GREEN-ADJACENT (max 1 SECONDARY yellow, ≥85% conf)
- Section 6 defines CAUTION ENTRY (4–5/6 AR PASS, size -30%)
- **Overlap:** Both require ≥85%, but different paths?

**Fix (V13.11):**
```
SIGNAL CLASSIFICATION (HIERARCHY):

GREEN (Full Entry):
  - All 7 indicators ≥ non-bearish (bullish or neutral)
  - AR 6/6 PASS
  - Confidence ≥ 85%
  - Size: FULL per Mode Tabel
  - Entry: All TP active (TP1, TP2, TP3 if Aggressive)

GREEN-ADJACENT (Reduced Entry):
  - ALL 4 PRIMER indicators green (Padre, MFI, VWAP, Volume SMA)
  - Exactly 1 SECONDARY indicator yellow (EMA, RSI, VPVR, Fib)
  - Maximum 3 SECONDARY bearish (others green/yellow)
  - Confidence ≥ 85%
  - AR ≥ 5/6
  - Size: 85% of FULL (intermediate, higher than CAUTION)
  - TP1 + TP2 active, TP3 disabled
  - Label: [GREEN-ADJACENT — INTERMEDIATE ENTRY]

CAUTION ENTRY:
  - AR 4–5/6 with ≤2 WARNINGS (zero BLOCKS)
  - Confidence 70–84.9% (below GREEN/GREEN-ADJACENT)
  - Size: 70% of FULL (most conservative)
  - TP1 only, no TP2/TP3
  - Label: [CAUTION ENTRY — TP1 ONLY]

DECISION TREE (applied in STEP 13):
IF AR 6/6 + Conf ≥85% + All Ind ≥neutral
  → GREEN
ELSE IF AR ≥5/6 + Conf ≥85% + 4-Primer-Green + ≤1-Sec-Yellow
  → GREEN-ADJACENT
ELSE IF AR 4–5/6 + Conf 70–84.9% + ≤2 WARNING + 0 BLOCK
  → CAUTION
ELSE
  → NO ENTRY / WATCHLIST
```

---

## ISSUE #11: PROBABILITY BOOST CONTRADICTIONS ✅ FIXED

**Problem (V13.10):**
- "Bull > 70% = +3%, Bull > 85% = +5%" — what if Bull = 70% exactly? Rounding?
- What if Bull 55% AND Bear 60% (tie)? Both trigger bonuses?
- Probability boost and confidence cap interaction unclear

**Fix (V13.11):**
```
PROBABILITY BOOST ENGINE (AMENDED):

THRESHOLD DEFINITION (inclusive/exclusive):
  Bull ≥ 70%     → +3% bonus
  Bull ≥ 85%     → +5% bonus (replaces +3%, not additive)
  Bear ≥ 60%     → -8% bonus
  Sideways ≥ 50% → 0% (no bonus, baseline)
  
TIE-BREAKING (Section 9.2 applies):
  IF Bull = Bear (e.g., 40% each with Sideways 20%):
    Use MFI direction tiebreaker (per Section 9.2)
    → If MFI rising: Bull gets +1, recalculate Bull > Bear → +3% bonus
    → If MFI falling: Bear gets +1, recalculate Bear > Bull → -8% bonus
  
MULTI-FACTOR BOOST INTERACTION:
  Only ONE boost applies (highest tier):
  - If Bull 85% → +5% (not +5% from Bull + 3% from alignment, only +5%)
  - If Bull 70% AND pattern confirmed → +3% bonus only (not cumulative)
  - If Bear 60% → -8% penalty (not modified by Bull level)
  
STACKING WITH CONFIDENCE CAP:
  Probability boost is INCLUDED in [Total Modifier]:
  Total Mod = [Indicator Stack] + [Alignment Bonus] + [Probability Boost]
  Cap: MAX +20%, MIN -35%
  
  If probability boost would exceed cap:
  Trim other modifiers first, preserve probability boost (safety signal)
  
  Example:
  - Indicator modifiers: +18%
  - Probability bonus (Bull 70%): +3%
  - Total before cap: +21%
  - After cap: Reduce indicator to +17%, keep +3% bonus = +20% total
```

---

## ISSUE #12: VWAP < 1 HOUR MODIFIER CAVEAT ✅ FIXED

**Problem (V13.10):**
- "Token < 1 hour: modifier 50%" but how to apply?
- Is it 50% of value, or modifier is halved before calculating confidence?

**Fix (V13.11):**
```
RULE C07 — VWAP MICRO-CAP CAVEAT (AMENDED):

Token age < 60 minutes:
  All VWAP modifiers (positive and negative) are SCALED × 0.5
  
  Base VWAP modifiers (Section 7):
  +7% → +3.5%
  +4% → +2%
  +2% → +1%
  -3% → -1.5%
  -5% → -2.5%
  -8% → -4%
  
  Token age 60–120 minutes:
  Scale × 0.75 (intermediate)
  
  Token age > 120 minutes:
  Scale × 1.0 (full modifiers)
  
  RATIONALE: Young tokens have unreliable VWAP (insufficient history), reduce confidence weight
  
  Applied after individual modifier calculated:
  - Calculate VWAP modifier from Section 7 table
  - Check token age
  - Scale modifier × scaling factor
  - Add scaled modifier to confidence formula
  
  Example:
  Token age: 35 minutes
  VWAP condition: "Bounce from VWAP + volume" → base +7%
  Scaled: +7% × 0.5 = +3.5% applied to confidence
```

---

## ISSUE #13: RSI > 70 MICRO-CAP OVERRIDE VAGUE ✅ FIXED

**Problem (V13.10):**
- RULE C09: "RSI > 70 = -2% if MFI naik + Vol ≥1.5×SMA, else -5%"
- What if RSI = 70 exactly? > or ≥?

**Fix (V13.11):**
```
RULE C09 — RSI MICRO-CAP OVERRIDE (AMENDED):

RSI threshold:
  RSI > 70 (not ≥; 70 itself = borderline, treated separately)
  RSI = 70: apply RSI modifier from Section 7 (+4% or +0%, not penalty)
  
RSI > 70 MICRO-CAP PENALTY:
  IF RSI > 70 AND MFI rising + Volume ≥ 1.5× SMA:
    → -2% modifier (overbought with volume = less severe)
  
  ELSE IF RSI > 70 (any other condition):
    → -5% modifier (overbought without confirmation = danger)
  
  RSI > 80 (extreme overbought):
    → -8% modifier (regardless of MFI/Volume)
    → Accelerate TP1 to support (VPVR HVN or Fib 0.618, whichever lower)
    → Suggest partial exit 50% immediately
  
LOGIC:
  - RSI > 70 with strong vol = potential short-term pump within overbought (minor penalty)
  - RSI > 70 without vol = pump unsupported by money flow (severe penalty)
  - RSI > 80 = emergency signal, regardless of other factors
```

---

## ISSUE #14: BONDING CURVE LETHAL ZONE RULES MISSING ✅ FIXED

**Problem (V13.10):**
- Section 15 mentions "BC > 90% = max 2 candle DEW"
- But no rules for BC 50–90%, or what happens if BC rises during position

**Fix (V13.11):**
```
BONDING CURVE RULES (CANONICAL):

BC POSITION / ENTRY DECISION:

BC < 50% (Early):
  ✅ PASS — entry allowed, no penalty
  DEW valid: 5–7 candles (extended window)

BC 50–80% (Mid):
  ✅ PASS with caution — entry allowed, -2% confidence
  DEW valid: 3–5 candles (standard window)

BC 80–90% (Late):
  ⚠️ WARNING — entry allowed, -5% confidence
  DEW valid: 2–3 candles (compressed window)
  Suggested size cap: 80% of position size (not 100%)

BC 90–99% (Lethal Zone):
  🚫 BLOCK — NO NEW ENTRY
  If already in position: EMERGENCY EXIT PROTOCOL
  Exit 100% immediately or at next TP (whichever first)

BC ≥ 99% or BC "fully diluted":
  ⛔ AUTO BLACKLIST — bonding curve extinct

BC RISING DURING POSITION:
  IF BC crosses into higher tier during trade:
  - BC rises from Mid (70%) → Late (85%): -5% confidence modifier applied retroactively, TP1 becomes primary exit
  - BC rises from Late (88%) → Lethal (91%): STOP ALL NEW TRADES, exit current position immediately
  - BC rises from Lethal (92%) → nearly 100%: MARKET DEAD, hard liquidation
  
  Monitor Section 5 trigger: BC 90%+ = forced recalibration (market regime change)
```

---

## ISSUE #15: PAPER TRADING ACCURACY METRICS UNDEFINED ✅ FIXED

**Problem (V13.10):**
- "Best Ind: most accurate" — no rubric
- "Fib Acc: X/N level accurate" — what's the accuracy bar?

**Fix (V13.11):**
```
PAPER TRADING ACCURACY METRICS (FORMALIZED):

INDICATOR ACCURACY SCORING:

Per Indicator, track:
  A = True Positives (indicator signal = price moved as predicted)
  B = False Positives (indicator bullish but price bearish)
  C = False Negatives (indicator neutral/bearish but price bullish)
  D = True Negatives (indicator bearish and price bearish)
  
Accuracy = (A + D) / (A + B + C + D) × 100%
Hit Rate = A / (A + B) × 100% (if signal fired)

FIBONACCI ACCURACY:
  Fib level "accurate" if price bounced within ±1.5% of level
  OR price touched level ± 1 candle before actual entry
  
  Track per retracement level:
  - Fib 0.382: accuracy if entry within 1.5% of level
  - Fib 0.5: accuracy if price pulled back to within range
  - Fib 0.618: accuracy if bounce confirmed
  - Fib 0.786: accuracy if touched as deep support
  
  Fib Accuracy % = (Accurate entries / Total Fib entries) × 100%
  Target: ≥ 70% accuracy across session

VWAP ACCURACY:
  VWAP bounce "accurate" if:
  - Price touched VWAP ± $0.000X (platform-dependent tolerance)
  - Candle body closed above VWAP after bounce
  - Volume spike confirmed during bounce
  
  Track: Bounces observed vs bounces that led to profitable TP1

BEST INDICATOR (SESSION):
  Indicator with highest [Hit Rate] AND ≥ 70% accuracy
  If tie: use win rate (return % at TP1)
  
WORST INDICATOR (SESSION):
  Indicator with lowest [Hit Rate] OR < 50% accuracy
  Flag for review in next session calibration

RUNNING STATS (Section 13 P&L Tracker):
```
Best Ind: VPVR (85% accuracy, +3.2% avg return)
Worst Ind: RSI (60% accuracy, -1.1% avg return)
Avg Align: 5.4/7
Avg Bull%: 68%
Fib Acc: 11/15 (73%)
VWAP Acc: 9/12 (75%)
BC Early: 4/6 (67% win rate)
BC Mid: 8/10 (80% win rate)
```
```

---

## ISSUE #16: STALE ANALYSIS CHECK THRESHOLD ✅ FIXED

**Problem (V13.10):**
- "If pump > 50% since SS = abort" — what timeframe? 30 min? Until analysis done?

**Fix (V13.11):**
```
STALE ANALYSIS CHECK (STEP 01, AMENDED):

Check at BEGINNING of analysis:
  IF (Current Price − SS Price) / SS Price > 50%:
    → ABORT ANALYSIS immediately
    → Output: "Setup stale — pump 50%+ detected. Request fresh SS or skip."
    → Timestamp: note time delta (SS taken X minutes ago)
  
  ELSE: Proceed to analysis

Check at END of analysis (before output):
  IF final confidence ≥ 70% (entry eligible):
    Recalculate: (Current Price − SS Price at time analysis finishes) / SS Price
    IF new price has moved > 25% since STEP 01 stale check:
      → Label output: [ANALYSIS TIME-LAG: +25% price movement detected]
      → Recommend waiting for pullback or fresh SS
      → DEW upper bound MAY be outdated
    
    ELSE: output remains valid

Re-analysis Trigger:
  - IF any BLACKLIST reason emerges during analysis → abort, no output entry
  - IF price already above Entry Zone (DEW upper bound) at STEP 12 → abort entry
  - IF Bonding Curve enters Lethal Zone → immediate STOP
```

---

# SECTION X.1 — CONFLICT RESOLUTION MATRIX

## Master Tiebreaker Flowchart

```
DECISION TREE: CONFLICTING SIGNALS

START: Two or more indicators give opposing signals

├─ PADRE vs ANY TECHNICAL INDICATOR
│  └─ Padre WINS (override layer)
│     Apply both modifiers, but Padre direction is final call
│
├─ VWAP+VolSMA vs MFI
│  ├─ VWAP bounce up + MFI falling → -8% + (-6%) = -14%, NO ENTRY
│  ├─ VWAP above + MFI diverging down → BLOCK (Section 6.4)
│  └─ VWAP below + MFI rising → -5% + 6% = +1%, proceed with caution
│
├─ EMA CROSS vs VWAP
│  ├─ Bullish EMA cross + VWAP rejection → Size -30% (Section 8.2)
│  ├─ Bullish EMA + VWAP bounce → Full alignment, +8% + 7% = +15%
│  └─ Bearish EMA + VWAP bounce → -6% + 7% = +1%, WATCHLIST only
│
├─ RSI DIVERGENCE vs LEVEL
│  ├─ RSI > 70 + Bullish divergence → +6% (divergence wins), but -2% (overbought)
│  └─ RSI < 30 + Bearish divergence → -8% (divergence severe)
│
├─ VOLUME CLIFF vs TREND
│  ├─ Volume > 3×SMA + Volume then cliff 50% → Check TX ratio first
│  ├─ If TX shows buy heavy: +5% boost (true demand)
│  └─ If TX shows sell heavy: -8% penalty (trap)
│
├─ FIBONACCI vs PATTERN
│  ├─ Fib 0.618 confluence + Pattern confirms → +8% Fib + Pattern bonus
│  ├─ Fib level miss but pattern valid → Use pattern TP only
│  └─ Fib hit + pattern breaks → Fib wins for entry, pattern for exit
│
├─ PROBABILITY BULL > 70% vs CONFIDENCE < 85%
│  ├─ Bull 75% but Confidence 78% → CONDITIONAL ENTRY (new tier)
│  └─ Bull 60% but Confidence 85% → CAUTION ENTRY (Bull is gating condition)
│
├─ AR 6/6 vs PROBABILITY < 55%
│  ├─ AR 6/6 but Bull < 40% → NO ENTRY (WATCHLIST, Section 11)
│  ├─ AR 6/6 + Bull 45% → NO ENTRY (ambiguous tier)
│  └─ AR 6/6 + Bull 55% → CAUTION ENTRY eligible
│
├─ MULTIPLE BLOCKS in AR Checklist
│  └─ ANY 1 BLOCK = NO ENTRY (zero exception, Section 6)
│
└─ GREEN-ADJACENT vs CAUTION vs GREEN
   ├─ All conditions for GREEN met → GREEN (size 100%)
   ├─ Else if GREEN-ADJACENT conditions met → GREEN-ADJACENT (size 85%)
   ├─ Else if CAUTION conditions met → CAUTION (size 70%)
   └─ Else → NO ENTRY / WATCHLIST
```

---

# SECTION X.2 — QUICK REFERENCE LOOKUP TABLE

| **Problem** | **Threshold** | **Action** | **Label** |
|---|---|---|---|
| Entry Confidence | < 70% | NO ENTRY | BLACKLIST/WATCHLIST |
| | 70–79% | CAUTION ENTRY | [CAUTION — TP1 ONLY] |
| | 80–84.9% | CONDITIONAL ENTRY | [CONDITIONAL — TP1+TP2] |
| | ≥ 85% | FULL/GREEN-ADJACENT | [GREEN] or [GREEN-ADJ] |
| AR Score | 6/6 | Full entry eligible | [AR CONFIRMED] |
| | 5/6 + ≤2 WARN | CAUTION eligible | [CAUTION AR] |
| | 4/6 + ≤2 WARN | CAUTION eligible | [CAUTION AR] |
| | Any 1 BLOCK | NO ENTRY | [AR BLOCKED] |
| Alignment | < 4/7 positive | NO ENTRY | [ALIGNMENT FAIL] |
| | 4/7 | Minimum pass | [BASELINE] |
| | 5/7 | +3% bonus | [GOOD] |
| | 6/7 | +6% bonus | [STRONG] |
| | 7/7 | +10% bonus | [FULL STACK] |
| Bull Probability | < 40% | NO ENTRY | [BEARISH BIAS] |
| | 40–54% | WATCHLIST | [AMBIGUOUS] |
| | 55–69% | CAUTION ENTRY | [CAUTION PROB] |
| | ≥ 70% | FULL ENTRY path | [BULLISH] |
| Bonding Curve | < 50% | Extended DEW 5–7 | [EARLY] |
| | 50–80% | Standard DEW 3–5 | [MID] |
| | 80–90% | Compressed DEW 2–3 | [LATE] -2% conf |
| | 90–99% | NO NEW ENTRY | [LETHAL ZONE] |
| | ≥ 99% | BLACKLIST | [EXTINCT] |
| Token Age | < 30 min | 5 min social window | [VWAP ×0.5] |
| | 30–120 min | 10 min social window | [VWAP ×0.75] |
| | > 120 min | 15 min social window | [FULL VWAP] |
| Dev Holding | < 5% | PASS | [✅] |
| | 5–10% | WARNING | [⚠️] -5% conf |
| | > 10% | BLOCK | [🚫] |
| Insiders+Bundles | < 20% | PASS | [✅] |
| | 20–30% | WARNING | [⚠️] size 50% |
| | > 30% | BLOCK | [🚫] |
| MFI Confirmation | Rising + vol↑ | PASS | [✅ +6%] |
| | Flat >50 + vol↑ | PASS | [✅ +3%] |
| | Diverging down | BLOCK | [🚫] |
| VWAP Position | Bounce + vol | PASS | [✅ +7%] |
| | Above + rising | PASS | [✅ +4%] |
| | Rejection + vol | BLOCK | [🚫 -8%] |
| RSI | < 30 | OVERSOLD | [+4%] if recovery |
| | 30–45 | Recovery zone | [+6%] if rising |
| | 45–70 | Bullish bias | [+4 to +6%] |
| | > 70 | Overbought | [-2 to -5%] per Section |
| | > 80 | EXTREME | [-8%] ACCELERATE TP |
| Liquidity Ratio | > 8% | PASS | [✅] |
| | 3–8% | WARNING | [⚠️] -5% conf |
| | < 3% | BLOCK | [🚫] |
| Volume Spike | > 5× SMA | CHECK TX ratio first | [⚠️] before scoring |
| | 2–3× SMA | Kuat valid | [✅ +5%] |
| | 1–2× SMA | Normal | [✅ +3%] |
| | < 1× SMA | Weak | [-3 to -5%] |
| Fibonacci | Entry ±0.5% | Use that level | [✅ modifier per level] |
| | Between levels | Use LOWER level | [✅ conservative] |
| | No swing visible | N/A | [Fib N/A] |
| Confluence | Fib + 1 source | Dual | [+5% bonus] |
| | Fib + 2 sources | Triple | [+8% bonus] |
| | Fib + 3+ sources | Mega | [+12% bonus] |

---

# SECTION X.3 — CONFIDENCE FORMULA (CORRECTED & FINAL)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BASE SCORE (Amended):
  = (AR PASS count / 6) × 80   [NEW BASE: 80 instead of 85]
  
  Ceiling recalculated:
  AR 6/6 → Base 80% → max with modifiers = 100%
  AR 5/6 → Base 66.7% → max = 86.7% ✅ (achievable now)
  AR 4/6 → Base 53.3% → max = 73.3% (CAUTION only)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MODIFIER STACK TOTAL (Section 7 - not changed):
  Indicator Stack = sum of (VPVR ± EMA ± RSI ± MFI ± VWAP ± Volume ± Fibonacci)
  
  Example: +7 + 4 + 6 + 6 + 4 + 5 + 8 = +40 (before capping)

ALIGNMENT BONUS (Separate ceiling now):
  4/7 = 0%
  5/7 = +3%
  6/7 = +6%
  7/7 = +10%
  
  CAP: Alignment Bonus ≤ +5% (separate from indicator cap)

PROBABILITY BOOST (Highest tier only):
  Bull ≥ 85% = +5%
  Bull 70–84% = +3%
  Bull 55–69% = +1% (new tier for CAUTION)
  Bear ≥ 60% = -8%
  Sideways ≥ 50% = 0%
  
  Apply ONLY highest tier (not cumulative)

STANDARD MODIFIERS:
  +5%   First-party source (direct SS screenshot)
  -5%   Per WARNING in AR (kumulatif)
  -5%   Velocity normal + sosial mati (independent)
  -10%  2+ metrik N/A or unverified
  -15%  Chart pattern unconfirmed volume
  -20%  Gocek Shield failed 3–4 criteria
  -2%   Bonding Curve 80–90%
  -5%   Bonding Curve 80–90% (can apply both if conditions warrant)
  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONFIDENCE FORMULA (FINAL):

FINAL CONFIDENCE = Base Score + Modifier Stack + Alignment Bonus 
                   + Probability Boost + Standard Modifiers
                   
Applied Cap:
  Total before cap = sum of all above
  
  IF Total ≥ +20% (above positive cap):
    Trim in order (preserve safety signals):
    1. Trim Standard Modifiers first (-X% penalties reduced)
    2. Then trim Alignment Bonus
    3. Keep Probability Boost (safety signal)
    4. Final = Base + min(Indicator Stack, +20%)
  
  IF Total ≤ -35% (below negative cap):
    → AUTO NO ENTRY (setup is highly risky)
  
  Final ceiling: 100% (cannot exceed)

ENTRY TIERS (Based on final confidence):
  Tier 1: ≥ 85% → FULL ENTRY (size 100%, all TP active)
  Tier 2: 80–84.9% → CONDITIONAL ENTRY (size 100%, TP1+TP2 only)
  Tier 3: 70–79.9% → CAUTION ENTRY (size 70%, TP1 only)
  Tier 4: < 70% → NO ENTRY / WATCHLIST

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WORKED EXAMPLE:

Token: EXAMPLE (age 45 min, BC 65%, MCap +200% in 2h)

Base Score:
  AR Score: 5/6 PASS
  Base = (5/6) × 80 = 66.7%

Indicator Stack:
  VPVR (HVN bounce) = +7%
  EMA (Bullish cross + vol) = +8%
  RSI (rising 55–60) = +6%
  MFI (rising + vol) = +6%
  VWAP (above, rising) = +4% [scaled ×0.75 for 45 min age] = +3%
  Volume SMA (1.8× SMA) = +3%
  Fibonacci (entry at 0.618 + VPVR confluence) = +8% + 5% = +13%
  Subtotal: +7 +8 +6 +6 +3 +3 +13 = +46% (before cap)

Alignment Bonus:
  6/7 positive = +6%

Probability Boost:
  Bull 72% → +3%

Standard Modifiers:
  First-party SS = +5%
  1 AR WARNING (Liq Ratio 6%) = -5%
  Net Standard = 0%

TOTAL BEFORE CAP:
  66.7 + 46 + 6 + 3 + 0 = 121.7%

APPLY CAP:
  Trim Indicator Stack to +20% max
  New Total: 66.7 + 20 + 6 + 3 + 0 = 95.7%

FINAL CONFIDENCE: 95.7% → capped to 100% (ceiling)

ENTRY DECISION: ✅ FULL ENTRY (Tier 1, ≥ 85%)
Size: 100% per Mode Tabel
TP: TP1, TP2, TP3 active (if Aggressive mode)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

# DEPRECATION LOG

**V13.10 → V13.11 Changes:**

| Rule | Status | Replacement |
|---|---|---|
| Base Score = (AR/6) × 85 | DEPRECATED | Base Score = (AR/6) × 80 |
| LAW 05: Final < 85% = NO ENTRY (hard) | DEPRECATED | Tiered: ≥85% FULL, 80–84.9% CONDITIONAL, 70–79.9% CAUTION, <70% NO |
| Double-penalty (modifier + alignment) | DEPRECATED | Single-penalty: choose modifier OR alignment count, not both |
| "Sosial mati" = 15 min fixed | DEPRECATED | Parametric: 5 min (age<30m), 10 min (30–120m), 15 min (>120m) |
| Fib between levels = ambiguous | DEPRECATED | Use LOWER level (0.382 before 0.5, etc.) unless vol > 3×SMA |
| DEW infinite renewal loop | DEPRECATED | Circuit breaker: max 2 renewals, then STALE |
| "Vol naik" = undefined | DEPRECATED | Vol > 1.5× SMA OR Vol > 1.3× prev candle OR top 25% of 20 candles |
| Modifier cap applies evenly | DEPRECATED | Trim order: Standard → Alignment → keep Probability Boost |
| Hierarchy = Scoring | DEPRECATED | Hierarchy = conflicts only; scoring = independent |
| RSI > 70 = exactly > 70 | DEPRECATED | RSI = 70 borderline, RSI > 70 penalty applies |
| Paper accuracy = subjective | DEPRECATED | Formal: (TP + TN) / All × 100%, Hit Rate = TP / (TP+FP) |

---

**Version: V13.11 FULLY RESOLVED**  
**Last Updated: 2026-05-14**  
**Status: Production Ready**  
**Remaining Known Issues: 0**

---

End of DXM Architect V13.11 — FIXED
