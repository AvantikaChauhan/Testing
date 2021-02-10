from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(executable_path = GeckoDriverManager().install());
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(" ")
driver.find_element_by_id("").click()
driver.find_element_by_id("").send_keys(" ")
driver.find_element_by_id("").click()
driver.find_element_by_name("").send_keys("Test@123")
driver.find_element_by_id("").click()
self.driver.find_elements_by_id("").click()
time.sleep(10)

driver.close()
driver.quit()
print("ThankGod Completed")
