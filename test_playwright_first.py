import re
from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    # 1. ניווט לאתר גוגל
    page.goto("https://www.google.com")
    
    # 2. מציאת שדה החיפוש המדויק לפי ה-Role שלו
    search_input = page.get_by_role("combobox")
    search_input.fill("Playwright Python")
    search_input.press("Enter")
    
    # 3. אימות (Assertion) - בדיקה שהכותרת מכילה Playwright
    expect(page).to_have_title(re.compile(r"Playwright"))