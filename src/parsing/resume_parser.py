import fitz
import re
import spacy

nlp = spacy.load("en_core_web_sm")

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

def extract_candidate_phrases(text):
    doc = nlp(text)
    candidates = []
    for ent in doc.ents:
        candidates.append(ent.text.lower())
    
    for chunk in doc.noun_chunks:
        candidates.append(chunk.text.lower())
    
    return list(set(candidates))

def extract_resume_skills(file_path):
    # create a skills list given in resume
    skills_db = load_skills()
    text = extract_text_from_pdf(file_path)
    candidates = extract_candidate_phrases(text)
    found_skills = []
    for candidate in candidates:
        if candidate in skills_db:
            found_skills.append(candidate)
    return found_skills