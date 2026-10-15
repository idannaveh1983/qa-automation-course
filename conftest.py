import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """
    Fixture שמייצר את מופע ה-LoginPage ומנווט אליו
    אוטומטית לפני כל טסט שמבקש אותו.
    """
    login_pg = LoginPage(page)
    login_pg.navigate("https://practice.expandtesting.com/login")
    return login_pg