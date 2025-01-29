from selenium.webdriver.common.by import By
from const.baseConst import *

facility = [
    # Header
    {
        'label': 'Select Product',
        'type': select,
        'selector': By.NAME,
        'key': 'productCode',
        'value': 'XDBKPR',
        'timeSleep': 3,
    },
    {
        'label': 'Add',
        'type': button,
        'selector': By.NAME,
        'key': 'Add',
        'value': 'Add',
        'timeSleep': 10,
    },
    # Body
    {
        'label': 'Facility Package',
        'type': buttonPopUpWindowRadio,
        'selector': By.CSS_SELECTOR,
        'key': 'input[onclick="onFacilityPackagePickListClick(this.form);"]',
        'value': 'XDB5THG$KPR XTra Dinamis B Fix 5 Tahun - Grading$$FIX5TH$1$304$XDBKPR$0$FIX5$Pricing KPR Fix 5 Tahun',
    },
    {
        'label': 'Facility Amount',
        'type': inputText,
        'selector': By.NAME,
        'key': 'amount07',
        'value': '500000000',
    },
    {
        'label': 'Down Payment',
        'type': inputText,
        'selector': By.NAME,
        'key': 'downPaymentAmount',
        'value': '100000000',
    },
    {
        'label': 'Facility Tenure (Months)',
        'type': inputText,
        'selector': By.NAME,
        'key': 'tenure04',
        'value': '120',
    },
]