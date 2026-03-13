import streamlit as st
from src.matching import match_skills
from src.scoring import calculate_score
from src.explanation import generate_report

st.title("HireX Candidate Analyzer")

resume_file = st.file_uploader("Upload Candidate Resume", type=["pdf", "docx"])
job_file = st.file_uploader("Upload Job Description", type=["pdf", "docx"])

if resume_file and job_file:

   
    candidate_info = parse_resume(resume_file)


    candidate_name = candidate_info.get("name", "Unknown")
    resume_skills = candidate_info.get("skills", [])
    github_username = candidate_info.get("github_username", None)

  
    job_skills = parse_resume(job_file).get("skills", [])

   
    if github_username:
        candidate_data = fetch_github_data(github_username)
        github_skills = candidate_data.get("languages", [])
    else:
        st.warning("GitHub username not found in resume. Using only resume skills.")
        candidate_data = {"repo_metrics": {}, "activity": [], "languages": []}
        github_skills = []

    
    # Combine Resume and GitHub Skills
   
    candidate_skills_combined = list(set(resume_skills + github_skills))

  
    skill_results = match_skills(candidate_skills_combined, job_skills)
    total_score_dict = calculate_score(candidate_data, skill_results)

    report_dict, paragraph = generate_report(candidate_name, skill_results, total_score_dict)

    st.subheader("Candidate Fit Summary")
    st.write(paragraph)

    st.subheader("Detailed Report")
    st.json(report_dict)