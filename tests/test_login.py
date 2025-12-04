import time

from pages.login_page import LoginPage

def test_login_happy_path(driver, base_url):
    """
    Login dengan email & password valid
    """
    login_page = LoginPage(driver, base_url)
    login_page.open()

    valid_email = "fareldazz123@gmail.com"   # ganti sesuai user yang sudah kamu register
    valid_password = "farel1"             # ganti sesuai password

    login_page.login(valid_email, valid_password)
    time.sleep(1)

    # Setelah login → harus redirect ke list pengguna (root)
    assert base_url.rstrip("/") == driver.current_url.rstrip("/")


def test_login_negative_invalid_credentials(driver, base_url):
    """
    Login gagal dengan email/password salah
    """
    login_page = LoginPage(driver, base_url)
    login_page.open()

    login_page.login("email.salah@example.com", "wrongpassword")
    time.sleep(1)

    assert "/login" in driver.current_url.lower()

    error_text = login_page.get_error_text().lower()
    assert "invalid" in error_text or "gagal" in error_text or "salah" in error_text
