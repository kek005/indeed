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
        form_completed = False
        timeout = 300  # Set a timeout period (e.g., 5 minutes)

        
        try:
            print("I'm in the apply for job function")
            while time.time() - start_time < timeout:

                # Assuming the resume button is present, proceed with the application process
                self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[2]/div/fieldset/div[3]/label"))
                ))
                time.sleep(random.uniform(5, 10))

                print("I selected the resume, Now I will click on the continue button")

                # click continue button
                self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button[3]"))
                ))
                time.sleep(random.uniform(5, 10))



                # Check and fill empty fields on the continue page and fill them with gpt response
                # Input text field
                try:
                    input_fields = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']:not(.search-global-typeahead__input)")
                    for field in input_fields:
                        value = field.get_attribute('value')
                        if not value:  # If the field is empty
                            outer_html = field.get_attribute('outerHTML')
                            field_id = field.get_attribute('id')  # Get the id of the input field
                            print("I got the field id: ")
                            print(field_id)
                            if field_id:
                                label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{field_id}']")
                                question = label.text
                                print("I just retrieve the following question continue page: ")
                                print(question)
                            print("I got the outerHTML of the input field continue page")
                            print(outer_html)

                            # Send the question text related to this field to GPT for answer generation
                            if question:
                                time.sleep(random.uniform(2, 3))
                                #prompt = f"Given the profile summary: '{summary_of_experience}', answer the following: '{question}' as a single digit. Just send the digit, as I am sending it directly to a variable for automation. send 0 when there is no answer."
                                prompt = f"Given the profile summary: '{summary_of_experience}', answer the following: '{question}' as a single digit. Just send the digit, as I am sending it directly to a variable for automation. send 1 when there is no answer. Send in this format: '6', Do not send in the following format: 'Given the information provided, the number of years of work experience with python is 6'."
                                response = self.get_gpt_response(prompt)
                                print("Here is the response from GPT in the if block: ")
                                print(response)

                            # Send outerHTML to GPT for XPath generation
                            time.sleep(random.uniform(2, 3))
                            print("I am sending the outerHTML to GPT for XPath generation continue page")
                            xpath_prompt = f"Given this outerHTML element: '{outer_html}', Send me the Xpath locator. (do not teach me how to write a Xpath) Just send me a single xpath without comment. Just One single Xpath. I am sending it to a variable for automation. Do not send something like this: //input[@class='artdeco-text-input--input' and @id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-2705633535-106227781-numeric'], but something in this format: //*[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-2705633535-33492811-numeric'] "
                            #xpath_prompt = f"Generate a precise XPath locator for the following HTML element: {outer_html}. Provide a single, accurate XPath expression. I am sending it to a variable for automation."
                            xpath_response = self.get_gpt_response(xpath_prompt)
                            print("Here is the xpath generated by gpt GPT main function on continue application page: ")
                            print(xpath_response)
                            try:
                                self.driver.find_element(By.XPATH, xpath_response).send_keys(response)
                                print("Filing the form with the generated response from gpt")
                            except:
                                print("I could not find the xpath generated by gpt")

                except Exception as e:
                    print("there is no input field empty ", e)

                # Find the fieldset that contains the radio buttons continue page
                # Radio button
                try:
                    # Find all fieldsets that contain radio buttons continue page
                    time.sleep(random.uniform(2, 3))
                    fieldsets = self.driver.find_elements(By.XPATH, "//fieldset[@data-test-form-builder-radio-button-form-component='true']")
                    for fieldset in fieldsets:
                        # Check if a response is needed (no existing selection)
                        radio_containers = fieldset.find_elements(By.XPATH, ".//div[@data-test-text-selectable-option]")
                        if not any(container.find_element(By.XPATH, ".//input[@type='radio']").is_selected() for container in radio_containers):
                            # Send the question to GPT for answer (assuming function get_gpt_response exists)
                            # Extract the question
                            question_span = fieldset.find_element(By.XPATH, ".//span[@aria-hidden='true']")
                            question = question_span.text.strip()
                            print("I just retrieve the following question for radio button from continue page: ")
                            print(question)
                            if question:
                                promptradio = f"Given the profile summary: '{summary_radio_questions}', answer the following: '{question}' by sending yes or no. Just send the word yes or the word no, as I am sending it directly to a variable for automation. Do not add anything else."
                                gpt_response = self.get_gpt_response(promptradio)
                                time.sleep(random.uniform(2, 3))
                                print("Here is the response from GPT for radio button continue page: ")
                                print(gpt_response)
                                # Iterate through radio containers to find and click the appropriate option
                                for container in radio_containers:
                                    print("I am iterating through radio containers to find and click the appropriate option")
                                    radio_input = container.find_element(By.XPATH, ".//input[@type='radio']")
                                    print("I found the radio input")
                                    label = container.find_element(By.XPATH, ".//label")
                                    print("I found the label that contain yes or no and I am ready to click continue pge")
                                    # Decide which radio button to click based on its value
                                    # Use case-insensitive comparison for matching GPT response with label text
                                    if gpt_response.lower() == label.text.strip().lower():  # Stripping any leading/trailing whitespace
                                        print("I am clicking the radio button on continue page")
                                        label.click()
                                        break  # Assuming only one needs to be selected
                except Exception as e:
                    print(f"Error handling radio buttons within div containers: {e}")

                # Find unselected dropdowns and select it based on gpt response to the question from continue page
                # Dropdown
                try:
                    # Find all select elements
                    selects = self.driver.find_elements(By.XPATH, "//select[@data-test-text-entity-list-form-select]")
                    for select_element in selects:
                        select_id = select_element.get_attribute('id')
                        # Create a Select object to interact with the <select> element
                        select = Select(select_element)
                        # Check if the first option (default "Select an option") is selected
                        if select.first_selected_option.get_attribute('value') == "Select an option":
                            # Find the corresponding label with the question
                            label = self.driver.find_element(By.XPATH, f"//label[@for='{select_id}']")
                            question = label.text.strip()
                            print("I just retrieve the following question for dropdown from continue page: ")
                            print(question)

                            # Extract all dropdown options except the default "Select an option"
                            options = [option.text.strip() for option in select.options if option.get_attribute('value') != "Select an option"]
                            print("I just retrieve the following options for dropdown from continue page: ")
                            print(options)

                            # Send the question and options to GPT for an answer
                            if question and options:
                                promptselect = f"Given the profile summary: '{summary_select_questions}', and the available options {options}, answer the following: '{question}'. Please send the exact option that you choose, as I am sending it directly to a variable for automation. Do not send anything else. No comment, nothing else. Send you choice from the available options."
                                gpt_response = self.get_gpt_response(promptselect)
                                time.sleep(random.uniform(2, 3))
                                print("Here is the response from GPT for dropdown: ")
                                print(gpt_response)
                                # Iterate through options to find and select the appropriate one
                                # Select the option that matches the GPT response
                                try:
                                    select.select_by_visible_text(gpt_response)
                                except Exception as e:
                                    print(f"Error selecting dropdown option: {e}")
                        else:
                            print("The dropdown has already been selected, skipping GPT call")
                except Exception as e:
                    print(f"Error handling dropdowns: {e}")



                try:
                    # Click the continue button
                    time.sleep(random.uniform(2, 3))
                    self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Continue to next step']").click()
                    time.sleep(random.uniform(2, 3))
                except Exception as e:
                    print(f"Error clicking continue button: {e}")
                # Click 'Continue to next step' after handling fields
                #self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Continue to next step']").click()
                #time.sleep(random.uniform(2, 3))


            # On the review button page check and file require fields before clicking on review your application
            # which is the page after applyPages-2
            # Input text field
            try:
                input_fields = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']:not(.search-global-typeahead__input)")
                for field in input_fields:
                    value = field.get_attribute('value')
                    if not value:  # If the field is empty
                        # Logic to fill the field
                        outer_html = field.get_attribute('outerHTML')
                        field_id = field.get_attribute('id')  # Get the id of the input field
                        print("I got the field id:")
                        print(field_id)
                        if field_id:
                            label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{field_id}']")
                            question = label.text
                            print("I just retrieve the following question: ")
                            print(question)
                        print("I got the outerHTML of the input field")
                        print(outer_html)

                        # Send the question text related to this field to GPT for answer generation from review page.
                        if question:
                            time.sleep(random.uniform(2, 3))
                            prompt = f"Given the profile summary: '{summary_of_experience}', answer the following: '{question}' as a single digit. Just send the digit, as I am sending it directly to a variable for automation. send 1 when there is no answer. Send in this format: '6', Do not send in the following format: 'Given the information provided, the number of years of work experience with python is 6'"
                            response = self.get_gpt_response(prompt)
                            print("Here is the response from GPT in the if block: ")
                            print(response)

                        # Send outerHTML to GPT for XPath generation  response['choices'][0].message.content
                        time.sleep(random.uniform(2, 3))
                        print("I am sending the outerHTML to GPT for XPath generation from review page")
                        #xpath_prompt = f"Given this outerHTML element: '{outer_html}', write for me the XPath locator (do not teach me how to write a Xpath) Just send me a single xpath without comment, do not send all the ways I can write a xpath. Just send one because I am sending it to a variable for automation."
                        xpath_prompt = f"Given this outerHTML element: '{outer_html}', Send me the Xpath locator. (do not teach me how to write a Xpath) Just send me a single xpath without comment. Just One single Xpath. I am sending it to a variable for automation. Do not send in this format: //input[@class='artdeco-text-input--input' and @id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-2705633535-106227781-numeric'], but send in this format: //*[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-2705633535-33492811-numeric'] "
                        #xpath_prompt = f"Generate a precise XPath locator for the following HTML element: {outer_html}. Provide a single, accurate XPath expression. I am sending it to a variable for automation."
                        xpath_response = self.get_gpt_response(xpath_prompt)
                        print("Here is the xpath generated by gpt GPT printing from main function on review page: ")
                        print(xpath_response)
                        try:
                            self.driver.find_element(By.XPATH, xpath_response).send_keys(response)
                            print("Filing the form with the generated response from gpt")
                        except:
                            print("I could not find the xpath generated by gpt")
            except Exception as e:
                print("there is no input field empty ", e)

            # Find the fieldset that contains the radio buttons on review page
            # Radio button
            try:
                # Find all fieldsets that contain radio buttons
                time.sleep(random.uniform(2, 3))
                fieldsets = self.driver.find_elements(By.XPATH, "//fieldset[@data-test-form-builder-radio-button-form-component='true']")
                for fieldset in fieldsets:
                    # Check if a response is needed (no existing selection)
                    radio_containers = fieldset.find_elements(By.XPATH, ".//div[@data-test-text-selectable-option]")
                    if not any(container.find_element(By.XPATH, ".//input[@type='radio']").is_selected() for container in radio_containers):
                        # Send the question to GPT for answer (assuming function get_gpt_response exists)
                        # Extract the question
                        question_span = fieldset.find_element(By.XPATH, ".//span[@aria-hidden='true']")
                        question = question_span.text.strip()
                        print("I just retrieve the following question for radio button from review page: ")
                        print(question)
                        if question:
                            promptradio = f"Given the profile summary: '{summary_radio_questions}', answer the following: '{question}' by sending yes or no. Just send the word yes or the word no, as I am sending it directly to a variable for automation. Do not add anything else."
                            gpt_response = self.get_gpt_response(promptradio)
                            time.sleep(random.uniform(2, 3))
                            print("Here is the response from GPT for radio button: ")
                            print(gpt_response)
                            # Iterate through radio containers to find and click the appropriate option
                            for container in radio_containers:
                                print("I am iterating through radio containers to find and click the appropriate option")
                                radio_input = container.find_element(By.XPATH, ".//input[@type='radio']")
                                print("I found the radio input")
                                print("Now I am finding the label that contain yes or no")
                                label = container.find_element(By.XPATH, ".//label")
                                print("I found the label that contain yes or no and I am ready to click")
                                # Decide which radio button to click based on its value
                                # Use case-insensitive comparison for matching GPT response with label text
                                if gpt_response.lower() == label.text.strip().lower():  # Stripping any leading/trailing whitespace
                                    print("I am clicking the radio button")
                                    label.click()
                                    print("I clicked the radio button")
                                    break  # Assuming only one needs to be selected
            except Exception as e:
                print(f"Error handling radio buttons within div containers: {e}")


            # Find unselected dropdowns and select it based on gpt response to the question from review page
            # Select dropdown
            try:
                # Find all select elements
                selects = self.driver.find_elements(By.XPATH, "//select[@data-test-text-entity-list-form-select]")
                for select_element in selects:
                    select_id = select_element.get_attribute('id')
                    # Create a Select object to interact with the <select> element
                    select = Select(select_element)
                    # Check if the first option (default "Select an option") is selected
                    if select.first_selected_option.get_attribute('value') == "Select an option":
                        # Find the corresponding label with the question
                        label = self.driver.find_element(By.XPATH, f"//label[@for='{select_id}']")
                        question = label.text.strip()
                        print("I just retrieve the following question for dropdown from review page: ")
                        print(question)

                        # Extract all dropdown options except the default "Select an option"
                        options = [option.text.strip() for option in select.options if option.get_attribute('value') != "Select an option"]
                        print("I just retrieve the following options for dropdown from continue page: ")
                        print(options)

                        # Send the question and options to GPT for an answer
                        if question and options:
                            promptselect = f"Given the profile summary: '{summary_select_questions}', and the available options {options}, answer the following: '{question}'. Please send the exact option that you choose, as I am sending it directly to a variable for automation. Do not send anything else. No comment, nothing else. Send you choice from the available options."
                            gpt_response = self.get_gpt_response(promptselect)
                            time.sleep(random.uniform(2, 3))
                            print("Here is the response from GPT for dropdown: ")
                            print(gpt_response)
                            # Iterate through options to find and select the appropriate one
                            # Select the option that matches the GPT response
                            try:
                                select.select_by_visible_text(gpt_response)
                            except Exception as e:
                                print(f"Error selecting dropdown option: {e}")
                    else:
                        print("The dropdown has already been selected, skipping GPT call")
            except Exception as e:
                print(f"Error handling dropdowns: {e}")




            self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Review your application']").click() 
            time.sleep(random.uniform(2, 3))

            #self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Submit application']").click()
            time.sleep(random.uniform(2, 3))
            submit_button =  WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"button[aria-label='Submit application']")))
            #submit_button = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/footer[1]/div[3]/button[2]")
            actions = ActionChains(self.driver)
            actions.move_to_element(submit_button).perform()
            submit_button.click()
            time.sleep(random.uniform(2, 3))

        except Exception as e:
            print("Was not able to apply for job")
            # If for some reason it couldn't apply to the job, it will return the link of the job











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
