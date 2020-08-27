from sign_page import Sign_Page
from main_page import Main_Page
from drivers import driver
import json
import time
#---------------------------------------------
with open("log_in.json", "r") as read_file:
    data = json.load(read_file)
#---------------------------------------------
# data navigation user menu
number_step_profile = 1                               # integers menu is --> 1 or 3 or 4 or 5 
number_step_logout = 5
# data user
new_name = "Maxmax"                              # new name for change data field |Your_name| in Profile information 
country = "Ukraine"
number = 975555555
#--------------------------------------------- 
# Log in
page = Sign_Page()
page.open_page(driver, data['URL_sign']) 
#--------------------------------------------- 
page.open_form(driver)
time.sleep(1)
page.log_in(driver, data['login'], data['password']) 
#---------------------------------------------   
page2 = Main_Page()
time.sleep(1)
page2.open_step_setting(driver, number_step_profile)
take_old_name = page2.take_data_Your_name(driver)
print("Take old name in Profile information: (%s)" %(take_old_name))
time.sleep(1)
page2.change_new_user_info(driver, new_name, country, number)
page2.logout_user(driver, number_step_logout)
#--------------------------------------------- 
# Log in againe
page3 = Sign_Page()
page3.open_form(driver)
time.sleep(1)
page.log_in(driver, data['login'], data['password']) 
#--------------------------------------------- 
page4 = Main_Page()
time.sleep(1)
page4.open_step_setting(driver, number_step_profile)
#--------------------------------------------- 
page4.take_user_phone(driver)
page4.take_user_country(driver)
page4.check_all_info_after_update(driver, new_name, number, country)
page2.close_page(driver)
