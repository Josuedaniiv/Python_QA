import unittest
from selenium import webdriver
from pages.login_page import LoginPage

class LoginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.login_page.login("admin", "admin123")
        self.assertEqual(self.driver.current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard")

    def test_failed_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.login_page.login("invalid_username", "invalid_password")
        self.assertEqual(self.login_page.get_error_message(), "Invalid credentials")

if __name__ == "__main__":
    unittest.main()