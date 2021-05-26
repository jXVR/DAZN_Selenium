from locators import sign_up_page_locators as locators
from assets.urls import SIGN_UP_URL
from assets.lib import Lib
from selenium.webdriver.common.by import By


class SignInPageObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def open_page(self):
        self.driver.get(SIGN_UP_URL)

    def wait_for_the_select_subscription_plan_page_to_be_open(self):
        Lib.wait_for_element(self, locators.SELECT_SUBSCRIPTION_PLAN_PAGE, By.CSS_SELECTOR)

    def wait_for_the_create_account_page_to_be_open(self):
        Lib.wait_for_element(self, locators.CREATE_ACCOUNT_PAGE, By.CSS_SELECTOR)

    def wait_for_the_select_payment_page_to_be_open(self):
        Lib.wait_for_element(self, locators.SELECT_PAYMENT_PAGE, By.CSS_SELECTOR)

    def wait_for_the_sign_up_confirmation_page_to_be_open(self):
        Lib.wait_for_element(self, locators.SIGN_UP_CONFIRMATION_PAGE, By.CSS_SELECTOR)

    def annual_plan_container(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PLAN_DETAILS_ANNUAL)

    def monthly_plan_container(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PLAN_DETAILS_MONTHLY)

    # def monthly_plan_container(self):
    #     self.driver.find_element(By.XPATH, '//*[contains(text(), "PAY WITH CREDIT")')

    def monthly_plan_regular_button(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PLAN_DETAILS_REGULAR_BUTTON)

    def first_name_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.FIRST_NAME_FIELD)

    def last_name_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.LAST_NAME_FIELD)

    def email_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.EMAIL_FIELD)

    def email_confirmation_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.CONFIRM_EMAIL_FIELD)

    def password_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def create_account_button(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def select_credit_card_payment_method(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def credit_card_number_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def credit_card_expiry_month_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def credit_card_expiry_year_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def credit_card_security_code_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def credit_card_street_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def credit_card_house_number_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def credit_card_postal_code_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def credit_card_city_field(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def credit_card_submit_button(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)

    def sign_up_confirmation_button(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)


