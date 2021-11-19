from pages.base_page import BasePage, LOGOUT_LINK, PROJECTS_LINK
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.projects_page import ProjectPage
from utils import build_browser


class TestsProjectPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def teardown_method(self, method):
        page = LogoutPage(self.browser, LOGOUT_LINK)
        page.open()

    def test_create_project_logged_user(self):
        page = LoginPage(self.browser, LOGOUT_LINK)
        page.open()
        page.authorization()

        page = ProjectPage(self.browser, PROJECTS_LINK)
        page.open()
        page.create_project()

    def test_create_project_without_name_logged_user(self):
        page = LoginPage(self.browser, LOGOUT_LINK)
        page.open()
        page.authorization()

        page = ProjectPage(self.browser, PROJECTS_LINK)
        page.open()
        page.create_project_without_name()

        self.browser.get_screenshot_as_file("screenshots/test_create_project_without_name_logged_user.png")

    def test_open_projects_page_with_not_logged_user(self):
        page = ProjectPage(self.browser, PROJECTS_LINK)
        page.open()
        page.open_projects_without_login()

        self.browser.get_screenshot_as_file("screenshots/test_open_projects_page_with_not_logged_user.png")
