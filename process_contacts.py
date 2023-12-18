#!/usr/bin/env python3
#
# process-contacts.py - Generate LabelNation address input from a Google Contacts export.
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

# Separates label contents in the LabelNation input.
LABEL_SEPERATOR = "---"

# Types of relations that should be merged into the address.
MERGEABLE_RELATIONS = ['Spouse', 'Partner', 'Domestic Partner']

# For reference, here are all the address fields in the Google Contacts CSV:
# Address 1 - Type
# Address 1 - Formatted
# Address 1 - Street
# Address 1 - City
# Address 1 - PO Box
# Address 1 - Region
# Address 1 - Postal Code
# Address 1 - Country
# Address 1 - Extended Address

def conditionally_append(a, value):
  "Append a value to a list if that value is not blank."
  if value.strip() != "":
    a.append(value)

def format_address(row):
  "Given a CSV row from a contacts export, return the mailing address as a string."
  addr = []
  conditionally_append(addr, row['Address 1 - PO Box'])
  conditionally_append(addr, row['Address 1 - Street'])
  conditionally_append(addr, row['Address 1 - Extended Address'])
  addr.append("{0}, {1} {2}".format(
    row['Address 1 - City'] or "<OOPS Missing City>",
    row['Address 1 - Region'] or "<OOPS Missing Region>",
    row['Address 1 - Postal Code'] or "<OOPS Missing Postal Code>"))
  if (row['Address 1 - Country'] != MY_COUNTRY):
    conditionally_append(addr, row['Address 1 - Country'])
  return "\n".join(addr)

def format_name(row):
  "Given a CSV row from a contacts export, return the addressee name as a string."
  given_name = row['Given Name'] or "<OOPS Given Name missing>"
  family_name = row['Family Name'] or "<OOPS Family Name missing>"
  relation_name = get_relation_name(row)
  if relation_name:
    if relation_name.endswith(" " + family_name):
      return given_name + " & " + relation_name
    else:
       return given_name + ' ' + family_name + " & " + relation_name
  return given_name + ' ' + family_name

def get_relation_name(row):
  if 'Relation 1 - Type' in row:
    if row['Relation 1 - Type'] in MERGEABLE_RELATIONS:
      if 'Relation 1 - Value' in row:
        return row['Relation 1 - Value']
      else:
        return "<OOPS Relation Name missing>"
  # else returns None

def format_row(row):
  "Given a CSV row from a contacts export, return the name, address, and separator as a newline delimited string."
  return "\n".join([
      format_name(row),
      format_address(row),
      LABEL_SEPERATOR
    ])

def main():
  for row in csv.DictReader(sys.stdin):
    print(format_row(row))

if __name__ == "__main__":
    main()