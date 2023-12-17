# mk-labels-from-contacts
Generate address labels from a Google Contacts export.

The _mk-labels-from-contacts_ processes a Google Contacts export to a date file.
This data file can be fed into the _LabelNation_ utilty by Karl Fogel to print
onto adhesive address label sheets.

## Procedure

The process for making your labels is:

1. Unbundle the _LabelNation_ package.
2. Export selected Google Contacts to a CSV file.
3. Process the CSV file with _mk-labels-from-contacts_ to get a data file.
4. Process the data file with LabelNation to get a PS (PostScript) file.
5. Print the PS file onto sheets of blank labels.

### Download LabelNation

To unbundle the _LabelNation_ package, do:

    tar xvf labelnation-1.231.tar.gz

This is version 1.231. If a newer version is available, you may prefer to 
retrieve and use that.

Links:

  * Home page: https://www.red-bean.com/labelnation/
  * Source code: https://code.librehq.com/kfogel/labelnation

### Export Contacts

These directions are for the web version of Google Contacts. I suggest 
putting all the contacts you want to make labels for into a group, and then 
export that group.

  * Select all the contacts you want to export.
  * Click the "Manage Labels" icon at the top.
  * Select "Create Label" and give the group a name.
  * Click the "..." icon at the top and select "Export".
  * Choose "Export selected contacts".
  * Choose "Export as Google CSV".
  * Click "Export" and save to a local file (default "contacts.csv").

### Process the Contacts

Next, run:

    python3 process-contacts.py <contacts.csv >contacts.txt

This will create a data file that contains the contacts and addresses.
Open this file with an editor, review the results, and make any corrections.

### Generate Labels Printout

Next, run:

    python3 labelnation-*/labelnation --list-types

This will list all the supported label types (like "Avery-5162"). Identify
which label type you will be using.

Next:

    cp run-labelnation.defs.example run-labelnation.defs

Next, edit the _run-labelnation.defs_ file, set LABEL_TYPE to the value 
selected. Make any other adjustments as required.

Next, run:

    sh run-labelnation.sh <contacts.txt >labels.ps

This will generate your labels to a PostScript file.

You should inspect the _labels.ps_ file (with a PostScript viewer) to verify it 
is ok. If it is, go ahead and print it.


## FAQ

**Is there sample data I can test on?**

Yes. There is an example Google Contacts export in:  _example-contacts.csv_ 

**Can I generate sample data with 37 addresses?**

Yes. You may wish to do this if the provided _example-contacts.csv_ does not
include sufficient addresses for your testing.

Run:

    pip install Faker
    python3 mk-example-contacts.py --num-entries 37 >whatever.csv

**Can I test first on plain paper?**

Yes, to avoid wasting labels it would be good to test first on plain paper.

Edit the _run-labelnation.defs_ file and add:

    LABELNATION_OPTIONS="--show-bounding-box"

Now, when you run _run-labelnation.sh_ it will draw a box where it expects the
label edges to be. Print this onto plain paper and inspect for correctness.

**What do I do if the labels are misaligned?**

Read the section "What To Do If The Text Is A Little Bit Off From The Labels"
in the document: https://www.red-bean.com/labelnation/help.txt

Set your margin adjustments with something like:

    LABELNATION_OPTIONS="--left-margin 15 --bottom-margin 40"


## Author

Courtney Rosenthal<br />
cr@crosenthal.com
