"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    # URL
    URL = 'https://www.duckduckgo.com'

    # Locators
    SEARCH_INPUT = (By.ID, 'searchbox_input')    # Adding search input locator.

    # Initialiser
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        # TODO
        pass

    def search(self):
        # TODO 
        pass