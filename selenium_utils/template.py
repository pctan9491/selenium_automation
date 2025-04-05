from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

class SeleniumTemplate:
    def __init__(self, timeout=30, browser_type="chrome"):
        """Initialize the Selenium template with configurable timeout and browser type"""
        self.timeout = timeout
        self.browser_type = browser_type.lower()
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

        # Common options
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
            
        return self.driver
    
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
        
    
