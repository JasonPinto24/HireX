from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def normalize_skills(skills):

    #remove spaces and convert to lowercase

    if not skills:
        return []

    return [skill.strip().lower() for skill in skills]


def embed_skills(skills):

    return model.encode(skills)


def match_skills(candidate_skills, job_skills, threshold=0.6):
  

    candidate_embeddings = embed_skills(candidate_skills)
    job_embeddings = embed_skills(job_skills)

    matched = []
    missing = []

    for i, job_vec in enumerate(job_embeddings):

        #enumerate: This allows you to loop through a sequence 
        #and have access to both the index and the element at the same time
        
        similarity_scores = cosine_similarity(
            [job_vec], candidate_embeddings
        )[0]

        best_score = max(similarity_scores)

        if best_score >= threshold:
            matched.append(job_skills[i])
        else:
            missing.append(job_skills[i])

    return {
        "matched": matched,
        "missing": missing,
        "match_count": len(matched),
        "total_required": len(job_skills)
    }

def calculate_match_percentage(skill_results):
    
    total = skill_results["total_required"]
    matched = skill_results["match_count"]

    if total == 0:
        return 0

    return (matched / total) * 100