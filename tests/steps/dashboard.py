from behave import given, when, then
from tests.pages.dashboard import dashboard
from tests.framework.webapp import webapp


@then('Dashboard shows correct headers for row {tittle}')
def verify_section_header(context, tittle):
    dashboard.verify_section_header(tittle)
    webapp.quit()
