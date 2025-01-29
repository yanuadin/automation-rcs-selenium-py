from selenium.webdriver.common.by import By
from const.baseConst import *

customers = {
    'header': [
        #Customer Inquiry
        {
            'label': 'Organization',
            'type': select,
            'selector': By.NAME,
            'key': 'maintenanceSBUCode',
            'value': '01'
        },
        # OCR Inquiry
        {
            'label': 'Scan OCR Data',
            'type': radio,
            'selector': By.NAME,
            'key': 'customerVO.ocrScanData',
            'value': 'N'
        },
        {
            'label': 'By Pass OCR Reason',
            'type': buttonPopUpWindow,
            'selector': By.NAME,
            'key': 'ocrPassReasonBtn',
            'value': 'HL5000',
        },
        # Customer Information
        {
            'label': 'ID Type',
            'type': select,
            'selector': By.NAME,
            'key': 'firstIdentificationTypeCode',
            'value': '10'
        },
        {
            'label': 'ID No.',
            'type': inputText,
            'selector': By.NAME,
            'key': 'firstIdentificationNumber',
            'value': '1271031903770003'
            # 'value': '3172055011931001'
        },
    ],
    'body': [
        # Customer Information
        {
            'label': 'Is CBP',
            'type': radio,
            'selector': By.NAME,
            'key': 'customerVO.isCBP',
            'value': 'N'
        },
        {
            'label': 'Joint Income',
            'type': select,
            'selector': By.NAME,
            'key': 'customerVO.isJointIncome',
            'value': 'N'
        },
        {
            'label': 'Customer Name',
            'type': inputText,
            'selector': By.NAME,
            'key': 'customerVO.name',
            'value': 'ROBOTYANU',
            'skipException': True
        },
        {
            'label': 'Marital Status',
            'type': select,
            'selector': By.NAME,
            'key': 'customerIndividualVO.maritalStatusCode',
            'value': 'S'
        },
        {
            'label': 'Date Of Birth',
            'type': hiddenInputText,
            'selector': By.NAME,
            'key': 'customerVO.registeredDateDay',
            'value': '01',
        },
        {
            'label': 'Date Of Birth',
            'type': hiddenInputText,
            'selector': By.NAME,
            'key': 'customerVO.registeredDateMonth',
            'value': '01',
        },
        {
            'label': 'Date Of Birth',
            'type': hiddenInputText,
            'selector': By.NAME,
            'key': 'customerVO.registeredDateYear',
            'value': '1990',
        },
        {
            'label': 'Gender',
            'type': select,
            'selector': By.NAME,
            'key': 'customerIndividualVO.genderCode',
            'value': 'M'
        },
        {
            'label': 'Place of Birth',
            'type': inputText,
            'selector': By.NAME,
            'key': 'customerVO.placeOfBirth',
            'value': 'Jakarta'
        },
        {
            'label': 'NPWP No',
            'type': inputText,
            'selector': By.NAME,
            'key': 'customerVO.npwpNo',
            'value': '1111111111111111'
        },
        {
            'label': "Mother's Maiden Name",
            'type': inputText,
            'selector': By.NAME,
            'key': 'customerIndividualVO.motherMaidenName',
            'value': 'Mother Name'
        },
        {
            'label': 'Educational Level',
            'type': select,
            'selector': By.NAME,
            'key': 'customerIndividualVO.educationLevelCode',
            'value': '2'
        },
        {
            'label': 'Citizenship',
            'type': select,
            'selector': By.NAME,
            'key': 'customerVO.citizenshipCode',
            'value': '1'
        },

        # ID Address
        {
            'label': 'ID Address',
            'type': inputText,
            'selector': By.NAME,
            'key': 'idAddressVO.addressLine1',
            'value': 'Jakarta No 1'
        },
        {
            'label': 'Postcode',
            'type': buttonPopUpWindow,
            'selector': By.CSS_SELECTOR,
            'key': 'input[onclick="onIdPostalCodePickListButtonClick();"]',
            'value': '001'
        },
        # Residential Address
        {
            'label': 'Click if the above is the same',
            'type': buttonConfirmation,
            'selector': By.NAME,
            'key': 'clickIfTheAboveIsTheSame',
            'value': 'Y'
        },
        {
            'label': 'Mobile Phone No.',
            'type': inputText,
            'selector': By.NAME,
            'key': 'residentialAddressVO.mobileNumberAreaCode',
            'value': '021'
        },
        {
            'label': 'Mobile Phone No.',
            'type': inputText,
            'selector': By.NAME,
            'key': 'residentialAddressVO.mobileNumber',
            'value': '323232'
        },
        {
            'label': 'Email',
            'type': inputText,
            'selector': By.NAME,
            'key': 'residentialAddressVO.email',
            'value': 'robotyanu@mail.com'
        },
        {
            'label': 'Duration In Current Residence',
            'type': inputText,
            'selector': By.NAME,
            'key': 'residentialAddressVO.durationInResidenceYear',
            'value': '2'
        },
        {
            'label': 'Duration In Current Residence',
            'type': inputText,
            'selector': By.NAME,
            'key': 'residentialAddressVO.durationInResidenceMonth',
            'value': '2'
        },
        # Employment Information
        {
            'label': 'Employer Name/ Own Company',
            'type': buttonPopUpWindow,
            'selector': By.CSS_SELECTOR,
            'key': 'input[onclick="onEmployerPickListButtonClick();"]',
            'value': 'ADIRA'
        },
        {
            'label': 'Employment Type',
            'type': select,
            'selector': By.NAME,
            'key': 'customerEmploymentVO.employmentTypeCode',
            'value': '01'
        },
        {
            'label': 'Employment Status',
            'type': select,
            'selector': By.NAME,
            'key': 'customerEmploymentVO.employmentStatusCode',
            'value': '01'
        },
        {
            'label': 'Is Own Company?',
            'type': radio,
            'selector': By.NAME,
            'key': 'customerEmploymentVO.isOwnCompany',
            'value': 'N'
        },
        {
            'label': 'Employment Country',
            'type': buttonPopUpWindow,
            'selector': By.CSS_SELECTOR,
            'key': 'input[onclick="onEmploymentCountryPickListButtonClick();"]',
            'value': 'ID'
        },
        {
            'label': 'Net Monthly Income',
            'type': inputText,
            'selector': By.NAME,
            'key': 'customerEmploymentIncomeVO.monthlyMainIncome',
            'value': '10000000'
        },
        {
            'label': 'Occupation',
            'type': buttonPopUpWindow,
            'selector': By.CSS_SELECTOR,
            'key': 'input[onclick="onOccupationPickListButtonClick();"]',
            'value': '0001'
        },
        {
            'label': 'Office Address',
            'type': inputText,
            'selector': By.NAME,
            'key': 'officeAddressVO.addressLine1',
            'value': 'Jakarta No 2'
        },
        {
            'label': 'Postcode',
            'type': buttonPopUpWindow,
            'selector': By.CSS_SELECTOR,
            'key': 'input[onclick="onOfficePostalCodePickListButtonClick();"]',
            'value': '001'
        },
        {
            'label': 'Length of Service',
            'type': inputText,
            'selector': By.NAME,
            'key': 'customerEmploymentVO.lengthOfServiceYear',
            'value': '2'
        },
        {
            'label': 'Length of Service',
            'type': inputText,
            'selector': By.NAME,
            'key': 'customerEmploymentVO.lengthOfServiceMonth',
            'value': '2'
        },
    ]
}