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

### Download Files
You can download all the necessary files as a zip package from this link:
https://drive.google.com/file/d/1HqVkZUtbTZREffDPnO6F0skJbO4DxiQj/view?usp=sharing
---

## Usage

### 1. Run the Scraping Script
1. Add TikTok usernames to Follower.txt in the format:
   Username: example_username1
   Username: example_username2
2. Run the scraping script using the provided batch file:
   run_follower_bot.bat
3. Check the results in TikTok_Followers.xlsx.

### 2. Open TikTok Profiles
1. Run the open_tiktok_profiles.py script using the batch file:
   run_open_tiktok_profiles.bat
2. Follow the prompts to:
   - Specify a follower count range.
   - Set a delay between browser openings.
3. The script will open TikTok profiles filtered by your criteria.

---

## File Structure

TikTok-Follower-Scraper/
├── follower_bot.py                # Main scraping script
├── open_tiktok_profiles.py        # Profile opening script
├── run_follower_bot.bat           # Batch file to run the scraper
├── run_open_tiktok_profiles.bat   # Batch file to open profiles
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
