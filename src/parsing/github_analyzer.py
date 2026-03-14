from collections import Counter


def analyze_github_profile(profile_data: dict, repos_data: list) -> dict:
    """
    Analyze raw GitHub profile and repository data.
    """
    if not profile_data or "error" in profile_data:
        return {
            "github_followers": 0,
            "github_following": 0,
            "github_public_repos": 0,
            "github_total_stars": 0,
            "github_total_forks": 0,
            "github_top_languages": [],
            "github_recently_active_repos": 0,
        }

    language_counter = Counter()
    total_stars = 0
    total_forks = 0
    recent_active_repos = 0

    for repo in repos_data:
        language = repo.get("language")
        if language:
            language_counter[language] += 1

        total_stars += repo.get("stargazers_count", 0)
        total_forks += repo.get("forks_count", 0)

        if repo.get("updated_at"):
            recent_active_repos += 1

    top_languages = [lang for lang, _ in language_counter.most_common(5)]

    return {
        "github_followers": profile_data.get("followers", 0),
        "github_following": profile_data.get("following", 0),
        "github_public_repos": profile_data.get("public_repos", 0),
        "github_total_stars": total_stars,
        "github_total_forks": total_forks,
        "github_top_languages": top_languages,
        "github_recently_active_repos": recent_active_repos,
        "github_account_created_at": profile_data.get("created_at"),
        "github_profile_url": profile_data.get("html_url"),
    }