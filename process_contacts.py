#!/usr/bin/env python3
#
# process-contacts.py - Generate mail merge input from a Google Contacts export.
#
# I use the processed output with the "gLabels" program.
#
# There is an "Address 1 - Formatted" field in the CSV which ought to
# be what we want -- but it does some weird things (like combining the
# second address line with the city/state/zip line). So we will build
# up the address from bits.
#

import sys
import csv

# The country field won't be printed if it matches this value.
MY_COUNTRY = "US"

# Field names that identify related person
RELATION_TYPE = 'Relation 1 - Label'
RELATION_VALUE = 'Relation 1 - Value'

# Types of relations that should be merged into the address.
MERGEABLE_RELATIONS = ['Spouse', 'Partner', 'Domestic Partner', 'Fiancee']


def format_name(contact):
  first_name = contact['First Name'] or "<OOPS First Name missing>"
  last_name = contact['Last Name'] or "<OOPS Last Name missing>"
  relation_name = get_relation_name(contact)
  if relation_name:
    if relation_name.endswith(" " + last_name):
      return first_name + " & " + relation_name
    else:
      return first_name + ' ' + last_name + " & " + relation_name
  return first_name + ' ' + last_name


def get_relation_name(contact):
  if RELATION_TYPE in contact:
    if contact[RELATION_TYPE] in MERGEABLE_RELATIONS:
      if RELATION_VALUE in contact:
        return contact[RELATION_VALUE]
      else:
        return "<OOPS Relation Name missing>"
  # else returns None


def get_city_state_zip(contact):
  return "{0}, {1} {2}".format(
    contact['Address 1 - City'] or "<OOPS Missing City>",
    contact['Address 1 - Region'] or "<OOPS Missing Region>",
    contact['Address 1 - Postal Code'] or "<OOPS Missing Postal Code>")


def get_country(contact):
  COUNTRY = 'Address 1 - Country'
  return contact[COUNTRY] if (contact[COUNTRY] != MY_COUNTRY) else None

def process_contact(contact):
  return [
    format_name(contact),
    contact['Address 1 - PO Box'],
    contact['Address 1 - Street'],
    contact['Address 1 - Extended Address'],
    get_city_state_zip(contact),
    get_country(contact)
  ]

def main():
  writer = csv.writer(sys.stdout)
  writer.writerow(["F1", "F2", "F3", "F4", "F5"])
  for contacy in csv.DictReader(sys.stdin):
    results = [x for x in process_contact(contacy) if x]
    writer.writerow(results)

if __name__ == "__main__":
    main()
