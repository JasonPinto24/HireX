import streamlit as st

st.title("HireX Candidate Analyzer")

username = st.text_input("GitHub Username")

if st.button("Analyze"):

    st.metric("Candidate Score", -)

    st.write("### Strengths")
    st.write("-")

    st.write("### Weaknesses")
    st.write("-")