import pytest
import requests
import sqlite3
from playwright.sync_api import sync_playwright

# -------------------------------
# Fixture'lar
# -------------------------------

@pytest.fixture(scope="session")
def api_base_url():
    """Demo API endpoint"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def db_conn():
    """Basit bir in-memory SQLite veritabanı"""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO users(name) VALUES ('Ali')")
    conn.commit()
    yield conn
    conn.close()

@pytest.fixture(scope="session")
def browser():
    """Playwright ile headless Chromium tarayıcısı"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

# -------------------------------
# Testler
# -------------------------------

def test_api_user_check(api_base_url):
    """API testi: JSONPlaceholder sitesinden user bilgisi kontrolü"""
    resp = requests.get(f"{api_base_url}/users/1")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
    assert "email" in data

def test_ui_title_check(browser):
    """UI testi: example.com sayfa başlığını kontrol et"""
    page = browser.new_page()
    page.goto("https://example.com")
    title = page.title()
    page.close()
    assert "Example Domain" in title

def test_db_user_exists(db_conn):
    """Database testi: users tablosunda 'Ali' kaydını kontrol et"""
    cursor = db_conn.execute("SELECT name FROM users WHERE name='Ali'")
    row = cursor.fetchone()
    assert row is not None
    assert row[0] == "Ali"
