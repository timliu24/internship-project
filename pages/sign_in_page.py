from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE = (By.CSS_SELECTOR, "[class*='login-button w-button']")

    def log_in_to_the_page(self):
        self.input_text('enter your own email', *self.EMAIL_FIELD)
        self.input_text('enter your own password', *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE)
