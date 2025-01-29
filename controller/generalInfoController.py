from selenium.webdriver.common.by import By
from controller.baseController import BaseController
from const.baseConst import *
import time 

class GeneralInfoController(BaseController):
    def create(self, generalInfoData):
        self.switchWindow(1, 'main')
        self.switchInnerFrame()
        self.handleButton({
            'selector': By.ID,
            'key': 'tab_dcms_70001'
        })
        self.handleButton({
            'selector': By.NAME,
            'key': 'Edit'
        })
        self.driver.implicitly_wait(5)
        for field in generalInfoData:
            self.fillField(field)
            if field['type'] == buttonPopUpWindow:
                self.switchInnerFrame()

        try:
            self.handleButton({
                'selector': By.NAME,
                'key': 'Check',
            })
        except Exception as e:
            print("Skipped checking chacha because not found")
        self.driver.implicitly_wait(5)
        self.handleButtonConfirmation({
            'selector': By.NAME,
            'key': 'Update',
            'value': 'Y'
        })
    
    def switchInnerFrame(self):
        fs100Frame = self.driver.find_element(By.CSS_SELECTOR, 'frameset[id="fs100"] > frame:nth-child(1)')
        self.driver.switch_to.frame(fs100Frame)
        fs200Frame = self.driver.find_element(By.CSS_SELECTOR, 'frameset[id="fs200"] > frame:nth-child(2)')
        self.driver.switch_to.frame(fs200Frame)
        