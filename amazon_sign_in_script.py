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

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//a[@id='nav-orders']"). click()

# create a new Chrome browser instance
service = Service(driver_path)

driver.find_element(By.XPATH, "//div[@class='a-section a-padding-medium auth-workflow']")

driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

driver.find_element(By.XPATH, "//label[@class='a-form-label']")

expected_result = '"label"'
actual_result = driver.find_element(By.XPATH, "//label[@class='a-form-label']")

print('Test Passed!')

driver.quit()
