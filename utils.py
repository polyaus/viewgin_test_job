import random

from selenium import webdriver


def build_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')

    return webdriver.Chrome(chrome_options=chrome_options)


def random_project_code():
    project_code = ""
    max_len = 6
    alfavit = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for _ in range(max_len):
        randomindex = random.randint(0, len(alfavit) - 1)
        point = alfavit[randomindex]
        project_code += point
    return project_code
