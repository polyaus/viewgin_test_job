import time


LOGIN_LINK = "https://office.ideadeploy.space/login"
LOGOUT_LINK = "https://office.ideadeploy.space/logout"
PROJECTS_LINK = "https://office.ideadeploy.space/projects"
ADD_PROJECT_LINK = "https://office.ideadeploy.space/add-project"


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        time.sleep(2)
