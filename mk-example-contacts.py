#!/usr/bin/env python3
#
# Generates example data that can be used for testing.
#

import argparse
from sys import stdout
from random import random
import csv
from faker import Faker

parser = argparse.ArgumentParser(description = 'Generate example contacts.')
parser.add_argument('-n', '--num-entries', default = 20, type = int)
args = parser.parse_args()
if (args.num_entries <= 0):
  print("ERROR: bad num-entries value")
  exit(1)

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


for i in range(args.num_entries):
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

