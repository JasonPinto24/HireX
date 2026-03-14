import requests


GITHUB_API_BASE = "https://api.github.com"


def fetch_github_profile(github_username: str) -> dict:
    """
    Fetch GitHub user profile data.
    """
    if not github_username:
        return {}

    url = f"{GITHUB_API_BASE}/users/{github_username}"
    response = requests.get(url, timeout=15)

    if response.status_code != 200:
        return {"error": f"Failed to fetch GitHub profile for {github_username}"}

    return response.json()


def fetch_github_repositories(github_username: str) -> list:
    """
    Fetch public repositories for a GitHub user.
    """
    if not github_username:
        return []

    url = f"{GITHUB_API_BASE}/users/{github_username}/repos?per_page=100"
    response = requests.get(url, timeout=15)

    if response.status_code != 200:
        return []

    return response.json()