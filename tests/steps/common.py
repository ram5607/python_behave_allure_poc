from behave import given, when, then
from tests.framework.webapp import webapp
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I login into Sales force')
def step_impl_load_website(context):
    webapp.load_website()
    webapp.login_sales_force()


@then('I see Home page')
def step_impl_verify_dashboard(context):
    webapp.verify_dashboard_exists()


@given('I login with {username} and {password} into Sales force')
def step_impl_verify_login(context, username, password):
    webapp.load_website()
    webapp.login_into_sales_force(username, password)


@then('I see the message {message}')
def step_impl_see_message(context, message):
    try:
        WebDriverWait(webapp.get_driver(), 40).until(
            EC.presence_of_element_located((By.XPATH, message)))
        webapp.get_driver().find_element_by_xpath(message)
    except NoSuchElementException:
        print("No element found")
