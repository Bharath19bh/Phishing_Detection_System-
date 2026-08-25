# ============================================
# ADVANCED PHISHING URL DETECTION DASHBOARD
# WITH PHISHING REASON EXPLANATION
# ============================================

import streamlit as st
import joblib
import validators
import webbrowser
import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import plotly.graph_objects as go

# --------------------------------------------
# PAGE CONFIG
# --------------------------------------------

st.set_page_config(
    page_title="AI Phishing Shield",
    page_icon="🛡️",
    layout="centered"
)

# --------------------------------------------
# CSS
# --------------------------------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg,#0f0c29,#302b63,#24243e,#1f4037);
    background-size:400% 400%;
    animation:gradientBG 10s ease infinite;
    color:white;
}
@keyframes gradientBG {
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.safe{
background:linear-gradient(90deg,#00c853,#00e676);
padding:20px;
border-radius:20px;
text-align:center;
font-size:22px;
font-weight:bold;
}

.danger{
background:linear-gradient(90deg,#ff1744,#ff5252);
padding:20px;
border-radius:20px;
text-align:center;
font-size:22px;
font-weight:bold;
}

.reason{
background:rgba(255,255,255,0.08);
padding:15px;
border-radius:15px;
margin-top:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------
# LOAD MODEL
# --------------------------------------------

@st.cache_resource
def load_model_files():
    model = load_model("cnn_bilstm_phishing_model.h5")
    tokenizer = joblib.load("tokenizer_cnn.pkl")
    return model, tokenizer

model, tokenizer = load_model_files()
max_length = 120

# --------------------------------------------
# HEADER
# --------------------------------------------

st.title("🛡️ AI Phishing Shield")
st.caption("CNN-BiLSTM Deep Learning URL Security Scanner")

url_input = st.text_input("🌍 Enter Website URL")

# --------------------------------------------
# PHISHING REASON ANALYSIS
# --------------------------------------------

def analyze_url(url):

    reasons = []

    # IP address detection
    ip_pattern = r'http[s]?://\d+\.\d+\.\d+\.\d+'
    if re.search(ip_pattern, url):
        reasons.append("⚠️ URL contains an IP address instead of a domain")

    # Too long URL
    if len(url) > 75:
        reasons.append("⚠️ URL length is unusually long")

    # @ symbol
    if "@" in url:
        reasons.append("⚠️ URL contains '@' symbol which hides real domain")

    # Too many dots
    if url.count(".") > 3:
        reasons.append("⚠️ URL has too many subdomains")

    # Hyphen in domain
    if "-" in url:
        reasons.append("⚠️ Suspicious hyphen '-' in domain")

    # HTTP instead of HTTPS
    if url.startswith("http://"):
        reasons.append("⚠️ Website not using secure HTTPS")

    # Suspicious keywords
    suspicious_words = [
        "login","verify","update","bank","secure","account",
        "paypal","confirm","password","signin"
    ]

    for word in suspicious_words:
        if word in url.lower():
            reasons.append(f"⚠️ Suspicious keyword detected: '{word}'")

    return reasons

# --------------------------------------------
# PREDICTION
# --------------------------------------------

def predict_url(url):
    sequence = tokenizer.texts_to_sequences([url])
    padded = pad_sequences(sequence, maxlen=max_length, padding='post')
    prediction = model.predict(padded, verbose=0)
    return float(prediction[0][0])

# --------------------------------------------
# BUTTON
# --------------------------------------------

if st.button("🔎 Scan Now"):

    if not url_input:
        st.warning("⚠️ Enter URL")
    
    elif not validators.url(url_input):
        st.error("❌ Invalid URL")
    
    else:

        with st.spinner("🧠 AI analyzing URL..."):
            probability = predict_url(url_input)

        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability*100,
            title={'text':"Phishing Risk %"},
            gauge={
                'axis':{'range':[0,100]},
                'bar':{'color':"red" if probability>0.5 else "green"},
                'steps':[
                    {'range':[0,50],'color':"#00c853"},
                    {'range':[50,100],'color':"#ff1744"}
                ]
            }
        ))

        st.plotly_chart(fig)

        # Result
        if probability > 0.5:

            st.markdown(
                '<div class="danger">🚨 PHISHING WEBSITE DETECTED</div>',
                unsafe_allow_html=True
            )

            # Show reasons
            reasons = analyze_url(url_input)

            st.subheader("⚠️ Possible Reasons")

            if reasons:
                for r in reasons:
                    st.markdown(f'<div class="reason">{r}</div>', unsafe_allow_html=True)
            else:
                st.info("AI detected phishing patterns in URL structure.")

        else:

            st.markdown(
                '<div class="safe">✅ SAFE WEBSITE</div>',
                unsafe_allow_html=True
            )

            if st.button("🌐 Visit Website"):
                webbrowser.open_new_tab(url_input)

# --------------------------------------------
# FOOTER
# --------------------------------------------

st.caption("🛡️ AI Cyber Security System | CNN-BiLSTM Model")