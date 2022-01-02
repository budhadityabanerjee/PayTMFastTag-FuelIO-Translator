#!/usr/bin/env python3

try:
    import argparse
    import sys
    import pandas as pd
except ImportError as e:
    sys.exit("Error: " + str(e) + "\nPlease install this module and retry.\n")

'''Basic setup stuff

    Take 3 arguments:

    infile    : Input CSV file to be parsed
    outfile   : Output CSV file to be generated
    uid_start : Start value for unique id'''

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="Input csv file to be parsed", type=str)
parser.add_argument("outfile", help="Output csv file to be generated", type=str)
parser.add_argument("uid_start", help="Unique ID start value", type=int)

args = parser.parse_args()
infile = args.infile
outfile = args.outfile
start_id = args.uid_start
cost_title = "Fastag"
odo = 0
cost_type_id = 7
flag = 0
idr = 0
read = 1
remind_odo =  0
remind_date = '2011-01-01'
is_template = 0
repeat_odo = 0
repeat_months = 0
is_income = 0


'''The input file is expected to be of type:

    "Date","Activity","Source/Destination","Wallet Txn ID","Comment","Debit","Credit","Transaction Breakup","Status"
    "25/12/2021 23:20:47","Paid for order","Toll Fastag Order #892115852","38071755187","","100","","","SUCCESS"
    "25/12/2021 17:29:46","Paid for order","Toll Fastag Order #891524834","38064372089","","200","","","SUCCESS"

    We're interested in the columns: Date, Source/Destination, Wallet Txn ID, and Debit'''
try:
    df = pd.read_csv(infile, usecols = ['Date', 'Source/Destination', 'Wallet Txn ID', 'Debit'])
except FileNotFoundError as e:
    print("Error: Infile not found at location specified")
    sys.exit(e)

'''
    df is now a Pandas dataframe that needs the following massaging:

    Date column must be stripped of seconds and converted to timestamp
    Source/Destination and Wallet Txn ID should be merged into a single column titled Notes
    Debit column must be renamed to Cost'''

# Remove seconds and convert everything to timezone format
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d %H:%M')

# Concatenate columns and remove old ones
df["Notes"] = df["Source/Destination"].map(str) + " " + df["Wallet Txn ID"].map(str)
df.drop(columns=['Source/Destination', 'Wallet Txn ID'], inplace=True)

# Rename Debit to Cost
df = df.rename({'Debit':'Cost'}, axis='columns')

'''The output file is expected to be of type:
    "CostTitle","Date"            ,"Odo","CostTypeID","Notes"                                   ,"Cost" ,"flag","idR","read","RemindOdo","RemindDate","isTemplate","RepeatOdo","RepeatMonths","isIncome","UniqueId"
    "Fastag"   ,"2021-12-25 23:20","0"  ,"7"         ,"Toll Fastag Order #892115852 38071755187","100.0","0"   ,"0"  ,"1"   ,"0"        ,"2011-01-01","0"         ,"0"        ,"0"           ,"0"       ,"29"
    "Fastag"   ,"2021-12-25 17:29","0"  ,"7"         ,"Toll Fastag Order #891524834 38064372089","200.0","0"   ,"0"  ,"1"   ,"0"        ,"2011-01-01","0"         ,"0"        ,"0"           ,"0"       ,"29"

    Add the required columns
'''
# Move Notes to the right location
df.insert(loc=1, column='Notes', value=df.pop('Notes'))

# Insert columns with the values
df.insert(loc=0, column='CostTitle', value=cost_title)
df.insert(loc=2, column='Odo', value=odo)
df.insert(loc=3, column='CostTypeID', value=cost_type_id)
df.insert(loc=6, column='flag', value=flag)
df.insert(loc=7, column='idR', value=idr)
df.insert(loc=8, column='read', value=read)
df.insert(loc=9, column='RemindOdo', value=remind_odo)
df['RemindDate'] = pd.to_datetime(remind_date)
df.insert(loc=11, column='isTemplate', value=is_template)
df.insert(loc=12, column='RepeatOdo', value=repeat_odo)
df.insert(loc=13, column='RepeatMonths', value=repeat_months)
df.insert(loc=14, column='isIncome', value=is_income)
df.insert(loc=15, column='UniqueId', value=range(start_id, start_id + len(df)))

# Write to file
try:
    df.to_csv(outfile, index=False)
except Exception as e:
    sys.exit(e)




