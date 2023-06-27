from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPT_SELECT = (By.ID, 'searchDropdownBox')
    APP_SUBMENU = (By.CSS_SELECTOR, "[data-category='appliances']")
    NEW_ARRIVALS = (By.CSS_SELECTOR, 'a.nav-a.nav-hasArrow')
    DEAL_OPTION = (By.CSS_SELECTOR, 'nav-template nav-flyout-content')

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def hover_lang(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)

        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def select_dept(self):
        select_dept = self.find_element(*self.DEPT_SELECT)
        select = Select(select_dept)
        select.select_by_value('search-alias=appliances')

    def verify_spanish_lang_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def hover_new_arrivals(self):
        self.find_element(*self.NEW_ARRIVALS)

    def verify_deal(self):
        deals = self.find_element(*self.DEAL_OPTION)

        actions = ActionChains(self.driver)
        actions.click_and_hold(deals)
        actions.perform()