from playwright.sync_api import expect

def test_login_with_wrong_password(page):
    page.goto("https://www.saucedemo.com")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Username and password do not match")).to_be_visible()



def test_successful_login(page):
    page.goto("https://www.saucedemo.com")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Products")).to_be_visible()