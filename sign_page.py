#from drivers import driver
from core_page import Core_Page
from selenium.webdriver.common.keys import Keys

# class Sign page.
class Sign_Page(Core_Page):

    # open sign_in form.
    def open_form(self, driver):
        driver.find_element_by_css_selector('.btn.signin').click()

    # input login in field
    def input_login(self, driver, login): 
        driver.find_element_by_id('signin-login').send_keys(login)

    # input password in field
    def input_password(self, driver, password): 
        driver.find_element_by_css_selector('.main .sign-form [type=password]:nth-child(2)').send_keys(password)

    # press button the form
    def press_button(self, driver):   
        driver.find_element_by_css_selector('.sign__submit:nth-child(1)').click()

    # open sign_in form, input login and pswd, and press button the form
    def log_in(self, driver, login, password): 
        self.open_form(driver)
        self.input_login(driver, login)
        self.input_password(driver, password)
        self.press_button(driver)
