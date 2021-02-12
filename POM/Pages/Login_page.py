class Login_page():
    def __init__(self, driver):
        self.driver = driver
        self.user_id = ""
        self.password_id = ""
        self.submit_id   = ""
    def UserName(self, Uname):
        self.driver.find_element_by_id(self.user_id).clear()
        self.driver.find_element_by_id(self.user_id).send_keys(Uname)
    def Password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)
    def ClickLogin(self):
        self.driver.find_element_by_id(self.submit_id).click()
