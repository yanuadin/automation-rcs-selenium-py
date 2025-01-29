from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

class BaseController:
    def __init__(self, driver):
        self.driver = driver

    def switchWindow(self, index, frameName = None): 
        self.driver.switch_to.window(self.driver.window_handles[index])
        if frameName is not None :
            self.switchFrame(frameName)
    
    def switchFrame(self, frameName): 
        self.driver.switch_to.default_content() #exit current frame
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, 'frame[name="'+ frameName +'"]'))

    def fillField(self, field):
        try:
            match field['type']:
                case 'inputText':
                    return self.handleInputText(field)
                case 'select':
                    return self.handleSelect(field)
                case 'radio':
                    return self.handleRadio(field)
                case 'buttonPopUpWindow':
                    return self.handleButtonPopUpWindow(field)
                case 'hiddenInputText':
                    return self.handleHiddenInputText(field)
                case 'button':
                    return self.handleButton(field)
                case 'buttonConfirmation':
                    return self.handleButtonConfirmation(field)
                case 'buttonPopUpWindowRadio':
                    return self.buttonPopUpWindowRadio(field)
                case default:
                    print(field['type'] + " - Field Type Not Found")
                    self.driver.quit()
                    exit()
        except Exception as e:
            if 'skipException' not in field:
                print(str(e))
                self.driver.quit()
                exit()

    def handleInputText(self, field): 
        element = self.driver.find_element(field['selector'], field['key'])
        element.send_keys(Keys.HOME);
        element.send_keys(Keys.DELETE);
        element.send_keys(field['value'])

    def handleSelect(self, field):
        select = self.driver.find_element(field['selector'], field['key'])
        Select(select).select_by_value(field['value'])
    
    def handleRadio(self, field):
        tempKey = field['key']
        field['key'] = 'input[type="radio"][value="'+ field['value'] +'"]'
        if field['selector'] == By.NAME:
            field['key'] += '[name="'+ tempKey +'"]'
        
        field['selector'] = By.CSS_SELECTOR
        self.handleButton(field)
    
    def handleButtonPopUpWindow(self, field):
        self.handleButton(field)
        time.sleep(1)
        self.switchWindow(2)
        self.handleRadio({
            'selector': By.NAME,
            'key': 'searchCriteria',
            'value': 'code'
        })
        self.handleInputText({
            'selector': By.NAME,
            'key': 'searchValue',
            'value': field['value']
        })
        self.handleButton({
            'selector': By.NAME,
            'key': 'Go'
        })
        self.handleButton({
            'selector': By.XPATH,
            'key': '//a[normalize-space()="'+ field['value'] +'"]'
        })
        self.switchWindow(1, 'main')

    def handleHiddenInputText(self, field):
        element = self.driver.find_element(field['selector'], field['key'])
        self.driver.execute_script("arguments[0].value='"+ field['value'] +"';", element)

    def handleButton(self, field):
        self.driver.find_element(field['selector'], field['key']).click()
        self.driver.implicitly_wait(3)
    
    def handleButtonConfirmation(self, field):
        self.handleButton(field)
        self.driver.implicitly_wait(3)
        if field['value'] == 'Y':
            self.driver.switch_to.alert.accept()
        else:
            self.driver.switch_to.alert.dismiss()
    
    def buttonPopUpWindowRadio(self, field):
        self.handleButton(field)
        time.sleep(1)
        self.switchWindow(2)
        self.handleRadio({
            'selector': By.CSS_SELECTOR,
            'key': field['value'],
            'value': field['value']
        })
        self.handleButton({
            'selector': By.NAME,
            'key': 'Submit'
        })
        self.switchWindow(1, 'main')
