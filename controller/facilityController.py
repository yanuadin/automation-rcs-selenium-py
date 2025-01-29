from selenium.webdriver.common.by import By
from controller.baseController import BaseController
from const.baseConst import *
import time 

class FacilityController(BaseController):
    def create(self, facilityData):
        self.switchWindow(1, 'main')
        self.switchInnerFrame()
        self.handleButton({
            'selector': By.ID,
            'key': 'tab_dcms_70003'
        })
        for field in facilityData:
            self.driver.implicitly_wait(5)
            self.fillField(field)
            if 'timeSleep' in field:
                time.sleep(field['timeSleep'])
            if field['type'] == buttonPopUpWindow or field['type'] == buttonPopUpWindowRadio:
                self.switchInnerFrame()
        
        self.handleButton({
            'selector': By.NAME,
            'key': 'calculate',
        })
        time.sleep(5)
        self.handleButton({
            'selector': By.NAME,
            'key': 'add',
        })
        self.driver.implicitly_wait(5)
    
    def switchInnerFrame(self):
        fs100Frame = self.driver.find_element(By.CSS_SELECTOR, 'frameset[id="fs100"] > frame:nth-child(1)')
        self.driver.switch_to.frame(fs100Frame)
        fs200Frame = self.driver.find_element(By.CSS_SELECTOR, 'frameset[id="fs200"] > frame:nth-child(2)')
        self.driver.switch_to.frame(fs200Frame)
        self.driver.implicitly_wait(5)