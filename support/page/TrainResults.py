from time import sleep
from selenium.webdriver.common.by import By


class TrainResults:
    # Locators
    RESULT_TABLE = (By.CSS_SELECTOR, "#tickets")
    OUTWARD_RADIO_BUTTON = (By.CSS_SELECTOR, ".no-print input[name='selectedOutward']")
    RETURN_RADIO_BUTTON = (By.CSS_SELECTOR, ".no-print input[name='selectedReturn']")
    BUY_BUTTON = (By.CSS_SELECTOR, "#buyTicketButton")

    def __init__(self, browser):
        self.browser = browser

    def buy_tickets(self):
        self.browser.find_element(*TrainResults.OUTWARD_RADIO_BUTTON).click()
        sleep(1)
        self.browser.find_element(*TrainResults.RETURN_RADIO_BUTTON).click()
        self.browser.find_element(*TrainResults.BUY_BUTTON).click()
