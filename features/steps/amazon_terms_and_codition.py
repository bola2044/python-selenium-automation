from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


ORDER_BTN = (By.ID, "//a[@id='nav-orders']")
SIGN_IN_PAGE = (By.CSS_SELECTOR, "div.a-section")
HELP_PAGE = (By.CSS_SELECTOR, 'a.cs-help-title')
HELP_CONTENT = (By.CSS_SELECTOR, "div.cs-help-content")
PRIVACY_NOTICE_LINK = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


@when('Open and verify amazon help page opens')
def verify_help_page(context):
    context.app.help_page.verify_help_page()


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on amazon privacy notice link')
def click_on_amazon_privacy_and_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    print('After window opened:, all windows:', all_windows)
    context.driver.switch_to.window(all_windows[1])


@then('Verify amazon Privacy Notice page is opened')
def amazon_privacy_and_notice_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/privacy'))


@then('User can close new Window')
def close_blog(context):
    context.driver.close()
    all_windows = context.driver.window_handles
    print('After blog closed:, all windows:', all_windows)


@then('Switch back to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
