class Login_page():
    def __init__(self, driver):
        self.driver = driver
        self.account_id = ""
        self.email_id = ""
        self.continue_id = ""
        self.password_id = ""
        self.submit_id   = ""
    def UserName(self, Uname):
        self.driver.find_element_by_id(self.account_id).click()
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(Uname)
        self.driver.find_element_by_id(self.continue_id).click()
    def Password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)
    def ClickLogin(self):
        self.driver.find_element_by_id(self.submit_id).click()
