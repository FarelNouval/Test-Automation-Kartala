# pages/users_page.py
from selenium.webdriver.common.by import By

class UsersPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/"   # list pengguna di root

    # Contoh locator, sesuaikan dengan HTML aslinya:
    HEADING = (By.XPATH, "//h1[contains(., 'User') or contains(., 'Users')]")
    USER_ROWS = (By.CSS_SELECTOR, "table tbody tr, .user-row")

    # NANTI: kamu bilang mau kasih id ke button logout.
    # misal id="btn-logout"
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")


    def is_at_users_page(self):
        return self.url.rstrip("/") == self.driver.current_url.rstrip("/")

    def has_any_user(self):
        rows = self.driver.find_elements(*self.USER_ROWS)
        return len(rows) > 0

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
