import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import random
import shutil
from datetime import datetime

# Function to scrape followers from a TikTok profile
def scrape_followers(username, retries=3):
    """
    Scrape the follower count from a TikTok profile with retry logic.
    """
    url = f"https://www.tiktok.com/@{username}"
    attempt = 0
    while attempt < retries:
        try:
            # Open TikTok profile
            driver.get(url)

            # Dynamically wait for the follower count element to load
            followers_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//strong[@title='Followers']"))
            )
            followers = followers_element.text.strip()

            # Convert 'K' or 'M' to numbers
            followers = convert_followers_to_number(followers)

            # Highlight accounts with 5k+ followers
            if followers >= 5000:
                print(f"Username: {username}, Followers: {followers} *** High Follower Count ***")
            else:
                print(f"Username: {username}, Followers: {followers}")
            
            return followers
        except Exception as e:
            attempt += 1
            print(f"Retrying {username}... Attempt {attempt}/{retries}")
            time.sleep(random.uniform(2, 4))  # Wait before retrying
            if attempt >= retries:
                print(f"Error scraping {username}: {e}")
                return "Error"

# Convert followers like '10.6K' or '1.2M' to integers
def convert_followers_to_number(followers):
    """
    Convert followers from formats like '10K' or '1.2M' to integers.
    """
    if 'K' in followers:
        return int(float(followers.replace('K', '')) * 1000)
    elif 'M' in followers:
        return int(float(followers.replace('M', '')) * 1000000)
    else:
        return int(followers)

# Load usernames from the provided file
def load_usernames(file_path):
    """
    Load usernames from a file with 'Username' format.
    """
    usernames = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith("Username:"):
                    usernames.append(line.split(":")[1].strip())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return usernames

# Load processed usernames from the existing Excel file
def load_processed_usernames(output_file):
    """
    Load already processed usernames from the output Excel file.
    """
    if os.path.exists(output_file):
        try:
            df = pd.read_excel(output_file)
            return set(df['Username'].astype(str))
        except Exception as e:
            print(f"Error reading {output_file}: {e}")
            return set()
    return set()

# Append a row to the Excel file
def append_to_excel(output_file, row):
    """
    Append a row to the Excel file.
    """
    try:
        # If the file doesn't exist, create it with the headers
        if not os.path.exists(output_file):
            df = pd.DataFrame([row])
            df.to_excel(output_file, index=False)
        else:
            # Append the row to the existing file
            df = pd.read_excel(output_file)
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
            df.to_excel(output_file, index=False)
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")

# Backup the Excel file
def backup_excel_file(output_file):
    """
    Create a timestamped backup of the Excel file if it exists.
    """
    if os.path.exists(output_file):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"{os.path.splitext(output_file)[0]}_backup_{timestamp}.xlsx"
        try:
            shutil.copy(output_file, backup_file)
            print(f"Backup created: {backup_file}")
        except Exception as e:
            print(f"Error creating backup: {e}")

# Main script
if __name__ == "__main__":
    # Input and output file paths in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, 'Follower.txt')
    output_file = os.path.join(script_dir, 'TikTok_Followers.xlsx')

    # Create a backup of the Excel file
    backup_excel_file(output_file)

    # Load usernames
    usernames = load_usernames(input_file)
    total_usernames = len(usernames)

    # Load already processed usernames
    processed_usernames = load_processed_usernames(output_file)
    already_processed_count = len(processed_usernames)
    print(f"Skipping {already_processed_count} previously checked usernames.")

    # Setup Selenium WebDriver
    options = Options()
    # Temporarily disable headless mode for debugging
    # options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        scanned_count = already_processed_count  # Start scanned count from already processed usernames
        total_scanned = already_processed_count  # Include skipped usernames in total_scanned

        for username in usernames:
            if username in processed_usernames:
                print(f"Skipping already processed username: {username}")
                continue
            
            followers = scrape_followers(username)

            # Append results to the Excel file
            append_to_excel(output_file, {"Username": username, "Followers": followers})

            # Update progress
            scanned_count += 1
            total_scanned += 1
            print(f"Scanned: {scanned_count}/{total_usernames} accounts. Total in file: {total_scanned}")

    except KeyboardInterrupt:
        print("\nScript interrupted by user. Saving progress and exiting...")
    finally:
        # Ensure the browser is closed and progress is saved
        driver.quit()

    print(f"Scraping completed! Total accounts scanned: {total_scanned}/{total_usernames}.")
