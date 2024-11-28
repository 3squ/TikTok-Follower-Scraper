import os
import pandas as pd
import time
import subprocess

# Path to the Excel file in the same folder as the script
file_path = os.path.join(os.path.dirname(__file__), "TikTok_Followers.xlsx")

# Prompt user for the follower cutoff
try:
    cutoff_min = int(input("Enter the minimum number of followers: "))
except ValueError:
    print("Invalid input. Using default minimum cutoff of 5000.")
    cutoff_min = 5000

# Prompt user for the maximum follower count
try:
    cutoff_max = int(input("Enter the maximum number of followers (0 for unlimited): "))
    if cutoff_max == 0:
        cutoff_max = float('inf')  # No upper limit
except ValueError:
    print("Invalid input. Using no upper limit.")
    cutoff_max = float('inf')

# Prompt user for the delay between openings
try:
    delay = float(input("Enter the delay between openings in seconds (at least 2 seconds is recommended to avoid traffic blocks): "))
    if delay < 2:
        print("Delay too short! Setting to the recommended minimum of 2 seconds.")
        delay = 2
except ValueError:
    print("Invalid input. Using the default delay of 2 seconds.")
    delay = 2

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' was not found. Ensure it is in the same folder as this script.")
    exit()

# Load the Excel file
data = pd.read_excel(file_path)

# Ensure the Followers column is numeric
data["Followers"] = pd.to_numeric(data["Followers"], errors="coerce")

# Filter usernames within the follower range and sort by followers in descending order
filtered_users = data[(data["Followers"] >= cutoff_min) & (data["Followers"] <= cutoff_max)].sort_values(by="Followers", ascending=False)

# Construct TikTok profile URLs and open them in the background with the specified delay
base_url = "https://www.tiktok.com/@"

for username, followers in zip(filtered_users["Username"], filtered_users["Followers"]):
    profile_url = f"{base_url}{username}"
    print(f"Opening: {profile_url} with {followers} followers")
    
    # Open the URL in Chrome in the background
    subprocess.Popen(["start", "chrome", "--new-tab", profile_url], shell=True)
    
    time.sleep(delay)  # Delay specified by the user
