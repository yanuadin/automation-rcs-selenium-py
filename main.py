from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from controller import *
from const import *

import time 

def newTicket(driver, controller, customerController):
    controller.switchWindow(1, 'menu')
    driver.find_element(By.CSS_SELECTOR, '#menu_15').click()
    time.sleep(1)
    controller.switchFrame('main')
    
    # Create Customer
    customerController.create(customerConst.customers)

def prewashTicketList(driver, controller):
    controller.switchWindow(1, 'menu')
    driver.find_element(By.CSS_SELECTOR, '#menu_13').click()
    time.sleep(1)
    controller.switchFrame('main')
    controller.handleSelect({
        'selector': By.NAME,
        'key': 'applicationStatusCode',
        'value': 'CIMB_HL_prewash_new_ticket_creation'
    })
    controller.handleRadio({
        'selector': By.NAME,
        'key': 'ascendingSortingFlag',
        'value': 'N'
    })
    controller.handleButton({
        'selector': By.NAME,
        'key': 'Go'
    })
    time.sleep(2)
    controller.handleButton({
        'selector': By.XPATH,
        'key': '/html[1]/body[1]/form[1]/table[4]/tbody[1]/tr[3]/td[2]/a[1]'
    })
    driver.implicitly_wait(5)

###########################################################################
################################# MAIN ####################################
###########################################################################

# Option for unclose window
#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True);
#driver = webdriver.Chrome(options=options)

# Bypass Private Connection
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)
driver.get("https://10.25.136.209:9446/login.view")
driver.implicitly_wait(5)

# Login
loginController = loginController.LoginController(driver)
loginController.login(loginConst.credentialLogin['userId'], loginConst.credentialLogin['password'])
time.sleep(1)

##### Choose 1 of 2 Gate : New Ticket / Prewash Ticket List
##### Please comment unchoosen gate
########## New Ticket
newTicket(driver, loginController, customerController.CustomerController(driver))

########## Prewash Ticket List
# prewashTicketList(driver, loginController)

# Create General Info
generalInfoController = generalInfoController.GeneralInfoController(driver)
generalInfoController.create(generalInfoConst.generalInfo)

# Create Facility
facilityController = facilityController.FacilityController(driver)
facilityController.create(facilityConst.facility)

# Create Collateral
collateralController = collateralController.CollateralController(driver)
collateralController.create(collateralConst.collateral)

time.sleep(3)
driver.quit()