from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_CONTAINER = (By.ID, 'div#nav-cart-count-container')
CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")


@given('Open amazon main page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()


@when('click on cart button')
def click_cart_container(context):
    context.click_cart_container = context.driver.find_element(*CART_CONTAINER).click()


@then('Verify User see empty cart message')
def user_see_empty_cart_message(context):
    # context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    # context.driver.user_see_empty_cart_message = context.driver.find_element(*CART).text()
    context.app.cart_page.verify_user_see_empty_cart()