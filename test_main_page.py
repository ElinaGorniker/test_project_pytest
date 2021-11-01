from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)  # initialize the Page Object, pass the driver instance and url to the constructor
    page.open()  # open page
    page.go_to_login_page()  # execute the page method — go to the login page
    login_page = LoginPage(browser, browser.current_url)  # initialize the Login Page Object
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
