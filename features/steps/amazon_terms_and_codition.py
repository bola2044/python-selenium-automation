from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



ORDER_BTN = (By.ID, "//a[@id='nav-orders']")
SIGN_IN_PAGE = (By.CSS_SELECTOR, "div.a-section")
COND_OF_USE = (By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use']")
HELP_PAGE = (By.XPATH, "//div[@class='cs-help-container']")
HELP_CONTENT = (By.CSS_SELECTOR, "div.cs-help-content")
PRIVACY_NOTICE_LINK = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when("User Clicks on orders button")
def click_orders_button(context):
    context.driver.find_element(*ORDER_BTN).click()


@then('User can see sign-in page')
def user_see_sign_in_page(context):
    context.driver.find_element(*SIGN_IN_PAGE)
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))


@when('click on condition of use button')
def condition_of_use(context):
    context.driver.find(*COND_OF_USE).click()


# @when('Opens amazon help page')
# def amazon_help_page(context):
#     context.driver.find_element(*HELP_PAGE)


@then('User can see help content')
def help_content(context):
    context.driver.find_element(*HELP_CONTENT )


@given('User is on amazon help page')
def amazon_help_page(context):
    # context.driver.find_element(*HELP_PAGE)
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


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
