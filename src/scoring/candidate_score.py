
def skill_match_score(skill_results):
    """""
    Max: 40 points
    """

    return (skill_results["match_percentage"] / 100) * 40


def repo_score(candidate_data):
    """
    Max: 20 points
    """

    repos = candidate_data.get("repo_metrics", {}).get("total_repos", 0)

    return min(repos * 2, 20)


import datetime

def activity_score(candidate_data):
    """
    Max: 20 points
    Considers recency of commits: recent commits weigh more.
    """
    commits = candidate_data.get("activity", []) 
    total_score = 0
    now = datetime.datetime.now()

    for commit in commits:
        # commit date should be a datetime object, or parse if string
        date = commit.get("date")
        if isinstance(date, str):
            date = datetime.datetime.fromisoformat(date) 
        age_days = (now - date).days
        weight = max(0, 1 - age_days / 365) 
        total_score += weight

    return min(total_score, 20)


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