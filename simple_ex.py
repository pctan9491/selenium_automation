# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Added import for Keys

# Create a webdriver object. Here we use Firefox, but you can choose other browsers like Chrome, Edge, etc.
driver = webdriver.Chrome()

# Navigate to the GeeksforGeeks website
driver.get("https://www.geeksforgeeks.org/")

# Maximize the browser window
driver.maximize_window()

# Locate the search icon element using XPath
searchIcon = driver.find_element(By.XPATH, "//span[@class='flexR gs-toggle-icon']")

# Click on the Search Icon to activate the search field
searchIcon.click()

# Locate the input field for search text using XPath
enterText = driver.find_element(By.XPATH, "//input[@class='gs-input']")

# Enter the search query "Data Structure" into the input field
enterText.send_keys("Data Structure")

# Send the RETURN key to submit the search query
enterText.send_keys(Keys.RETURN)
