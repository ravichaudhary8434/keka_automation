import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
print(EMAIL)

# Using this to check if its the first time of the day or not
# Default initiated with True.
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() + "/chromedriver"
print(chrome_driver)

def keka_logout():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    print('Logout Process Started: ')

    browser.get("https://lcx.keka.com/#/home")
    print('Website Opened')

    time.sleep(5)

    email = browser.find_element('id', 'email')
    email.send_keys(EMAIL) # Enter your email here
    print('Email Entered')

    continue_button = browser.find_element('xpath', '/html/body/div/div[2]/div[1]/div[2]/form[1]/div/button')
    continue_button.click()
    print('Continue Button clicked')

    password = browser.find_element('id','password')
    password.send_keys(PASSWORD) # Enter your password here
    print('Password Entered')

    login_button = browser.find_element('xpath','/html/body/div/div[2]/div[1]/div[2]/form/div/button')
    login_button.click()
    print('Login Button Clicked')


    time.sleep(15)

    web_clockout_button = browser.find_element('xpath', '/html/body/xhr-app-root/div/xhr-home/div/home-dashboard/div/div/div/div/div[2]/div/div[5]/div[6]/home-attendance-clockin-widget/div/div[1]/div/div[2]/div/div[2]/div[1]/div/button')
    web_clockout_button.click()
    print('WebClock Out Button Clicked')

    time.sleep(5)

    web_clockout_confirm_button = browser.find_element('xpath', '/html/body/xhr-app-root/div/xhr-home/div/home-dashboard/div/div/div/div/div[2]/div/div[5]/div[6]/home-attendance-clockin-widget/div/div[1]/div/div[2]/div/div[2]/div/div[1]/button[1]')
    web_clockout_confirm_button.click()
    print('Confirmed WebClock Out')


    time.sleep(5)

    location_request_button = browser.find_element('xpath', '/html/body/modal-container/div[2]/div/xhr-confirm-dialog/div[3]/button[1]')
    
    location_request_button.click()
    print('Rejected location request')

    time.sleep(5)
    print(time.strftime("Cron Successfully ran last at: " + "%Y-%m-%d %H:%M"))
    browser.quit()


keka_logout()
