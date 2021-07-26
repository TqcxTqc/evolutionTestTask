from selenium.webdriver.common.by import By
from .BasePage import BasePage


class HomePage(BasePage):
    # Locators
    DEPART_FROM_FIELD = (By.CSS_SELECTOR, "input[placeholder='From ']")
    ARRIVE_TO_FIELD = (By.CSS_SELECTOR, "input[placeholder='To ']")
    CALENDAR_DEPART_FIELD = (By.CSS_SELECTOR, "input#datepicker-first")
    CALENDAR_ARRIVAL_FIELD = (By.CSS_SELECTOR, "input#datepicker-second")
    ARRIVAL_TABLE_DATES = (By.XPATH,
                           "//table[@id='datepicker-second_table']//div[@class='picker__day picker__day--infocus'] | //table[@id='datepicker-second_table']//div[@class='picker__day picker__day--outfocus']")
    DEPARTURE_TABLE_DATES = (By.XPATH,
                             "//table[@id='datepicker-first_table']//div[@class='picker__day picker__day--infocus'] | //table[@id='datepicker-first_table']//div[@class='picker__day picker__day--outfocus']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[value='Submit »']")
    CONFORT_1ST_LABEL = (By.CSS_SELECTOR, "#option1Label")
    PASSENGERS = (By.CSS_SELECTOR, ".filter-option")

    def select_departure_date(self, calendar_date):
        self.browser.find_element(*HomePage.CALENDAR_DEPART_FIELD).click()
        date_table = self.browser.find_elements(*HomePage.DEPARTURE_TABLE_DATES)

        self.__select_calendar_date(date_table, calendar_date)

    def select_arrival_date(self, calendar_date):
        self.browser.find_element(*HomePage.CALENDAR_ARRIVAL_FIELD).click()
        date_table = self.browser.find_elements(*HomePage.ARRIVAL_TABLE_DATES)

        self.__select_calendar_date(date_table, calendar_date)

    def fill_and_search_departure_and_arrival(self, train_from, train_to):
        self.browser.find_element(*HomePage.DEPART_FROM_FIELD).send_keys(train_from)
        self.browser.find_element(*HomePage.ARRIVE_TO_FIELD).send_keys(train_to)
        self.browser.find_element(*HomePage.SUBMIT_BUTTON).click()

    def check_searched_train_data(self, train_from, train_to, selected_class,
                                  pasenger_quantity, calendar_from_date, calendar_to_date):

        assert train_from == self.browser.find_element(*HomePage.DEPART_FROM_FIELD).get_attribute("value")
        assert calendar_from_date == self.browser.find_element(*HomePage.CALENDAR_DEPART_FIELD).get_attribute("value")
        assert train_to == self.browser.find_element(*HomePage.ARRIVE_TO_FIELD).get_attribute("value")
        assert calendar_to_date == self.browser.find_element(*HomePage.CALENDAR_ARRIVAL_FIELD).get_attribute("value")
        assert selected_class == self.browser.find_element(*HomePage.CONFORT_1ST_LABEL).text
        assert pasenger_quantity == self.browser.find_element(*HomePage.PASSENGERS).text

    def __select_calendar_date(self, calendar_table, calendar_date):
        for date_element in calendar_table:
            date = date_element.text
            if date == calendar_date.split()[0]:
                date_element.click()
                break
