---
DXM OUTPUT TEMPLATE V2 — PRIORITY-FIRST
Menggantikan SECTION 12 di DXM V13.10-FIXED
Urutan output baru: 6 Priority Sections → Compact Audit Trail
---

SECTION 12 — OUTPUT TEMPLATE V2 (PRIORITY-FIRST)
> Urutan output baru. Priority sections tampil PERTAMA — data keputusan langsung terlihat.
> Audit Trail (data pendukung) di bawah dalam format kompres.
> Blok 3–10 di-skip jika Signal = BLACKLIST / NO ENTRY.

```
╔══════════════════════════════════════════════════════════╗
║  ⚡ DXM SCAN V13.10  —  [NAMA TOKEN]  /  $[CA]           ║
╚══════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 VERDICT & EXECUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ [Narasi 2–3 kalimat. Gw ngomong as a trader — bukan AI. No fluff.
   Jelaskan kenapa ini layak entry atau kenapa skip — spesifik, tajam.]

╭──────────────────────────────────────────────────────────╮
│  SIGNAL   🟢 GREEN — ANTI-RUNGKAD CONFIRMED              │
│           🟡 YELLOW — CAUTION ENTRY [GREEN-ADJACENT]     │
│           🔴 RED — NO ENTRY                               │
│           ⛔ BLACKLIST                                    │
│                                                           │
│  CONF     ██████████████████████░░░  [X%]                 │
│  GATE     AR [X/6]  ·  ALIGN [X/7]  ·  BULL [X%]         │
╰──────────────────────────────────────────────────────────╯

  📍 ENTRY   $[X] – $[Y]       Ref: [Fib 0.618 / VWAP / EMA / VPVR HVN]
  🎯 TP1     $[X]   (+[X]%)    MIN (Fib Ext 1.272, VPVR resistance)
  🎯 TP2     $[X]   (+[X]%)    Fib Ext 1.618 / VPVR next HVN
  🌙 TP3     $[X]   (+[X]%)    Fib Ext 2.0 — Aggressive only  /  N/A
  🛑 INV     $[X]               Setup gugur — Ref: [Fib/VWAP/EMA/VPVR/Swing]
  📦 SIZE    [FULL 100%  /  CAUTION 70%  /  WARNING-MODE 50%  /  NO POSITION]

  Pattern : [nama pola] — [CONFIRMED / UNCONFIRMED]
  Stack   : [X/7] positif — [nama indicator yang hijau]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 DYNAMIC ENTRY WINDOW (DEW)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ⏱️  Expiry: [N candle]  (~[X] menit)  ·  Status: 🟢 AKTIF / 🟡 EDGE / 🔴 EXPIRED

  ╔════════════════════════════════════════════════════════╗
  ║  🚫  CHASING ZONE     ░░░░░░░░░░░░░░  di atas $[X]    ║
  ╠══════════════════════ UPPER BOUND ════════════════════ ║
  ║  ✅  ENTRY ZONE       ████████████████  $[X] – $[Y]   ║
  ╠══════════════════════ LOWER BOUND ════════════════════ ║
  ║  🛑  ABORT ZONE       ░░░░░░░░░░░░░░  di bawah $[X]   ║
  ╚════════════════════════════════════════════════════════╝

  Pump > Upper Bound  →  Jangan chase. Tunggu pullback ke zone max 3 candle.
                          Pullback terjadi  →  DEW RENEWAL (valid kembali)
                          Tidak pullback    →  Fresh scan, setup sudah beda
  Drop < Lower Bound  →  Support break. Setup gugur. NO ENTRY — pindah token.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🕯️ CANDLE PROJECTION  (3–5 candle ke depan)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  TF: [1m/3m/5m/15m]  ·  Last Close: $[X]  ·  Momentum: [STRONG / NORMAL / WEAK]

       C1            C2            C3            C4            C5
   [🟢/🔴/⚪]   [🟢/🔴/⚪]   [🟢/🔴/⚪]   [🟡/🔘]      [🔘]
    [▲/▼/─]      [▲/▼/─]      [▲/▼/─]      [▲/▼/─]       [~]
    [X%] conf    [X%] conf    [X%] conf    [X%] conf    [X%] conf

  ┌─────────────────────────────────────────────────────────┐
  │  C1  $[Low]–$[High]   Trigger   : [kondisi konfirmasi]  │
  │  C2  $[Low]–$[High]   If C1 🟢 : [proyeksi arah + range]│
  │  C3  $[Low]–$[High]   Decision  : [kondisi penentu C3]  │
  │  C4  ~$[X]            Monitor   : confidence decay      │
  │  C5  ~$[X]            Spekulatif: outer projection      │
  └─────────────────────────────────────────────────────────┘

  If C1 🔴  →  [Pullback ke Entry Zone? / Support hold? / Setup gugur?]
  Proj. vs §9: [✅ AGREE — dual confirmation +2% / ⚠️ DIVERGE — DEW -1 CANDLE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌀 FIBONACCI MAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📈 SH: $[X]   ·   📉 SL: $[X]   ·   Source: [SS / USER INPUT — UNVERIFIED]

  ┌──────────────────────────────────────────────────────────┐
  │                     ── EXTENSION ──                      │
  │  🌙  Ext 2.618   $[X]                  ← Moonshot 🚀    │
  │  🌙  Ext 2.000   $[X]                  ← TP3 Aggressive │
  │  🎯  Ext 1.618   $[X]                  ← TP2            │
  │  📍  Ext 1.272   $[X]                  ← TP1            │
  ├────────────── ▶▶  PRICE NOW  $[X]  ◀◀ ─────────────────┤
  │                    ── RETRACEMENT ──                     │
  │       0.236      $[X]                                    │
  │       0.382      $[X]                  ← Entry zona 1   │
  │       0.500      $[X]                  ← Decision zone  │
  │  🎯   0.618      $[X]                  ← Golden ratio ✨│
  │       0.786      $[X]                  ← Deep support   │
  │  💀   1.000      $[X]  = SL           ← Setup gugur    │
  └──────────────────────────────────────────────────────────┘

  🔗 Confluence: [level + sumber aktif]
     Tier      : [Dual +5% / Triple +8% / Mega +12% / NONE]
     Modifier  : [+X%]

  ⚠️  N/A: Swing tidak teridentifikasi dari SS → Fib tidak dihitung (LAW 10)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔮 FORWARD PROJECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  🟢 BULL  ────────────────────────────────────────  [X%]
     Trigger  : [kondisi yang mengaktifkan]
     Target 1 : $[X]  (~[N] candle)  ←  [Fib Ext / VPVR / pattern]
     Target 2 : $[X]  (~[N] candle)  ←  [level teknikal berikutnya]
     Batal jika: [kondisi invalidasi bull]

  🔴 BEAR  ────────────────────────────────────────  [X%]
     Trigger  : [kondisi yang mengaktifkan]
     Target 1 : $[X]   ←  [Fib 0.786 / VPVR HVN bawah / neckline]
     Target 2 : $[X]   ←  [level support berikutnya jika dump berlanjut]
     Implikasi: [exit watchlist / tunggu bottom konfirmasi / pindah token]

  ⚪ SIDEWAYS  ─────────────────────────────────────  [X%]
     Range      : $[X] – $[Y]
     Atas  ↑    : $[X]  →  Bull aktif      Bawah ↓ : $[X]  →  Bear aktif
     Action     : Watchlist — set alert di kedua breakout level, jangan entry di tengah range

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 PROBABILITY ENGINE  +  🚨 TRAP RADAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  🟢 Bull      [X%]   ████████████████████░░░░░░░░░░  faktor: [list]
  🔴 Bear      [X%]   ████████░░░░░░░░░░░░░░░░░░░░░░  faktor: [list]
  ⚪ Sideways  [X%]   ████░░░░░░░░░░░░░░░░░░░░░░░░░░  faktor: [list]

  Dominant  : [skenario]  →  [rekomendasi action berdasarkan probabilitas]
  Tiebreaker: [jika Bull = Bear → MFI direction: naik → Bull / turun → Bear]

  🚨 TRAP RADAR
  ┌────────────────────────┬───────────────────┬──────────────────────┐
  │  🎣 FOMO Trap          │  ░░░░░░░░░░░░░░░  │  🟢 RENDAH           │
  │  🎭 Gocek / Fake Break │  ░░░░░░░░░░░░░░░  │  🟢 RENDAH           │
  │  🌊 Wash Candle        │  ░░░░░░░░░░░░░░░  │  🟢 TIDAK AKTIF      │
  │  💧 Exit Liquidity     │  ████░░░░░░░░░░░  │  🟡 MEDIUM — WATCH   │
  │  🕵️ Insider Distrib.  │  ░░░░░░░░░░░░░░░  │  🟢 TIDAK AKTIF      │
  └────────────────────────┴───────────────────┴──────────────────────┘

  Trap aktif (jika ada):
  ⚠️  [Nama trap]: [kondisi yang trigger] → [action yang harus diambil]

  Scoring Trap (internal — tidak ditampilkan ke user, hanya trigger section ini):
  → 🎣 FOMO      : RSI > 70 + vol spike + sosial hype + Bonding Curve > 70%
  → 🎭 Gocek     : Bullish breakout + Padre Sell Heavy + MFI divergen turun
  → 🌊 Wash      : Vol > 5x SMA + TX buy count < 10 wallet unik (LAW 13)
  → 💧 Exit Liq  : Liq/MCap < 5% + MCap naik + Dev wallet bergerak
  → 🕵️ Insider  : Sosial mati + green candles terus + Top10 > 50%

  Bar visual (gunakan karakter █ dan ░ — 15 karakter total):
  RENDAH      = ░░░░░░░░░░░░░░░  (0–2 trigger aktif dari faktor trap tersebut)
  MEDIUM      = ████░░░░░░░░░░░  (3–4 trigger aktif)
  TINGGI      = ████████░░░░░░░  (5–7 trigger aktif)
  KRITIS      = ███████████████  (semua trigger aktif → mengarah ke LAW 13)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
▼  AUDIT TRAIL  —  Data Pendukung  (baca jika butuh justifikasi)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 SESSION
  Scan: [timestamp]  ·  Status: [NEW / REVISIT]  ·  Mode: [Aggressive/Normal/Warning/Defensive/FullStop]
  ΔMCap: [prior $X → now $Y | ±Z%]  ·  ΔLiq: [prior $X → now $Y]  ·  Source: [SS / UNVERIFIED / NO PRIOR]

📊 VITAL DATA
  Token: [nama]  ·  Age: [X]  ·  MCap: $[X]  ·  Liq: $[X]  ·  Liq/MCap: [X%]
  Dev: [X%]  ·  Inside: [X%]  ·  Bundles: [X%]  ·  Top10: [X%]  ·  Vol/MCap: [X%]

🧠 NEURAL MAP
  Volume: [analisa]  ·  MFI: [Rising/Falling/Div/N/A]  ·  TX: [Buy/Sell/Neutral]
  Sosial: [Active/Dead/Artificial]  ·  Pattern: [nama] — [CONFIRMED/UNCONFIRMED]
  Velocity: [Organic/Trap/Artificial]  ·  Psych: [trap yang dipasang + kondisi retail]

📊 INDICATOR STACK
  ┌──────────────┬─────────────────────────────┬──────┬────────┐
  │ VPVR         │ [HVN/LVN/POC/N/A]           │ [+/-]│ [+X%]  │
  │ EMA Cross    │ [Bullish/Bearish/Flat/N/A]   │ [+/-]│ [+X%]  │
  │ RSI          │ [value + label / N/A]         │ [+/-]│ [+X%]  │
  │ MFI          │ [Rising/Falling/Div/N/A]     │ [+/-]│ [+X%]  │
  │ VWAP         │ [Bounce/Above/Below/N/A]     │ [+/-]│ [+X%]  │
  │ Vol SMA      │ [Xx SMA / Zombie / N/A]      │ [+/-]│ [+X%]  │
  │ Fibonacci    │ [level aktif / N/A]           │ [+/-]│ [+X%]  │
  ├──────────────┼─────────────────────────────┼──────┼────────┤
  │ ALIGNMENT    │ [X/7 positif]                │      │ [bonus]│
  └──────────────┴─────────────────────────────┴──────┴────────┘
  Dominant: [indicator]  ·  Conflict: [jika ada — resolusi LAW 12]

🛡️ ANTI-RUNGKAD
  Dev:    [✅/⚠️/🚫]  Bundle:  [✅/⚠️/🚫]  Sosial: [✅/⚠️/🚫]
  MFI:    [✅/⚠️/🚫]  InvBuf:  [✅/🚫]  LiqR:   [✅/⚠️/🚫]
  Score:  [X/6]  ·  WARNING Count: [X]  →  [CAUTION ELIGIBLE ≤2 / NO ENTRY ≥3]
  InvBuf Source: [VPVR/VWAP/EMA/Swing/Base/Fib0.618/Fib0.786/NONE]  ·  Distance: [X%]

📊 CONFIDENCE SCORE
  Base: [X%]  +  Standar: [+/-X%]  +  Stack: [+/-X%]  +  Align: [+X%]  +  Prob: [+/-X%]
  Total Modifier: [+/-X%] (cap: +20/–35)  →  FINAL: [X%]  [✅ ELIGIBLE / ❌ BELOW]

📝 LOGIC UPDATE
  Trade #[N]  ·  Status: [OPEN/WATCHING/SKIPPED/UPDATE PENDING]
  Entry: $[X] | TP1/TP2: $[X]/$[X] | Inv: $[X] | Align: [X/7] | Conf: [X%]
  Lesson: [catatan atau update dari scan ini]

╔══════════════════════════════════════════════════════════╗
║  ⚡ DXM V13.10  |  Zero-Loss  |  Anti-Gocek  |  Predictive║
║  Bull: [X%]  |  Bear: [X%]  |  Align: [X/7]  |  Conf: [X%]║
╚══════════════════════════════════════════════════════════╝
```

---
CONFIDENCE BAR GUIDE (gunakan karakter █ dan ░ — 25 karakter total):
50% = █████████████░░░░░░░░░░░░
65% = ████████████████░░░░░░░░░
75% = ██████████████████░░░░░░░
85% = █████████████████████░░░░
91% = ██████████████████████░░░
95% = ███████████████████████░░
100%= █████████████████████████

FORWARD PROJECTION BAR GUIDE (gunakan ─ — 50 karakter total):
25% = 🟢 BULL  ─────────────                       25%
65% = 🟢 BULL  ─────────────────────────────────── 65%
Bar diisi proporsional dengan panjang angka %.

TRAP RADAR BAR GUIDE (15 karakter per bar):
RENDAH      = ░░░░░░░░░░░░░░░  (tidak ada trigger aktif)
LOW-MEDIUM  = ██░░░░░░░░░░░░░  (1–2 sub-kondisi aktif)
MEDIUM      = █████░░░░░░░░░░  (3–4 sub-kondisi aktif)
HIGH        = ██████████░░░░░  (5–6 sub-kondisi aktif)
KRITIS      = ███████████████  (semua sub-kondisi → LAW 13 risk)
---
