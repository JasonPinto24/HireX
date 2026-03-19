from .resume_parser import (
    extract_resume_skills,
    extract_candidate_ids,
    extract_name
)

def build_candidate_profile(file_path):
    profile = {}

    profile["skills"] = extract_resume_skills(file_path)
    profile_links = extract_candidate_ids(file_path)
    profile["github_username"] = profile_links.get("github", None)
    profile["leetcode_username"] = profile_links.get("leetcode", None)
    profile["codeforces_username"] = profile_links.get("codeforces", None)
    profile["name"] = extract_name(file_path)

    return profile