# SAS Enterprise Guide Parser

For those of us who grew up in an open source analytical world, we may chaffe at the thought of having to use a closed source tool to do our work.

If you're in charge of SAS Enterprise Guide at your workplace, you'll understand the frustration of having to deal with hundreds of "EGPs" scattered across a network of directories and sub-directories.  The pain of having to identify what tables and even what columns are being used can be awful.

So I created egp-parse as a way of...
* Scanning a network for .egp files.
* Extracting the code inside an EGP.
* Returning the tables and columns used inside of each one as two text files.

# Using EGP Parse
    python egpparse.py startdir outputdir

* Requires **Python 2.7**
* The one external dependency is **xmltodict**

## Using EGP Parse on Windows

    C:\Python27\python.exe egpparse.py C:\Users C:\Users\<You>\<TEMP>

This example assumes...

* You are using Python2.7.
* You have command prompted into the egp-parse\egpparse directory.
 * This lets you reference the egpparse.py file directly.
* C:\Users is where you'll start scanning.
* C:\Users\<You>\<TEMP> is where copies of every EGP and the final two text files will be placed.
