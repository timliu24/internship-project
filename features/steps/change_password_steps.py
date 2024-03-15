from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Verify the right page opens')
def verify_the_right_page_opens(context):
    context.app.change_password_page.verify_the_right_page_opens()


@when('Add some test password to the input fields')
def add_some_test_password_to_the_input_fields(context):
    context.app.change_password_page.add_some_test_password_to_the_input_fields()


@then('Verify the “Change password” button is available')
def verify_the_change_password_button_is_available(context):
    context.app.change_password_page.verify_the_change_password_button_is_available()