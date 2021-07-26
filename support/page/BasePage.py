from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .TrainResults import TrainResults


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.train_results = TrainResults(browser)
        self.wait = WebDriverWait(self.browser, 5)

    def open_page(self):
        self.browser.get(self.browser.url)
        self.browser.maximize_window()

    def wait_visibility_of_elements(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.train_results.RESULT_TABLE))
        self.browser.implicitly_wait(5)

    def wait_page_title_is_loaded(self, title):
        self.wait.until(EC.title_is(title))
