
# main class
class Core_Page(object):

    # open URL
    def open_page(self, driver, url):
        driver.get(url) 
         
    # close browser
    def close_page(self, driver):
        driver.close()   
