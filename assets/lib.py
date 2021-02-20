from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Lib:
    def __init__(self, driver):
        self.driver = driver


    def wait_for_element(self, selector, by):
        return WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((by, selector)))