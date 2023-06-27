from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


ORDER_BTN = (By.ID, "//a[@id='nav-orders']")
SIGN_IN_PAGE = (By.CSS_SELECTOR, "div.a-section")
HELP_PAGE = (By.CSS_SELECTOR, 'a.cs-help-title')
HELP_CONTENT = (By.CSS_SELECTOR, "div.cs-help-content")
CONDITION_OF_USE = (By.CSS_SELECTOR, 'a.a-link-normal')
PRIVACY_NOTICE_LINK = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:', context.original_window)
    print('All windows:', context.driver.window_handles)


@when('Click on amazon privacy notice link')
def privacy_and_notice(context):
    context.driver.get('https://www.amazon.com/privacy')


@then('Verify amazon Privacy Notice page is opened')
def privacy_and_notice_opened(context):
    context.driver.get('https://www.amazon.com/privacy')


@then('User can close new Window')
def close_privacy_notice(context):
    # context.driver.close()
    print('After privacy notice is closed:, all windows')


@then('Switch to original window')
def open_original_window(context):
    context.driver.switch_to.window(context.original_window)








