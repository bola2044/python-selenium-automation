from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


HELP_PAGE = (By.XPATH, "//div[@class='cs-help-container']")
TC_PAGE = (By.XPATH, "//div[@class='cs-help-sidebar-module topic-sidebar']")
COND_OF_USE = (By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use']")
PRIVACY_NOTICE_LINK = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-link-accountList')

@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

    @when('Click on SignIn popup button')
    def click_sign_in_popup_btn(context):
        context.driver.find_element(*SIGNIN_BTN).click()
        context.driver.wait.until(EC.new_window_is_opened)
sleep(3)
@then('Amazon T&C page is opened')
def open_amazon_terms_and_condition_page(context):
    context.driver.open_amazon_terms_and_condition_page = context.driver.find_element(*COND_OF_USE ).text

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

    @then('Close new Window')
    def close_blog(context):
        context.driver.close()
        all_windows = context.driver.window_handles
        print('After blog closed:, all windows:', all_windows)

    @then('Return to original window')
    def switch_to_original_window(context):
        context.driver.switch_to.window(context.original_window)
