import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import SelectorsForPages
from pages.base_page import BasePage, ADD_PROJECT_LINK, LOGIN_LINK
from utils import random_project_code


class ProjectPage(BasePage):
    def create_project(self):
        add_project_button = self.browser.find_element(*SelectorsForPages.ADD_PROJECT_BUTTON)
        add_project_button.click()
        assert self.browser.current_url == ADD_PROJECT_LINK, f"Create project is not started! Url - {self.url}"

        code_project = self.browser.find_element(*SelectorsForPages.CODE_PROJECT)
        random_code_project = random_project_code()
        code_project.send_keys(random_code_project)

        name_project = self.browser.find_element(*SelectorsForPages.NAME_PROJECT)
        name_project.send_keys("Test Selenium(timestamp)")

        table_workers = self.browser.find_elements(*SelectorsForPages.TABLE_WORKERS)
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
                add_workers = self.browser.find_elements(*SelectorsForPages.ADDED_WORKERS)
                assert add_workers[-1].text == worker_name, f"Wrong added worker name: {add_workers[-1].text}"
                assert len(add_workers) == add_workers_count, \
                    f"Count add workers is not actual: {len(add_workers)}, {add_workers_count}"

        data_finish_project = self.browser.find_element(*SelectorsForPages.DATA_FINISH_PROJECT)
        data_finish_project.click()
        months_finish = self.browser.find_element(*SelectorsForPages.MONTHS_FINISH)
        months_finish.click()
        november = months_finish.find_element(*SelectorsForPages.NOVEMBER)
        november.click()

        year = self.browser.find_element(*SelectorsForPages.YEAR)
        year.click()
        year.send_keys("2021")

        day = self.browser.find_element(*SelectorsForPages.DAY)
        day.click()
        time.sleep(5)

        save_project = self.browser.find_element(*SelectorsForPages.SAVE_PROJECT)
        self.browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", save_project)
        time.sleep(5)
        save_project.click()

        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.visibility_of_element_located(SelectorsForPages.NAME_PROJECT_IN_PROJECTS))
        projects_title = self.browser.find_element(*SelectorsForPages.PROJECTS_TITLE)
        assert projects_title.text == "Проекты", "Page with projects not opened."

        name_project_in_projects = self.browser.find_element(*SelectorsForPages.NAME_PROJECT_IN_PROJECTS)
        assert name_project_in_projects.text == "Test Selenium(timestamp)", \
            f"The project is not added. {name_project_in_projects.text}"

    def create_project_without_name(self):
        add_project_button = self.browser.find_element(*SelectorsForPages.ADD_PROJECT_BUTTON)
        add_project_button.click()
        assert self.browser.current_url == ADD_PROJECT_LINK, f"Create project is not started! Url - {self.url}"

        code_project = self.browser.find_element(*SelectorsForPages.CODE_PROJECT)
        random_code_project = random_project_code()
        code_project.send_keys(random_code_project)

        table_workers = self.browser.find_elements(*SelectorsForPages.TABLE_WORKERS)
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
                add_workers = self.browser.find_elements(*SelectorsForPages.ADDED_WORKERS)
                assert add_workers[-1].text == worker_name, f"Wrong added worker name: {add_workers[-1].text}"
                assert len(add_workers) == add_workers_count, \
                    f"Count add workers is not actual: {len(add_workers)}, {add_workers_count}"

        data_finish_project = self.browser.find_element(*SelectorsForPages.DATA_FINISH_PROJECT)
        data_finish_project.click()
        months_finish = self.browser.find_element(*SelectorsForPages.MONTHS_FINISH)
        months_finish.click()
        november = months_finish.find_element(*SelectorsForPages.NOVEMBER)
        november.click()

        year = self.browser.find_element(*SelectorsForPages.YEAR)
        year.click()
        year.send_keys("2021")

        day = self.browser.find_element(*SelectorsForPages.DAY)
        day.click()
        time.sleep(5)

        save_project = self.browser.find_element(*SelectorsForPages.SAVE_PROJECT)
        self.browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", save_project)
        time.sleep(5)
        save_project.click()

        error_enter_name_project = self.browser.find_element(*SelectorsForPages.ERROR_ENTER_NAME_PROJECT)
        assert error_enter_name_project.text == "Пожалуйста введите название проекта", \
            f"Project added without name, {error_enter_name_project.text}"

    def open_projects_without_login(self):
        assert self.url != self.browser.current_url, "User is logged!"
        assert self.browser.current_url == LOGIN_LINK, "Wrong url!"
