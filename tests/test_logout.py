# tests/test_users_logout.py
import time
from pages.login_page import LoginPage
from pages.users_page import UsersPage

def test_users_list_requires_login(driver, base_url):
    """
    Negative-ish for list pengguna:
    - akses / tanpa login
    - biasanya akan redirect ke /login (tergantung implementasi)
    """
    driver.get(base_url + "/")
    time.sleep(1)

    # kalau belum login, kemungkinan diarahkan ke /login
    assert "/login" in driver.current_url.lower()


def test_logout_from_users_page(driver, base_url):
    """
    Happy path logout:
    - login dengan user valid
    - sampai di halaman list pengguna
    - klik tombol logout
    - kembali ke halaman login
    """
    login_page = LoginPage(driver, base_url)
    users_page = UsersPage(driver, base_url)

    # login dulu
    login_page.open()
    valid_email = "fareldazz123@gmail.com"  # GANTI
    valid_password = "farel1"           # GANTI
    login_page.login(valid_email, valid_password)
    time.sleep(1)

    # pastikan sudah di list pengguna
    assert base_url.rstrip("/") == driver.current_url.rstrip("/")

    # klik logout (butuh id tombol logout sudah di-set di HTML)
    users_page.click_logout()
    time.sleep(1)

    # harus kembali ke /login
    assert "/login" in driver.current_url.lower()
