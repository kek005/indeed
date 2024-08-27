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
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
import openai
from openai import OpenAI

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Get today's date
today = datetime.date.today()
formatted_date = today.strftime("%Y-%m-%d")

summary_of_experience = f"My name is Jesugnon Maxime KEKE, 7 years of experience in IT overall as of {formatted_date}. 6 years of experience with Test automation, manual tesing, performance testing, jmeter, selenium webdriver, python programming language, pytest, Postman, Jenkins, DevOps, Jira, white box, SQL, agile methodologies, robot framework, Confluence, testrail, data base, test cases, Testrail, test scenarios, scrum, user acceptance testing, git, continuous integration, qa/qc, Linux, REST API, unit testing, azure boards, Microsoft azure, healfcare domain. 5 years of selenium, appium, chrome dev tool, ISTQB, Mobile testing, Charles Proxy, iOS. 3 years managing QA team, Salesforce, AWS, C#, Cypress, surpervising QA team. 2 years of etl testing, javascript, customer service experience. Salary: $135,000/year which equal $65/hr. I heard about this job from LinkedIn. Not comfortable commuting to job location."
summary_radio_questions = "yes for drug test, background check, US Citizen. no for sponsorship, I will never require sponsoreship, I'm US Citizen."
summary_select_questions = "profectional english, yes for full time, contract, part time. US citizen, Do not required sponsorship."

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

        # Set preferences to avoid "controlled by automated test software" message
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('useAutomationExtension', False)
        options.set_preference("toolkit.telemetry.reportingpolicy.firstRun", False)
        options.set_preference("privacy.reduceTimerPrecision", False)  # Optional: Disables certain WebDriver detection mechanisms
        options.set_preference("general.useragent.override", "your-custom-user-agent-string")  # Optional: Change the User Agent

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
                time.sleep(random.uniform(2, 3))

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
        start_time = time.time()
        timeout = 300  # Set a timeout period (e.g., 5 minutes)

        try:
            print("I'm in the apply for job function")
            while time.time() - start_time < timeout:

                # Assuming the resume button is present, proceed with the application process
                time.sleep(random.uniform(5, 10))
                print("I waited 5 seconds for the resume to be present. Now I will select it")
                resume_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[2]/div/fieldset/div[3]/label"))
                )
                self.driver.execute_script("arguments[0].click();", resume_button)
                time.sleep(random.uniform(5, 10))
                print("I just selected the resume now I will be clicking the first continue button")

                # Scroll the page by a predefined coordinate (e.g., 1000 pixels down)
                self.driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(random.uniform(2, 3))  # Give the page time to scroll

                # Click the first continue button using multiple selectors
                continue_button_clicked = False
                for i in range(1, 9):
                    xpath_selector = f"(//button[contains(., 'Continue')])[{i}]"
                    try:
                        print(f"Trying XPath selector {xpath_selector}")
                        button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath_selector))
                        )
                        self.driver.execute_script("arguments[0].click();", button)
                        time.sleep(random.uniform(2, 5))  # Wait for the next page to load
                        print(f"Successfully clicked the Continue button using XPath with index {i}.")
                        continue_button_clicked = True
                        break
                    except Exception as e:
                        print(f"Error clicking continue button with XPath {xpath_selector}: {e}")

                if not continue_button_clicked:
                    print("No continue button clicked, skipping this job.")
                    return False

                # Continue navigating pages until the Submit button is found
                while True:
                    time.sleep(random.uniform(2, 3))  # Give the page time to load
                    print("Handling the continue page by trying to answer questions if present")
                    self.handle_continue_page()  # Your function to handle all fields on the page

                    # Look for the submit button
                    try:
                        submit_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Submit')]"))
                        )
                        self.driver.execute_script("arguments[0].click();", submit_button)
                        time.sleep(random.uniform(2, 3))
                        print("Successfully submitted the application.")
                        return True
                    except Exception:
                        print("Submit button not found, checking for other buttons.")

                    # Look for the review application button
                    try:
                        review_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Review')]"))
                        )
                        self.driver.execute_script("arguments[0].click();", review_button)
                        time.sleep(random.uniform(2, 3))
                        print("Clicked the Review Application button.")
                        continue
                    except Exception:
                        print("Review Application button not found, checking for Continue button.")

                    # Look for the next continue button if submit or review buttons are not present
                    continue_button_clicked = False
                    for i in range(1, 9):
                        xpath_selector = f"(//button[contains(., 'Continue')])[{i}]"
                        try:
                            print(f"Trying XPath selector {xpath_selector}")
                            button = WebDriverWait(self.driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, xpath_selector))
                            )
                            self.driver.execute_script("arguments[0].click();", button)
                            time.sleep(random.uniform(2, 5))  # Wait for the next page to load
                            print(f"Successfully clicked the Continue button using XPath with index {i}.")
                            continue_button_clicked = True
                            break
                        except Exception as e:
                            print(f"Error clicking continue button with XPath {xpath_selector}: {e}")

                    if not continue_button_clicked:
                        print("No continue button clicked, no more actions to take. Exiting.")
                        return False
                    

            print("Job application process timed out.")
            
        except Exception as e:
            print(f"Was not able to apply for job: {e}")
            return False



    def handle_continue_page(self):
        """
        Method to handle any interactions required on the continue page.
        This includes filling out fields, selecting radio buttons, and dropdowns.
        """
        print("I am in the handle continue function to answer questions ")
        try:
            # Check and fill empty fields on the continue page and fill them with GPT response
            # Input text field
            print("Im checking if there are empty input field")
            input_fields = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']:not(.search-global-typeahead__input)")
            for field in input_fields:
                value = field.get_attribute('value')
                if not value:  # If the field is empty
                    outer_html = field.get_attribute('outerHTML')
                    field_id = field.get_attribute('id')
                    if field_id:
                        label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{field_id}']")
                        question = label.text
                        if question:
                            prompt = f"Given the profile summary: '{summary_of_experience}', answer the following: '{question}' as a single digit. Just send the digit, as I am sending it directly to a variable for automation. send 1 when there is no answer."
                            response = self.get_gpt_response(prompt)
                            xpath_prompt = f"Given this outerHTML element: '{outer_html}', Send me the Xpath locator."
                            xpath_response = self.get_gpt_response(xpath_prompt)
                            try:
                                self.driver.find_element(By.XPATH, xpath_response).send_keys(response)
                            except Exception as e:
                                print(f"Could not find the XPath generated by GPT: {e}")

            # Handle radio buttons
            self.handle_radio_buttons()

            # Handle dropdowns
            self.handle_dropdowns()

        except Exception as e:
            print(f"Error handling continue page: {e}")



    def handle_radio_buttons(self):
        """Handles the radio buttons on the continue page."""
        print("Im checking if there are unselected radio button")
        try:
            fieldsets = self.driver.find_elements(By.XPATH, "//fieldset[@data-test-form-builder-radio-button-form-component='true']")
            for fieldset in fieldsets:
                radio_containers = fieldset.find_elements(By.XPATH, ".//div[@data-test-text-selectable-option]")
                if not any(container.find_element(By.XPATH, ".//input[@type='radio']").is_selected() for container in radio_containers):
                    question_span = fieldset.find_element(By.XPATH, ".//span[@aria-hidden='true']")
                    question = question_span.text.strip()
                    if question:
                        promptradio = f"Given the profile summary: '{summary_radio_questions}', answer the following: '{question}' by sending yes or no."
                        gpt_response = self.get_gpt_response(promptradio)
                        for container in radio_containers:
                            radio_input = container.find_element(By.XPATH, ".//input[@type='radio']")
                            label = container.find_element(By.XPATH, ".//label")
                            if gpt_response.lower() == label.text.strip().lower():
                                label.click()
                                break
        except Exception as e:
            print(f"Error handling radio buttons: {e}")


    def handle_dropdowns(self):
        """Handles dropdowns on the continue page."""
        print("Im checking if there are unhandled dropdowns")
        try:
            selects = self.driver.find_elements(By.XPATH, "//select[@data-test-text-entity-list-form-select]")
            for select_element in selects:
                select_id = select_element.get_attribute('id')
                select = Select(select_element)
                if select.first_selected_option.get_attribute('value') == "Select an option":
                    label = self.driver.find_element(By.XPATH, f"//label[@for='{select_id}']")
                    question = label.text.strip()
                    options = [option.text.strip() for option in select.options if option.get_attribute('value') != "Select an option"]
                    if question and options:
                        promptselect = f"Given the profile summary: '{summary_select_questions}', and the available options {options}, answer the following: '{question}'."
                        gpt_response = self.get_gpt_response(promptselect)
                        try:
                            select.select_by_visible_text(gpt_response)
                        except Exception as e:
                            print(f"Error selecting dropdown option: {e}")
        except Exception as e:
            print(f"Error handling dropdowns: {e}")



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

    def get_gpt_response(self, prompt):
        try:
            client = OpenAI()
            response = client.chat.completions.create(
  model="gpt-3.5-turbo",
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
IndeedJobApplier().search_jobs()
end = time.time()
print(f"Total time taken: {end - start} seconds")
