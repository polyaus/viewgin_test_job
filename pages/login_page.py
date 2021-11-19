import time

from locators import SelectorsForPages
from pages.base_page import BasePage
from utils import random_project_code


class LoginPage(BasePage):
    def authorization(self):
        username = self.browser.find_element(*SelectorsForPages.USERNAME)
        username.send_keys("qa@viewgin.com")

        password = self.browser.find_element(*SelectorsForPages.PASSWORD)
        password.send_keys("qaviewgin")

        login_button = self.browser.find_element(*SelectorsForPages.LOGIN)
        login_button.click()

        nickname = self.browser.find_element(*SelectorsForPages.NICKNAME)
        assert nickname.text == "QA", f"Nickname is not correct for user: {nickname.text}"

    def enter_invalid_user_data_in_login_form(self):
        username = self.browser.find_element(*SelectorsForPages.USERNAME)
        username.send_keys("qa@viewgin.com")

        password = self.browser.find_element(*SelectorsForPages.PASSWORD)
        random_password = random_project_code()
        password.send_keys(random_password)

        login_button = self.browser.find_element(*SelectorsForPages.LOGIN)
        login_button.click()

        time.sleep(2)
        data_entry_error = self.browser.find_element(*SelectorsForPages.DATA_ENTRY_ERROR)
        assert data_entry_error.text == "Неверные учетные данные", f"User is logged: {data_entry_error.text}"
