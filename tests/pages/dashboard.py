# from framework.webapp import webapp
from tests.framework.webapp import webapp


class Dashboard:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Dashboard()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def verify_section_header(self, tittle):
        print('The headers are:' + self.driver.find_element_by_xpath('(//h4[@class="slds-text-title_caps section-header"])[1]').text)
        self.driver.find_element_by_class_name('slds-text-title_caps section-header').text


dashboard = Dashboard.get_instance()
