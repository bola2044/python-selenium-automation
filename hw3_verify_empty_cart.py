from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ORDER_BUTTON = (By.ID, "nav-cart-count")
EMPTY_CART = (By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]")


@when('click on cart button')
def click_on_cart_button(context):
    context.driver.find_element("*ORDER_BUTTON").click()


@then('User see empty cart message')
def user_see_empty_cart_message(context):
    context.driver.find_element("*EMPTY_CART").text()