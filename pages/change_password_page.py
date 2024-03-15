from selenium.webdriver.common.by import By
from pages.base_page import Page


class ChangePasswordPage(Page):
    NEW_PASSWORD_SUBTITLE = (By.XPATH, "//div[contains(text(), 'Please enter new password')]")
    NEW_PASSWORD_FIELD = (By.ID, "Enter-new-password")
    REPEAT_PASSWORD_FIELD = (By.ID, "Repeat-password")
    CHANGE_PASSWORD_BUTTON = (By.XPATH, "//a[@class='submit-button-2 w-button']")

    def verify_the_right_page_opens(self):
        actual_text = self.find_element(*self.NEW_PASSWORD_SUBTITLE).text
        assert "enter new password" in actual_text, f"Enter new password text not found."

    def add_some_test_password_to_the_input_fields(self):
        self.input_text('test1234', *self.NEW_PASSWORD_FIELD)
        self.input_text('test1234', *self.REPEAT_PASSWORD_FIELD)

    def verify_the_change_password_button_is_available(self):
        actual_text = self.find_element(*self.CHANGE_PASSWORD_BUTTON).text
        assert "Change password" in actual_text, f"Change password button not found."