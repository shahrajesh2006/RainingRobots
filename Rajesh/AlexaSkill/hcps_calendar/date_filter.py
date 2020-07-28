from datetime import date
import datetime

#This function will take String parameter convert to date and compare and return True if the date is before today
def isBeforeToday(date_str):
    #Step 1: convert string to date object
    format_str = '%m/%d/%Y' # The format
    date_object = datetime.datetime.strptime(date_str, format_str).date()
    #print("Date object:", date_object)
    #Step 2: get today's date
    today = date.today()
    #print("Today's date:", today)
    #Step 3: Compare dates
    if date_object<today:
        return True

# Using readlines() 
file1 = open('Rajesh/hcps_calendar.txt', 'r') 
Lines = file1.readlines() # this list of all the lines from the file

search_query="holiday"
lines_matched=""

for line in Lines:
        if line.lower().find(search_query) != -1:
            line_split=line.split(":")
            date_str=line_split[0]
            if isBeforeToday(date_str):
                print("Date is before today then we are skipping the line", date_str)
            else:
                print("Date is after or today itself:", date_str)
                lines_matched = lines_matched + line

print(lines_matched)

#today = date.today()#today's date object
#print("Today's date:", today)

#date_str = '11/28/2020' # The date - 29 Dec 2017

#if isBeforeToday(date_str):
#    print("Date is before today:", date_str)
#else:
#    print("Date is after or today itself:", date_str)

#format_str = '%m/%d/%Y' # The format
#hcps_date_obj = datetime.datetime.strptime(date_str, format_str).date()
#print(hcps_date_obj)


# Check the dates 


 