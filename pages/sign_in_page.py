from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL = (By.ID, 'ap_email')
    CONDITION_OF_USE = (By.CSS_SELECTOR, 'a.a-link-normal')
    PRIVACY_NOTICE_LINK = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


    def verify_signin_opens(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
        self.verify_element_text('Sign in', *self.SIGNIN_HEADER)
        self.find_element(*self.EMAIL)

    def click_condition_of_use(self):
        condition_of_use = self.driver.find_element(*self.CONDITION_OF_USE)

        actions = ActionChains(self.driver)
        actions.click(condition_of_use)
        actions.perform()

    def click_on_amazon_privacy_notice_link(self):
        privacy_notice_link = self.driver.find_element(*self.PRIVACY_NOTICE_LINK)

        actions = ActionChains(self.driver)
        actions.click(privacy_notice_link)
        actions.perform()

        # print(f"Opening {self.base_url + 'signin'}")
        # self.open_url('https://www.amazon.com/ap/signin')