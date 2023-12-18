from types import MappingProxyType

from process_contacts import *

# create an example row as an immutable dict
ex = MappingProxyType({
    'Name': 'dont use this',
    'Given Name': 'Amanda',
    'Family Name': 'Harris',
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
    z['Relation 1 - Type'] = 'Spouse'
    z['Relation 1 - Value'] = 'William Harris'
    assert get_relation_name(z) == 'William Harris'

def test_format_name():
    assert format_name(ex) == 'Amanda Harris'

    z = ex.copy()
    z['Relation 1 - Type'] = 'Spouse'
    z['Relation 1 - Value'] = 'William Harris'
    assert format_name(z) == 'Amanda & William Harris'

    z['Relation 1 - Value'] = 'William Moreno'
    assert format_name(z) == 'Amanda Harris & William Moreno'

    z['Relation 1 - Type'] = 'Nothing'
    assert format_name(ex) == 'Amanda Harris'


def test_format_address():
    assert format_address(ex) == "3644 Sheila St\nRodneyville, Michigan 38619"
    
    z = ex.copy()
    z['Address 1 - Country'] = "XYZ"
    assert format_address(z) == "3644 Sheila St\nRodneyville, Michigan 38619\nXYZ"
    
    z = ex.copy()
    z['Address 1 - Extended Address'] = "Suite 314159"
    assert format_address(z) == "3644 Sheila St\nSuite 314159\nRodneyville, Michigan 38619"

    z = ex.copy()
    z['Address 1 - PO Box'] = "PO Box 314159"
    assert format_address(z) == "PO Box 314159\n3644 Sheila St\nRodneyville, Michigan 38619"


def test_format_row():
    assert format_row(ex) == "Amanda Harris\n3644 Sheila St\nRodneyville, Michigan 38619\n---"
