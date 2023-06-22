from selenium.webdriver.common.by import By
from behave import given, when, then
# from selenium.webdriver.support import expected_conditions as EC


SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, 'ap_email')
ORDERS_BTN = (By.ID, 'nav-orders')


@when("Clicks on orders button")
def click_orders_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()


@then("User see sign-in page")
def sign_in_verification(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("Verification Complete")
    # context.driver.wait_until(EC.title_contains('Verification Complete'))
    context.app.sign_in_page.verify_signin_opens()

