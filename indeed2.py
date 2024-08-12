import time
import random
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Get today's date
today = datetime.date.today()
formatted_date = today.strftime("%Y-%m-%d")

summary_of_experience = f"My name is Jesugnon Maxime KEKE, 7 years of experience in IT overall as of {formatted_date}. 6 years of experience with Test automation, manual tesing, performance testing, jmeter, selenium webdriver, python programming language, pytest, Postman, Jenkins, DevOps, Jira, white box, SQL, agile methodologies, robot framework, Confluence, testrail, data base, test cases, Testrail, test scenarios, scrum, user acceptance testing, git, continuous integration, qa/qc, Linux, REST API, unit testing, azure boards, Microsoft azure, healfcare domain. 5 years of selenium, appium, chrome dev tool, ISTQB, Mobile testing, Charles Proxy, iOS. 3 years managing QA team, Salesforce, AWS, C#, Cypress, surpervising QA team. 2 years of etl testing, javascript, customer service experience. Salary: $135,000/year which equal $65/hr. I heard about this job from LinkedIn. Not comfortable commuting to job location."

class IndeedJobApplier:
    def __init__(self):
        options = FirefoxOptions()
        profile_path = r'C:\Users\DELL\AppData\Roaming\Mozilla\Firefox\Profiles\6d4dc8w2.default-release'
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        # Uncomment the next line to run in headless mode
        # options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.profile = profile_path
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)
        self.current_page = 1

    def search_jobs(self):
        self.driver.get("https://www.indeed.com/")
        print("I just opened the Indeed page")
        time.sleep(random.uniform(5, 10))

        # Search for jobs
        input_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='text-input-what']"))
        )
        input_element.click()
        input_element.send_keys(Keys.CONTROL + "a")
        input_element.send_keys(Keys.BACK_SPACE)
        input_element.send_keys("QA")
        time.sleep(random.uniform(5, 10))

        # Set location to Remote
        location_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='text-input-where']"))
        )
        location_element.clear()
        location_element.send_keys("Remote")
        location_element.send_keys(Keys.RETURN)
        time.sleep(random.uniform(5, 10))

        # Start processing job listings
        while True:
            self.process_jobs_on_page()
            if not self.go_to_next_page():
                break

    def process_jobs_on_page(self):
        job_links = self.get_job_links()

        for job_link in job_links:
            self.process_job_link(job_link)
            time.sleep(random.uniform(3, 5))  # Add a small delay between processing each job

    def get_job_links(self):
        try:
            # Get all job links on the page
            job_links = self.driver.find_elements(By.XPATH, "/html/body/main/div/div[2]/div/div[5]/div/div[1]/div[4]/div/ul/li")
            return job_links[:15]  # Only the first 15 job links
        except Exception as e:
            print("Error getting job links on current page:", e)
            return []

    def process_job_link(self, job_link):
        try:
            original_window = self.driver.current_window_handle
            job_link.click()  # Click the job link to bring up the job details
            time.sleep(random.uniform(5, 10))  # Wait for the job details to load

            try:
                # Try to find the Easy Apply button
                easy_apply_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='indeedApplyButton']"))
                )
                self.driver.execute_script("arguments[0].click();", easy_apply_button)
                time.sleep(random.uniform(5, 10))

                # Switch to the new window or tab that opens after clicking Easy Apply
                for window_handle in self.driver.window_handles:
                    if window_handle != original_window:
                        self.driver.switch_to.window(window_handle)
                        break

                # Check for the resume button after switching to the new window
                resume_button = self.wait_for_resume_button()
                if resume_button:
                    print("Found resume upload button, proceeding with application")
                    self.apply_for_job()
                else:
                    print("No resume upload button found, closing the job page")
                    self.driver.close()

                # Close the current application window and switch back to the original window
                self.driver.close()
                self.driver.switch_to.window(original_window)

            except TimeoutException:
                print("Easy Apply button not found, skipping this job")

        except Exception as e:
            print(f"Error processing job link: {e}")
            # No need to switch windows if the Easy Apply button wasn't found


    def wait_for_resume_button(self):
        """Helper function to wait for the resume button to appear"""
        try:
            resume_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[2]/div/fieldset/div[3]/label"))
            )
            return resume_button
        except Exception:
            return None
    


    def apply_for_job(self):
        try:
            # Assuming the resume button is present, proceed with the application process
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[2]/div/fieldset/div[3]/label"))
            ))
            time.sleep(random.uniform(5, 10))

            # click continue button
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[3]"))
            ))
            time.sleep(random.uniform(5, 10))






            # Submit the application
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span/text()='Submit your application']"))
            )
            self.driver.execute_script("arguments[0].click();", submit_button)  # Click using JavaScript
            print("Application submitted successfully.")
        except Exception as e:
            print(f"Error during form submission: {e}")

    def go_to_next_page(self):
        try:
            self.current_page += 1
            next_page_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//ul[@class='pagination-list']//a[text()='{self.current_page}']"))
            )
            self.driver.execute_script("arguments[0].click();", next_page_link)  # Click using JavaScript
            time.sleep(random.uniform(5, 10))
            return True
        except Exception as e:
            print(f"No more pages available or error navigating to the next page: {e}")
            return False

start = time.time()
IndeedJobApplier().search_jobs()
end = time.time()
print(f"Total time taken: {end - start} seconds")
