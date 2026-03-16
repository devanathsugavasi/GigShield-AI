# 🛡️ GigShield — AI-Powered Parametric Income Protection for Q-Commerce Delivery Partners

> **Guidewire DEVTrails 2026 | University Hackathon**  
> *Seed → Scale → Soar*

GigShield is an **AI-enabled parametric income insurance platform** for Q-Commerce delivery partners (Zepto, Blinkit, Swiggy Instamart). When weather, AQI, curfew, or platform outages disrupt a partner’s zone, GigShield detects it, validates it, and pays out automatically — **no forms, no paperwork, no waiting**.

We insure **income loss only** during verified external disruptions.

---

## 📁 Repository Structure

| Folder | Description |
|--------|-------------|
| **backend/** | FastAPI (Python 3.11) — auth, workers, policies, claims, payouts, ML inference, external APIs |
| **mobile/** | Flutter worker app — onboarding, dashboard, policy, claims, payouts |
| **web/** | Next.js admin dashboard — insurer overview, claims review, analytics, zone heatmap |
| **data/** | Synthetic training datasets (zone risk, claims, weather) |
| **infra/** | Docker Compose (Postgres, Redis, backend) and CI workflow |

---

## 🚀 Quick Start

- **Backend:** `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`  
  *(Requires `app/main.py` — add FastAPI app entry when implementing.)*
- **Mobile:** `cd mobile && flutter pub get && flutter run`
- **Web:** `cd web && npm install && npm run dev`
- **Full stack (Docker):** `cd infra && docker-compose up -d`

---

## 📖 Full Documentation

For problem statement, persona, workflow, premium model, parametric triggers, AI/ML plan, system architecture, database schema, and 6-week roadmap, see:

- **[README (3).md](./README%20(3).md)** — Complete product and technical specification

---

## 👥 Team

| Role | Responsibility |
|------|----------------|
| Team Lead / Product | Strategy, persona research, documentation, video |
| Backend Engineer | FastAPI, DB, trigger monitoring, API integrations |
| Mobile Engineer | Flutter worker app |
| ML Engineer | XGBoost premium, Isolation Forest fraud, LSTM forecasting |
| Frontend / DevOps | Next.js admin, Docker, CI/CD |

---

*Built for India’s Q-Commerce delivery partners.*  
*Guidewire DEVTrails 2026 | Team GigShield*
