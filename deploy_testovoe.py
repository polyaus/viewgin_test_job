import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import SelectorsForProject
from utils import random_project_code


def build_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')

    return webdriver.Chrome(chrome_options=chrome_options)


login_link = "https://office.ideadeploy.space/login"
logout_link = "https://office.ideadeploy.space/logout"
projects_link = "https://office.ideadeploy.space/projects"
add_project_link = "https://office.ideadeploy.space/add-project"


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        time.sleep(2)


class LoginPage(BasePage):
    def authorization(self):
        username = self.browser.find_element(*SelectorsForProject.USERNAME)
        username.send_keys("qa@viewgin.com")

        password = self.browser.find_element(*SelectorsForProject.PASSWORD)
        password.send_keys("qaviewgin")

        login_button = self.browser.find_element(*SelectorsForProject.LOGIN)
        login_button.click()

        nickname = self.browser.find_element(*SelectorsForProject.NICKNAME)
        assert nickname.text == "QA", f"Nickname is not correct for user: {nickname.text}"

    def enter_invalid_user_data_in_login_form(self):
        username = self.browser.find_element(*SelectorsForProject.USERNAME)
        username.send_keys("qa@viewgin.com")

        password = self.browser.find_element(*SelectorsForProject.PASSWORD)
        random_password = random_project_code()
        password.send_keys(random_password)

        login_button = self.browser.find_element(*SelectorsForProject.LOGIN)
        login_button.click()

        time.sleep(2)
        data_entry_error = self.browser.find_element(*SelectorsForProject.DATA_ENTRY_ERROR)
        assert data_entry_error.text == "Неверные учетные данные", f"User is logged: {data_entry_error.text}"


class ProjectPage(BasePage):
    def create_project(self):
        add_project_button = self.browser.find_element(*SelectorsForProject.ADD_PROJECT_BUTTON)
        add_project_button.click()
        assert self.browser.current_url == add_project_link, f"Create project is not started! Url - {self.url}"

        code_project = self.browser.find_element(*SelectorsForProject.CODE_PROJECT)
        random_code_project = random_project_code()
        code_project.send_keys(random_code_project)

        name_project = self.browser.find_element(*SelectorsForProject.NAME_PROJECT)
        name_project.send_keys("Test Selenium(timestamp)")

        table_workers = self.browser.find_elements(*SelectorsForProject.TABLE_WORKERS)
        add_workers_count = 0
        for idx, table_worker in enumerate(table_workers):
            if idx - 2 >= 0:
                self.browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", table_workers[idx-2])
            worker_name = table_worker.text.strip()
            if worker_name in ["Test", "Vlad"]:
                time.sleep(1)
                table_worker.click()

                time.sleep(1)
                add_workers_count += 1
                add_workers = self.browser.find_elements(*SelectorsForProject.ADDED_WORKERS)
                assert add_workers[-1].text == worker_name, f"Wrong added worker name: {add_workers[-1].text}"
                assert len(add_workers) == add_workers_count, \
                    f"Count add workers is not actual: {len(add_workers)}, {add_workers_count}"

        data_finish_project = self.browser.find_element(*SelectorsForProject.DATA_FINISH_PROJECT)
        data_finish_project.click()
        months_finish = self.browser.find_element(*SelectorsForProject.MONTHS_FINISH)
        months_finish.click()
        november = months_finish.find_element(*SelectorsForProject.NOVEMBER)
        november.click()

        year = self.browser.find_element(*SelectorsForProject.YEAR)
        year.click()
        year.send_keys("2021")

        day = self.browser.find_element(*SelectorsForProject.DAY)
        day.click()
        time.sleep(5)

        save_project = self.browser.find_element(*SelectorsForProject.SAVE_PROJECT)
        self.browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", save_project)
        time.sleep(5)
        save_project.click()

        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.visibility_of_element_located(SelectorsForProject.NAME_PROJECT_IN_PROJECTS))
        projects_title = self.browser.find_element(*SelectorsForProject.PROJECTS_TITLE)
        assert projects_title.text == "Проекты", "Page with projects not opened."

        name_project_in_projects = self.browser.find_element(*SelectorsForProject.NAME_PROJECT_IN_PROJECTS)
        assert name_project_in_projects.text == "Test Selenium(timestamp)", \
            f"The project is not added. {name_project_in_projects.text}"

    def create_project_without_name(self):
        add_project_button = self.browser.find_element(*SelectorsForProject.ADD_PROJECT_BUTTON)
        add_project_button.click()
        assert self.browser.current_url == add_project_link, f"Create project is not started! Url - {self.url}"

        code_project = self.browser.find_element(*SelectorsForProject.CODE_PROJECT)
        random_code_project = random_project_code()
        code_project.send_keys(random_code_project)

        table_workers = self.browser.find_elements(*SelectorsForProject.TABLE_WORKERS)
        add_workers_count = 0
        for idx, table_worker in enumerate(table_workers):
            if idx - 2 >= 0:
                self.browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});",
                                            table_workers[idx - 2])
            worker_name = table_worker.text.strip()
            if worker_name in ["Test", "Vlad"]:
                time.sleep(1)
                table_worker.click()

                time.sleep(1)
                add_workers_count += 1
                add_workers = self.browser.find_elements(*SelectorsForProject.ADDED_WORKERS)
                assert add_workers[-1].text == worker_name, f"Wrong added worker name: {add_workers[-1].text}"
                assert len(add_workers) == add_workers_count, \
                    f"Count add workers is not actual: {len(add_workers)}, {add_workers_count}"

        data_finish_project = self.browser.find_element(*SelectorsForProject.DATA_FINISH_PROJECT)
        data_finish_project.click()
        months_finish = self.browser.find_element(*SelectorsForProject.MONTHS_FINISH)
        months_finish.click()
        november = months_finish.find_element(*SelectorsForProject.NOVEMBER)
        november.click()

        year = self.browser.find_element(*SelectorsForProject.YEAR)
        year.click()
        year.send_keys("2021")

        day = self.browser.find_element(*SelectorsForProject.DAY)
        day.click()
        time.sleep(5)

        save_project = self.browser.find_element(*SelectorsForProject.SAVE_PROJECT)
        self.browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", save_project)
        time.sleep(5)
        save_project.click()

        error_enter_name_project = self.browser.find_element(*SelectorsForProject.ERROR_ENTER_NAME_PROJECT)
        assert error_enter_name_project.text == "Пожалуйста введите название проекта", \
            f"Project added without name, {error_enter_name_project.text}"

    def open_projects_without_login(self):
        assert self.url != self.browser.current_url, "User is logged!"
        assert self.browser.current_url == login_link, "Wrong url!"


class TestsLoginPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def teardown_method(self, method):
        page = BasePage(self.browser, logout_link)
        page.open()

    def test_authorization(self):
        page = LoginPage(self.browser, login_link)
        page.open()
        page.authorization()

    def test_invalid_user_data(self):
        page = LoginPage(self.browser, login_link)
        page.open()
        page.enter_invalid_user_data_in_login_form()


class TestsProjectPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def teardown_method(self, method):
        page = BasePage(self.browser, logout_link)
        page.open()

    def test_create_project_logged_user(self):
        page = LoginPage(self.browser, login_link)
        page.open()
        page.authorization()

        page = ProjectPage(self.browser, projects_link)
        page.open()
        page.create_project()

    def test_create_project_without_name_logged_user(self):
        page = LoginPage(self.browser, login_link)
        page.open()
        page.authorization()

        page = ProjectPage(self.browser, projects_link)
        page.open()
        page.create_project_without_name()

    def test_open_projects_page_with_not_logged_user(self):
        page = ProjectPage(self.browser, projects_link)
        page.open()
        page.open_projects_without_login()
