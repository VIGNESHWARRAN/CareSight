# CareSight 🧠🧓  
**An Adaptive Agentic AI System for Caregiver-Centric Elderly Care**

CareSight is a **caregiver-first, agentic AI system** designed to reduce the mental and operational burden of caring for elderly individuals. Instead of relying on elderly users to interact with apps, chatbots, or voice assistants, CareSight treats the elderly phone as a **passive sensor** and builds a **real-time adaptive AI agent for caregivers**.

The system continuously observes behavioral signals such as sound activity, silence, responsiveness during medication times, and caregiver inputs. It remembers doctor instructions, tracks care tasks, detects early warning signs, and alerts caregivers **only when attention is truly needed**—via a caregiver app and WhatsApp.

CareSight is **not a chatbot**.  
It is a **stateful, long-running AI agent** built on the **Pathway Engine**, aligned with production-grade Agentic AI principles.

---

## 🌍 The Problem We Are Solving

Caregiving is cognitively exhausting. Caregivers must:
- Track medications and stock levels  
- Monitor behavior changes (sleep, activity, responsiveness)  
- Remember doctor instructions and follow-ups  
- Detect early signs of decline or emergency  
- Manage multiple elders simultaneously  

Most elder-care apps provide **tools**, but still require humans to constantly think, monitor, and decide.

**CareSight reduces caregiver thinking**, not by adding features, but by introducing an AI agent that pays attention continuously.

---

## 💡 Core Idea

> **The elderly person should not have to understand or operate technology.  
The AI should quietly observe and help the caregiver decide what matters.**

CareSight treats **sound and time patterns** as behavioral signals, not language.  
It reasons over **long-term trends**, not one-off events.

---

## ✨ Key Capabilities

- 👩‍⚕️ **Caregiver-Centric Design**  
  The caregiver is the primary user; elderly interaction is minimal or passive.

- 🧠 **Agentic AI (Level-3 Adaptive)**  
  Maintains long-term memory, reasons over time, adapts alert thresholds, and learns caregiver preferences.

- 🔊 **Sound-First Behavioral Monitoring**  
  Uses silence, activity, stress, and acoustic events instead of speech-to-text.

- 💊 **Medication & Care Task Intelligence**  
  Tracks schedules, predicts stock-outs, and integrates doctor advice into care logic.

- 🏥 **Doctor Visit Memory (Consent-Based)**  
  Records doctor visits with permission and converts spoken advice into structured, recallable medical memory.

- 🚨 **Emergency Awareness**  
  Detects prolonged silence, distress sounds, or abnormal acoustic events with contextual reasoning.

- 📲 **Low-Friction Alerts**  
  Sends clear, actionable alerts and summaries via WhatsApp—no dashboards required.

- 🔐 **Privacy-First by Design**  
  No continuous raw audio storage; short encrypted audio snippets only on explicit triggers and consent.

---

## 🏗️ High-Level Architecture

[Elderly Phone – Background App]
(sound activity & event signals)
↓
[Pathway Engine – Adaptive Agent]
(state, memory, reasoning)
↓
[Caregiver App + WhatsApp Alerts]


Each elderly individual is handled by an **independent AI agent**, allowing a single caregiver to manage **multiple elders** without cognitive overload.

---

## 🧠 Agentic AI Design

CareSight operates as a **Level-3 Adaptive Agent**:

1. **Observe** – Acoustic events, silence windows, care interactions  
2. **Remember** – Long-term per-elder memory and baselines  
3. **Reason** – Compare current behavior with historical norms  
4. **Act** – Log, summarize, retry, or alert  
5. **Learn** – Adapt thresholds based on caregiver responses  

The system behaves differently over time based on outcomes, not fixed rules.

---

## 🔊 Acoustic Intelligence Strategy

There is no single dataset that matches real-world elderly monitoring.  
CareSight uses a **bootstrapping + personalization** approach:

- Public datasets for general acoustic understanding:
  - IEMOCAP (emotion dynamics)
  - RAVDESS / CREMA-D (controlled emotion)
  - ESC-50 (ambient events)
  - AudioSet (general sound embeddings)
- Online personalization to learn what is *normal* for each elder

Most inference runs **on-device using features**.  
Short encrypted audio snippets are uploaded **only on triggers** (emergency, doctor visit mode, explicit consent).

---

## 🛠️ Tech Stack

- **Backend / Agent Runtime**
  - Python
  - **Pathway Engine**
  - Pathway LLM Tooling
  - LangGraph (agent orchestration)

- **Elderly Background App**
  - Android (Kotlin)
  - Foreground Service
  - On-device acoustic feature extraction

- **Caregiver App**
  - Flutter / React Native
  - Voice queries
  - Multi-elder overview

- **AI / ML**
  - CNN / CNN+LSTM acoustic models
  - On-device inference (TFLite)
  - LLMs for summarization & explanation

- **Communication**
  - WhatsApp API
  - Telephony APIs (scheduled calls)

---

## 🔐 Privacy & Ethics

- No passive conversation recording  
- No continuous raw audio upload  
- Trigger-based, consent-aware audio snippets  
- Encrypted storage with TTL  
- Human-in-the-loop escalation  
- Clear “Monitoring ON” indicators  

CareSight follows **privacy-by-design** and **data minimization** principles.

---

## 📁 Repository Structure

The repository is intentionally split into two tracks:

- **`hackathon/`** – Time-boxed, demo-focused implementation  
- **`research/`** – Long-term models, datasets, personalization, and scalability  
- **`shared/`** – Event schemas, configs, and utilities  

This allows rapid prototyping without blocking future research or production work.

---

## 🚀 Why This Is Novel

Most elder-care apps help caregivers **do tasks**.  
CareSight helps caregivers **decide what matters**.

It introduces:
- Continuous attention instead of periodic check-ins  
- Memory as intelligence, not storage  
- Preventive reasoning instead of reactive alerts  

---

## 📌 One-Line Summary

> **CareSight is an adaptive AI caregiver agent that quietly watches, remembers, and reasons—so human caregivers don’t have to do it all themselves.**

---

## 📄 License

[Add your license here]
