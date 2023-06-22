from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)

        def click_orders(self):
            self.click(*self.ORDERS_BTN)
