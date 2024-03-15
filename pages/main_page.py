from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SETTINGS_TAB = (By.XPATH, "//div[text()='Settings']")

    def open_main(self):
        self.open('https://soft.reelly.io/')

    def click_on_settings_option(self):
        self.click(*self.SETTINGS_TAB)