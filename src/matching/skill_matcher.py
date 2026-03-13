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


def match_skills(candidate_skills, job_skills, min_similarity=0.3):
  
    #returns partial skill matches based on similarity.
    #skills with similarity >= min_similarity are considered partially matched.
    

    candidate_embeddings = embed_skills(candidate_skills)
    job_embeddings = embed_skills(job_skills)

    matched = []
    missing = []

    total_score=0

    for i, job_vec in enumerate(job_embeddings):

        #enumerate: This allows you to loop through a sequence 
        #and have access to both the index and the element at the same time

        similarity_scores = cosine_similarity(
            [job_vec], candidate_embeddings
        )[0]

        best_score = max(similarity_scores)
        total_score+=best_score
        max_score=len(job_skills)

        match_percentage = (total_score / max_score) * 100 if max_score > 0 else 0


        if best_score >= min_similarity:
            matched.append(job_skills[i])
        else:
            missing.append(job_skills[i])



    return {
        "matched": matched,
        "missing": missing,
        "match_count": len(matched),
        "total_required": len(job_skills),
        "match_percentage": round(match_percentage,2)
        
    }

