# mk-labels-from-contacts
Generate address labels from a Google Contacts export

This package generates pages of mailing addresses from a Google Contacts 
export. Those pages can be printed on adhesive address label sheets.


## LabelNation

This package depends on LabelNation by Karl Fogel.

  * Home page: https://www.red-bean.com/labelnation/
  * Source code: https://code.librehq.com/kfogel/labelnation

LabelNation version 1.231 is included in this package. You probably ought to 
download the latest version from the project's home page.

## Prerequisites

You will need Python3 to use these utilities.

Install LabelNation: either download the latest version from the 
project home page (preferred) or unbundle the tarball provided in this package.

## Procedure

Generate labels as follows.

### Make Google Contacts export

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

### Configure the generator

Open the _mk-labels-from-contacts.defs_ file with a text editor and make any 
adjustments. In particular, you will want to set _LABEL_TYPE_ to the label 
type you are using.

To see a list of supported label types, run:

    $ python3 labelnation-*/labelnation --list-types
    Predefined label types:
    
      2 labels per page:           Avery-5444
      4 labels per page:           Avery-5168
      6 labels per page:           Avery-5264 
        .
        .
        .

### Generate the labels

Finally, generate the labels by running a command such as:

    sh mk-labels-from-contacts.sh example-contacts.csv >labels.ps

The output file is PostScript. You may be able to send that directly to your 
printer.

## Sample Data

The _example-contacts.csv_ file is sample data that can be used to test the 
printing process. It was generated with _mk-example-contacts.py_

    python3 mk-example-contacts.py >example-data.ps

This utility requires the _Faker_ package. If you want to generate example 
data (but you don't need this for actual label generation), do:

    pip install Faker

## Author

Courtney Rosenthal<br />
cr@crosenthal.com