import time

from selenium import webdriver

from locators import SelectorsForProject
from utils import random_project_code


def build_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')

    return webdriver.Chrome(chrome_options=chrome_options)


login_link = "https://office.ideadeploy.space/"


class Page:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def authorization(self):
        username = self.browser.find_element(*SelectorsForProject.USERNAME)
        username.send_keys("qa@viewgin.com")

        password = self.browser.find_element(*SelectorsForProject.PASSWORD)
        password.send_keys("qaviewgin")

        login_button = self.browser.find_element(*SelectorsForProject.LOGIN)
        login_button.click()

    def create_project(self):
        add_project_button = self.browser.find_element(*SelectorsForProject.ADD_PROJECT_BUTTON)
        add_project_button.click()

        code_project = self.browser.find_element(*SelectorsForProject.CODE_PROJECT)
        code_project.send_keys(random_project_code())

        name_project = self.browser.find_element(*SelectorsForProject.NAME_PROJECT)
        name_project.send_keys("Test Selenium(timestamp)")

        table_workers = self.browser.find_elements(*SelectorsForProject.TABLE_WORKERS)
        for idx, table_worker in enumerate(table_workers):
            if idx - 2 >= 0:
                self.browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", table_workers[idx-2])
            if table_worker.text.strip() in ["Test", "Vlad"]:
                time.sleep(1)
                table_worker.click()

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


class TestPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def test_authorization(self):
        page = Page(self.browser, login_link)
        page.open()
        page.authorization()
        page.create_project()