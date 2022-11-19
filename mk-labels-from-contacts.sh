#!/bin/sh
#
# mk-labels-from-contacts.sh - Generate address labels from a Google Contacts export.
#
# Courtney Rosenthal
# cr@crosenthal.com
#

USAGE="usage: $0 FILE (typically \"contacts.csv\" exported from Google Contacts)"
set -o errexit

# Load definitions.
. ./mk-labels-from-contacts.defs
: ${LABEL_TYPE:?} ${LABELNATION:?} ${PYTHON:?}

# Get input file from command line.
if [ $# -ne 1 ] ; then
  echo "$USAGE" >&2
  exit 1
fi
INPUT_FILE="$1"
if [ ! -f "${INPUT_FILE}" ] ; then
  echo "$0: input file \"${INPUT_FILE}\" not found" >&2
  exit 1
fi

# Process the contacts into a PS file to stdout.
${PYTHON} process-contacts.py < ${INPUT_FILE} \
  | ${PYTHON} ${LABELNATION} \
      --infile "-" \
      --delimiter "---" \
      --type ${LABEL_TYPE} \
      --outfile "-"

