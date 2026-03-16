import re

def load_skills(file_path="data/skills_dataset.txt"):
    # load skills from data/skills_dataset
    skills = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line:
                cleaned_line = cleaned_line.lower()
                skills.append(cleaned_line)
    return skills

def extract_job_skills(job_text):
    skills_db = load_skills()
    job_text = job_text.lower()
    found_skills = []
    for skill in skills_db:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, job_text):
            found_skills.append(skill)
        
    return found_skills