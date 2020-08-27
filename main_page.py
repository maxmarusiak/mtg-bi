from core_page import Core_Page
from selenium.webdriver.common.keys import Keys
import time

# class Page User after Log In
class Main_Page(Core_Page):

    # open Menu
    def open_menu(self, driver):
        driver.find_element_by_css_selector('.header [type=button]').click()

    # open user settings menu
    def open_user_setting(self, driver):
        driver.find_element_by_css_selector('.sidebarMenu__item:nth-child(6)').click()

    # choice user settings № step menu
    def change_step_setting(self, driver, number): 
        driver.find_element_by_css_selector('.sidebarMenu__item .subMenu__item:nth-child(%d)' %(number)).click() 

    # open user settings № step menu
    def open_step_setting(self, driver, number): 
        self.open_menu(driver)
        self.open_user_setting(driver)
        self.change_step_setting(driver, number)
#---------------------------------------------
    # take data from field |Email_address| in Profile information after Log In
    def take_data_Email_address(self, driver):
        result_email = driver.find_element_by_xpath('html/body/div[2]/div[5]/main/div[6]/section/form/div[2]/input').get_attribute('value')
        return result_email

    # take data from field |Your_name| in Profile information after Log In
    def take_data_Your_name(self, driver):
        result_name = driver.find_element_by_xpath('html/body/div[2]/div[5]/main/div[6]/section/form/div[1]/input').get_attribute('value')
        return result_name

    def take_user_phone(self, driver):
        result_phone = driver.find_element_by_xpath('html/body/div[2]/div[5]/main/div[6]/section/form/div[4]/div/input[2]').get_attribute('value')
        if result_phone == '':
            return 0
        else:    
            _result = int(result_phone)
            return _result
         

    def take_user_country(self, driver):
        result_country = driver.find_element_by_xpath('html/body/div[2]/div[5]/main/div[6]/section/form/div[3]/select').get_attribute('value')
        return result_country
                  

    # change data field |Your_name| in Profile information 
    def change_data_Your_name(self, driver, new_name):
        field_elem = driver.find_element_by_xpath('html/body/div[2]/div[5]/main/div[6]/section/form/div[1]/input')
        field_text = driver.find_element_by_xpath('html/body/div[2]/div[5]/main/div[6]/section/form/div[1]/input').get_attribute('value')
        size_s = len(field_text)
        while size_s != 0:
            field_elem.send_keys(Keys.BACKSPACE)
            size_s = size_s - 1
        field_elem.send_keys(new_name)
        print("Entering new usr name: %s" %(new_name))

    # press button form the Profile information
    def press_button_form_profile_information(self, driver):
        driver.find_element_by_xpath('html/body/div[2]/div[5]/main/div[6]/section/form/div[7]/button').click()

    # check if correct e_mail/login users in Profile information, after log in
    def check_email_after_login(self, driver, login_e_mail):
        read_mail = self.take_data_Email_address(driver) 
        if login_e_mail == read_mail:
            result = "User correct in Profile information, after Log In is: (%s)" %(read_mail)
            print(result)
        else:
            result = "User NOT correct in Profile information, after Log In!"   
            print(result)

    # check if correct Your_name users in Profile information, after log in
    def check_name_after_update(self, driver, new_name):
        read_name = self.take_data_Your_name(driver) 
        if new_name == read_name:
            result = "Updated name in Profile information: (%s)" %(read_name)
            print(result)
        else:
            result = "NOT Updated name in Profile information: (%s)" %(read_name)   
            print(result) 
   
    # check if correct phone users in Profile information, after update and log in
    def check_phone_after_update(self, driver, new_phone):
        read_phone = self.take_user_phone(driver) 
        if new_phone == read_phone:
            result = "Updated phone in Profile information: (%d)" %(read_phone)
            print(read_phone)
        else:
            result = "NOT Updated phone in Profile information: (%d)" %(read_phone)  
            print(result)

    # check if correct country users in Profile information, after update and log in
    def check_country_after_update(self, driver, new_country):
        read_country = self.take_user_country(driver) 
        if new_country == read_country:
            result = "Updated country in Profile information: (%s)" %(read_country)
            print(result)
        else:
            result = "NOT Updated country in Profile information: (%s)" %(read_country)  
            print(result)

    # input number phone in Profile information for change info user
    def input_phone(self, driver, phone):
        driver.find_element_by_id('profile-phone').send_keys(phone)
        print("Entering new usr phone: %d" %(phone))

    # choice country in Profile information for change info user
    def choice_country(self, driver, country):  
        driver.find_element_by_id('profile-country').click()
        c = driver.find_element_by_xpath("html/body/div[2]/div[5]/main/div[6]/section/form/div[3]/select/option[.='%s']" %(country))
        c.click()
        print("Entering new usr country: %s" %(country))

    # input new data about user in Profile information
    def change_new_user_info(self, driver, new_name, country, phone):
        self.change_data_Your_name(driver, new_name)
        self.choice_country(driver, country)
        self.input_phone(driver, phone)
        self.press_button_form_profile_information(driver)

    # log out in account
    def logout_user(self, driver, step_menu): 
        self.change_step_setting(driver, step_menu)

    # check user info after update and log in againe
    def check_all_info_after_update(self, driver, new_name, new_phone, new_country):
        self.check_name_after_update(driver, new_name)    
        self.check_phone_after_update(driver, new_phone)    
        self.check_country_after_update(driver, new_country)    
#---------------------------------------------            
