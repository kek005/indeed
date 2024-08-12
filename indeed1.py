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
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Get today's date
today = datetime.date.today()
formatted_date = today.strftime("%Y-%m-%d")

summary_of_experience = f"My name is Jesugnon Maxime KEKE, 7 years of experience in IT overall as of {formatted_date}. 6 years of experience with Test automation, manual tesing, performance testing, jmeter, selenium webdriver, python programming language, pytest, Postman, Jenkins, DevOps, Jira, white box, SQL, agile methodologies, robot framework, Confluence, testrail, data base, test cases, Testrail, test scenarios, scrum, user acceptance testing, git, continuous integration, qa/qc, Linux, REST API, unit testing, azure boards, Microsoft azure, healfcare domain. 5 years of selenium, appium, chrome dev tool, ISTQB, Mobile testing, Charles Proxy, iOS. 3 years managing QA team, Salesforce, AWS, C#, Cypress, surpervising QA team. 2 years of etl testing, javascript, customer service experience. Salary: $135,000/year which equal $65/hr. I heard about this job from LinkedIn. Not comfortable commuting to job location."
summary_radio_questions = "yes for drug test, background check, US Citizen. no for sponsorship, I will never require sponsoreship, I'm US Citizen, No for disability."
summary_select_questions = "profectional english, yes for full time, contract, part time. US citizen, Do not required sponsorship."

class Dice:
    def __init__(self):
        options = FirefoxOptions()
        profile_path = r'C:\Users\DELL\AppData\Roaming\Mozilla\Firefox\Profiles\6d4dc8w2.default-release'
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        #options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.profile = profile_path
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)
        self.countJobApply = 0

    def search_jobs(self):
        self.driver.get("https://www.indeed.com/")
        print("I just opened the indeed page")
        time.sleep(random.uniform(5, 10))

        input_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='text-input-what']"))
        )
        input_element.click()
        input_element.send_keys(Keys.CONTROL + "a")
        input_element.send_keys(Keys.BACK_SPACE)
        input_element.send_keys("QA")
        time.sleep(random.uniform(5, 10))


        location_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='text-input-where']"))
        )
        location_element.clear()
        location_element.send_keys("Remote")
        location_element.send_keys(Keys.RETURN)
        time.sleep(random.uniform(5, 10))

        page = 5

        job_links = self.get_job_links()

        for job_link in job_links:
            self.process_job_link(job_link)

    def get_job_links(self):
        try:
            job_links = self.driver.find_elements(By.XPATH, "//a[@class='JobCard_trackingLink__GrRYn']")
            return job_links
        except Exception as e:
            print("Error getting job links on current page:", e)
            return []

    def process_job_link(self, job_link):
        try:
            original_window = self.driver.current_window_handle
            self.driver.execute_script("arguments[0].click();", job_link)

            easyApplyButton = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".JobDetails_applyButtonContainer__L36Bs > button:nth-child(1)"))
            )
            self.driver.execute_script("arguments[0].click();", easyApplyButton)

            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break

            self.apply_for_job()

            self.driver.close()
            self.driver.switch_to.window(original_window)
        except Exception as e:
            print("Error processing job link:", e)

    def diceJobApply(self):
        print("Starting diceJobApply method")
        self.search_jobs()

    def apply_for_job(self):
        start_time = time.time()
        form_completed = False
        timeout = 300  # Set a timeout period (e.g., 5 minutes)

        while time.time() - start_time < timeout:
            try:
                print("Attempting to fill and submit the form.")
                self.questionnaire()  # Fill out the form
                submit_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[span/text()='Submit your application']"))
                )
                submit_button.click()
                form_completed = True
                break
            except Exception as e:
                print(f"Error during form submission: {e}")

            selectors = [
                (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[2]/div/div/main/div[3]/div/button"),
                (By.CSS_SELECTOR, "button[data-testid='continue-button']")
            ]

            for selector in selectors:
                try:
                    button = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable(selector)
                    )
                    self.driver.execute_script("arguments[0].click();", button)
                    self.questionnaire()  # Call questionnaire again for the next page
                    break
                except Exception as e:
                    print(f"Error clicking continue button with selector {selector}: {e}")

        if not form_completed:
            print("Failed to complete the form within the timeout period.")

    def questionnaire(self):
        print('I am in questionnaire')
        try:
            input_fields = self.driver.find_elements(By.XPATH, "//input[@type='text' or @type='checkbox' or @type='radio'] | //textarea")
            for field in input_fields:
                field_type = field.get_attribute('type')
                question_label = field.find_element(By.XPATH, "ancestor::div[contains(@class, 'ia-Questions-item')]//label").text
                if field_type == 'text' or field_type == 'textarea':
                    value = field.get_attribute('value')
                    if not value:  # If the field is empty
                        self.process_text_field(field, summary_of_experience, question_label)
                elif field_type == 'checkbox' and not field.is_selected():
                    self.process_checkbox(field, summary_of_experience, question_label)
                elif field_type == 'radio' and not field.is_selected():
                    self.process_radio_button(field, summary_of_experience, question_label)

            dropdowns = self.driver.find_elements(By.TAG_NAME, "select")
            for dropdown in dropdowns:
                self.process_dropdown(dropdown, summary_of_experience)
        except Exception as e:
            print("Error processing input fields: ", e)

    def process_text_field(self, field, summary_of_experience, question):
        try:
            response = self.get_gpt_response(question)
            if response:
                field.send_keys(response)
        except Exception as e:
            print("Error processing text field: ", e)

    def process_checkbox(self, field, summary_of_experience, question):
        try:
            response = self.get_gpt_response(question)
            if response.lower() == 'yes':
                self.driver.execute_script("arguments[0].click();", field)
        except Exception as e:
            print("Error processing checkbox: ", e)

    def process_radio_button(self, field, summary_of_experience, question):
        try:
            response = self.get_gpt_response(question)
            if response.lower() == 'yes':
                self.driver.execute_script("arguments[0].click();", field)
        except Exception as e:
            print("Error processing radio button: ", e)

    def process_dropdown(self, dropdown, summary_of_experience):
        try:
            response = self.get_gpt_response(summary_select_questions)
            if response:
                select = Select(dropdown)
                select.select_by_visible_text(response)
        except Exception as e:
            print("Error processing dropdown: ", e)

    def get_gpt_response(self, prompt):
        try:
            response = openai.Completion.create(
                model="gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=50
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error getting GPT response: {e}")
            return None

start = time.time()
Dice().diceJobApply()
end = time.time()
