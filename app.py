import streamlit as st
import requests
from bs4 import BeautifulSoup

from nlp_utils import clean_text, extract_skills
from portfolio import Portfolio
from llm_chain import ColdEmailChain

st.set_page_config(page_title="Cold Email Generator")

st.title("📧 Cold Email Generator (Groq LLM)")

st.subheader("Job Description Input")

job_url = st.text_input("Enter Job URL (optional)")
job_text_manual = st.text_area(
    "Or paste the Job Description here (recommended for career sites)",
    height=250
)

if st.button("Generate Cold Email"):

    # CASE 1: Manual JD pasted (BEST & RECOMMENDED)
    if job_text_manual.strip():
        job_text = clean_text(job_text_manual)

    # CASE 2: URL provided (may fail for Cloudflare sites)
    elif job_url.strip():
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            html = requests.get(job_url, headers=headers, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            job_text = clean_text(soup.get_text())

        except Exception as e:
            st.error("Failed to fetch job description from URL")
            st.stop()

    else:
        st.error("Please provide a job URL or paste job description")
        st.stop()

    # NLP
    skills = extract_skills(job_text)

    # RAG
    portfolio = Portfolio()
    projects = portfolio.retrieve(skills)

    # LLM
    chain = ColdEmailChain()
    email = chain.generate(job_text[:2000], projects)

    

    st.subheader("✉️ Generated Cold Email")
    st.text_area("", email, height=300)
