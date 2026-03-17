from src.scoring.profile_scoring import compute_profile_score


def calculate_score(candidate_data, skill_results):

    # Skill score (max 40)
    skill_score = (skill_results["match_percentage"] / 100) * 40

    # Profile score
    profile_scores = compute_profile_score(candidate_data)

    github_score = (profile_scores["github_score"] / 10) * 30
    coding_score = (profile_scores["coding_score"] / 10) * 30

    total_score = skill_score + github_score + coding_score

    return {
        "total_score": round(float(total_score), 2),
        "breakdown": {
            "skill_match": round(float(skill_score), 2),
            "github": round(float(github_score), 2),
            "coding_profiles": round(float(coding_score), 2)
        }
}