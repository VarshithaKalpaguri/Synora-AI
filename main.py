import streamlit as st
from ollama import chat

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Synora AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# COLOR PALETTE
# ============================================================

PRIMARY = "#4F6DF5"
SECONDARY = "#7C6FF2"
ACCENT = "#38BDF8"

TEXT = "#172554"
TEXT_SECONDARY = "#64748B"

BACKGROUND = "#F4F8FF"
CARD = "#FFFFFF"

USER_BG = "#E7F0FF"
BORDER = "#DCE7FA"

# ============================================================
# CUSTOM CSS
# ============================================================

st.html(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ==========================================================
   GLOBAL
   ========================================================== */

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(56, 189, 248, 0.15),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(124, 111, 242, 0.14),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #F8FBFF 0%,
            #F1F6FF 50%,
            #F7F5FF 100%
        );

    color: {TEXT};
}}

/* ==========================================================
   MAIN CONTAINER
   ========================================================== */

.block-container {{
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 6rem;
}}

/* ==========================================================
   SIDEBAR
   ========================================================== */

section[data-testid="stSidebar"] {{
    background:
        linear-gradient(
            180deg,
            #FFFFFF 0%,
            #F4F8FF 100%
        );

    border-right: 1px solid {BORDER};
}}

section[data-testid="stSidebar"] > div {{
    padding-top: 1.5rem;
}}

/* Sidebar logo */

.sidebar-brand {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
}}

.sidebar-logo {{
    width: 38px;
    height: 38px;
    border-radius: 12px;

    display: flex;
    align-items: center;
    justify-content: center;

    background:
        linear-gradient(
            135deg,
            {PRIMARY},
            {SECONDARY}
        );

    color: white;
    font-size: 21px;

    box-shadow:
        0 8px 20px rgba(79, 109, 245, 0.25);
}}

.sidebar-title {{
    font-size: 25px;
    font-weight: 800;
    color: {PRIMARY};
}}

.sidebar-description {{
    color: {TEXT_SECONDARY};
    font-size: 13px;
    line-height: 1.7;
    margin-bottom: 22px;
}}

/* Sidebar headings */

.sidebar-heading {{
    color: {TEXT};
    font-weight: 700;
    font-size: 14px;
    margin: 18px 0 10px 0;
}}

/* ==========================================================
   SIDEBAR BUTTONS
   ========================================================== */

.stButton > button {{
    width: 100%;
    min-height: 43px;

    border-radius: 13px;

    border: 1px solid {BORDER};

    background: rgba(255, 255, 255, 0.85);

    color: {TEXT};

    font-weight: 600;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        border-color 0.2s ease;
}}

.stButton > button:hover {{
    transform: translateY(-1px);

    border-color: #BFD0F7;

    box-shadow:
        0 8px 20px rgba(79, 109, 245, 0.10);

    color: {PRIMARY};
}}

/* ==========================================================
   HERO / HEADER
   ========================================================== */

.hero {{
    position: relative;
    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.95),
            rgba(239,246,255,0.92)
        );

    border: 1px solid {BORDER};

    border-radius: 28px;

    padding: 38px 42px;

    margin-bottom: 22px;

    box-shadow:
        0 15px 45px rgba(71, 94, 145, 0.08);
}}

.hero::before {{
    content: "";

    position: absolute;

    width: 220px;
    height: 220px;

    right: -70px;
    top: -90px;

    background:
        radial-gradient(
            circle,
            rgba(56,189,248,0.25),
            transparent 70%
        );

    border-radius: 50%;
}}

.hero::after {{
    content: "";

    position: absolute;

    width: 250px;
    height: 150px;

    right: 80px;
    bottom: -110px;

    background:
        radial-gradient(
            circle,
            rgba(124,111,242,0.18),
            transparent 70%
        );

    border-radius: 50%;
}}

.hero-content {{
    position: relative;
    z-index: 2;
    max-width: 700px;
}}

.hero-small {{
    display: inline-block;

    padding: 6px 12px;

    border-radius: 20px;

    background: #EEF4FF;

    color: {PRIMARY};

    font-size: 12px;
    font-weight: 700;

    margin-bottom: 12px;
}}

.hero-title {{
    font-size: 44px;

    line-height: 1.1;

    font-weight: 800;

    color: {TEXT};

    margin: 0;
}}

.hero-title span {{
    background:
        linear-gradient(
            90deg,
            {PRIMARY},
            {SECONDARY}
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.hero-description {{
    color: {TEXT_SECONDARY};

    font-size: 15px;

    line-height: 1.7;

    margin-top: 14px;

    max-width: 720px;
}}

/* ==========================================================
   HERO FEATURES
   ========================================================== */

.feature-row {{
    display: flex;
    gap: 10px;
    margin-top: 22px;
    flex-wrap: wrap;
}}

.feature {{
    display: flex;
    align-items: center;
    gap: 7px;

    padding: 9px 14px;

    border-radius: 30px;

    background: rgba(255,255,255,0.80);

    border: 1px solid {BORDER};

    color: {TEXT};

    font-size: 12px;
    font-weight: 600;
}}

/* ==========================================================
   ROBOT
   ========================================================== */

.robot {{
    position: absolute;

    right: 55px;
    top: 45px;

    width: 120px;
    height: 120px;

    border-radius: 35px;

    background:
        linear-gradient(
            145deg,
            #FFFFFF,
            #E9F2FF
        );

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 65px;

    box-shadow:
        0 18px 40px rgba(79,109,245,0.16);

    border: 1px solid rgba(255,255,255,0.9);
}}

/* ==========================================================
   STATUS
   ========================================================== */

.status {{
    display: flex;
    justify-content: center;

    margin: 10px 0 22px;
}}

.status-pill {{
    display: inline-flex;
    align-items: center;
    gap: 8px;

    padding: 8px 15px;

    border-radius: 30px;

    background: rgba(255,255,255,0.85);

    border: 1px solid #DDEBDD;

    color: #16845B;

    font-size: 12px;
    font-weight: 600;

    box-shadow:
        0 5px 20px rgba(71,94,145,0.05);
}}

.status-dot {{
    width: 8px;
    height: 8px;

    border-radius: 50%;

    background: #22C55E;

    box-shadow:
        0 0 0 4px rgba(34,197,94,0.12);
}}

/* ==========================================================
   WELCOME CARD
   ========================================================== */

.welcome-card {{
    background:
        rgba(255,255,255,0.82);

    border: 1px solid {BORDER};

    border-radius: 22px;

    padding: 20px 24px;

    margin-bottom: 22px;

    box-shadow:
        0 10px 30px rgba(71,94,145,0.05);
}}

.welcome-title {{
    color: {PRIMARY};

    font-size: 17px;

    font-weight: 700;

    margin-bottom: 7px;
}}

.welcome-text {{
    color: {TEXT_SECONDARY};

    font-size: 14px;

    line-height: 1.7;
}}

/* ==========================================================
   CHAT MESSAGE CONTAINER
   ========================================================== */

[data-testid="stChatMessage"] {{
    border-radius: 20px;

    padding: 14px 18px;

    margin-bottom: 12px;
}}

/* User message */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) {{
    background:
        linear-gradient(
            135deg,
            #EAF2FF,
            #E2EDFF
        );

    border: 1px solid #D6E4FA;

    box-shadow:
        0 7px 25px rgba(79,109,245,0.06);
}}

/* Assistant message */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-assistant"]
) {{
    background:
        rgba(255,255,255,0.92);

    border: 1px solid {BORDER};

    box-shadow:
        0 10px 30px rgba(71,94,145,0.07);
}}

/* Chat text */

[data-testid="stChatMessage"] p {{
    color: {TEXT} !important;

    font-size: 15px;

    line-height: 1.75;
}}

/* ==========================================================
   CHAT INPUT
   ========================================================== */

[data-testid="stChatInput"] {{
    background: white;

    border: 2px solid #DCE7FA;

    border-radius: 22px;

    box-shadow:
        0 12px 35px rgba(71,94,145,0.10);
}}

[data-testid="stChatInput"] textarea {{
    color: {TEXT} !important;

    font-size: 15px;
}}

[data-testid="stChatInput"] textarea::placeholder {{
    color: #94A3B8 !important;
}}

/* ==========================================================
   SESSION CARD
   ========================================================== */

.session-card {{
    background:
        rgba(255,255,255,0.85);

    border: 1px solid {BORDER};

    border-radius: 18px;

    padding: 16px;

    margin-top: 15px;
}}

.session-title {{
    color: {TEXT};

    font-weight: 700;

    font-size: 14px;

    margin-bottom: 10px;
}}

.session-item {{
    display: flex;
    justify-content: space-between;

    color: {TEXT_SECONDARY};

    font-size: 12px;

    padding: 5px 0;
}}

.session-value {{
    color: {TEXT};

    font-weight: 600;
}}

/* ==========================================================
   FOOTER
   ========================================================== */

.footer {{
    text-align: center;

    color: #94A3B8;

    font-size: 11px;

    padding: 30px 0;
}}

/* ==========================================================
   MOBILE
   ========================================================== */

@media (max-width: 800px) {{

    .hero {{
        padding: 28px;
    }}

    .hero-title {{
        font-size: 34px;
    }}

    .robot {{
        display: none;
    }}

}}

</style>
""")

# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": """
You are Synora, a friendly AI assistant.

Be helpful, friendly and practical.
Explain difficult concepts simply.
Use examples when useful.
Help with programming, learning, projects and general questions.
Keep answers reasonably concise.
Do not invent information.
"""
        }
    ]

if "message_count" not in st.session_state:
    st.session_state.message_count = 0

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div class="sidebar-brand">

        <div class="sidebar-logo">
            🤖
        </div>

        <div class="sidebar-title">
            Synora
        </div>

    </div>

    <div class="sidebar-description">
        Your friendly AI companion running locally
        with <b>Ollama + Gemma 3</b>.
    </div>
    """)

    st.html("""
    <div class="sidebar-heading">
        💬 Chat
    </div>
    """)

    # New chat
    if st.button("✨ New Chat"):

        st.session_state.messages = [
            {
                "role": "system",
                "content": """
You are Synora, a friendly AI assistant.

Be helpful, friendly and practical.
Explain difficult concepts simply.
Use examples when useful.
"""
            }
        ]

        st.session_state.message_count = 0

        st.rerun()

    # Clear conversation
    if st.button("🗑️ Clear Conversation"):

        st.session_state.messages = [
            {
                "role": "system",
                "content": """
You are Synora, a friendly AI assistant.
Be helpful, clear and practical.
"""
            }
        ]

        st.session_state.message_count = 0

        st.rerun()

    st.divider()

    st.html("""
    <div class="sidebar-heading">
        💡 Try asking
    </div>
    """)

    # Quick prompt buttons
    quick_prompts = [
        "Explain Python loops",
        "What is an API?",
        "Give me a project idea",
        "Help me debug my code",
        "Explain AI simply",
        "What is machine learning?"
    ]

    for prompt in quick_prompts:

        if st.button(
            f"›  {prompt}",
            key=f"prompt_{prompt}"
        ):

            st.session_state.pending_prompt = prompt

            st.rerun()

    st.divider()

    # Session info
    st.html(f"""
    <div class="session-card">

        <div class="session-title">
            📊 Session Info
        </div>

        <div class="session-item">
            <span>💬 Messages</span>
            <span class="session-value">
                {st.session_state.message_count}
            </span>
        </div>

        <div class="session-item">
            <span>🧠 Model</span>
            <span class="session-value">
                Gemma 3 1B
            </span>
        </div>

        <div class="session-item">
            <span>⚡ Runtime</span>
            <span class="session-value">
                Ollama
            </span>
        </div>

        <div class="session-item">
            <span>💻 Interface</span>
            <span class="session-value">
                Streamlit
            </span>
        </div>

    </div>
    """)

# ============================================================
# MAIN HERO
# ============================================================

st.html("""
<div class="hero">

    <div class="hero-content">

        <div class="hero-small">
            ✨ LOCAL AI ASSISTANT
        </div>

        <div class="hero-title">
            Welcome to <span>Synora</span>
        </div>

        <div class="hero-description">
            Ask questions, learn concepts, brainstorm projects,
            debug code or simply have a conversation.
            Synora runs a local AI model through Ollama.
        </div>

        <div class="feature-row">

            <div class="feature">
                📚 Learn
            </div>

            <div class="feature">
                💻 Code
            </div>

            <div class="feature">
                💡 Ideas
            </div>

            <div class="feature">
                💬 Chat
            </div>

        </div>

    </div>

    <div class="robot">
        🤖
    </div>

</div>
""")

# ============================================================
# STATUS
# ============================================================

st.html("""
<div class="status">

    <div class="status-pill">

        <span class="status-dot"></span>

        Local AI • Ollama Ready

    </div>

</div>
""")

# ============================================================
# WELCOME CARD
# ============================================================

if len(st.session_state.messages) == 1:

    st.html("""
    <div class="welcome-card">

        <div class="welcome-title">
            👋 What can I help you with?
        </div>

        <div class="welcome-text">
            Ask Synora about programming, AI, projects,
            college subjects, debugging or anything you
            want to understand.
        </div>

    </div>
    """)

# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    if message["role"] == "user":

        avatar = "🧑‍💻"

    else:

        avatar = "🤖"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):

        st.markdown(message["content"])

# ============================================================
# CHECK QUICK PROMPT
# ============================================================

question = None

if "pending_prompt" in st.session_state:

    question = st.session_state.pending_prompt

    del st.session_state.pending_prompt

# ============================================================
# NORMAL CHAT INPUT
# ============================================================

typed_question = st.chat_input(
    "Ask Synora anything..."
)

if typed_question:

    question = typed_question

# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    # --------------------------------------------------------
    # Save user message
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    st.session_state.message_count += 1

    # --------------------------------------------------------
    # Display user
    # --------------------------------------------------------

    with st.chat_message(
        "user",
        avatar="🧑‍💻"
    ):

        st.markdown(question)

    # --------------------------------------------------------
    # Generate AI response
    # --------------------------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        with st.spinner("Synora is thinking..."):

            try:

                # Keep recent conversation
                conversation = st.session_state.messages[-12:]

                response = chat(
                    model="gemma3:1b",
                    messages=conversation
                )

                answer = response.message.content

                st.markdown(answer)

                # Save response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as error:

                st.error(
                    "⚠️ Synora couldn't connect to Ollama."
                )

                st.info(
                    """
                    Make sure Ollama is running.

                    Run:

                    ollama run gemma3:1b
                    """
                )

                st.caption(
                    f"Technical error: {error}"
                )

# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">
    Synora AI • Built with Streamlit + Ollama + Gemma 3
</div>
""")