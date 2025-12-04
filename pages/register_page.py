# pages/register_page.py
from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/register"

    # LOCATORS – sesuaikan jika perlu
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE_INPUT = (By.NAME, "phone")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Register']")
    # misal error message pakai class .error atau .text-red-500
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error, .text-red-500")

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, name, email, phone, password):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

        self.driver.find_element(*self.PHONE_INPUT).clear()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
