# Aura (أورا) - The Self-Healing Infrastructure Guard

**Aura** is an intelligent orchestration layer that bridges the gap between cloud infrastructure monitoring and project management. It transforms passive alerts into active remediations.

## 🚀 The Vision
In modern DevOps, identifying a problem is only half the battle. The other half is context switching between monitoring tools and task managers. Aura eliminates this by:
1. **Detecting** anomalies in Neon/Render (e.g., slow queries, high latency).
2. **Analyzing** the root cause using AI.
3. **Triggering** remediation workflows directly in Linear with proposed fixes.

## ✨ Features
- **Proactive Monitoring:** Integrates with Neon to track SQL performance.
- **Auto-Ticketing:** Automatically creates Linear issues for infrastructure regressions.
- **Glassmorphic Dashboard:** A futuristic command center to visualize system health and AI actions.
- **Self-Healing Loop:** Designed to eventually deploy fixes automatically upon developer approval.

## 🏗️ Architecture
- **Backend:** Python Engine (`aura/backend/engine.py`) for anomaly detection logic.
- **Database:** Neon Postgres for incident logging and service registry.
- **UI/UX:** Stitch-generated futuristic design system (Dark Mode / Glassmorphism).
- **Task Management:** Linear for remediation tracking.

## 📂 Project Structure
- `aura/backend/`: Core logic and integration scripts.
- `aura/frontend/`: UI prototypes and dashboard templates.
- `aura/tests/`: Unit tests for reliability.
- `README.md`: Project overview.

---
*Created with ❤️ by Jules (Your AI Software Engineer).*
