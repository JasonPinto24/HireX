
def generate_report(candidate_name, skill_results, total_score_dict):
   
    total_score = total_score_dict["total_score"]
    breakdown = total_score_dict["breakdown"]
    
    if total_score >= 80:
        fit = "excellent fit"
    elif total_score >= 60:
        fit = "good fit"
    elif total_score >= 40:
        fit = "average fit"
    else:
        fit = "not recommended"
    
    matched = skill_results['matched'] if skill_results['matched'] else []
    missing = skill_results['missing'] if skill_results['missing'] else []
    match_percentage = skill_results['match_percentage']
    
    report={
        "candidate_name": candidate_name,
        "skill_matching": {
            "matched_skills": matched,
            "missing_skills": missing,
            "match_percentage": match_percentage
        },
        "score_breakdown": breakdown,
        "total_score": total_score,
        "fit_conclusion": fit
    }
    paragraph = (
        f"{candidate_name} appears to be a {fit} for the role, scoring {total_score} out of 100. "
        f"Key skills matched include {', '.join(matched) if matched else 'none'}, "
        f"while the candidate is missing {', '.join(missing) if missing else 'none'}. "
        f"With a skill match of {match_percentage}%, combined with their activity and experience, "
        f"this profile suggests the candidate has the ability to meet the role requirements effectively."
    )
    
    return report,paragraph