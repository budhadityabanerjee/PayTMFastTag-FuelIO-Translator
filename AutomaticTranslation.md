PayTM and FastTag
Instructions to automatically import PayTM Fastag transaction data into FuelIO:


### Get the FuelIO Data file
1. Make sure that FuelIO is setup to backup files to Google Drive.
2. Trigger a backup if it has not happened already
3. Locate the FuelIO folder in Google Drive, then from the "sync" subfolder download the file corresponding to your vehicle - normally named **vehicle-N-sync.csv**
4. If you use FuelIO for multiple vehicles you can open this file in a plain text editor (gedit, vim, notepad, etc.) to make sure the file corresponds to the correct vehicle.

### Get PayTM Transactions CSV
1. Open the PayTM app, select "Balance and History / Passbook"; then click on "PayTM Balance" then click on "PayTM Wallet". There appears to be no way to do this from a browser at the moment.
2. On the new screen, click "Request Statement", set dates, and confirm.
3. Get the statement as a text (CSV) file in your email. This file has all the transaction data but does not (for some reason) have the names of the Toll Plazas. If you want the Toll Plaza names, you will need to open PayTM in a browser/app and manually add this data.
4. Open the Statement CSV file in a plain-text editor and delete all lines that are not Toll transactions relevant to the present vehicle. For example wallet recharges, cahsbacks, and store payments all need to be deleted.
5. Run the translate script:
```translate.py --infile PayTM_Wallet_Txn_History_Sample2.csv --outfile FuelIOSample-vehicle-3-sync.csv```
6. Upload the updated FuelIO CSV back into GoogleDrive - making sure not to rename the file (overwrite on upload).
7. Open the FuelIO app on your device(s) and run a "Fetch from Google Drive"
