import os
import sys
import unittest
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_utils.template import SeleniumTemplate
import time

class WritingTest(SeleniumTemplate, unittest.TestCase):
    def __init__(self, timeout=30):
        super().__init__(timeout)
        self.base_url = "https://www.geeksforgeeks.org/"

    def print_elements_text(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Then navigate and perform actions
            self.navigate_to(self.base_url)
            
            

            # # Test Partial Link Text
            # print("Testing Partial Link Text selector...")
            # button_txt = self.wait_for_clickable(By.PARTIAL_LINK_TEXT, "Full Stack Live")
            # button_txt.click()
            # time.sleep(3)
            
            # # Store the main window handle
            # main_window = self.driver.current_window_handle
            
            # # Handle multiple windows
            # for handle in self.driver.window_handles:
            #     self.driver.switch_to.window(handle)
            #     if "Full Stack Development with React & Node JS - Live" in self.driver.title:
            #         time.sleep(2)
            #         self.driver.close()
            #         break
            
            # # Switch back to the main window
            # self.driver.switch_to.window(main_window)
            
            # Test XPATH selector
            print("Testing XPATH selector...")
            option_btn = self.wait_for_elements(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[3]/a[1]')
            # Get and print the text content of all buttons
            button_texts = [btn.text for btn in option_btn]
            print(f"Button texts: {button_texts}")
            time.sleep(3)

            # Test LINK_TEXT selector
            print("Testing LINK_TEXT...")
            option_btn = self.wait_for_elements(By.LINK_TEXT, 'Master DS & ML')
            # Get and print the text content of all buttons
            button_texts = [btn.text for btn in option_btn]
            print(f"Button texts: {button_texts}")
            time.sleep(3)

            # Test PARTIAL_LINK_TEXT selector
            print("Testing PARTIAL_LINK_TEXT...")
            option_btn = self.wait_for_elements(By.PARTIAL_LINK_TEXT, 'Master D')
            # Get and print the text content of all buttons
            button_texts = [btn.text for btn in option_btn]
            print(f"Button texts: {button_texts}")
            time.sleep(3)

            # Test TAG_NAME selector
            print("Testing TAG_NAME...")
            option_btn = self.wait_for_elements(By.TAG_NAME, 'a')
            # Get and print the text content of all buttons
            button_texts = [btn.text for btn in option_btn]
            print(f"Button texts: {button_texts}")
            time.sleep(3)

            # Test CLASS_NAME selector
            print("Testing CLASS_NAME...")
            option_btn = self.wait_for_elements(By.CLASS_NAME, 'SearchChip_searchChip__oKfVN')
            # Get and print the text content of all buttons
            button_texts = [btn.text for btn in option_btn]
            print(f"Button texts: {button_texts}")
            time.sleep(3)

            # Test CSS_SELECTOR selector
            print("Testing CSS_SELECTOR...")
            option_btn = self.wait_for_elements(By.CSS_SELECTOR, '#comp > div.index_homePageContainer__H8GJD > div.HomePageSearchContainer_homePageSearchContainer__bNc8c > div.SearchContainerChips_searchContainerChips__PnpvD > a:nth-child(1)')
            # Get and print the text content of all buttons
            button_texts = [btn.text for btn in option_btn]
            print(f"Button texts: {button_texts}")
            time.sleep(3)
            
            # return True
            
        except Exception as e:
            print(f"Error performing search: {e}")
            # return False
        
        finally:
            if self.driver:  # Only cleanup if driver exists
                self.cleanup()

    def tearDown(self):
        if self.driver:  # Only cleanup if driver exists
            self.cleanup()