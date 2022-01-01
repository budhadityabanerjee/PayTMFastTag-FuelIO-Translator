PayTM and FastTag
Instructions to import PayTM Fastag transaction data to FuelIO:


### Get the FuelIO Data file
1. Make sure that FuelIO is setup to backup files to Google Drive.
2. Trigger a backup if it has not happened already
3. Locate the FuelIO folder in Google Drive, then from the "sync" subfolder download the file corresponding to your vehicle - normally named **vehicle-N-sync.csv**
4. Open this file in gnumeric and look at the columns for UniqueID (Col P and Q) - and identify the largest value. The UniqueIDs we will assign to our entries will be greater than this.

### Get PayTM Transactions CSV
1. Open the PayTM app, select "Balance and History / Passbook"; then click on "PayTM Balance" then click on "PayTM Wallet".
2 On the new screen, click "Request Statement", set dates, and confirm.
3. Get the statement as a text (CSV) file in your email. This file has all the transaction data but does not (for some reason) have the names of the Toll Plazas.

### Get Toll Plaza Names
4. Open PayTM in a browser, log in, then select PayTM wallet to see a list of all the transactions [Link](http://paytm.com/paytmwallet)
5. Copy-paste the data for the relevant transactions into gedit and then reformat using a three-step find-and replace:
    * Find and replace **\n\n** with **;NL;**
    * Find and replace **\n** with a comma **,** 
    * Find and replace **;NL;** with **\n**
6. Copy-paste the data into the statement and concatenate as necessary to get the Toll name, transaction ID, etc in a single column.

### Format the Data
1. Open the FuelIO-FastTag-Template.xls file using Gnumeric
2. Start Copying data into this sheet column-wise:
    * **Col A:** Set all to Fastag
    * **Col B:** Copy the date. Make sure the format is **yyyy-mm-dd HH:MM**
    * **Col C:** Set ODO to zero for all rows
    * **Col D:** Set CostType to 7 for all rows
    * **Col E:** Fill the Notes column with names of toll plaza, transaction ID, and wallet transaction ID (note that there are two transaction IDs)
    * **Col F:** Copy the cost. Note that it should be a pure number - it should not have Rupee symbol, negative sign or brackets, etc.
    * **Col G:** Set Flag to zero for all rows
    * **Col H:** Set idR to zero for all rows
    * **Col I:** Set "read" to 1 for all rows
    * **Col J:** Set RemindOdo to zero for all rows
    * **Col K:** Set RemindDate to some date in the past, e.g. *2011-01-01 00:00* for all rows
    * **Col L, M, N and O:** Set all these columns to zero for all rows
    * **Col P:** This column requires a Unique ID (integer) to be set for each transaction). Assign a uniqueID that will not overlap with one that is already in use.
    * Save the file. It is now ready for export.
3. Exporting:
    1. From Gnumeric, select Data > Export Data > Export into Other format
    2. On the bottom left, select File Type as **Text (configurable)**
    3. Set a filename like "dataexport.txt", then click save
    4. In the Export configuration dialog, set:
        * line-termination : UNIX (linefeed)
        * separator: comma
        * Quoting: Always
        * Character Encoding: UTF-8
        * Locale: Current Locale
        * Format: Preserve
    5. Then click Save to export the text file.
    6. Open the resulting exported file in a text editor and make sure that all fields are enclosed in quote marks
4. Merging:
    * Copy this text and paste it into the **vehicle-N-sync.csv** file in the appropriate place. Make sure to not copy the heading line.
5. Save and upload this edited file back into Google Drive, overwriting the old **vehicle-N-sync.csv** file.
6. Open the FuelIO app, click on Google Drive, then click download from Google Drive.
