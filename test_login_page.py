from pages.base_page import LOGIN_LINK, LOGOUT_LINK, BasePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from utils import build_browser


class TestsLoginPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def teardown_method(self, method):
        page = LogoutPage(self.browser, LOGOUT_LINK)
        page.open()

    def test_authorization(self):
        page = LoginPage(self.browser, LOGIN_LINK)
        page.open()
        page.authorization()

    def test_invalid_user_data(self):
        page = LoginPage(self.browser, LOGIN_LINK)
        page.open()
        page.enter_invalid_user_data_in_login_form()

        self.browser.get_screenshot_as_file("screenshots/test_invalid_user_data.png")
