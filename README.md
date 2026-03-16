# 🛡️ GigShield — AI-Powered Parametric Income Protection for Q-Commerce Delivery Partners

> **Guidewire DEVTrails 2026 | University Hackathon**
> *Seed → Scale → Soar*

---

## 🎯 Problem Statement

India's Q-Commerce delivery partners (Zepto, Blinkit, Swiggy Instamart) operate under an extreme performance contract — **deliver in 10 minutes or lose your incentive**. They work across hyper-local dark store micro-zones, outdoors, all day, every day. Yet when a cloudburst, a severe AQI spike, or a flash curfew shuts down their zone, they don't just lose a few orders — they lose their **entire shift's income**, with no compensation from the platform and no insurance safety net anywhere.

A single bad monsoon week can cost a Blinkit delivery partner ₹3,000–₹5,000 in lost wages. Multiply that across 2 million active Q-Commerce partners and you have a **₹600 crore annual uninsured income loss problem** — hidden, untracked, and completely ignored by the existing insurance industry.

**GigShield changes that.**

---

## 💡 Our Solution

GigShield is an **AI-enabled parametric income insurance platform** built exclusively for Q-Commerce delivery partners on Zepto, Blinkit, and Swiggy Instamart. When an external disruption crosses a measurable threshold — rainfall intensity, AQI level, temperature, a curfew notice — GigShield automatically detects it, validates it against the worker's active zone and online status, and processes a direct income payout — **zero manual claim filing, zero paperwork, zero waiting**.

We insure **income loss only** — not vehicles, not health, not accidents.

---

## 👤 Persona: Q-Commerce Delivery Partner

### Who We're Protecting

| Attribute | Profile |
|---|---|
| **Platform** | Zepto / Blinkit / Swiggy Instamart delivery partners |
| **Income** | ₹600 – ₹1,100/day · ₹4,000 – ₹7,500/week |
| **Work Pattern** | 8–12 hrs/day · 6–7 days/week · Hyperlocal zone (2–4 km radius from dark store) |
| **Delivery Pressure** | 10–20 min delivery SLA · Incentive-heavy, penalty-heavy model |
| **Location** | Tier-1 & Tier-2 metros: Bengaluru, Mumbai, Delhi, Hyderabad, Chennai, Pune |
| **Device** | Budget Android (₹6,000–₹15,000 range) |
| **Digital Comfort** | UPI-native, Blinkit/Zepto partner app daily user, WhatsApp-first communicator |
| **Pain Point** | Zero income during weather shutdowns, AQI emergencies, curfews, or platform outages |

### Real-World Scenarios

**Scenario 1 — The Bengaluru Monsoon Shutdown (Environmental)**
> Ravi is a Blinkit partner operating out of a dark store in Koramangala. A Red Alert rainfall warning is issued at 5 PM. Blinkit suspends all orders in his micro-zone. He sits idle for 5 hours during peak dinner time. That's ₹550 gone — no compensation from the platform. With GigShield Standard (₹99/week), our system detects the IMD rainfall alert, cross-validates his GPS against the affected zone, confirms he was online at trigger time, and automatically credits ₹450 to his UPI ID by 11 PM. No form. No call.

**Scenario 2 — The Delhi AQI Emergency (Environmental)**
> Priya delivers for Zepto in West Delhi. In November, AQI in her zone crosses 400 (Severe) by 10 AM and stays there for 6 hours. The platform advises partners to avoid outdoor activity. Priya loses her most profitable morning shift. With GigShield Premium (₹149/week), her coverage activates automatically once the AQI breach is validated via CPCB data. She receives ₹600 — her estimated 6-hour income — directly to her account before the day ends.

**Scenario 3 — The Mumbai Flash Curfew (Social Disruption)**
> Suresh operates out of a Swiggy Instamart dark store in Dharavi. A sudden Section 144 is issued in his delivery zone at 8 AM with 2 hours' notice. The platform halts all orders. GigShield's social disruption monitor detects the government notification, validates Suresh's zone overlap with the curfew perimeter, and initiates a half-day payout of ₹350. By noon, his wallet is topped up — before his next shift even begins.

**Scenario 4 — The Zepto App Outage (Operational)**
> Anjali is logged into the Zepto partner app and marked available during the 7–10 PM peak window — the most lucrative 3 hours of her day. The Zepto partner app goes down for 2.5 hours. She receives zero orders despite being ready. GigShield's platform uptime monitor detects the API health failure, confirms Anjali was active and in-zone, and compensates her ₹280 for verified lost peak hours — a trigger no other insurance product on the market covers.

---

## 🔄 Application Workflow

```
┌──────────────────────────────────────────────────────────────────────┐
│                       GIGSHIELD PLATFORM FLOW                        │
└──────────────────────────────────────────────────────────────────────┘

  [Worker Opens Mobile App (Flutter)]
        │
        ▼
  [Phone OTP Auth] → [KYC: Aadhaar Verification (DigiLocker mock)]
        │
        ▼
  [Platform Link] → [Zepto / Blinkit / Instamart Partner ID verified]
        │
        ▼
  [AI Risk Profiling Engine]
    → Zone disruption history score
    → Dark store cluster risk tier
    → Worker tenure + activity hours
    → Season / city adjustment
    → Recommended plan surfaced
        │
        ▼
  [Weekly Policy Selection]
    → ₹49 Basic | ₹99 Standard | ₹149 Premium
    → Coverage period: Mon 00:00 → Sun 23:59
        │
        ▼
  [UPI Auto-Debit Setup] ← Premium deducted every Monday 6:00 AM
        │
        ▼
  ┌───────────────────────────────────────────────────────────────┐
  │             REAL-TIME DISRUPTION MONITORING ENGINE            │
  │  OpenWeatherMap + CPCB AQI + IMD Alerts + Govt Feed          │
  │  + Platform API Health Monitor                                │
  │  Polling interval: every 10 minutes | Active: 24x7           │
  └───────────────────────────────────────────────────────────────┘
        │
        ▼
  [Parametric Trigger Detected in Worker's Zone]
        │
        ▼
  ┌───────────────────────────────────────────────────────────────┐
  │                  AI FRAUD VALIDATION ENGINE                   │
  │  ① GPS Cross-Check — Was worker in disrupted zone?           │
  │  ② Platform Activity Check — Was worker online?              │
  │  ③ Duplicate Fingerprint — Same event claimed elsewhere?     │
  │  ④ Anomaly Score — Claim pattern vs peer cohort normal?      │
  │  ⑤ Weather Triple-Validation (3 API sources cross-confirmed) │
  └───────────────────────────────────────────────────────────────┘
        │                       │                      │
  [Score < 40]           [Score 40–70]           [Score > 70]
  Auto-Approved          Human Review Queue       Auto-Rejected
        │
        ▼
  [Payout Calculated]
    = (Weekly Coverage Limit ÷ 60 hrs) × Verified Disruption Hours
        │
        ▼
  [Instant Payout → UPI / Bank Transfer (Razorpay Test Mode)]
        │
        ▼
  [Worker App Updated] → Active policy · Earnings protected · Claim history
        │
        ▼
  [Admin Web Dashboard] → Loss ratios · Zone heatmap · Fraud queue · Forecasts
```

---

## 💰 Weekly Premium Model

### Why Weekly?

Q-Commerce delivery partners are settled **weekly** by Zepto, Blinkit, and Swiggy Instamart — all three platforms disburse partner earnings on a 7-day cycle. Aligning insurance premiums to this same cycle removes all friction: the worker earns in weeks, spends in weeks, and now **insures in weeks**. A weekly ₹99 deduction from a ₹5,500 weekly earning is 1.8% — barely noticeable. A monthly ₹400 premium feels like a bill.

### Pricing Tiers

| Plan | Weekly Premium | Max Weekly Payout | Coverage Events | Best For |
|---|---|---|---|---|
| **Basic** | ₹49/week | ₹1,200 | Weather (Rain + Heat) only | Part-time / trial users |
| **Standard** | ₹99/week | ₹2,800 | Weather + AQI + Social Disruption | Regular full-time partners |
| **Premium** | ₹149/week | ₹5,000 | All triggers incl. Platform Outage | Power workers / high earners |

### How the Weekly Premium is Dynamically Calculated

```
Weekly Premium = Base Rate
               × Zone Risk Multiplier        (0.8x – 1.4x)
               × Seasonal Adjustment         (0.9x – 1.3x)
               × Worker Activity Modifier    (0.9x – 1.15x)
               × Claim History Factor        (0.9x – 1.25x)
               × Tenure Loyalty Discount     (up to –15%)

Where:
  Base Rate              = Tier selected (₹49 / ₹99 / ₹149)
  Zone Risk Multiplier   = AI-scored from 2-year historical disruption
                           frequency per dark-store micro-zone cluster
  Seasonal Adjustment    = Monsoon (Jun–Sep): 1.25x
                           Winter AQI (Oct–Dec): 1.2x
                           Summer heat (Mar–May): 1.15x
                           Other months: 1.0x
  Activity Modifier      = Avg weekly hours logged on platform (normalised)
  Claim History Factor   = <1 claim/month: 0.9x | >3 claims/month: 1.25x
  Tenure Discount        = 3–6 months: –5% | 6–12 months: –10% | >12 months: –15%
```

**Live Example:**
> Ravi — Standard plan (₹99), Koramangala zone (flood-risk 1.2x), Monsoon season (1.25x),
> 40 hrs/week activity (1.0x), 2 claims last month (1.1x), 4 months tenure (–5%)
> `= ₹99 × 1.2 × 1.25 × 1.0 × 1.1 × 0.95 = ₹155.27/week`

The AI engine recalculates every Sunday night and presents the worker with a transparent breakdown in the app before Monday's deduction.

---

## ⚡ Parametric Triggers

Unlike traditional insurance requiring manual proof and adjuster review, parametric insurance pays out automatically when **pre-defined, objectively measurable thresholds** are crossed. No paperwork. No adjuster. No waiting.

| # | Trigger Type | Data Source | Threshold | Payout Logic |
|---|---|---|---|---|
| 1 | **Heavy Rainfall** | OpenWeatherMap API + IMD | > 15mm/hr sustained for 90+ min | Proportional to verified downtime (max 8 hrs) |
| 2 | **Extreme Heat** | OpenWeatherMap Heat Index | Heat Index > 44°C for 2+ hrs | Proportional to duration |
| 3 | **Severe AQI** | CPCB / OpenAQ API | AQI > 300 (Very Poor) for 3+ hrs | Proportional to duration |
| 4 | **Flood / Waterlogging** | IMD Flood Alert (mock) | Orange/Red flood advisory in worker's micro-zone | Half-day or full-day flat payout |
| 5 | **Curfew / Social Disruption** | Government alert feed (mock) | Section 144 / Bandh declared in zone | Payout for full declared duration |
| 6 | **Platform App Outage** | Blinkit/Zepto health monitor (mock) | Downtime > 45 min in peak hours (7–10 PM) | Flat payout for peak outage window |

**Payout Formula:**
```
Payout Amount = (Weekly Coverage Limit ÷ 60 working hours) × Verified Disruption Hours

Example: Standard plan (₹2,800 max) · 4 disrupted hours
= (₹2,800 ÷ 60) × 4 = ₹186.67 → rounded to ₹187
```

---

## 🤖 AI/ML Integration Plan

### 1. Dynamic Premium Calculation — XGBoost Regressor

**Purpose:** Produce a personalised, risk-adjusted weekly premium for each worker, recalculated every Sunday night.

**Model:** XGBoost Regressor trained on a synthetic dataset of 50,000 worker-week records generated from IMD historical weather archives and mock platform activity data.

**Feature Set:**

| Feature | Type | Description |
|---|---|---|
| `zone_lat`, `zone_lng` | Numeric | Micro-zone centroid coordinates (dark store cluster) |
| `zone_flood_score` | Numeric (0–1) | 2-year historical flood/waterlogging frequency |
| `zone_aqi_score` | Numeric (0–1) | 2-year historical severe AQI frequency |
| `zone_heat_score` | Numeric (0–1) | 2-year historical extreme heat frequency |
| `month_of_year` | Categorical | Encoded seasonal risk (monsoon / winter / summer / other) |
| `city_tier` | Categorical | Tier-1 vs Tier-2 metro (different base risk rates) |
| `worker_avg_weekly_hours` | Numeric | Platform-verified average active hours over last 4 weeks |
| `worker_tenure_weeks` | Numeric | Weeks since first delivery on platform |
| `claim_count_last_4w` | Numeric | Claims filed in the last 28 days |
| `platform` | Categorical | Zepto / Blinkit / Instamart (different SLA and earnings patterns) |

**Output:** `premium_multiplier` (float, 0.75 – 1.50) applied to the plan's base rate.

**Training Approach:**
- 80/20 train/test split with 5-fold cross-validation
- Evaluation metric: RMSE on premium multiplier
- Hyperparameter tuning: GridSearchCV on `n_estimators`, `max_depth`, `learning_rate`

**Serving:** FastAPI `/ml/premium` endpoint — batch recalculates all active policies every Sunday at 10 PM via APScheduler cron job.

---

### 2. Worker Risk Profiling at Onboarding — Logistic Regression Classifier

**Purpose:** Assign an initial Risk Tier (Low / Medium / High) to new workers at signup, before personal claim history exists, to seed their first premium calculation.

**Model:** Logistic Regression (lightweight, interpretable, sub-50ms inference at registration).

**Inputs at registration:**
- Zone selected → mapped to pre-computed zone risk scores (flood, AQI, heat)
- Platform chosen (Zepto / Blinkit / Instamart)
- Self-declared weekly hours (bucketed: <20 / 20–40 / 40+)
- City + month of signup (season proxy)

**Output → Initial Risk Tier → Starting Premium Multiplier:**

| Risk Tier | Condition Example | Initial Multiplier |
|---|---|---|
| Low | Low-flood, low-AQI zone · dry season | 0.85x |
| Medium | Moderate risk zone · standard season | 1.00x |
| High | Flood-prone or high-AQI zone · monsoon / winter | 1.25x |

This tier is replaced by the XGBoost model's output after 4 weeks of activity data is collected.

---

### 3. Intelligent Fraud Detection — Isolation Forest + Rule Engine

**Purpose:** Validate every auto-triggered claim before payout. Catch Q-Commerce specific fraud patterns without blocking legitimate claims from honest workers.

**Q-Commerce Specific Fraud Vectors & Detection Methods:**

| Fraud Type | Description | Detection Method |
|---|---|---|
| **GPS Spoofing** | Worker fakes location inside a disrupted zone they weren't actually in | GPS velocity check (movement > 120 km/h = impossible); cross-validate last 3 GPS pings before trigger window |
| **Fake Weather Claims** | Manual dispute claiming disruption on a clear day | Triple-source weather validation — OpenWeatherMap + IMD mock + zone sensor feed — all 3 must agree |
| **Duplicate Claims** | Same worker claiming the same event multiple times via different accounts or devices | SHA-256 hash of (worker_id + trigger_event_id + zone_id) → checked against Redis deduplication table before any approval |
| **Claim Velocity Fraud** | Worker claiming in every possible disruption window, far above peer cohort average | Rolling 4-week claim frequency Z-score vs zone peer group; Z > 2.5 flagged |
| **Platform Outage Fraud** | Claims platform outage payout but GPS shows they were outside delivery zone during outage | GPS position + platform login activity cross-validated for entire outage window |

**Full Detection Pipeline:**

```
Layer 1 — Hard Rules (instant block, no ML needed):
  → Duplicate hash match                           → REJECTED immediately
  → GPS delta > 5 km from declared zone at trigger → REJECTED
  → Policy not active at trigger timestamp         → REJECTED
  → Trigger event not confirmed by 2+ data sources → REJECTED

Layer 2 — Isolation Forest Anomaly Scorer:
  Feature vector per claim:
    [claim_frequency_4w, zone_peer_z_score, gps_confidence_score,
     weather_source_agreement, platform_activity_score, time_of_day_risk]

  Model: sklearn.ensemble.IsolationForest
  Contamination: 0.05 (5% expected fraud rate, per industry benchmarks)
  Anomaly score mapped to fraud_risk_score (0 = clean, 100 = highly anomalous)

Layer 3 — Final Decision Gate:
  fraud_risk_score < 40  → ✅ Auto-Approved → Payout queued immediately
  fraud_risk_score 40–70 → 🔍 Human Review Queue (target: <5% of all claims)
  fraud_risk_score > 70  → ❌ Auto-Rejected → Worker notified with reason code
```

**Model Lifecycle:** Isolation Forest retrained weekly on new claim data to adapt to emerging fraud patterns. Previous week's flagged + confirmed fraud cases used as labelled anomaly seeds for the next training cycle.

---

### 4. Predictive Disruption Forecasting — LSTM Time-Series Model

**Purpose:** Predict the probability of a disruption trigger event in each zone for the next 7 days. Used by the insurer admin dashboard to forecast claim volumes and manage reserve pools, and by the worker app to nudge proactive policy upgrades before high-risk weeks.

**Model:** LSTM (Long Short-Term Memory) neural network — TensorFlow/Keras.

**Input Sequences (per zone, per day):**
- 90-day rolling window: daily rainfall (mm), max temperature (°C), humidity (%)
- 90-day AQI readings per city zone
- Historical binary trigger labels (was a GigShield trigger crossed on that day: 0/1)

**Output:**
- `disruption_probability[zone_id][day_0..day_6]` — 7-element probability array (0.0–1.0) per zone for the next 7 days

**LSTM Architecture:**
```
Input (90-day sequence, 5 features per day)
  → LSTM Layer (128 units, return_sequences=True)
  → Dropout (0.2)
  → LSTM Layer (64 units)
  → Dropout (0.2)
  → Dense (32, ReLU)
  → Dense (7, Sigmoid)   ← 7-day probability output
```

**Use Cases in Platform:**

| Use Case | Where Used | Trigger |
|---|---|---|
| Reserve pre-allocation | Admin Dashboard | >70% disruption probability flagged to insurer |
| Proactive worker nudge | Worker App push notification | >60% probability in worker's zone this week |
| Dynamic pricing signal | Premium recalculation engine | Forecast probability fed as additional risk feature to XGBoost |
| Zone heatmap | Admin Dashboard | Visual overlay of next 7-day expected disruption intensity |

---

### 5. ML Model Serving Architecture

```
┌────────────────────────────────────────────────────────────┐
│                    FastAPI ML Service                       │
│                                                            │
│  POST /ml/premium        → XGBoost premium multiplier      │
│  POST /ml/risk-profile   → Logistic regression risk tier   │
│  POST /ml/fraud-score    → Isolation Forest claim checker  │
│  GET  /ml/forecast/{zone}→ LSTM 7-day disruption forecast  │
└────────────────────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────────────────────┐
│                 Model Registry (Local filesystem)           │
│                                                            │
│  xgboost_premium_v1.pkl          (updated weekly)          │
│  logreg_risk_profile_v1.pkl      (updated monthly)         │
│  isolation_forest_fraud_v1.pkl   (updated weekly)          │
│  lstm_disruption_v1.h5           (updated monthly)         │
└────────────────────────────────────────────────────────────┘
```

All models are loaded at FastAPI startup and kept in memory for sub-10ms inference. MLflow experiment tracking is introduced in Phase 3 to manage model versioning and retraining pipelines.

---

## 🏗️ System Architecture

### Platform Choice

**Flutter (Mobile) — Worker App**
- Q-Commerce partners are 100% mobile-first and never leave their delivery app
- Flutter delivers native Android/iOS performance from a single codebase — no duplicate development effort
- Offline-capable local state handles connectivity drops mid-shift
- Budget Android device optimisation out of the box

**React + Next.js (Web) — Admin / Insurer Dashboard**
- Insurer operations (loss ratio review, fraud queue management, analytics) are desktop-first tasks
- Next.js SSR delivers fast initial load for data-heavy chart dashboards
- Rich charting ecosystem (Recharts / D3.js) for the insurer analytics views

### Full Stack

| Layer | Technology | Rationale |
|---|---|---|
| **Worker Mobile App** | Flutter (Dart) | Native cross-platform, offline support, budget device optimised |
| **Admin Web Dashboard** | React + Next.js (TypeScript) | SSR, fast data dashboards, insurer analytics |
| **Backend API** | FastAPI (Python 3.11) | Async-first, best ML ecosystem, auto OpenAPI docs |
| **ML Engine** | scikit-learn + XGBoost + TensorFlow/Keras | Industry standard, lightweight inference |
| **Primary Database** | PostgreSQL 15 | Relational integrity for policies, claims, payouts |
| **Cache / Real-time** | Redis 7 | Trigger event cache, session store, duplicate fingerprints |
| **Authentication** | Firebase Auth (Phone OTP) | Essential for non-email workers, UPI-native login |
| **Weather API** | OpenWeatherMap (free tier) | Real-time weather + historical archives |
| **AQI API** | OpenAQ + CPCB feed (mock) | Zone-level air quality data |
| **Maps / Zone Validation** | Google Maps API / Nominatim (OSM) | Zone risk mapping, GPS cross-validation |
| **Payment (Mock)** | Razorpay Test Mode / UPI Simulator | Simulated instant payouts end-to-end |
| **Cloud** | GCP Cloud Run + Cloud SQL (free tier) | Serverless, scalable, zero cost in development |
| **Containerisation** | Docker + Docker Compose | Consistent dev/prod environments |
| **CI/CD** | GitHub Actions | Automated test and deploy pipeline |

### Detailed System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          GIGSHIELD SYSTEM ARCHITECTURE                      │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌───────────────────────┐          ┌──────────────────────────────────┐
  │  Flutter Mobile App   │          │  React + Next.js Admin Web       │
  │  (Worker Interface)   │          │  (Insurer / Ops Dashboard)       │
  │                       │          │                                  │
  │  • Onboarding + KYC   │          │  • Live Zone Disruption Map      │
  │  • Policy Dashboard   │          │  • Claims Review Queue           │
  │  • Disruption Alerts  │          │  • Fraud Flag Management         │
  │  • Claim Status       │          │  • Loss Ratio Analytics          │
  │  • Payout History     │          │  • LSTM 7-Day Forecast Heatmap   │
  │  • Earnings Protected │          │  • Worker Cohort Analytics       │
  └──────────┬────────────┘          └──────────────┬───────────────────┘
             │  HTTPS REST / WebSocket               │  HTTPS REST
             └──────────────────┬────────────────────┘
                                │
             ┌──────────────────▼──────────────────────┐
             │             FastAPI Backend               │
             │             (Python 3.11)                 │
             │                                          │
             │  /auth        → OTP + JWT Auth            │
             │  /workers     → Profile + risk tier       │
             │  /policies    → Weekly plan + pricing     │
             │  /triggers    → Disruption monitor        │
             │  /claims      → Auto-claim engine         │
             │  /payouts     → Payout processing         │
             │  /ml          → ML inference endpoints    │
             │  /admin       → Insurer analytics APIs    │
             └──────┬──────────────┬────────────────────┘
                    │              │
        ┌───────────▼────┐   ┌─────▼──────────────┐
        │  PostgreSQL 15  │   │      Redis 7         │
        │                 │   │                      │
        │  • workers      │   │  • Trigger event     │
        │  • zones        │   │    cache (TTL 24h)   │
        │  • policies     │   │  • Session tokens    │
        │  • claims       │   │  • Duplicate hashes  │
        │  • payouts      │   │  • Real-time events  │
        │  • trigger_logs │   │  • Rate limiting     │
        │  • audit_logs   │   └──────────────────────┘
        └─────────────────┘
                    │
        ┌───────────▼─────────────────────────────────┐
        │            ML Microservice Layer              │
        │                                             │
        │  ┌──────────────────────────────────────┐  │
        │  │  XGBoost Premium Calculator           │  │
        │  │  Input:  zone_risk + season + hours   │  │
        │  │  Output: premium_multiplier (float)   │  │
        │  └──────────────────────────────────────┘  │
        │  ┌──────────────────────────────────────┐  │
        │  │  Logistic Regression Risk Profiler    │  │
        │  │  Input:  zone + platform + hours      │  │
        │  │  Output: risk_tier (Low/Med/High)     │  │
        │  └──────────────────────────────────────┘  │
        │  ┌──────────────────────────────────────┐  │
        │  │  Isolation Forest Fraud Detector      │  │
        │  │  Input:  claim feature vector         │  │
        │  │  Output: fraud_score (0–100)          │  │
        │  └──────────────────────────────────────┘  │
        │  ┌──────────────────────────────────────┐  │
        │  │  LSTM Disruption Forecaster           │  │
        │  │  Input:  90-day weather time series   │  │
        │  │  Output: 7-day prob array per zone    │  │
        │  └──────────────────────────────────────┘  │
        └─────────────────────────────────────────────┘
                    │
        ┌───────────▼─────────────────────────────────┐
        │       External API Integration Layer          │
        │                                             │
        │  OpenWeatherMap   → Real-time weather data  │
        │  OpenAQ / CPCB    → Zone-level AQI data     │
        │  IMD Mock API     → Flood / alert feeds     │
        │  Govt Alert Feed  → Curfew notifications    │
        │  Blinkit Mock API → Platform health + GPS   │
        │  Zepto Mock API   → Partner activity data   │
        │  Razorpay Test    → Simulated UPI payouts   │
        │  Firebase Auth    → Phone OTP verification  │
        │  Google Maps API  → GPS zone validation     │
        └─────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                   DISRUPTION MONITORING ENGINE — DETAIL                     │
│                                                                             │
│  APScheduler cron → Runs every 10 minutes across all active policy zones   │
│                                                                             │
│  For each active zone:                                                      │
│    1. Fetch weather data   → Check rainfall / heat thresholds              │
│    2. Fetch AQI data       → Check severity thresholds                     │
│    3. Fetch govt feed      → Check for curfew / disruption notices         │
│    4. Fetch platform health→ Check Blinkit/Zepto/Instamart API status      │
│                                                                             │
│  On threshold breach:                                                       │
│    → Write trigger_event to PostgreSQL + Redis cache (TTL 24h)             │
│    → Query all workers with active policy + GPS in affected zone           │
│    → For each eligible worker → invoke Fraud Validation Engine             │
│    → If fraud_score < 40 → calculate payout → write claim → queue payout  │
│    → Push notification sent to worker's Flutter app                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Core Database Schema

```sql
-- Core entities (simplified)

workers        (id, phone, name, aadhaar_hash, platform, zone_id,
                tenure_weeks, risk_tier, avg_weekly_hours, created_at)

zones          (id, city, lat, lng, flood_score, aqi_score, heat_score,
                dark_store_cluster_id, city_tier)

policies       (id, worker_id, plan_tier, base_premium, final_premium,
                multiplier_breakdown_json, coverage_start, coverage_end, status)

trigger_events (id, zone_id, trigger_type, source_api, threshold_value,
                actual_value, detected_at, duration_hrs, source_agreement_count)

claims         (id, policy_id, trigger_event_id, fraud_score, fraud_flags_json,
                status, payout_amount, approved_at, reviewed_by)

payouts        (id, claim_id, worker_id, amount, upi_id,
                gateway_ref, status, processed_at)

audit_logs     (id, entity_type, entity_id, action, actor,
                timestamp, metadata_json)
```

---

## 📅 Development Plan (6-Week Roadmap)

### Phase 1 — Seed (Weeks 1–2): Ideation & Foundation ✅ *Current Phase*

| Task | Owner | Status |
|---|---|---|
| Problem research & Q-Commerce persona definition | Full Team | ✅ Done |
| System architecture design | Backend Lead | ✅ Done |
| AI/ML integration plan | ML Engineer | ✅ Done |
| Weekly premium model & parametric trigger design | Product Lead | ✅ Done |
| Database schema design | Backend Lead | 🔄 In Progress |
| FastAPI project scaffold + Docker Compose setup | Backend | 🔄 In Progress |
| Flutter app scaffold + routing setup | Mobile Lead | 🔄 In Progress |
| Next.js admin dashboard scaffold | Frontend Lead | 🔄 In Progress |
| Mock API stubs (weather, AQI, platform health) | Backend | 🔄 In Progress |
| Synthetic training dataset generation (50K records) | ML Engineer | 🔄 In Progress |
| README + Phase 1 video | Team | ✅ Done |

### Phase 2 — Scale (Weeks 3–4): Automation & Protection

- Worker registration + OTP auth (Flutter + Firebase)
- KYC flow: Aadhaar mock + Partner ID (Zepto/Blinkit) verification
- Policy creation engine + weekly premium calculator (XGBoost model v1)
- All 6 parametric trigger monitors live (weather, AQI, heat, flood, curfew, platform outage)
- Auto-claim initiation engine: trigger → fraud check → claim record
- Fraud detection v1: Rule-based hard blocks + Isolation Forest scoring
- UPI auto-debit setup (Razorpay test mode)
- Basic worker dashboard (Flutter): policy status, active trigger alerts, claim history
- Phase 2 demo video (2-minute)

### Phase 3 — Soar (Weeks 5–6): Scale & Optimise

- Advanced GPS velocity spoofing detection + peer cohort Z-score fraud analysis
- LSTM disruption forecasting model fully trained and integrated
- Razorpay test mode — full end-to-end payout flow (trigger → approve → credit)
- Worker earnings protection dashboard: weekly coverage summary, earnings protected stat
- Insurer admin dashboard: loss ratio charts, fraud queue, zone disruption heatmap, 7-day forecast
- Full end-to-end disruption simulation: fake rainstorm → auto-trigger → fraud validated → payout credited
- Performance optimisation + security hardening (rate limiting, AES-256 PII encryption)
- Final pitch deck (PDF) + 5-minute walkthrough demo video

---

## 📁 Repository Structure

```
gigshield/
├── backend/                          # FastAPI Python backend
│   ├── app/
│   │   ├── api/                      # Route handlers
│   │   │   ├── auth.py               # OTP + JWT auth
│   │   │   ├── workers.py            # Worker profile endpoints
│   │   │   ├── policies.py           # Policy creation + renewal
│   │   │   ├── claims.py             # Claim management
│   │   │   ├── payouts.py            # Payout processing
│   │   │   └── admin.py              # Insurer dashboard APIs
│   │   ├── models/                   # SQLAlchemy ORM models
│   │   ├── services/
│   │   │   ├── premium_engine.py     # Weekly premium calculator
│   │   │   ├── trigger_monitor.py    # Disruption polling engine (APScheduler)
│   │   │   ├── fraud_engine.py       # Multi-layer fraud validation pipeline
│   │   │   └── payout_service.py     # Razorpay + UPI integration
│   │   ├── ml/                       # ML model inference layer
│   │   │   ├── premium_model.py      # XGBoost premium predictor
│   │   │   ├── risk_profiler.py      # Logistic regression onboarding scorer
│   │   │   ├── fraud_model.py        # Isolation Forest anomaly detector
│   │   │   ├── forecast_model.py     # LSTM zone disruption forecaster
│   │   │   └── models/               # Serialised .pkl / .h5 model files
│   │   └── integrations/             # External API connectors
│   │       ├── openweather.py
│   │       ├── openaq.py
│   │       ├── razorpay.py
│   │       └── platform_mock.py      # Simulated Blinkit/Zepto partner API
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
│
├── mobile/                           # Flutter worker mobile app
│   ├── lib/
│   │   ├── screens/                  # Onboarding, Dashboard, Policy, Claims, Payouts
│   │   ├── widgets/                  # Reusable UI components
│   │   ├── services/                 # API client, local storage, notifications
│   │   └── models/                   # Dart data classes
│   └── pubspec.yaml
│
├── web/                              # Next.js admin dashboard
│   ├── app/
│   │   ├── dashboard/                # Main insurer overview
│   │   ├── claims/                   # Claims review + fraud queue
│   │   ├── analytics/                # Loss ratios + predictive forecasts
│   │   └── zones/                    # Zone disruption heatmap
│   ├── components/
│   └── package.json
│
├── data/                             # Synthetic training datasets
│   ├── zone_risk_scores.csv
│   ├── synthetic_worker_claims.csv
│   └── imd_weather_historical_mock.csv
│
├── infra/
│   ├── docker-compose.yml            # Full local dev stack
│   └── .github/
│       └── workflows/ci.yml          # GitHub Actions CI/CD
│
└── README.md
```

---

## 🔐 Compliance & Constraints

- ✅ **Income Loss Only:** Coverage strictly limited to income lost during verified external disruptions. No health, life, accident, or vehicle repair coverage — in any plan tier, under any circumstance.
- ✅ **Weekly Pricing:** All premiums, coverage windows, and payout caps operate on a strict 7-day cycle (Monday 00:00 → Sunday 23:59). No monthly or annual billing.
- ✅ **Persona Exclusivity:** Platform built exclusively for Q-Commerce delivery partners (Zepto / Blinkit / Swiggy Instamart). No other gig worker categories in scope.
- ✅ **Data Privacy:** Worker Aadhaar/phone collected only for KYC and fraud validation. Stored AES-256 encrypted. Never used for any purpose beyond insurance risk scoring.
- ✅ **Parametric Only:** No manual claim filing exists anywhere in the system. All payouts are triggered by objective, verifiable, external data sources — eliminating adjuster subjectivity entirely.

---

## 👥 Team

| Role | Responsibility |
|---|---|
| **Team Lead / Product** | Strategy, persona research, documentation, video |
| **Backend Engineer** | FastAPI, DB schema, trigger monitoring engine, API integrations |
| **Mobile Engineer** | Flutter worker app — onboarding, dashboard, claim notifications |
| **ML Engineer** | XGBoost premium model, Isolation Forest fraud detection, LSTM forecasting |
| **Frontend / DevOps** | Next.js admin dashboard, Docker, CI/CD, cloud deployment |

---

## 🔗 Links

- **GitHub Repository:** *(this repo)*
- **Demo Video (Phase 1):** *[Link to be added]*
- **Live Demo (Phase 2+):** *[Link to be added]*

---

*Built with ❤️ for India's invisible workforce — the delivery partners keeping our cities running at 10-minute speed.*
*Guidewire DEVTrails 2026 | Team GigShield*
