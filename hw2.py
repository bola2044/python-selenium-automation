from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# By ID
driver.find_element(By.ID, "//span[@id='nav-link-accountList-nav-line-1']")

# By Xpath, logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# By ID, sign in
driver.find_element(By.ID, "//span[@id='glow-ingress-line1']")
# By Xpath,
driver.find_element(By.XPATH, "//div[@class='nav-line-1-container']")

# By ID, e-mail
driver.find_element(By.ID, "//input[@id='ap_email']")
driver.find_element(By.XPATH, "//label[@class='a-form-label']")

# By ID, continue button
driver.find_element(By.ID, "//input[@id='continue']")

# By ID ,legal txt, contains
driver.find_element(By.ID, "//id='legalTextRow']")
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use']")
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice']")

# By Xpath, need help
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# By ID, forgot your password
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")

# By ID, other sign issues
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")

# By ID, create account
driver.find_element(By.ID, "//a[@id='createAccountSubmit']")