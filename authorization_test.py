from sign_page import Sign_Page
from main_page import Main_Page
from drivers import driver
import json
import time
#---------------------------------------------
with open("log_in.json", "r") as read_file:
    data = json.load(read_file)
number_step = 1 # integers menu is --> 1 or 3 or 4 or 5    
#--------------------------------------------- 
page = Sign_Page()
page.open_page(driver, data['URL_sign']) 
#--------------------------------------------- 
page.open_form(driver)
time.sleep(1)
page.log_in(driver, data['login'], data['password']) 
#---------------------------------------------   
page2 = Main_Page()
time.sleep(1)
page2.open_step_setting(driver, number_step)
page2.check_email_after_login(driver, data['login'])
page2.close_page(driver)
