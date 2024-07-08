"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:
    
    # Locators
    SEARCH_INPUT = (By.ID, 'search_form_input')                    # Adding search input locator.
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.eVNpHGjtxRBq_gLOfGDr')     # Adding result page locator

    # Initialiser
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def title(self):
        return self.browser.title
