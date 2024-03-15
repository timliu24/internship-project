from pages.base_page import Page
from pages.change_password_page import ChangePasswordPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.change_password_page = ChangePasswordPage(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SignInPage(driver)

