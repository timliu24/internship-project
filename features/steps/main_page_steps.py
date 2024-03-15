from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(5)


@when('Click on settings option')
def click_on_settings_option(context):
    context.app.main_page.click_on_settings_option()
