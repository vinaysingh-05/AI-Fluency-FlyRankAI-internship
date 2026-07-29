# ⚡ Gemini-Style AI Agent (Streamlit + Groq)

A sleek, fast, and interactive AI agent built with **Streamlit** and **Groq's Llama 3.1 8B**. Featuring a modern Google Gemini-inspired dark interface, custom CSS micro-animations, real-time message streaming, and a **ReAct tool-calling loop** for live web data integration.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)
![Groq](https://img.shields.io/badge/Groq-API-orange.svg)
![Model](https://img.shields.io/badge/Model-Llama--3.1--8b--Instant-purple.svg)

---

## ✨ Features

- **🎨 Gemini-Inspired UI**: Styled with modern glassmorphism, floating content cards, smooth CSS keyframe animations, and a prominent centered search bar.
- **🔄 ReAct Agent Loop**: Intelligent tool execution engine that automatically determines whether to answer conversationally or invoke tools for external data.
- **🌤️ Live Tool Integration**: Embedded real-time weather tool (`wttr.in` API) providing temperature, condition, humidity, and wind details.
- **⚡ Character Streaming**: Typewriter-style real-time response generation powered by Groq's low-latency inference engine.
- **🔒 Secure Key Handling**: Uses `.env` environment variables to protect API secrets and prevent accidental leaks.

---

## 🛠️ Tech Stack

- **Frontend / Framework:** Streamlit, Custom HTML5/CSS3
- **LLM Engine:** Groq SDK (`llama-3.1-8b-instant`)
- **Live Tool Source:** `requests`, `wttr.in` REST API
- **Environment Management:** `python-dotenv`

---

## 📁 Repository Structure

```text
├── app.py              # Main Streamlit application & ReAct engine
├── .env                # Local environment variables (API keys)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation