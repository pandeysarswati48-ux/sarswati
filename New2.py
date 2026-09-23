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
# GEMINI API KEY
# ==========================

API_KEY = "AQ.Ab8RN6K_nZE9Hyl5i5uWo2i0NsVaPggNSH8GBlZXv2_CDym68w"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.6-flash")

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>
.stApp{
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
    margin-bottom:20px;
}

.prediction-box{
    background:#1e293b;
    color:white;
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
# SYSTEM PROMPT
# ==========================

SYSTEM_PROMPT = """
You are AstroGuide AI.

Provide:
- Daily Horoscope
- Weekly Forecast
- Love Prediction
- Career Prediction
- Wellness Guidance
- Lucky Color
- Lucky Number
- Motivational Advice

Rules:
- Astrology is for entertainment purposes only.
- Never guarantee future events.
- Be positive and friendly.
- Use headings and emojis.
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
# USER INPUT
# ==========================

question = st.text_area(
    "✨ Ask AstroGuide AI",
    placeholder="What does this week look like for my career?"
)

# ==========================
# BUTTON
# ==========================

if st.button("🔮 Generate Prediction"):

    prompt = f"""
    {SYSTEM_PROMPT}

    Zodiac Sign: {zodiac}

    Prediction Type: {prediction_type}

    User Question:
    {question}
    """

    try:

        with st.spinner("Reading the stars... ✨"):

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
            "⚠️ Astrology readings are for entertainment and self-reflection only."
        )

    except Exception as e:

        st.error(f"Error: {str(e)}")

# ==========================
# FOOTER
# ==========================

st.markdown(
    """
    <div class='footer'>
    ✨ AstroGuide AI | Powered by Gemini ✨
    </div>
    """,
    unsafe_allow_html=True
)
