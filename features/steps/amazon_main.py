from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")
GC_SUBMENU = (By.CSS_SELECTOR, "[data-category='appliances']")
DEPT_SELECT = (By.ID, 'searchDropdownBox')
DEAL_OPTION = (By.CSS_SELECTOR, 'nav-template nav-flyout-content')
NEW_ARRIVALS = (By.CSS_SELECTOR, 'a.nav-a.nav-hasArrow')

@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    # context.app.main_page.open_main_page()


@when('Search for {search_query}')
def search_amazon(context, search_query):
    # context.driver.find_element(*SEARCH_FILED).send_keys(search_query)
    context.driver.find_element(*SEARCH_BTN).click()
    # context.app.header.search_amazon(search_query)


@when('Click Orders')
def click_orders(context):
    element = context.driver.find_element(*ORDERS_BTN)
    print('Before refresh: ', element)
    context.driver.refresh()
    element = context.driver.find_element(*ORDERS_BTN)
    print('After refresh: ', element)
    element.click()
    # context.app.header.click_orders()


@when('Verify Orders btn present')
def click_orders(context):
    # context.driver.find_element(*ORDERS_BTN)
    context.app.header.click_orders()


@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable'
    ).click()


@when('Wait for {sec_amount} sec')
def wait_sec(context, sec_amount):
    sleep(int(sec_amount))


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select a department appliances')
def select_dept(context):
    context.driver.find_element(*DEPT_SELECT)
    # context.app.header.select_dept()


@then('Hover new arrivals')
def hover_new_arrivals(context):
    context.driver.find_element(*NEW_ARRIVALS)


@then('Verify Sign In is clickable')
def verify_signin_popup_btn_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable'
    )


@then('Verify Sign In disappears')
def verify_signin_popup_disappears(context):
    context.driver.wait.until_not(
        EC.visibility_of_element_located(POPUP_SIGNIN_BTN),
        message='Signin btn did not disappear'
    )


@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    print('After conversion: => ', type(expected_amount))
    links_count = len(context.driver.find_elements(*FOOTER_LINKS)) # 36
    print(type(links_count))
    # 36 == 36
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'


@then('Verify Spanish option present')
def verify_spanish_lang_present(context):
    context.app.header.verify_spanish_lang_present()


@then('Verify correct department shown')
def verify_dept(context):
    context.driver.find_element(*DEPT_SELECT)


@then('Verify user sees the deals')
def verify_deal(context):
    context.driver.find_elements(*DEAL_OPTION)
