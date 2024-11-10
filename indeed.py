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
        profile_path = r'C:\Users\DELL\AppData\Roaming\Mozilla\Firefox\Profiles\your_profile_path2.default-release'
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
        time.sleep(random.uniform(100, 150))

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.NavigationBar_tabs__Zhi4b:nth-child(2) > a:nth-child(1)"))
        ).click()
        time.sleep(random.uniform(3, 7))

        input_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchBar-jobTitle"))
        )
        input_element.click()
        input_element.send_keys(Keys.CONTROL + "a")
        input_element.send_keys(Keys.BACK_SPACE)
        time.sleep(random.uniform(3, 7))
        input_element.send_keys("QA")
        time.sleep(random.uniform(3, 7))

        location_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchBar-location"))
        )
        location_element.clear()
        location_element.send_keys("Remote")
        time.sleep(5)

        location_element.send_keys(Keys.RETURN)
        time.sleep(random.uniform(3, 7))

        self.driver.find_element(By.CSS_SELECTOR, "button.SearchFiltersBar_pill__cT_sS:nth-child(2)").click()
        time.sleep(random.uniform(2, 4))

        self.driver.find_element(By.CSS_SELECTOR, "button.SearchFiltersBar_pill__cT_sS:nth-child(3)").click()
        time.sleep(random.uniform(2, 4))

        job_links = self.get_job_links()

        for job_link in job_links:
            self.process_job_link(job_link)

    def get_job_links(self):
        try:
            job_links = self.driver.find_elements(By.XPATH, "//a[@class='JobCard_trackingLink__GrRYn']")
            print("I'm printing the job links")
            print("Job Links:", job_links)
            time.sleep(random.uniform(5, 10))
        except Exception as e:
            print("Error getting job links on current page:", e)
            job_links = []

        return job_links

    def process_job_link(self, job_link):
        try:
            print("I'm in the try block to click on link")
            time.sleep(random.uniform(2, 7))
            print("I'M clicking job link")
            original_window = self.driver.current_window_handle
            time.sleep(random.uniform(2, 7))
            self.driver.execute_script("arguments[0].click();", job_link)
            time.sleep(random.uniform(6, 9))
            print("Clicked job link:", job_link)

            easyApplyButton = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".JobDetails_applyButtonContainer__L36Bs > button:nth-child(1)"))
            )
            self.driver.execute_script("arguments[0].click();", easyApplyButton)
            time.sleep(3)
            print("Now I will try to switch to the new tab")

            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
            time.sleep(random.uniform(8, 13))
            print("I just Switched to new tab")
            print("I'm calling the apply_for_job method")
            self.apply_for_job()

            self.driver.close()
            time.sleep(random.uniform(5, 7))
            self.driver.switch_to.window(original_window)
            print("I just switch back to the first window")
        except Exception as e:
            print("Error processing job link:", e)

    def diceJobApply(self):
        print("Starting diceJobApply method")
        self.search_jobs()
        countJobClicked = 0
        countJobs = 0

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
                time.sleep(random.uniform(5, 10))
                print("Submitted the application successfully.")
                form_completed = True
                break
            except Exception as e:
                print(f"Error during form submission: {e}")

            # Now try to click the continue button using multiple selectors
            selectors = [
                (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[2]/div/div/main/div[3]/div/button"),
                (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[1]"),
                (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[2]"),
                (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[3]"),
                (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[4]"),
                (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[5]"),
                (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[6]"),
                (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[7]"),
                (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[8]"),
                (By.CSS_SELECTOR, "button[data-testid='continue-button'][class*='event'][class*='flex']"),
                (By.CSS_SELECTOR, "button[data-testid='continue-button']"),
            ]

            for index, selector in enumerate(selectors):
                try:
                    print(f"Try block {index + 1}")
                    time.sleep(random.uniform(2, 5))
                    button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(selector)
                    )
                    self.driver.execute_script("arguments[0].click();", button)
                    time.sleep(random.uniform(2, 5))  # Wait for the next page to load
                    self.questionnaire()  # Call questionnaire again for the next page
                    break  # Break out of the for loop if a button is successfully clicked
                except Exception as e:
                    print(f"Error clicking continue button with selector {selector}: {e}")

        if not form_completed:
            print("Failed to complete the form within the timeout period.")

    def questionnaire(self):
        print('I am in questionnaire')
        try:
            # Find all input fields (both text and checkboxes) by their type
            input_fields = self.driver.find_elements(By.XPATH, "//input[@type='text' or @type='checkbox' or @type='radio'] | //textarea")
            for field in input_fields:
                field_type = field.get_attribute('type')
                if field.tag_name == 'textarea':
                    field_type = 'textarea'
                question_label = field.find_element(By.XPATH, "ancestor::div[contains(@class, 'ia-Questions-item')]//label").text
                if field_type == 'text' or field_type == 'textarea':
                    value = field.get_attribute('value')
                    if not value:  # If the field is empty
                        self.process_text_field(field, summary_of_experience, question_label)
                elif field_type == 'checkbox':
                    if not field.is_selected():  # If the checkbox is not selected
                        self.process_checkbox(field, summary_of_experience, question_label)
                elif field_type == 'radio':
                    if not field.is_selected():  # If the radio button is not selected
                        self.process_radio_button(field, summary_of_experience, question_label)

            # Find and process all dropdowns
            dropdowns = self.driver.find_elements(By.TAG_NAME, "select")
            for dropdown in dropdowns:
                self.process_dropdown(dropdown, summary_of_experience)

        except Exception as e:
            print("Error processing input fields: ", e)


    def process_text_field(self, field, summary_of_experience, question):
        try:
            field_id = field.get_attribute('id')  # Get the id of the input field
            print("I got the field id:")
            print(field_id)
            if field_id:
                label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{field_id}']")
                question = label.text
                print("I just retrieved the following question: ")
                print(question)

            print("I got the outerHTML of the input field")
            outer_html = field.get_attribute('outerHTML')
            print(outer_html)

            if question:
                time.sleep(random.uniform(1, 3))
                prompt = f"Given the profile summary: '{summary_of_experience}', answer the following: '{question}' as a single digit. Just send the digit, as I am sending it directly to a variable for automation. Send 1 when there is no answer. Send in this format: '6', Do not send in the following format: 'Given the information provided, the number of years of work experience with python is 6'"
                response = self.get_gpt_response(prompt)
                print("Here is the response from GPT in the if block: ")
                print(response)

                time.sleep(random.uniform(1, 3))
                print("I am sending the outerHTML to GPT for XPath generation from review page")
                xpath_prompt = f"Given this outerHTML element: '{outer_html}', Send me the XPath locator. (do not teach me how to write an XPath) Just send me a single XPath without comment. Just One single XPath. I am sending it to a variable for automation. Do not send in this format: //input[@class='artdeco-text-input--input' and @id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-2705633535-106227781-numeric'], but send in this format: //*[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-2705633535-33492811-numeric'] "
                xpath_response = self.get_gpt_response(xpath_prompt)
                print("Here is the xpath generated by GPT printing from main function on review page: ")
                print(xpath_response)

                try:
                    self.driver.find_element(By.XPATH, xpath_response).send_keys(response)
                    print("Filling the form with the generated response from GPT")
                except:
                    print("I could not find the XPath generated by GPT")
        except Exception as e:
            print("Error processing text field: ", e)

    def process_checkbox(self, field, summary_of_experience, question):
        try:
            field_id = field.get_attribute('id')  # Get the id of the checkbox
            print("I got the field id for checkbox:")
            print(field_id)
            if field_id:
                label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{field_id}']")
                question = label.text
                print("I just retrieved the following question for checkbox: ")
                print(question)

            if "optional" in question.lower():
                print("Skipping optional question")
                return

            if question:
                time.sleep(random.uniform(1, 3))
                prompt = f"Given the profile summary: '{summary_of_experience}', answer the following: '{question}' by sending yes or no. Just send the word yes or the word no, as I am sending it directly to a variable for automation. Do not add anything else."
                response = self.get_gpt_response(prompt)
                print("Here is the response from GPT for checkbox: ")
                print(response)

                if response.lower() == 'yes':
                    self.driver.execute_script("arguments[0].click();", field)
                    print("Checkbox clicked")
        except Exception as e:
            print("Error processing checkbox: ", e)


    def process_radio_button(self, field, summary_of_experience, question):
        try:
            field_id = field.get_attribute('id')
            print("I got the field id for radio button:")
            print(field_id)

            # Find the label associated with this radio button
            label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{field_id}']")
            label_text = label.text.strip().lower()

            if "optional" in question.lower():
                print("Skipping optional question")
                return

            if question:
                time.sleep(random.uniform(1, 3))
                prompt = (
                    f"Given the profile summary: '{summary_of_experience}', answer the following: '{question}' by sending yes or no. "
                    f"Just send the word yes or the word no, as I am sending it directly to a variable for automation. Do not add anything else."
                )
                response = self.get_gpt_response(prompt)
                print("Here is the response from GPT for radio button: ")
                print(response)

                if response.lower() == 'yes' and 'yes' in label_text:
                    self.driver.execute_script("arguments[0].click();", field)
                    print("Radio button clicked")
                elif response.lower() == 'no' and 'no' in label_text:
                    self.driver.execute_script("arguments[0].click();", field)
                    print("Radio button clicked")
        except Exception as e:
            print("Error processing radio button: ", e)


    def process_dropdown(self, dropdown, summary_of_experience):
        try:
            dropdown_id = dropdown.get_attribute('id')  # Get the id of the dropdown
            print("I got the dropdown id:")
            print(dropdown_id)
            if dropdown_id:
                label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{dropdown_id}']")
                question = label.text
                print("I just retrieved the following question for dropdown: ")
                print(question)

            if "optional" in question.lower():
                print("Skipping optional question")
                return

            if question:
                time.sleep(random.uniform(1, 3))
                prompt = f"Given the profile summary: '{summary_of_experience}', answer the following: '{question}' by selecting the most appropriate option. Just send the option text exactly as it appears in the dropdown."
                response = self.get_gpt_response(prompt)
                print("Here is the response from GPT for dropdown: ")
                print(response)

                # Select the option in the dropdown
                select = Select(dropdown)
                select.select_by_visible_text(response)
                print("Dropdown option selected")
        except Exception as e:
            print("Error processing dropdown: ", e)


    def get_gpt_response(self, prompt):
        try:
            client = OpenAI()
            response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": "You are my assistant"},
    {"role": "user", "content": prompt}
  ]
)
            print("Here is the response from GPT: ")
            print(response.choices[0].message)
            gpt_response = response.choices[0].message.content
            print("Here is the response from GPT gpt_response: ")
            print(gpt_response)
            
            return gpt_response
        except Exception as e:
            print(f"An error occurred: {e}")
            return None



start = time.time()
Dice().diceJobApply()
end = time.time()
