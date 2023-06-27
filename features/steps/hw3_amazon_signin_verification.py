from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC


ORDERS_BTN = (By.ID, 'nav-orders')
SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, 'ap_email')


# @when('Click orders')
# def click_orders_button(context):
#     context.driver.find_element(*ORDERS_BTN).click()
#     # context.app.header.click_orders()
#
#
# # @then('Verify Sign In page opens')
# # def verify_signin_opens(context):
# #     context.app.sign_in_page.verify_signin_opens()
#
# def sign_in_verification(context):
#     context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("Verification Complete")
#     context.driver.wait_until(EC.title_contains('Verification Complete'))
#     # context.app.sign_in_page.verify_signin_opens()
#
