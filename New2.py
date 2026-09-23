import streamlit as st
import google.generativeai as genai

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="🔮 AstroGuide AI",
    page_icon="✨",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.big-title{
    text-align:center;
    color:#FFD700;
    font-size:50px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:white;
    font-size:20px;
    margin-bottom:30px;
}

.prediction-box{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    border:1px solid #FFD700;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# API KEY
# ==========================

API_KEY = "AQ.Ab8RN6K_nZE9Hyl5i5uWo2i0NsVaPggNSH8GBlZXv2_CDym68w"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-flash-lite-latest")

# ==========================
# SYSTEM INSTRUCTION
# ==========================

SYSTEM_PROMPT = """
You are AstroGuide AI, a friendly astrology assistant.

Provide:
- Daily horoscope
- Weekly forecast
- Love prediction
- Career prediction
- Wellness guidance
- Lucky color
- Lucky number
- Motivational advice

Rules:
- Astrology is for entertainment and inspiration only.
- Never claim certainty about future events.
- Avoid medical, legal, financial, or harmful advice.
- Be positive, engaging, and supportive.
- Use headings and emojis.

Format:

🌟 Daily Horoscope
❤️ Love
💼 Career
🌿 Wellness
🎨 Lucky Color
🔢 Lucky Number
✨ Motivation
"""

# ==========================
# HEADER
# ==========================

st.markdown(
    "<div class='big-title'>🔮 AstroGuide AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Discover Astrology Insights & Daily Predictions ✨</div>",
    unsafe_allow_html=True
)

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:
    st.header("🌙 Zodiac Information")

    zodiac = st.selectbox(
        "Choose Your Zodiac Sign",
        [
            "Aries","Taurus","Gemini","Cancer",
            "Leo","Virgo","Libra","Scorpio",
            "Sagittarius","Capricorn","Aquarius","Pisces"
        ]
    )

    prediction_type = st.selectbox(
        "Prediction Type",
        [
            "Daily Horoscope",
            "Weekly Horoscope",
            "Love Prediction",
            "Career Prediction",
            "Full Reading"
        ]
    )

# ==========================
# USER QUERY
# ==========================

user_question = st.text_area(
    "✨ Ask AstroGuide AI",
    placeholder="Example: What does this week look like for my career?"
)

# ==========================
# GENERATE BUTTON
# ==========================

if st.button("🔮 Generate Prediction", use_container_width=True):

    prompt = f"""
    {SYSTEM_PROMPT}

    Zodiac Sign: {zodiac}

    Request: {prediction_type}

    User Question:
    {user_question}

    Generate a detailed astrology reading.
    """

    try:
        with st.spinner("🔮 Reading the stars..."):
            response = model.generate_content(prompt)

        st.markdown("### ✨ Your Astrology Reading")

        st.markdown(
            f"""
            <div class='prediction-box'>
            {response.text}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "⚠️ Astrology readings are provided for entertainment and self-reflection purposes only."
        )

    except Exception as e:
        st.error(f"Error: {e}")

# ==========================
# FOOTER
# ==========================

st.markdown(
    """
    <div class='footer'>
    ✨ AstroGuide AI | Entertainment Only | Powered by Gemini AI ✨
    </div>
    """,
    unsafe_allow_html=True
)
