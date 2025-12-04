# tests/test_registration.py
import time
from faker import Faker
from pages.register_page import RegisterPage

fake = Faker()

def test_register_happy_path(driver, base_url):
    """
    Happy path registrasi:
    - buka /register
    - isi semua field dengan data valid
    - submit
    - harus redirect ke /login
    """
    page = RegisterPage(driver, base_url)
    page.open()

    name = "nidha"          # minimal 2 huruf
    email = "nidhaalya05@gmail.com"
    phone = "081234567890"
    password = "secret123"

    page.fill_form(name, email, phone, password)
    page.submit()

    time.sleep(1)  # nanti bisa diganti WebDriverWait

    # Asersi: URL sekarang adalah halaman login
    assert "/login" in driver.current_url.lower()


def test_register_negative_name_too_short(driver, base_url):
    """
    Negative path registrasi:
    - Name hanya 1 karakter
    - Registrasi gagal, tetap di /register dan muncul pesan error
    """
    page = RegisterPage(driver, base_url)
    page.open()

    name = "A"                         # cuma 1 huruf
    email = "nidhaalya01@gmail.com"
    phone = "081234567890"
    password = "secret123"

    page.fill_form(name, email, phone, password)
    page.submit()

    time.sleep(1)

    # Masih di /register
    assert "/register" in driver.current_url.lower()

    # Ada pesan error (sesuaikan text dengan app)
    error_text = page.get_error_text().lower()
    assert "name" in error_text or "minimal" in error_text or "2" in error_text
