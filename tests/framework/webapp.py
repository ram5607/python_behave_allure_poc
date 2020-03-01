from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from tests.data.config import settings


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        # self.driver.implicitly_wait(100)

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def quit(self):
        self.driver.quit()

    def login_sales_force(self):
        self.driver.find_element_by_id('username').send_keys('ram1006@gmail.com')
        self.driver.find_element_by_id('password').send_keys('techm@123')
        self.driver.find_element_by_id('Login').click()

    def login_into_sales_force(self, un, pwd):
        self.driver.find_element_by_id('username').send_keys(un)
        self.driver.find_element_by_id('password').send_keys(pwd)
        self.driver.find_element_by_id('Login').click()

    def verify_dashboard_exists(self):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='title slds-truncate'])[1]")))
        try:
            self.driver.find_element_by_xpath("(//span[@class='title slds-truncate'])[1]")
        except NoSuchElementException:
            print("No element found")


webapp = WebApp.get_instance()
