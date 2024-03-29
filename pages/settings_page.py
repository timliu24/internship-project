from selenium.webdriver.common.by import By
from pages.base_page import Page


class SettingsPage(Page):
    # CHANGE_PASSWORD_TAB = (By.XPATH, "//a[@href='/set-new-password']")
    CHANGE_PASSWORD_TAB = (By.XPATH, "//div[contains(text(), 'Change password')]")

    def click_on_change_password_option(self):
        self.wait_element_clickable_click(*self.CHANGE_PASSWORD_TAB)