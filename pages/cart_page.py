from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def verify_empty_cart(self, expected_result):
        self.verify_element_text(expected_result, *self.CART)

    # from pages.base_page import Page
    #
    # class CartPage(Page):
    #     PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
    #
    #     def verify_product_name(self, part_name):
    #         self.verify_partial_text(part_name, *self.PRODUCT_NAME)






