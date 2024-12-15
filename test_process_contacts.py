from types import MappingProxyType
from process_contacts import *

# create an example row as an immutable dict
ex = MappingProxyType({
    'Name': 'dont use this',
    'First Name': 'Amanda',
    'Last Name': 'Harris',
    'Address 1 - Street': '3644 Sheila St',
    'Address 1 - City': 'Rodneyville',
    'Address 1 - PO Box': '',
    'Address 1 - Region': 'Michigan',
    'Address 1 - Postal Code': '38619',
    'Address 1 - Country': 'US',
    'Address 1 - Extended Address': ''
})

def test_get_relation_name():
    assert get_relation_name(ex) == None

    z = ex.copy()
    z[RELATION_TYPE] = 'Spouse'
    z[RELATION_VALUE] = 'William Harris'
    assert get_relation_name(z) == 'William Harris'

def test_format_name():
    assert format_name(ex) == 'Amanda Harris'

    z = ex.copy()
    z[RELATION_TYPE] = 'Spouse'
    z[RELATION_VALUE] = 'William Harris'
    assert format_name(z) == 'Amanda & William Harris'

    z[RELATION_VALUE] = 'William Moreno'
    assert format_name(z) == 'Amanda Harris & William Moreno'

    z[RELATION_TYPE] = 'Nothing'
    assert format_name(z) == 'Amanda Harris'

def test_get_city_state_zip():
    assert get_city_state_zip(ex) == "Rodneyville, Michigan 38619"

def test_get_country():
    assert get_country(ex) == None
    z = ex.copy()
    z['Address 1 - Country'] = 'CA'
    assert get_country(z) == 'CA'

def test_process_contact():
    assert process_contact(ex) == [
        'Amanda Harris',
        '',
        '3644 Sheila St',
        '',
        'Rodneyville, Michigan 38619',
        None
    ]
