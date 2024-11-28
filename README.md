# TikTok Follower Scraper

A Python-based project that automates the extraction of follower counts from TikTok profiles, exports the data to an Excel file, and provides user-friendly tools for filtering and opening TikTok profiles.

---

## Features

- Automated Scraping: Uses Selenium WebDriver to scrape follower counts from TikTok profiles.
- Data Export: Stores data in an Excel file (TikTok_Followers.xlsx) and appends new entries without overwriting existing records.
- Backup System: Automatically creates timestamped backups of the Excel file during each run.
- User Interaction:
  - Filter profiles by follower count ranges.
  - Open TikTok profiles in your default browser with a customizable delay.
- Error Handling: Implements retry logic for scraping and gracefully handles exceptions.
- Portable File Structure: Designed to run on any computer without modifying file paths.

---

## Installation

### Prerequisites
1. Python: Version 3.9 or later.
2. Google Chrome: Installed on your system.
3. ChromeDriver: Automatically managed via webdriver-manager.
4. Python Dependencies: Install the required libraries using the command:
   pip install -r requirements.txt

---

## Download Files

To download all the necessary files in a ZIP format, click the link below:

[DOWNLOAD](https://drive.google.com/file/d/1HqVkZUtbTZREffDPnO6F0skJbO4DxiQj/view?usp=sharing)

---

## How to Get Follower Data from TikTok

1. Open TikTok on your web browser.
2. Log in to the desired account.
3. Go to **Settings**.
4. Under **Privacy**, click **Data**.
5. Select **Download your data** or **Get a copy of your TikTok data**.
6. Choose **Custom** and select **Profile and Posts**.
7. Select the file format as **TXT**.
8. Download the ZIP file containing the profile data.
9. Extract the ZIP file and locate the **Follower.txt** file.
10. Drag and replace **Follower.txt** into the same folder where all the code files are located.

Done! Your follower data is now ready to be used with this project.

---

## How to Use the Code

### Step 1: Download Python
1. Go to https://www.python.org/downloads/ and download the latest version of Python.
2. During installation, make sure to check the box that says "Add Python to PATH."

### Step 2: Install the Required Libraries
1. Open the folder where the project files are located.
2. Hold down the Shift key, right-click inside the folder, and select **Open PowerShell window here** or **Open Terminal here**.
3. Type the following command and press Enter:
   pip install -r requirements.txt
4. Wait for the installation to complete.

### Step 3: Run the Scraping Script
1. Double-click on the file **run_follower_bot.bat** to start the scraping process.
2. The script will read TikTok usernames from the **Follower.txt** file and fetch their follower counts.
3. The results will be saved in **TikTok_Followers.xlsx**.

### Step 4: Open TikTok Profiles
1. Double-click on the file **run_open_tiktok_profiles.bat**.
2. Follow the on-screen prompts to:
   - Enter the minimum and maximum follower counts for filtering.
   - Specify the delay (in seconds) between opening profiles.
3. The script will open TikTok profiles in your default web browser.

---

## File Structure

TikTok-Follower-Scraper/
├── follower_bot.py                # Main scraping script
├── open_tiktok_profiles.py        # Profile opening script
├── run_follower_bot.bat           # Batch file to run the scraper
├── run_open_tiktok_profiles.bat   # Batch file to open profiler
├── Follower.txt                   # Input file for usernames
├── TikTok_Followers.xlsx          # Output file for results
├── requirements.txt               # Python dependencies

---

## Example Workflow

1. Prepare Input:
   Add usernames to Follower.txt in the same folder as the scripts.

2. Run Scraping:
   Execute the scraping script using run_follower_bot.bat.
   The results will be saved to TikTok_Followers.xlsx.

3. Open Profiles:
   Execute run_open_tiktok_profiles.bat to filter and open profiles in your browser.

---

## Known Issues and Troubleshooting

- TikTok Website Changes:
  If TikTok updates its website structure, the scraper's XPath selectors may need updating.
- Rate Limits or Captchas:
  Increase delays in the scraping script to reduce the risk of triggering rate limits.
- File Not Found Errors:
  Ensure Follower.txt and TikTok_Followers.xlsx are in the same folder as the scripts.

---

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
