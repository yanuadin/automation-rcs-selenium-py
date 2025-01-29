from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from controller.baseController import BaseController

class LoginController(BaseController):
    def login(self, userId, password):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="userId"]').send_keys(userId)
        pw = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)