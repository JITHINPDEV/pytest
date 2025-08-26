from Pages.locators import GoogleLocators

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.google.com")

    def search(self, text):
        self.driver.find_element(*GoogleLocators.SEARCH_BOX).send_keys(text)
        self.driver.find_element(*GoogleLocators.SEARCH_BOX).submit()
