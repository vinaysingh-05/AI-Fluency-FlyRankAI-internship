import os
import json
import time
import requests
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# 1. Page Configuration
st.set_page_config(
    page_title="AI Agent (Gemini UI)",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Advanced CSS for Gemini-Style Layout & Search Bar
st.markdown("""
<style>
    /* Google / Gemini Font & Color Palette */
    @import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Google Sans', 'Inter', sans-serif;
    }

    /* Clean Up Default Streamlit Wrappers */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Premium Gradient Background */
    .stApp {
        background:
            radial-gradient(circle at 15% 10%, rgba(124, 58, 237, 0.16) 0%, transparent 45%),
            radial-gradient(circle at 85% 0%, rgba(168, 199, 250, 0.14) 0%, transparent 40%),
            radial-gradient(circle at 50% 100%, rgba(242, 139, 130, 0.10) 0%, transparent 45%),
            #0b0c0d;
        color: #e3e3e3;
    }

    /* Wider, More Generous Content Frame */
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 9rem;
        max-width: 980px;
    }

    /* Keyframe Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(14px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 0 0 rgba(168, 199, 250, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(168, 199, 250, 0); }
        100% { box-shadow: 0 0 0 0 rgba(168, 199, 250, 0); }
    }

    @keyframes floatIn {
        from { opacity: 0; transform: translateY(20px) scale(0.98); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    /* ==========================================
       GLASSMORPHIC CONTENT FRAME / MESSAGE CARDS
       ========================================== */
    [data-testid="stChatMessage"] {
        background: rgba(30, 31, 32, 0.55);
        backdrop-filter: blur(18px) saturate(140%);
        -webkit-backdrop-filter: blur(18px) saturate(140%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 1.35rem 1.6rem;
        margin-bottom: 1.3rem;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.28);
        animation: fadeInUp 0.35s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    [data-testid="stChatMessage"]:hover {
        box-shadow: 0 10px 36px rgba(0, 0, 0, 0.35);
    }

    /* Assistant Message Specific Frame Accent */
    [data-testid="stChatMessage"]:nth-child(even) {
        background: linear-gradient(135deg, rgba(30, 31, 32, 0.65), rgba(30, 31, 32, 0.45));
        border-left: 3px solid #a8c7fa;
    }

    /* User Message Specific Frame Accent */
    [data-testid="stChatMessage"]:nth-child(odd) {
        background: linear-gradient(135deg, rgba(40, 42, 44, 0.7), rgba(40, 42, 44, 0.45));
        border-left: 3px solid #c4edd8;
    }

    /* ==============================
   GEMINI / CHATGPT INPUT
   ============================== */

div[data-testid="stChatInput"]{
    max-width:900px !important;
    margin:auto !important;
    position:fixed !important;
    left:50%;
    bottom:24px;
    transform:translateX(-50%);
    width:calc(100% - 40px);
    z-index:999;
}

div[data-testid="stChatInput"] > div{
    position:relative;
    border-radius:32px !important;
    background:rgba(30,31,32,.78)!important;
    backdrop-filter:blur(22px);
    border:1px solid rgba(255,255,255,.10)!important;
    min-height:72px;
    padding:10px 70px 10px 22px !important;
}

div[data-testid="stChatInput"] textarea{
    font-size:18px !important;
    color:#fff !important;
    background:transparent !important;
}

div[data-testid="stChatInput"] textarea::placeholder{
    color:#9aa0a6;
}

/* SEND BUTTON */

div[data-testid="stChatInput"] button{
    position:absolute !important;
    right:12px !important;
    top:50% !important;
    transform:translateY(-50%) !important;

    width:48px !important;
    height:48px !important;

    min-width:48px !important;
    min-height:48px !important;

    border-radius:50% !important;
    background:linear-gradient(135deg,#A8C7FA,#7C3AED)!important;

    display:flex !important;
    align-items:center;
    justify-content:center;

    border:none !important;
}

div[data-testid="stChatInput"] button:hover{
    transform:translateY(-50%) scale(1.08)!important;
}

    /* Hero Greeting Banner */
    .hero-wrap {
        text-align: center;
        padding: 3rem 0 1rem 0;
        animation: floatIn 0.5s ease-out forwards;
    }

    .hero-title {
        font-size: 3.4rem;
        font-weight: 600;
        background: linear-gradient(135deg, #a8c7fa 0%, #7c3aed 50%, #f28b82 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.4rem;
        letter-spacing: -0.02em;
    }

    .hero-subtitle {
        color: #9a9d9c;
        font-size: 1.25rem;
        font-weight: 400;
        margin-bottom: 2.2rem;
        letter-spacing: -0.01em;
    }

    /* Quick Action Suggestion Cards */
    div[data-testid="column"] .stButton > button {
        background: rgba(30, 31, 32, 0.6) !important;
        backdrop-filter: blur(14px) !important;
        border: 1px solid rgba(255, 255, 255, 0.09) !important;
        border-radius: 18px !important;
        padding: 1.1rem 1.2rem !important;
        min-height: 92px !important;
        text-align: left !important;
        white-space: normal !important;
        color: #e3e3e3 !important;
        font-weight: 400 !important;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    div[data-testid="column"] .stButton > button:hover {
        background: rgba(40, 42, 44, 0.85) !important;
        border-color: rgba(168, 199, 250, 0.4) !important;
        transform: translateY(-3px);
        box-shadow: 0 10px 28px rgba(168, 199, 250, 0.15) !important;
    }

    /* Tool Call Notification Badge */
    .tool-frame-badge {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: linear-gradient(135deg, rgba(168, 199, 250, 0.14), rgba(124, 58, 237, 0.1));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(168, 199, 250, 0.3);
        color: #a8c7fa;
        padding: 11px 20px;
        border-radius: 22px;
        font-size: 0.92rem;
        font-weight: 500;
        margin-bottom: 1rem;
        animation: pulseGlow 2s infinite, fadeInUp 0.3s ease;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #16171a 0%, #0f1011 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.06);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.6rem;
    }

    .sidebar-heading {
        font-size: 1.15rem;
        font-weight: 600;
        background: linear-gradient(135deg, #a8c7fa, #f28b82);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    .sidebar-caption {
        color: #7c7f7e;
        font-size: 0.85rem;
        margin-bottom: 0.6rem;
    }

    /* Status Card */
    .status-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1rem 1.1rem;
        margin-top: 0.6rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    }

    .status-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-size: 0.9rem;
        color: #c9cccb;
        padding: 4px 0;
    }

    .status-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #4ade80;
        box-shadow: 0 0 8px #4ade80;
        margin-right: 6px;
    }

    .tool-chip {
        display: inline-block;
        background: rgba(168, 199, 250, 0.12);
        color: #a8c7fa;
        border: 1px solid rgba(168, 199, 250, 0.25);
        border-radius: 12px;
        padding: 2px 10px;
        font-size: 0.8rem;
        font-family: monospace;
    }

    /* Custom New Chat Button */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05);
        color: #e3e3e3;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 0.65rem 1.2rem;
        font-weight: 500;
        transition: all 0.2s ease;
        width: 100%;
    }

    .stButton > button:hover {
        background: rgba(168, 199, 250, 0.1);
        border-color: #a8c7fa;
        color: #a8c7fa;
    }

    /* Responsive Layout */
    @media (max-width: 768px) {
        .hero-title { font-size: 2.2rem; }
        .hero-subtitle { font-size: 1rem; }
        .block-container { padding-top: 1.2rem; max-width: 100% !important; }
        div[data-testid="stChatInput"] { max-width: 100% !important; }
        div[data-testid="column"] .stButton > button { min-height: 76px !important; }
    }
</style>
""", unsafe_allow_html=True)

# 3. Setup Groq Client
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("⚠️ `GROQ_API_KEY` not found in `.env` file!")
    st.stop()

client = Groq(api_key=api_key)
MODEL = "llama-3.1-8b-instant"

# 4. Live Tool Setup
def get_weather(location: str) -> str:
    """Fetch live weather data from wttr.in."""
    try:
        res = requests.get(f"https://wttr.in/{location}?format=j1", timeout=5)
        if res.status_code == 200:
            data = res.json()["current_condition"][0]
            return json.dumps({
                "temperature_celsius": data["temp_C"],
                "condition": data["weatherDesc"][0]["value"],
                "humidity": f"{data['humidity']}%",
                "wind_speed_kmh": data["windspeedKmph"]
            })
        return json.dumps({"error": "Location not found."})
    except Exception as e:
        return json.dumps({"error": str(e)})

AVAILABLE_TOOLS = {"get_weather": get_weather}

TOOL_SCHEMA = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get real-time weather details for any city or location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name, e.g. Delhi, London, New York"}
            },
            "required": ["location"]
        }
    }
}]

# 5. ReAct Agent Engine
def run_agent_interactive(chat_history, placeholder):
    system_instruction = {
        "role": "system",
        "content": (
            "You are a helpful AI assistant modeled after Google Gemini. You have access to the 'get_weather' tool. "
            "Only call 'get_weather' if the user explicitly asks about weather or temperature. "
            "For all other topics, respond directly in standard formatting."
        )
    }

    messages = [system_instruction] + [
        {"role": m["role"], "content": m["content"]}
        for m in chat_history if m.get("content")
    ]

    for step in range(3):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOL_SCHEMA,
            tool_choice="auto"
        )

        msg = response.choices[0].message
        assistant_msg = {"role": "assistant", "content": msg.content or ""}

        if msg.tool_calls:
            assistant_msg["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments
                    }
                } for tc in msg.tool_calls
            ]

        messages.append(assistant_msg)

        if msg.tool_calls:
            for tool_call in msg.tool_calls:
                fn_name = tool_call.function.name

                if fn_name not in AVAILABLE_TOOLS:
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": fn_name,
                        "content": json.dumps({"error": f"Tool '{fn_name}' not found."})
                    })
                    continue

                fn_args = json.loads(tool_call.function.arguments)
                location_arg = fn_args.get("location", "Location")

                # Animated Badge for Tool Call
                placeholder.markdown(
                    f'<div class="tool-frame-badge">✨ <span>Calling Tool:</span> <b>{fn_name}</b>("{location_arg}")</div>',
                    unsafe_allow_html=True
                )
                time.sleep(0.5)

                tool_output = AVAILABLE_TOOLS[fn_name](**fn_args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": fn_name,
                    "content": tool_output
                })
        else:
            # Gemini-like streaming typewriter response
            full_text = msg.content or "No response returned."
            typed_text = ""
            for char in full_text:
                typed_text += char
                placeholder.markdown(typed_text + "▌")
                time.sleep(0.007)

            placeholder.markdown(typed_text)
            return typed_text

    return "Error: Agent reached execution limit."

# 6. Sidebar Controls
with st.sidebar:
    st.markdown('<div class="sidebar-heading">✨ Agent Workspace</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-caption">Streamlit + Groq Llama 3.1</div>', unsafe_allow_html=True)

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("""
    <div class="status-card">
        <div class="status-row"><span><span class="status-dot"></span>Status</span><span>Online</span></div>
        <div class="status-row"><span>Model</span><span style="font-family: monospace; font-size: 0.82rem;">llama-3.1-8b-instant</span></div>
        <div class="status-row"><span>Active Tool</span><span class="tool-chip">get_weather</span></div>
    </div>
    """, unsafe_allow_html=True)

# 7. Main UI Rendering
if "messages" not in st.session_state:
    st.session_state.messages = []
if "queued_prompt" not in st.session_state:
    st.session_state.queued_prompt = None

# Hero Header + Quick Action Cards when no messages exist
if not st.session_state.messages:
    st.markdown(
        '<div class="hero-wrap">'
        '<div class="hero-title">Hello</div>'
        '<div class="hero-subtitle">How can I help you today?</div>'
        '</div>',
        unsafe_allow_html=True
    )

    quick_actions = [
        ("🌦️", "Check the weather", "What's the weather like in Delhi right now?"),
        ("💡", "Explain a concept", "Explain quantum computing in simple terms."),
        ("✍️", "Write something", "Write a short, friendly email inviting a friend to lunch."),
        ("🧠", "Brainstorm ideas", "Give me 5 creative weekend project ideas."),
    ]

    cols = st.columns(4)
    for col, (icon, label, prompt_text) in zip(cols, quick_actions):
        with col:
            if st.button(f"{icon}  {label}", key=f"quick_{label}", use_container_width=True):
                st.session_state.queued_prompt = prompt_text
                st.rerun()

# Display Conversation History
for message in st.session_state.messages:
    if message["role"] in ["user", "assistant"] and message.get("content"):
        avatar = "👤" if message["role"] == "user" else "✨"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

# Prominent Gemini-Style Input Bar
prompt = st.chat_input("Ask me anything or check weather...")
if not prompt and st.session_state.queued_prompt:
    prompt = st.session_state.queued_prompt
    st.session_state.queued_prompt = None

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="✨"):
        response_placeholder = st.empty()
        final_answer = run_agent_interactive(st.session_state.messages, response_placeholder)
        st.session_state.messages.append({"role": "assistant", "content": final_answer})