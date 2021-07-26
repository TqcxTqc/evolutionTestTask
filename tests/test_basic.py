import pytest
from datetime import date, timedelta
from support.page import HomePage
from support.page import TrainResults
from support.page import OnlineTicketOffice

# CONSTANT FORMATTED DATES
DEPARTURE_DATE = (date.today() + timedelta(days=3)).strftime("%d %B, %Y")
ARRIVAL_DATE = (date.today() + timedelta(days=6)).strftime("%-d %B, %Y")


@pytest.mark.parametrize("train_to_lagos,train_to_porto_campanha,comfort_1st,passengers",
                         [("Lagos", "Porto - Campanha", "Comfort / 1st", "2 Passengers")])
def test_lagos_to_porto_travel(browser, train_to_lagos, train_to_porto_campanha, comfort_1st, passengers):
    # Search trains with special dates with comfort class passenger options
    home_page = HomePage(browser)
    train_result_page = TrainResults(browser)
    online_office_page = OnlineTicketOffice(browser)

    home_page.open_page()
    assert browser.title == "CP - Comboios de Portugal"
    home_page.select_departure_date(DEPARTURE_DATE)
    home_page.select_arrival_date(ARRIVAL_DATE)
    home_page.fill_and_search_departure_and_arrival(train_to_lagos, train_to_porto_campanha)
    home_page.wait_visibility_of_elements()
    train_result_page.buy_tickets()
    home_page.wait_page_title_is_loaded("Online Ticket Office | CP - Comboios de Portugal")
    online_office_page.select_confort_class()
    online_office_page.select_count_of_passengers(2)
    online_office_page.accept_terms_and_click_continue()
    online_office_page.click_cancel_button()
    home_page.wait_page_title_is_loaded("Buy Train Tickets Online | CP - Comboios de Portugal")
    home_page.check_searched_train_data(train_to_lagos, train_to_porto_campanha, comfort_1st, passengers,
                                        DEPARTURE_DATE, ARRIVAL_DATE)
