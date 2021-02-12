class Home_page():
    def __init__(self, driver):
        self.driver = driver
        self.signout_id = "logout"
    def SignOut(self):
        self.driver.find_elements_by_id(self.signout_id).click()
