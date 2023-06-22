from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL = (By.ID, 'ap_email')

    def verify_open_signin(self):
        print(f"Opening {self.base_url + 'signin'}")
        self.open_url('https://www.amazon.com/ap/signin')