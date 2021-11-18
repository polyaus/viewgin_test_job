from selenium.webdriver.common.by import By


class SelectorsForProject:
    CODE_PROJECT = (By.CSS_SELECTOR, "#code")
    USERNAME = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN = (By.CSS_SELECTOR, ".btn")
    ADD_PROJECT_BUTTON = (By.CSS_SELECTOR, ".main-content .btn-success")
    NAME_PROJECT = (By.CSS_SELECTOR, "#title")
    TABLE_WORKERS = (By.CSS_SELECTOR, ".card-body .table tr td:nth-child(2)")
    DATA_FINISH_PROJECT = (By.CSS_SELECTOR, ".card-body input[name='endDate']")
    MONTHS_FINISH = (By.CSS_SELECTOR, ".flatpickr-month .flatpickr-monthDropdown-months")
    DATES_FINISH = (By.CSS_SELECTOR, ".dayContainer .flatpickr-day")
    NOVEMBER = (By.CSS_SELECTOR, ".flatpickr-month .flatpickr-monthDropdown-months option[value='10']")
    YEAR = (By.CSS_SELECTOR, ".flatpickr-month .numInputWrapper .cur-year")
    DAY = (By.CSS_SELECTOR, ".flatpickr-innerContainer .dayContainer .flatpickr-day[aria-label='November 30, 2021']")
    SAVE_PROJECT = (By.CSS_SELECTOR, ".card-body .btn-primary[type='submit']")