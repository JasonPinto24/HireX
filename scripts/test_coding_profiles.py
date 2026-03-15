from src.services.coding_profile_service import analyze_coding_profiles

result = analyze_coding_profiles(
    codeforces_handle="tourist",
    leetcode_username="Jason_Pinto"
)

print(result)