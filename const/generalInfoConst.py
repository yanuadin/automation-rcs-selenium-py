from selenium.webdriver.common.by import By
from const.baseConst import *

generalInfo = [
    {
        'label': 'Sales Id',
        'type': select,
        'selector': By.NAME,
        'key': 'referredByTypeCode',
        'value': '10'
    },
    {
        'label': 'Referred By',
        'type': buttonPopUpWindow,
        'selector': By.CSS_SELECTOR,
        'key': 'input[onclick="onSalesPickListButtonClick();"]',
        'value': 'HANIFPW'
    },
    {
        'label': 'Parking Branch',
        'type': buttonPopUpWindow,
        'selector': By.CSS_SELECTOR,
        'key': 'input[onclick="onParkingBranchPickListButtonClick();"]',
        'value': '00002'
    },
    {
        'label': 'Facility Purpose',
        'type': select,
        'selector': By.NAME,
        'key': 'applicationPurposeCode',
        'value': '02'
    },
    {
        'label': 'Policy Program',
        'type': buttonPopUpWindow,
        'selector': By.CSS_SELECTOR,
        'key': 'input[onclick="onPolicyProgramPickListButtonClick();"]',
        'value': 'CAC007082018'
    },
]