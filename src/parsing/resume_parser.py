import fitz
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

def extract_resume_skills(file_path):
    # create a skills list given in resume
    skills_db = load_skills()
    text = extract_text_from_pdf(file_path)
    found_skills = []
    for skill in skills_db:
        # create regex pattern of all skills to search in resume text
        pattern = r"\b(" + "|".join(map(re.escape, skills_db)) + r")\b"
        matches = re.findall(pattern, text)
        found_skills = list(set(matches))
    return found_skills