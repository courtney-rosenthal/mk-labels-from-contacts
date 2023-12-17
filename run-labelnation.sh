#!/bin/sh

USAGE="usage: $0 <CONTACTS.TXT"
set -o errexit

# Load definitions file.
. ./`basename --suffix=.sh $0`.defs
: ${LABEL_TYPE:?} ${LABELNATION:?} ${PYTHON:?}

# Process the contacts data (from stdin) into a PS file (to stdout).
${PYTHON} ${LABELNATION}  \
    --infile "-"          \
    --delimiter "---"     \
    --outfile "-"         \
    --type ${LABEL_TYPE}  \
    ${LABELNATION_OPTIONS}

