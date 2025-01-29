from selenium.webdriver.common.by import By
from controller.baseController import BaseController
from const.baseConst import *
import time 

class CustomerController(BaseController):
    def create(self, customerData):
        self.createCustomerHeader(customerData['header'])
        self.driver.implicitly_wait(5)
        self.createCustomerDetail(customerData['body'])
        time.sleep(3)

    def createCustomerHeader(self, customerData):
        for field in customerData:
            self.fillField(field)

        self.driver.find_element(By.NAME, 'search').click()
        is_enabled_proceed = self.driver.find_element(By.NAME, 'proceed').is_enabled()
        if is_enabled_proceed:
            self.driver.find_element(By.NAME, 'proceed').click()
        else:
            self.driver.find_element(By.XPATH, '/html[1]/body[1]/form[1]/table[3]/tbody[1]/tr[3]/td[2]/a[1]').click()
        time.sleep(3)
    
    def createCustomerDetail(self, customerData):
        for field in customerData:
            self.fillField(field)
        
        self.handleButtonConfirmation({
            'type': buttonConfirmation,
            'selector': By.NAME,
            'key': 'Create',
            'value': 'Y'
        },)