from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

def perform_google_search(search_term, timeout=30):
    try:
        # Initialize the webdriver with options
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')  # Start with maximized window
        driver = webdriver.Chrome(options=options)
        
        # Navigate to Google
        driver.get("https://www.google.com")
        
        # Wait for search box to be present
        wait = WebDriverWait(driver, timeout)
        search_box = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]'))
        )
        
        # Enter the search term
        search_box.clear()  # Clear any existing text
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for search results to load
        wait.until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        
        return driver
        
    except TimeoutException:
        print(f"Timeout waiting for element after {timeout} seconds")
        driver.quit()
        raise
    except WebDriverException as e:
        print(f"WebDriver error occurred: {e}")
        driver.quit()
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        driver.quit()
        raise

if __name__ == "__main__":
    try:
        driver = perform_google_search("Testing")
        # Add your further processing here
        
    finally:
        # Always close the browser
        driver.quit()
        
