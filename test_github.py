from src.parsing.github_fetcher import fetch_github_profile, fetch_github_repositories
from src.parsing.github_analyzer import analyze_github_profile
from src.scoring.github_scoring import compute_github_score

# 🔥 CHANGE THIS USERNAME
username = "torvalds"   # or your GitHub username

print("Fetching data...")

profile = fetch_github_profile(username)
repos = fetch_github_repositories(username)

print("Analyzing profile...")

analysis = analyze_github_profile(profile, repos)

print("\n=== ANALYSIS ===")
for k, v in analysis.items():
    print(f"{k}: {v}")

print("\nComputing score...")

score = compute_github_score(analysis)

print("\n=== FINAL SCORE ===")
print(score)