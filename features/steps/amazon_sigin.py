from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC

SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, 'ap_email')


@then('Verify Sign In page opens')
def verify_signin_opens(context):
    context.app.sign_in_page.verify_signin_opens()

     # Verify URL:
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
    # Verify header
    # actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    # assert actual_text == 'Sign in', f'Expected Sign in header but got {actual_text}'
    # Verify email field present