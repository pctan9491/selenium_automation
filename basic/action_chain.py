import time
import unittest
import sys
import os
import pyperclip


# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium_utils.template import SeleniumTemplate
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class ActionChainTest(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):
        SeleniumTemplate.__init__(self, timeout=30) 
        unittest.TestCase.__init__(self, methodName)
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_action_chain(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Navigate to URL
            print(f"\nNavigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("Page loaded successfully.")

             # Updated method call
            self.action_reset_action()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                print("Browser closed.")
    
    #---------------------------------------------------------------------------
    #test action chain: clicked
    def action_chain_clicked(self):
        # Click method
        click_element = self.wait_for_clickable(By.XPATH, '//*[@id="topMainHeader"]/div/ul/li[1]/span/div')
        
        #Action Chain step 1
        action = ActionChains(self.driver)

        #Action Chain step 2 and 3 (perform)
        action.click(click_element).perform()
        print("Successfully perform action chain for click!")
        # Wait a bit to see the result
        time.sleep(3)
    
    #test action chain: click and hold
    def action_chain_click_and_hold_and_release(self):
        # Click method
        click_and_hold_element = self.wait_for_clickable(By.XPATH, '//*[@id="topMainHeader"]/div/a/div/img')
        target = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')

        #Action Chain step 1
        action = ActionChains(self.driver)

        #Action Chain step 2
        action.click_and_hold(on_element=click_and_hold_element)
        action.move_to_element(target)
        #Release action: Releasing a held mouse button on an element.
        action.release(target)
        #Action Chain step 3 (perform)
        action.perform()
        target.send_keys(Keys.RETURN)

        print("Successfully perform action chain for click and hold, release!")
        # Wait a bit to see the result
        time.sleep(3)

        #test action chain: click and hold
    
    def action_chain_context_click(self):
        # Context click method
        # imagine i want copy a text
        pyperclip.copy("text copy")
        target = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')

        action = ActionChains(self.driver)
        action.context_click(on_element=target)
        action.perform()

        print("Successfully perform action chain for context click!")
        # Wait a bit to see the result
        time.sleep(3)
    
    def action_chain_drag_and_drop(self):
        # Click method
        click_and_hold_element = self.wait_for_clickable(By.XPATH, '//*[@id="topMainHeader"]/div/a/div/img')
        target = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')

        #Action Chain step 1
        action = ActionChains(self.driver)

        #Action Chain step 2
        action.drag_and_drop(on_element=click_and_hold_element, target_element=target)

        #Action Chain step 3 (perform)
        action.perform()
        target.send_keys(Keys.RETURN)

        print("Successfully perform action chain for drag and drop!")
        # Wait a bit to see the result
        time.sleep(3)
    
    def action_chain_double_click(self):
        target = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        target.send_keys('Testing_for_double_click')

        #Action Chain step 1
        action = ActionChains(self.driver)

        #Action Chain step 2
        action.double_click(on_element=target)

        #Action Chain step 3 (perform)
        action.perform()
        print("Successfully perform action chain for double click!")
        # Wait a bit to see the result
        time.sleep(3)

    def action_chain_key_down_key_up(self):
        target = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        target.send_keys('Testing_for_key_down_key_up')
        time.sleep(3)

        #Action Chain step 1
        action = ActionChains(self.driver)

        #Action Chain step 2
        action.key_down(Keys.CONTROL, target).send_keys('A').key_up(Keys.CONTROL, target)
        action.key_down(Keys.CONTROL, target).send_keys('X').key_up(Keys.CONTROL, target)

        #Action Chain step 3 (perform)
        action.perform()
        print("Successfully perform action chain for key down and key up!")
        # Wait a bit to see the result
        time.sleep(3)

    def action_chain_move_by_offset(self):

        target = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')

        # Get initial element position as reference point
        initial_element_location = target.location
        print(f"Target element location: x={initial_element_location['x']}, y={initial_element_location['y']}")
        
        # Create a tracking element to monitor cursor position
        tracking_script = """
        // Create a hidden div to track mouse position
        if (!window.mouseTracker) {
            window.mouseTracker = {x: 0, y: 0};
            document.addEventListener('mousemove', function(e) {
                window.mouseTracker.x = e.clientX;
                window.mouseTracker.y = e.clientY;
            });
        }
        return {x: window.mouseTracker.x, y: window.mouseTracker.y};
        """
        
        # Initialize mouse tracking
        self.driver.execute_script(tracking_script)
        time.sleep(0.1)  # Brief pause to initialize
        
        # Get initial cursor position
        initial_position = self.driver.execute_script("return {x: window.mouseTracker.x, y: window.mouseTracker.y};")
        print(f"Initial cursor position: x={initial_position['x']}, y={initial_position['y']}")
    
        #Action Chain step 1
        action = ActionChains(self.driver)
    
        #Action Chain step 2: move the cursor
        print("Moving cursor by offset (100, 100)...")
        action.move_by_offset(100, 100)
        window_position = self.driver.get_window_position()
        window_size = self.driver.get_window_size()
        print(f"Window position: x={window_position['x']}, y={window_position['y']}")
        print(f"Window size: width={window_size['width']}, height={window_size['height']}")
        action.click()
        
        #Action Chain step 3 (perform)
        action.perform()
        
        # Check cursor position after first move
        time.sleep(0.5)  # Allow time for movement and event to register
        position_after_first_move = self.driver.execute_script("return {x: window.mouseTracker.x, y: window.mouseTracker.y};")
        print(f"Cursor position after first move: x={position_after_first_move['x']}, y={position_after_first_move['y']}")
        
        # Calculate movement distance
        x_movement = position_after_first_move['x'] - initial_position['x']
        y_movement = position_after_first_move['y'] - initial_position['y']
        total_movement = (x_movement**2 + y_movement**2)**0.5
        
        print(f"Movement detected: x_offset={x_movement}, y_offset={y_movement}, total_distance={total_movement:.2f}px")
        
        # Detect if cursor moved (allowing for small tolerance)
        if total_movement > 5:  # 5px tolerance for minor variations
            print("✓ CURSOR MOVEMENT DETECTED: First move_by_offset was successful!")
            print(f"  Expected: (100, 100), Actual: ({x_movement}, {y_movement})")
        else:
            print("✗ NO SIGNIFICANT CURSOR MOVEMENT: First move_by_offset may have failed")
        
        target.send_keys('Testing_move_by_offset_after_5s')
        time.sleep(2)
    
        print("\nSuccessfully performed action chain for move by offset with cursor detection!")
        # Wait a bit to see the result
        time.sleep(3)

    def action_chain_move_to_element(self):
        target = self.wait_for_element(By.XPATH, '//*[@id="topMainHeader"]/div/ul/li[1]/span')
        time.sleep(2)
        
        print("Using ActionChains to hover, then JavaScript to click...")
        
        # Hover with ActionChains
        action = ActionChains(self.driver)
        action.move_to_element(target).perform()
        
        # Try to find dropdown item and click with JavaScript
        try:
            time.sleep(5)
            target_insider = self.wait_for_element(By.XPATH, '//*[@id="secondarySubHeader"]/ul/li[12]/a')
            self.driver.execute_script("arguments[0].click();", target_insider)
            print("Successfully clicked with JavaScript!")
        except TimeoutException:
            print("Dropdown not found, clicking main element")
            self.driver.execute_script("arguments[0].click();", target)
        
        time.sleep(3)
        current_url = self.driver.current_url
        print(f"Current URL after click: {current_url}")

        # Check if URL changed or new window opened
        if len(self.driver.window_handles) > 1:
            print("New window/tab opened!")
            new_window_url = self.driver.window_handles[-1]
            self.driver.switch_to.window(new_window_url)
            print(f"New tab URL: {self.driver.current_url}")
            print("Successfully perform action chain for move_to_element!")

    def action_chain_pause(self):
        target = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        target.send_keys('Testing_for_pause')
        time.sleep(3)

        #Action Chain step 1
        action = ActionChains(self.driver)

        #Action Chain step 2
        action.pause(1)
        action.double_click(target)
        action.send_keys('Testing_for_pause_1s')
        action.pause(3)
        action.double_click(target)
        action.send_keys('Testing_for_pause_3s')
        action.pause(5)
        action.double_click(target)
        action.send_keys('Testing_for_pause_5s')

        #Action Chain step 3 (perform)
        action.perform()
        print("Successfully perform action chain for pause!")
        # Wait a bit to see the result
        time.sleep(3)

    def action_reset_action(self):
        target = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        target.send_keys('Testing_for_reset_action')
        time.sleep(3)

        #Action Chain step 1
        action = ActionChains(self.driver)

        #Action Chain step 2
        action.pause(1)
        action.double_click(target)
        action.send_keys('reset_action_now')
        action.pause(3)
        action.perform()
        action.reset_actions()
        action.double_click(target)
        action.send_keys('Reset Action completed')
        action.pause(3)

        #Action Chain step 3 (perform)
        action.perform()
        print("Successfully perform action chain for reset action!")
        # Wait a bit to see the result
        time.sleep(3)


