from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_utils.template import SeleniumTemplate

class GoogleSearch(SeleniumTemplate):
    def __init__(self, timeout=30):
        super().__init__(timeout)
        self.base_url = "https://www.google.com"
    
    def perform_search(self, search_term):
        """Perform a Google search using the top search bar"""
        try:
            # Navigate to Google
            self.navigate_to(self.base_url)
            
            # Find and fill the top search box
            search_box = self.wait_for_element(By.NAME, "q")  # Changed to use NAME selector for top search bar
            self.fill_form(search_box, search_term)
            search_box.send_keys(Keys.RETURN)
            
            # Wait for search results
            self.wait_for_element(By.ID, "search")
            
            return True
            
        except Exception as e:
            print(f"Search failed: {e}")
            return False
        
