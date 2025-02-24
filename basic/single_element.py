import os
import sys
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_utils.template import SeleniumTemplate
import time

class SingleElement(SeleniumTemplate):
    def __init__(self, timeout=30):
        super().__init__(timeout)
        self.base_url = "https://www.geeksforgeeks.org/"

    def perform_search(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Then navigate and perform actions
            self.navigate_to(self.base_url)
            
            # Find search box by XPATH
            search_box = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
            
            # Test Partial Link Text
            print("Testing Partial Link Text selector...")
            button_txt = self.wait_for_clickable(By.PARTIAL_LINK_TEXT, "Full Stack Live")
            button_txt.click()
            time.sleep(3)
            
            # Store the main window handle
            main_window = self.driver.current_window_handle
            
            # Handle multiple windows
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                if "Full Stack Development with React & Node JS - Live" in self.driver.title:
                    time.sleep(2)
                    self.driver.close()
                    break
            
            # Switch back to the main window
            self.driver.switch_to.window(main_window)
            
            # Test XPATH selector
            print("Testing XPATH selector...")
            search_box = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
            search_box.send_keys('detect by XPATH')
            time.sleep(3)
            search_box.clear()
            time.sleep(2)
            
            # Test CSS selector
            print("Testing CSS selector...")
            search_box = self.wait_for_element(By.CSS_SELECTOR, "#comp > div.index_homePageContainer__H8GJD > div.HomePageSearchContainer_homePageSearchContainer__bNc8c > div.HomePageSearchContainer_homePageSearchContainer_container__vWZMD > input")
            search_box.send_keys('detect by CSS')
            time.sleep(3)
            search_box.clear()
            time.sleep(2)
            
            # Test Class Name selector
            print("Testing Class Name selector...")
            search_box = self.wait_for_element(By.CLASS_NAME, "gs-input")
            search_box.send_keys('detect by Class')
            time.sleep(3)
            search_box.clear()
            time.sleep(2)
            return True
            
        except Exception as e:
            print(f"Error performing search: {e}")
            return False
        
        finally:
            if self.driver:  # Only cleanup if driver exists
                self.cleanup()




