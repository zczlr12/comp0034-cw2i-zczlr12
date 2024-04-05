import requests
from dash.testing.application_runners import import_app
from selenium.webdriver.common.by import By
import time


def test_server_live(dash_duo):
    """
    GIVEN the app is running
    WHEN a HTTP request to the home page is made
    THEN the HTTP response status code should be 200
    """

    # Start the app in a server
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Get the url for the web app root
    # You can print this to see what it is e.g. print(f'The server url is {url}')
    url = dash_duo.driver.current_url

    # Requests is a python library and here is used to make a HTTP request to the sever url
    response = requests.get(url)

    # Finally, use the pytest assertion to check that the status code in the HTTP response is 200
    assert response.status_code == 200


# For Current Trends page
def test_nav_link_current_trends(dash_duo):
    """
    Check the nav link for Current Trends works.
    """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#current-trends-page.nav-link", timeout=4)

    # Click on the Current Trends page
    dash_duo.driver.find_element(By.ID, "current-trends-page").click()

    # Wait for the tab to be active
    dash_duo.wait_for_element("#current-trends-page.nav-link.active", timeout=4)

    # Check the page url includes current_trends
    assert "current_trends" in dash_duo.driver.current_url


def test_current_trends_page(dash_duo):
    """
    Check whether Current Trends page can be accessed.
    """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#current-trends-page.nav-link", timeout=4)

    # Click on the Current Trends page
    dash_duo.driver.find_element(By.ID, "current-trends-page").click()

    # Wait for the tab to be active
    dash_duo.wait_for_element("#current-trends-page.nav-link.active", timeout=4)

    # Check the page H1 include the words "Current Trends"
    dash_duo.wait_for_element("H1", timeout=4)
    h1_text = dash_duo.driver.find_element(By.TAG_NAME, "H1").text
    assert h1_text == "Current Trends"


def test_current_trends_without_input(dash_duo):
    """
    Check the message displayed when no input is provided.
    """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#current-trends-page.nav-link", timeout=4)

    # Click on the Current Trends page
    dash_duo.driver.find_element(By.ID, "current-trends-page").click()

    # Wait for the error message to be displayed
    dash_duo.wait_for_element("#current-trend-error-message", timeout=4)
    time.sleep(2)

    # Check the message is displayed
    message = dash_duo.driver.find_element(By.ID, "current-trend-error-message").text
    assert message == "Please enter a brand number and an item number."


def test_current_trends_invalid_input(dash_duo):
    """
    Check the message displayed when invalid input is provided.
    """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#current-trends-page.nav-link", timeout=4)

    # Click on the Current Trends page
    dash_duo.driver.find_element(By.ID, "current-trends-page").click()

    # Enter an invalid input
    dash_duo.driver.find_element(By.ID, "current-trend-brand-input").send_keys("11")
    dash_duo.driver.find_element(By.ID, "current-trend-item-input").send_keys("100")

    # Wait for the message to be updated
    time.sleep(2)

    # Check the message is displayed
    message = dash_duo.driver.find_element(By.ID, "current-trend-error-message").text
    assert message == "Invalid value for brand number or item number."


def test_current_trends_valid_input(dash_duo):
    """
    Check the line chart displayed when valid input is provided.
    """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#current-trends-page.nav-link", timeout=4)

    # Click on the Current Trends page
    dash_duo.driver.find_element(By.ID, "current-trends-page").click()

    # Enter an invalid input
    dash_duo.driver.find_element(By.ID, "current-trend-brand-input").send_keys("1")
    dash_duo.driver.find_element(By.ID, "current-trend-item-input").send_keys("4")

    # Wait for the chart to be displayed
    time.sleep(3)

    # Check the chart title
    title = dash_duo.driver.find_element(By.CLASS_NAME, "gtitle").text
    assert title == "Current trend of sales for brand 1 item 4"


# For Future Trends page
def test_nav_link_future_trends(dash_duo):
    """
    Check the nav link for Future Trends works.
    """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#future-trends-page.nav-link", timeout=4)

    # Click on the Future Trends page
    dash_duo.driver.find_element(By.ID, "future-trends-page").click()

    # Wait for the tab to be active
    dash_duo.wait_for_element("#future-trends-page.nav-link.active", timeout=4)

    # Check the page url includes future_trends
    assert "future_trends" in dash_duo.driver.current_url


def test_future_trends_pages(dash_duo):
    """
    Check the nav link for Future Trends works.
    """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#future-trends-page.nav-link", timeout=4)

    # Click on the Future Trends page
    dash_duo.driver.find_element(By.ID, "future-trends-page").click()

    # Wait for the tab to be active
    dash_duo.wait_for_element("#future-trends-page.nav-link.active", timeout=4)

    # Check the page H1 include the title "Future Trends"
    dash_duo.wait_for_element("H1", timeout=4)
    h1_text = dash_duo.driver.find_element(By.TAG_NAME, "H1").text
    assert h1_text == "Future Trends"


def test_future_trends_without_input(dash_duo):
    """ Check the message displayed when no input is provided. """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#future-trends-page.nav-link", timeout=4)

    # Click on the Future Trends page
    dash_duo.driver.find_element(By.ID, "future-trends-page").click()

    # Wait for the error message to be displayed
    dash_duo.wait_for_element("#future-trend-error-message", timeout=4)
    time.sleep(2)

    # Check the message is displayed
    message = dash_duo.driver.find_element(By.ID, "future-trend-error-message").text
    assert message == "Please enter a brand number and an item number."


def test_future_trends_invalid_input(dash_duo):
    """ Check the message displayed when invalid input is provided. """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#future-trends-page.nav-link", timeout=4)

    # Click on the Future Trends page
    dash_duo.driver.find_element(By.ID, "future-trends-page").click()

    # Enter an invalid input
    dash_duo.driver.find_element(By.ID, "future-trend-brand-input").send_keys("5")
    dash_duo.driver.find_element(By.ID, "future-trend-item-input").send_keys("6")

    # Wait for the message to be updated
    time.sleep(2)

    # Check the message is displayed
    message = dash_duo.driver.find_element(By.ID, "future-trend-error-message").text
    assert message == "Invalid value for brand number or item number."


def test_future_trends_valid_input(dash_duo):
    """ Check the line chart displayed when valid input is provided. """
    app = import_app(app_file="pasta_sales.app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#future-trends-page.nav-link", timeout=4)

    # Click on the Future Trends page
    dash_duo.driver.find_element(By.ID, "future-trends-page").click()

    # Enter an invalid input
    dash_duo.driver.find_element(By.ID, "future-trend-brand-input").send_keys("1")
    dash_duo.driver.find_element(By.ID, "future-trend-item-input").send_keys("1")

    # Wait for the chart to be displayed
    time.sleep(10)

    # Check the chart title
    title = dash_duo.driver.find_element(By.CLASS_NAME, "gtitle").text
    assert title == "Trend predictions of sales for brand 1 item 1"