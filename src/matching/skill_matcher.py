def normalize_skills(skills):

    #remove spaces and convert to lowercase

    if not skills:
        return []

    return [skill.strip().lower() for skill in skills]


def match_skills(candidate_skills, job_skills):
    
    candidate_skills = normalize_skills(candidate_skills)
    job_skills = normalize_skills(job_skills)

    matched = []
    missing = []

    for skill in job_skills:
        if skill in candidate_skills:
            matched.append(skill)
        else:
            missing.append(skill)

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