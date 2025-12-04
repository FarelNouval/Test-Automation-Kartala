# Web Automation Testing – Selenium + Pytest

Project automation testing menggunakan **Python**, **Selenium**, dan **Pytest** untuk menguji fitur pada:

https://test-automation.kartala.dev

Fitur yang diuji:
- Registrasi
- Login
- List pengguna
- Logout

---

## 🔧 Setup Tools

### Install & Setup
``bash
git clone https://github.com/username/repo-name.git
cd repo-name
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows
# atau
source .venv/bin/activate     # Linux/Mac

pip install selenium pytest webdriver-manager


▶️ Menjalankan Test

Jalankan semua test:

python -m pytest -v


Jalankan test tertentu:

python -m pytest -v tests/test_login.py


Filter test:

python -m pytest -v -k login
