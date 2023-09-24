import os
import re
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_LOCATION = os.getenv("CHROME_BIN")

from keys import *

def get_codehs_info(student_number, exercise_number):
    global username, password
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')  # Uncomment this line for headless mode
    browser = webdriver.Chrome(options=options)

    browser.get('https://projectstem.org/users/sign_in')

    # fill in the username and password
    element = browser.find_element(By.NAME, 'user[login]')
    element.click()
    element.send_keys(username)
    element = browser.find_element(By.NAME, 'user[password]')
    element.click()
    element.send_keys(password)
    element.submit()


    #student_name = "Hannah Abenante"
    # student_psnr = "583538"
    student_psnr = student_number
    #assignment_nr = "17183038"
    assignment_nr = exercise_number
    assignment_id = "student_grading_" + assignment_nr

    # Navigate to the student's submission
    url = f"https://courses.projectstem.org/courses/128396/assignments/{assignment_nr}/submissions/{student_psnr}"
    print(url)
    browser.get(url)

    # Wait for the page to load

    # Define a maximum wait time (in seconds)
    max_wait_time = 10

    try:
        # Wait for a specific element to be present on the page
        element_present = WebDriverWait(browser, max_wait_time).until(
            EC.presence_of_element_located((By.ID, 'react-tabs-1'))
        )

        # Element found, take a screenshot
        browser.save_screenshot('static/scrn/screenshot.png')
        print("Screenshot taken after element is found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

        #take a screenshot
        print("Taking screenshot...")
        browser.save_screenshot('static/scrn/screenshot.png')

    #input("Press Enter to continue...")

    # Close browser
    browser.close()






