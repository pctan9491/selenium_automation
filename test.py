from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import unittest

class BrowserStackTutorials(unittest.TestCase):
    def test_soft_assert(self):
        # Set up Chrome options
        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Initialize Chrome driver with options
        driver = webdriver.Chrome(options=options)
        
        # Navigate to website
        driver.get("https://www.browserstack.com/")
        
        # Get actual title
        actual_title = driver.title
        expected_title = "Most Reliable App & Cross Browser Testing Platform | BrowserStack"
        
        try:
            # Perform soft assertions
            self.assertEqual(actual_title, expected_title, "Title does not match")
            self.assertNotEqual(actual_title, "Incorrect Title", "Title matches an incorrect value")
            self.assertIsNotNone(actual_title, "Page title should not be null")
            self.assertTrue(actual_title.lower() == expected_title.lower(), 
                          "Title does not match in case-insensitive comparison")
            
        finally:
            driver.quit()

if __name__ == '__main__':
    unittest.main()
