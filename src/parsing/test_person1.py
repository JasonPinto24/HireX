from src.parsing.profile_analytics_builder import build_profile_analytics
from src.scoring.candidate_score import compute_profile_score


if __name__ == "__main__":
    candidate_profile = {
        "github_username": "JasonPinto24",
        "leetcode_username": None,
        "codeforces_handle": None
    }

    analytics = build_profile_analytics(candidate_profile)
    scores = compute_profile_score(analytics)

    print("\n===== ANALYTICS =====")
    for key, value in analytics.items():
        print(f"{key}: {value}")

    print("\n===== SCORES =====")
    for key, value in scores.items():
        print(f"{key}: {value}")