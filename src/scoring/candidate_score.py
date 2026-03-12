
def skill_match_score(skill_results):
    """""
    Max: 40 points
    """

    matched = skill_results["match_count"]
    total = skill_results["total_required"]

    if total == 0:
        return 0

    percentage = matched / total

    return percentage * 40


def repo_score(candidate_data):
    """
    Max: 20 points
    """

    repos = candidate_data.get("repo_metrics", {}).get("total_repos", 0)

    return min(repos * 2, 20)


def activity_score(candidate_data):
    """
    Max: 20 points
    """

    commits = candidate_data.get("activity", {}).get("commits_last_year", 0)

    return min(commits / 50, 20)


def language_diversity_score(candidate_data):
    """
    Max: 20 points
    """

    languages = candidate_data.get("languages", [])

    return min(len(languages) * 5, 20)


def calculate_score(candidate_data, skill_results):
  
    s1 = skill_match_score(skill_results)
    s2 = repo_score(candidate_data)
    s3 = activity_score(candidate_data)
    s4 = language_diversity_score(candidate_data)

    total_score = s1 + s2 + s3 + s4

    return {
        "total_score": round(total_score, 2),
        "breakdown": {
            "skill_match": round(s1, 2),
            "repos": round(s2, 2),
            "activity": round(s3, 2),
            "languages": round(s4, 2)
        }
    }