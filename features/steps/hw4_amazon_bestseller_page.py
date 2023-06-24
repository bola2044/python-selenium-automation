from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep

SEARCH_BTN = (By.ID, 'nav-search-submit-button')
SEARCH_BESTSELLER = (By.CSS_SELECTOR, 'a.nav-a')
BESTSELLER_LINKS = (By.CSS_SELECTOR, "a[href='/Best-Sellers/zgbs/ref=zg_bsms_tab']")


@given('Open amazon main page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()


@when('Search for {search_query}')
def search_amazon(context, search_query):
    context.driver.find_element(*SEARCH_BESTSELLER).text().send_keys(search_query)
    context.driver.find_element(*SEARCH_BESTSELLER).click()


@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)

links_count = len(context.driver.find_element(*BESTSELLER_LINKS))  # 5
print(type(links_count))


# 5 == 5
assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'
