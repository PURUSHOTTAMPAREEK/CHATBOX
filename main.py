
import streamlit as st
from langgraph_flow import run_conversation

st.set_page_config(page_title="🏗️ SmartBuilder AI", layout="wide")

# Custom builder-style CSS
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
        }
        .stTextInput > div > div {
            border-radius: 6px;
            border: 1px solid #ccc;
            padding: 0.75rem;
            background-color: #ffffff;
        }
        .stButton > button {
            background-color: #1a73e8;
            color: white;
            font-weight: 600;
            font-size: 16px;
            border-radius: 6px;
            padding: 0.6rem 1.2rem;
        }
        .stButton > button:hover {
            background-color: #1558b0;
        }
        h1, h3 {
            color: #0a3d62;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🏗️ SmartBuilder AI")

# Subheading
st.markdown("### 👷 Enter your site challenge or project question")

# Input field
query = st.text_input("", placeholder="e.g., How can I optimize cement usage in slab casting?")

# Button and result
if st.button("🔧 Generate Strategy") and query:
    with st.spinner("🧱 Calculating the best construction approach..."):
        result = run_conversation(query)
        st.success("🏁 Here's your optimized site solution!")
        st.markdown("### 📋 Site Strategy Recommendation:")
        st.write(result)
