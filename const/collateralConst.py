from selenium.webdriver.common.by import By
from const.baseConst import *

collateral = [
    {
        'label': 'Primary / Secondary?',
        'type': select,
        'selector': By.NAME,
        'key': 'primarySecondaryCode',
        'value': '01',
    },
    {
        'label': 'Property Type',
        'type': buttonPopUpWindow,
        'selector': By.CSS_SELECTOR,
        'key': 'input[onclick="onPropertyTypePickListClick('+ "'propertyTypeDisplay'" +')"]',
        'value': '01'
    },
    {
        'label': 'Property Description',
        'type': buttonPopUpWindow,
        'selector': By.CSS_SELECTOR,
        'key': 'input[onclick="onPropertyDescriptionPickListClick('+ "'propertyDescriptionDisplay'" +')"]',
        'value': '0101'
    },
    {
        'label': 'Source of Property',
        'type': select,
        'selector': By.NAME,
        'key': 'purcSourceCode',
        'value': '01',
    },
    {
        'label': 'Request Built Up Area (amount)',
        'type': inputText,
        'selector': By.NAME,
        'key': 'buildUpArea',
        'value': '30',
    },
    {
        'label': 'Request Built Up Area (type)',
        'type': select,
        'selector': By.NAME,
        'key': 'buildAreaUnitCode',
        'value': '02',
    },
    {
        'label': 'Land Area (amount)',
        'type': inputText,
        'selector': By.NAME,
        'key': 'landArea',
        'value': '30',
    },
    {
        'label': 'Land Area (type)',
        'type': select,
        'selector': By.NAME,
        'key': 'landAreaUnitCode',
        'value': '02',
    },
    {
        'label': 'Status of Completion',
        'type': select,
        'selector': By.NAME,
        'key': 'propertyStatusCode',
        'value': '2',
    },
    {
        'label': 'Purchase Price/Estimated Property Price',
        'type': inputText,
        'selector': By.NAME,
        'key': 'purchasedPrice',
        'value': '500000000',
    },
    {
        'label': 'Collateral Address',
        'type': inputText,
        'selector': By.NAME,
        'key': 'addressLine1',
        'value': 'Jakarta No 3',
    },
    {
        'label': 'RT / RW',
        'type': inputText,
        'selector': By.NAME,
        'key': 'rt',
        'value': '01',
    },
    {
        'label': 'RT / RW',
        'type': inputText,
        'selector': By.NAME,
        'key': 'rw',
        'value': '01',
    },
    {
        'label': 'Collateral Postcode',
        'type': buttonPopUpWindow,
        'selector': By.CSS_SELECTOR,
        'key': 'input[onclick="onPostCodePickListClick('+ "'postView'" +')"]',
        'value': '001'
    },
    {
        'label': 'Developer Name',
        'type': buttonPopUpWindow,
        'selector': By.CSS_SELECTOR,
        'key': 'input[onclick="onDeveloperPickListClick('+ "'buildingDeveloperNameDisplay'" +')"]',
        'value': 'ALSALSUR'
    },
    {
        'label': 'Project Name',
        'type': buttonPopUpWindow,
        'selector': By.CSS_SELECTOR,
        'key': 'input[onclick="onProjectPickListClick('+ "'buildingProjectNameDisplay'" +')"]',
        'value': 'ALAMSUTE'
    },
    {
        'label': 'Collateral Owner Relationship To Principal',
        'type': select,
        'selector': By.NAME,
        'key': 'ownerRelationshipCode',
        'value': '1',
    },
    {
        'label': 'Tenure To Title',
        'type': select,
        'selector': By.NAME,
        'key': 'propertyLandStatusCode',
        'value': '01',
    },
]