# pages/login_page.py
import time
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/login"

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error, .text-red-500")

    def open(self):
        self.driver.get(self.url)
        time.sleep(5)
    
    def _type_slowly(self, element, text, delay: float = 1):
        element.clear()
        for ch in text:
            element.send_keys(ch)
            time.sleep(delay)

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
