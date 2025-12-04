# 🚀 Web Automation Testing – Selenium + Pytest

Automation testing untuk aplikasi web:

👉 **https://test-automation.kartala.dev**

Project ini menguji fitur:

- Registrasi pengguna  
- Login pengguna  
- List pengguna  
- Logout  

Teknologi yang digunakan:

- **Python**
- **Selenium WebDriver**
- **Pytest**
- **WebDriver Manager**

---

## 📁 Project Structure

TES-KARTALA/
├─ .venv/ # Virtual environment
├─ pages/ # Page Object Model (POM)
│ ├─ init.py
│ ├─ login_page.py
│ ├─ register_page.py
│ ├─ users_page.py
├─ tests/
│ ├─ test_login.py
│ ├─ test_register.py
│ ├─ test_users_logout.py
├─ conftest.py
└─ README.md

yaml
Salin kode

---

## 🛠️ Installation & Setup

### 1️⃣ Clone repository
bash
git clone https://github.com/username/repo-name.git
cd repo-name
2️⃣ Create virtual environment
bash
Salin kode
python -m venv .venv
3️⃣ Activate virtual environment
Windows (PowerShell)
bash
Salin kode
.\.venv\Scripts\Activate.ps1
Jika PowerShell memblokir script:

bash
Salin kode
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
Linux / MacOS
bash
Salin kode
source .venv/bin/activate
4️⃣ Install dependencies
bash
Salin kode
python -m pip install selenium pytest webdriver-manager
⚙️ Pytest Configuration (conftest.py)
python
Salin kode
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url():
    return "https://test-automation.kartala.dev"

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
🧩 Page Object Model (POM)
🔐 Login Page (pages/login_page.py)
python
Salin kode
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
        time.sleep(2)

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
📝 Register Page (pages/register_page.py)
python
Salin kode
import time
from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/register"

    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE_INPUT = (By.NAME, "phone")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Register']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-red-500, .error")

    def open(self):
        self.driver.get(self.url)
        time.sleep(2)

    def fill_form(self, name, email, phone, password):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
👥 Users Page (pages/users_page.py)
python
Salin kode
import time
from selenium.webdriver.common.by import By

class UsersPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/"

    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")

    def is_at_users_page(self):
        return self.url.rstrip("/") == self.driver.current_url.rstrip("/")

    def click_logout(self):
        time.sleep(1)
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
🧪 Test Scenarios
1️⃣ Login Tests (tests/test_login.py)
python
Salin kode
import time
from pages.login_page import LoginPage

def test_login_happy_path(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login("valid@example.com", "password123")
    time.sleep(1)
    assert base_url.rstrip("/") == driver.current_url.rstrip("/")

def test_login_negative_invalid_credentials(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login("invalid@example.com", "wrongpass")
    time.sleep(1)
    assert "/login" in driver.current_url.lower()
2️⃣ Registration Tests (tests/test_register.py)
python
Salin kode
import time
from pages.register_page import RegisterPage

def test_register_happy_path(driver, base_url):
    page = RegisterPage(driver, base_url)
    page.open()
    page.fill_form("DaffaUser", "user123@example.com", "08123456789", "secret123")
    page.submit()
    time.sleep(1)
    assert "/login" in driver.current_url.lower()

def test_register_negative_name_too_short(driver, base_url):
    page = RegisterPage(driver, base_url)
    page.open()
    page.fill_form("A", "invalid@example.com", "08123456789", "secret123")
    page.submit()
    time.sleep(1)
    assert "/register" in driver.current_url.lower()
3️⃣ Logout Tests (tests/test_users_logout.py)
python
Salin kode
import time
from pages.login_page import LoginPage
from pages.users_page import UsersPage

def test_users_list_requires_login(driver, base_url):
    driver.get(base_url + "/")
    time.sleep(1)
    assert "/login" in driver.current_url.lower()

def test_logout_from_users_page(driver, base_url):
    login_page = LoginPage(driver, base_url)
    users_page = UsersPage(driver, base_url)

    login_page.open()
    login_page.login("valid@example.com", "password123")
    time.sleep(1)

    assert users_page.is_at_users_page()

    users_page.click_logout()
    time.sleep(1)

    assert "/login" in driver.current_url.lower()
▶️ Running Tests
Jalankan semua test
bash
Salin kode
python -m pytest -v
Jalankan test tertentu
bash
Salin kode
python -m pytest -v tests/test_login.py
Filter test berdasarkan keyword
bash
Salin kode
python -m pytest -v -k login
