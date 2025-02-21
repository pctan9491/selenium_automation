import os
import sys
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from selenium import webdriver
from selenium_utils.template import SeleniumTemplate
from selenium.webdriver.common.by import By

def nav_link():
    nav_bot = SeleniumTemplate()
    try:
        # Setup the driver
        nav_bot.setup_driver(headless=False)
        
        # Navigate to Google
        nav_bot.navigate_to("https://www.google.com/")
        
        # Find and interact with the search box
        search_box = nav_bot.wait_for_element(By.XPATH, '//*[@id="APjFqb"]')
        nav_bot.fill_form(search_box, "geeksforgeeks")
        search_box.submit()
        
        # Wait for results
        nav_bot.wait_for_element(By.ID, "search")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Clean up resources
        nav_bot.cleanup()

if __name__ == "__main__":
    nav_link()
        

