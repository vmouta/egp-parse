# SAS Enterprise Guide Parser

For those of us who grew up in an open source analytical world, we may chaffe at the thought of having to use a closed source tool to do our work.

If you're in charge of SAS Enterprise Guide at your workplace, you'll understand the frustration of having to deal with hundreds of "EGPs" scattered across a network of directories and sub-directories.  The pain of having to identify what tables and even what columns are being used can be awful.

So I created egp-parse as a way of...
* Scanning a network for .egp files.
* Extracting the code inside an EGP.
* Returning the tables and columns used inside of each one.

