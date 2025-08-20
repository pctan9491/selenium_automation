# Import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create webdriver object with proper options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # Maximize window to ensure elements are visible
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Get geeksforgeeks.org
    driver.get("https://www.geeksforgeeks.org/")
    
    # Wait for page to load completely
    wait = WebDriverWait(driver, 10)
    
    # Wait for the "Courses" element to be present and visible
    element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Courses")))
    
    # Scroll the element into view to ensure it's visible
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    
    # Wait a moment for scroll to complete
    time.sleep(1)
    
    # Create action chain object
    action = ActionChains(driver)
    
    # Move to element first, then click
    action.click_and_hold(on_element = element).perform()

    
    print("Successfully clicked on Courses link!")
    
    # Wait a bit to see the result
    time.sleep(3)
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the driver
    driver.quit()