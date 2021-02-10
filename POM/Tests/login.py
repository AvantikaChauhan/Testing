from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
import unittest
from POM.Pages.Login_page import Login_page
from POM.Pages.HomePage import Home_page
    class LoginTest(unittest.TestCase):
        @classmethod
        def setUpClass(cls) :
            cls.driver = webdriver.Firefox(executable_path = GeckoDriverManager().install());
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
        def test_login_valid(self):
            driver = self.driver
            driver.get(" ")

            login = Login_page(driver)
            login.UserName("")
            login.Password("")
            login.ClickLogin()

            home = Home_page(driver)
            home.SignOut()

         
            time.sleep(10)
        @classmethod
        def tearDownClass(cls) :
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

if __name__ == "__main__":
    unittest.main()


