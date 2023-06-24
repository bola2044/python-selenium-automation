from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class HelpPage(Page):
    HELP_PAGE = (By.CSS_SELECTOR, 'a.cs-help-title')

    def verify_help_page(self):
        help_page = self.find_element(*self.HELP_PAGE)

        actions = ActionChains(self.driver)
        actions.move_to_element(help_page)
        actions.perform()

        # self.find_element(*self.HELP_PAGE)
        # self.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))



