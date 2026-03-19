def generate_report(candidate_name, skill_results, total_score_dict):

    total_score = total_score_dict["total_score"]
    breakdown = total_score_dict["breakdown"]

    if total_score >= 80:
        fit = "an excellent fit"
        conclusion = "clearly demonstrates strong alignment with the role requirements."
    elif total_score >= 60:
        fit = "a good fit"
        conclusion = "shows good potential to meet the role requirements."
    elif total_score >= 40:
        fit = "a moderate fit"
        conclusion = "has some relevant skills but may require further development."
    else:
        fit = "not recommended"
        conclusion = "currently does not meet the role requirements effectively."

    matched = skill_results['matched'] or []
    missing = skill_results['missing'] or []
    match_percentage = skill_results['match_percentage']

    report = {
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
        f"{candidate_name} is {fit} for the role, with an overall score of {total_score}/100. "
        f"They demonstrate proficiency in {', '.join(matched) if matched else 'no key skills'}, "
        f"but lack experience in {', '.join(missing) if missing else 'no major gaps identified'}. "
        f"Overall, with a skill match of {match_percentage}%, the candidate {conclusion}"
    )

    return report, paragraph