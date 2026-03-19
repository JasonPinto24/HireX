import re
import os


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
SKILLS_PATH = os.path.join(BASE_DIR, "data", "skills_dataset.txt")

def load_skills(file_path=SKILLS_PATH):
    # load skills from data/skills_dataset
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Skills file not found at: {file_path}")
    skills = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line:
                cleaned_line = cleaned_line.lower()
                skills.append(cleaned_line)
    return skills

def extract_text_from_pdf(file_path):
    # get text from resume pdf
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            content = page.get_text()
            if content:
                text += content + " "
    
    text = re.sub(r"\s+", " ", text)
    return text.lower()

def extract_job_skills(file_path):
    job_text = extract_text_from_pdf(file_path)
    skills_db = load_skills()
    job_text = job_text.lower()

    found_skills = []

    for skill in skills_db:
        skill_lower = skill.lower()

       
       

        if skill_lower == "c":
            # match standalone 'c' only (not inside c++)
            if re.search(r"(?:^|[^a-zA-Z0-9])c(?:[^a-zA-Z0-9]|$)", job_text):
                found_skills.append("c")
            continue

        # ✅ Normal skills
        pattern = r"(?<!\w)" + re.escape(skill_lower) + r"(?!\w)"

        if re.search(pattern, job_text):
            found_skills.append(skill_lower)

    return list(set(found_skills))
        
    