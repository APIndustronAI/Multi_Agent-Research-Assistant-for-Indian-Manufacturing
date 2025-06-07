import streamlit as st
from orchestrator import run_research_pipeline

st.title("🧠 Multi-Agent Research Assistant for Future Manufacturing")
topic = st.text_input("Enter a research topic")

if st.button("Run Research"):
    result = run_research_pipeline(topic)
    st.subheader("🔍 Search Results")
    st.text(result["search"])
    st.subheader("📝 Summary")
    st.text(result["summary"])
    st.subheader("✅ Fact Checker Feedback")
    st.text(result["corrections"])
    st.subheader("📄 Final Report")
    st.write(result["report"])