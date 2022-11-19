#!/usr/bin/env python3
#
# Generates example data that can be used for testing.
#

# Generate this many addresses.
NUM_ENTRIES = 20

from sys import stdout
from random import random
import csv
from faker import Faker

fake = Faker()

writer = csv.writer(stdout)
writer.writerow([
    'Name',
    'Address 1 - Street',
    'Address 1 - City',
    'Address 1 - PO Box',
    'Address 1 - Region',
    'Address 1 - Postal Code',
    'Address 1 - Country',
    'Address 1 - Extended Address'
])

def pick_randomly(chance, choice1, choice2):
    return choice1 if (random() <= chance) else choice2


for i in range(NUM_ENTRIES):
    writer.writerow([
        fake.name(),
        fake.street_address(),
        fake.city(),
        "", # 'Address 1 - PO Box',
        fake.state(),
        fake.postcode(),
        pick_randomly(0.8, "US", fake.country_code()),
        pick_randomly(0.85, "", "Second Address Line")
    ])

