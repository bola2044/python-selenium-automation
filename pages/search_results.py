from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    APP_SUBMENU = (By.CSS_SELECTOR, "[data-category='appliances']")
    DEPT_SELECT = (By.ID, 'searchDropdownBox')
    CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT_TEXT)

        ### Class example (we didn't have verify_element_text() in base Page):
        # actual_result = self.driver.find_element(*self.RESULT_TEXT).text
        # assert expected_result == actual_result, \
        #     f'Error! Expected {expected_result} bot got actual {actual_result}'

    def verify_dept(self):
        self.wait_for_element_appear(*self.DEPT_SELECT)

    def verify_user_see_empty_cart_message(self):
        self.wait_for_element_appear(*self.CART)
