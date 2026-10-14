import re
from playwright.sync_api import Page, expect

# אתר תרגול מעולה ומקובל לבדיקות אוטומציה
LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"

def test_successful_login(page: Page):
    """תסריט חיובי: התחברות בהצלחה עם פרטים נכונים"""
    page.goto(LOGIN_URL)
    
    # 1. מילוי שם משתמש וסיסמה
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    
    # 2. לחיצה על כפתור התחברות
    page.get_by_role("button", name="Submit").click()
    
    # 3. אימות (Assertions) - בדיקת URL והודעת הצלחה
    expect(page).to_have_url(re.compile(r"/logged-in-successfully/"))
    expect(page.get_by_role("heading", name="Logged In Successfully")).to_be_visible()

def test_failed_login(page: Page):
    """תסריט שלילי: ניסיון התחברות עם סיסמה שגויה"""
    page.goto(LOGIN_URL)
    
    # 1. מילוי פרטים שגויים
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("WrongPassword")
    
    # 2. לחיצה על Submit
    page.get_by_role("button", name="Submit").click()
    
    # 3. אימות - הופעת הודעת שגיאה מתאימה
    error_message = page.locator("#error")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Your password is invalid!")