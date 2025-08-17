import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

class SeleniumTemplate:
    def __init__(self, timeout=30, browser_type="chrome"):
        self.timeout = timeout
        self.browser_type = browser_type
        self.driver = None

    def setup_driver(self, headless=False):
        """Setup and configure WebDriver based on browser type"""
        if self.browser_type == "chrome":
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            options = webdriver.ChromeOptions()
        elif self.browser_type == "edge":
            from selenium.webdriver.edge.service import Service
            from webdriver_manager.microsoft import EdgeChromiumDriverManager
            options = webdriver.EdgeOptions()
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")

        # Simple, working options (like writing_test.py uses)
        options.add_argument('--start-maximized')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-gpu')
        
        if headless:
            options.add_argument('--headless')
        
        # Create driver based on browser type
        if self.browser_type == "chrome":
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        else:  # edge
            self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
        
        # Standard timeouts (like writing_test.py)
        self.driver.set_page_load_timeout(60)
        self.driver.implicitly_wait(30)
            
        return self.driver
    
    def set_implicit_wait(self, seconds=None):
        """Set implicit wait timeout for the driver
        
        Args:
            seconds (int, optional): Number of seconds to wait. If None, uses the default timeout.
                                     Set to 0 to disable implicit wait.
        
        Returns:
            None
        """
        wait_time = seconds if seconds is not None else self.timeout
        if self.driver:
            self.driver.implicitly_wait(wait_time)
            print(f"Implicit wait set to {wait_time} seconds")
        else:
            print("Driver not initialized. Call setup_driver() first.")
    
    def set_explicit_wait(self, condition, locator=None, timeout=None, poll_frequency=0.5):
        """Perform an explicit wait with a custom expected condition
        
        Args:
            condition: The expected condition from selenium.webdriver.support.expected_conditions
                      (e.g., EC.visibility_of_element_located)
            locator (tuple, optional): A tuple of (By.XXX, 'value') if the condition requires a locator
            timeout (int, optional): Custom timeout in seconds. If None, uses the default timeout.
            poll_frequency (float, optional): How often to check for the condition, in seconds
        
        Returns:
            The result of the wait (usually an element or boolean)
        
        Raises:
            TimeoutException: If the condition is not met within the timeout period
        """
        if not self.driver:
            raise WebDriverException("Driver not initialized. Call setup_driver() first.")
            
        wait_time = timeout if timeout is not None else self.timeout
        wait = WebDriverWait(self.driver, wait_time, poll_frequency=poll_frequency)
        
        try:
            # If condition requires a locator (most do)
            if locator:
                result = wait.until(condition(locator))
            else:
                # Some conditions don't need a locator (e.g., alert_is_present)
                result = wait.until(condition)
            return result
        except TimeoutException as e:
            print(f"Timeout waiting for condition: {e}")
            raise
    
    def wait_for_element(self, by, value):
        """Wait for an element to be present and return it"""
        wait = WebDriverWait(self.driver, self.timeout)
        return wait.until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_elements(self, by, value):
        """Wait for an element to be present and return it"""
        wait = WebDriverWait(self.driver, self.timeout)
        return wait.until(
            EC.presence_of_all_elements_located((by, value))
        )
    
    def wait_for_clickable(self, by, value):
        """Wait for an element to be clickable and return it"""
        wait = WebDriverWait(self.driver, self.timeout)
        return wait.until(
            EC.element_to_be_clickable((by, value))
        )
    
    def safe_click(self, element):
        """Safely click an element with error handling"""
        try:
            element.click()
        except WebDriverException:
            self.driver.execute_script("arguments[0].click();", element)
    
    def fill_form(self, element, text):
        """Clear and fill a form field"""
        element.clear()
        element.send_keys(text)
    
    def navigate_to(self, url):
        """Navigate to a URL with error handling"""
        try:
            self.driver.get(url)
        except WebDriverException as e:
            print(f"Navigation failed: {e}")
            raise
    
    def navigate_by_link(self, link_text, partial_match=False):
        """Navigate by clicking a link with exact or partial text match
        
        Args:
            link_text (str): The text of the link to click
            partial_match (bool): If True, uses partial link text matching
        """
        try:
            by_method = By.PARTIAL_LINK_TEXT if partial_match else By.LINK_TEXT
            link = self.wait_for_clickable(by_method, link_text)
            self.safe_click(link)
        except (TimeoutException, WebDriverException) as e:
            print(f"Link navigation failed: {e}")
            raise
    
    def get_text(self, by, value):
        """Get text from an element safely"""
        try:
            element = self.wait_for_element(by, value)
            return element.text
        except TimeoutException:
            print(f"Element not found: {value}")
            return None
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            try:
                # Check if the browser is still open by trying to get the current window handle
                self.driver.current_window_handle
                self.driver.quit()
            except Exception as e:
                print("Browser was already closed")
            finally:
                self.driver = None

    def smart_scroll_to_element(self, by, value, timeout=30):
        """Intelligently scroll to find and center an element
        
        Args:
            by: The locator strategy (e.g., By.ID, By.XPATH)
            value: The locator value
            timeout: Maximum time to wait for element
            
        Returns:
            WebElement: The found element
        """
        
        try:
            # First try to find element without scrolling
            element = self.driver.find_element(by, value)
            # Scroll to center the element in view
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            # Wait a moment for scroll to complete
            time.sleep(1)
            # Check if element is clickable after scroll
            self._ensure_element_clickable(element)
            return element
        except:
            # If not found, scroll down progressively to find it
            max_scrolls = 10
            scroll_height = 500
            
            for i in range(max_scrolls):
                try:
                    element = self.driver.find_element(by, value)
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
                    time.sleep(1)
                    self._ensure_element_clickable(element)
                    return element
                except:
                    self.driver.execute_script(f"window.scrollBy(0, {scroll_height});")
                    time.sleep(2)
            
            # If still not found, use explicit wait
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located((by, value)))
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            time.sleep(1)
            self._ensure_element_clickable(element)
            return element
    
    def _dismiss_overlays(self):
        """Try to dismiss common overlays like cookie banners, popups, etc."""
        overlay_selectors = [
            # Common cookie banner selectors
            "//button[contains(text(), 'Accept')]",
            "//button[contains(text(), 'OK')]", 
            "//button[contains(text(), 'Got it')]",
            "//button[contains(@class, 'cookie')]",
            "//div[contains(@class, 'cookie')]//button",
            "//span[contains(@class, 'cookie-text')]/..//button",
            # Close buttons
            "//button[contains(@aria-label, 'Close')]",
            "//button[contains(@class, 'close')]",
            "//span[contains(@class, 'close')]",
            # Modal dismiss buttons
            "//div[contains(@class, 'modal')]//button[contains(@class, 'close')]",
            "//div[contains(@class, 'popup')]//button"
        ]
        
        for selector in overlay_selectors:
            try:
                overlay_element = self.driver.find_element(By.XPATH, selector)
                if overlay_element.is_displayed():
                    self.driver.execute_script("arguments[0].click();", overlay_element)
                    time.sleep(0.5)
                    break  # Only dismiss one overlay at a time
            except:
                continue
    
    def _ensure_element_clickable(self, element):
        """Ensure element is clickable by checking for overlays"""
        try:
            # Try to click the element to see if it's intercepted
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            time.sleep(0.5)
            
            # Check if element is actually clickable
            wait = WebDriverWait(self.driver, 2)
            wait.until(EC.element_to_be_clickable(element))
        except TimeoutException:
            # If not clickable, try to dismiss overlays again
            self._dismiss_overlays()
            time.sleep(0.5)

    def element_exists(self, by, value):
        """Check if an element exists on the page
        
        Args:
            by: The locator strategy (e.g., By.ID, By.XPATH)
            value: The locator value
        
        Returns:
            bool: True if element exists, False otherwise
        """
        try:
            self.driver.find_element(by, value)
            return True
        except:
            return False

# Example usage:
if __name__ == "__main__":
    bot = SeleniumTemplate()
    try:
        # Setup the driver
        bot.setup_driver()
        
        # Navigate to a website
        bot.navigate_to("https://www.example.com")
        
        # Find and interact with elements
        element = bot.wait_for_element(By.ID, "search")
        bot.fill_form(element, "test search")
        
        # Click elements
        button = bot.wait_for_clickable(By.CLASS_NAME, "submit-button")
        bot.safe_click(button)
        
        # Get text from elements
        result = bot.get_text(By.CLASS_NAME, "result-text")
        print(f"Found text: {result}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Always cleanup
        bot.cleanup()
        
    
