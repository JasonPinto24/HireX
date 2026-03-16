def compute_github_score(github_data: dict) -> float:
    """
    Compute a simple GitHub score out of 10.
    """
    repos = github_data.get("github_public_repos", 0)
    stars = github_data.get("github_total_stars", 0)
    forks = github_data.get("github_total_forks", 0)
    followers = github_data.get("github_followers", 0)
    languages = len(github_data.get("github_top_languages", []))

    score = (
        min(repos / 10, 3.0) +
        min(stars / 20, 2.0) +
        min(forks / 10, 1.5) +
        min(followers / 20, 1.5) +
        min(languages / 5, 2.0)
    )

    return round(min(score, 10.0), 2)