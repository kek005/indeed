# Indeed Job Application Automation
This script automates the process of applying to jobs on Indeed, using Selenium WebDriver to navigate the site and OpenAI GPT to help fill out application forms. Ideal for job seekers who want to streamline their job application process on Indeed.

Features
Automated Job Searching and Application: Automatically searches for jobs based on specified keywords and location, navigates to job listings, and applies using stored profile information.
Dynamic Form Filling: Uses OpenAI GPT to generate answers to application form questions based on a pre-defined profile summary, making applications personalized yet efficient.
Error Handling: Manages potential errors during form submission, ensuring a smoother experience with robust exception handling.
Prerequisites
Python 3.x: Make sure Python is installed.

Selenium: Install Selenium for browser automation.
pip install selenium

GeckoDriver: Install GeckoDriver for Firefox.

Webdriver Manager: Simplifies driver setup.
pip install webdriver-manager

OpenAI API Key: Sign up for an API key at OpenAI and store it in a .env file.

Additional Libraries: Install other dependencies.
pip install python-dotenv

Setup
Clone the Repository:
git clone https://github.com/yourusername/IndeedJobAutomation.git

cd IndeedJobAutomation
Configure Environment Variables:

Create a .env file in the root directory with your OpenAI API key and Firefox profile path:
plaintext
Copy code
OPENAI_API_KEY=your_openai_api_key
FIREFOX_PROFILE_PATH=your_firefox_profile_path
Customize Profile Information:

Edit summary_of_experience, summary_radio_questions, and summary_select_questions to match your background and application preferences.
Usage

Run the Script:
python indeed_job_automation.py

Process:
The script will search for jobs on Indeed, click on job listings, and attempt to auto-fill application forms based on provided profile information.
Important Notes
Usage Limits: OpenAI API calls are limited by your API quota.
LinkedIn and Indeed Terms of Service: Ensure compliance with the terms of service of these platforms.
Disclaimer
This tool is designed for personal use. Automated job applications should be used responsibly, and users should ensure compliance with Indeed's terms of service.

License
MIT License
