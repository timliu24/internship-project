from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Log in to the page')
def log_in_to_the_page(context):
    context.app.sign_in_page.log_in_to_the_page()
    sleep(5)