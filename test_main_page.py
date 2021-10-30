from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # initialize the Page Object, pass the driver instance and url to the constructor
    page.open()  # open page
    page.go_to_login_page()  # execute the page method — go to the login page
