# mk-labels-from-contacts

Generate mail merge data from a Google Contacts export.

The input is a CSV file, produced by Google Contacts export.

The output is a CSV file that can be consumed by utilities such as [ gLabels 
](https://help.gnome.org/users/glabels/stable/).

Example:
```
python3 process_contacts.py < contacts.csv > labels.csv
```

In this example _contacts.csv_ is the export from Google Contacts, and 
_labels.csv_ will be imported into the utility you use for mail merge.


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

### Using gLabels

To generate address labels using _gLabels_, once you have run 
_process_contacts.py_, do:

* Create a new project with your selected label type
* Select: Object -> Merge Properties
    * set format: CSV with keys
    * select Location: _labels.csv_
* In the label design, select a text box that fills the label

In the label text box, enter as your template:
```
${F1}
${F2}
${F3}
${F4}
```


## FAQ

**Is there sample data I can test on?**

Yes. There is an example Google Contacts export in:  _example-contacts.csv_ 

**What results from processing the example-contacts.csv file?**

It should look like _example-labels.csv_.

**Can I generate sample data with 37 addresses?**

Yes. You may wish to do this if the provided _example-contacts.csv_ does not
include sufficient addresses for your testing.

Run:

    pip install Faker
    python3 mk-example-contacts.py --num-entries 37 >whatever.csv

**Are there test cases?**

Yes. Just run: ```pytest```


## Author

Courtney Rosenthal<br />
cr@crosenthal.com
