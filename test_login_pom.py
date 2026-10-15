from playwright.sync_api import expect

def test_successful_login(login_page):
    login_page.login("practice", "SuperSecretPassword!")
    # בדיקה גמישה שמחפשת את הליבה של הודעת ההצלחה
    expect(login_page.flash_message).to_contain_text("logged into a secure area")

def test_invalid_login_shows_error(login_page):
    login_page.login("wrong_user", "wrong_password")
    # בדיקה גמישה שמחפשת את הליבה של הודעת השגיאה
    expect(login_page.flash_message).to_contain_text("invalid")