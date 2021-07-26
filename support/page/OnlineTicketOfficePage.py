from support.page import BasePage
from selenium.webdriver.common.by import By


class OnlineTicketOffice(BasePage):
    # Locators
    CONFORT_1ST_BUTTON = (By.CSS_SELECTOR, "label[for='radioButtonClasse1']")
    TERMS_AND_CONDITION_CHECKBOX = (By.CSS_SELECTOR, "label[for='travelTerms'] i[class='glyphicon glyphicon-ok']")
    PASSENGER_DROPDOWN = (By.CSS_SELECTOR, "button[title='1 Passenger']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#buttonNext")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "#exitButton")

    def select_count_of_passengers(self, quantity):
        self.browser.find_element(*OnlineTicketOffice.PASSENGER_DROPDOWN).click()
        self.browser.find_element_by_css_selector(f"ul[role='menu'] li:nth-child({quantity})").click()

    def select_confort_class(self):
        self.browser.find_element(*OnlineTicketOffice.CONFORT_1ST_BUTTON).click()

    def accept_terms_and_click_continue(self):
        self.browser.find_element(*OnlineTicketOffice.TERMS_AND_CONDITION_CHECKBOX).click()
        self.browser.find_element(*OnlineTicketOffice.CONTINUE_BUTTON).click()

    def click_cancel_button(self):
        self.browser.find_element(*OnlineTicketOffice.CANCEL_BUTTON).click()
