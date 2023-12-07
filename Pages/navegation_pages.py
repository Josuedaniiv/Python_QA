from selenium.webdriver.common.by import By

class NavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.link = (By.LINK_TEXT, "Link Text")

    def click_link(self):
        self.driver.find_element(*self.link).click()