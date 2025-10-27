from selenium.webdriver.common.by import By
import time

class PomPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.search_box_locator = (By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        # Locator for the search button
        self.search_button_locator = (By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/span')
    
    def search_query(self, query):
        self.driver.find_element(*self.search_box_locator).send_keys(query)
        time.sleep(2)
    
    def click_search_button_locator(self):
        self.driver.find_element(*self.search_button_locator).click()
        time.sleep(2)
    
    def search_for(self, query):
        self.search_query(query)
        self.click_search_button_locator()