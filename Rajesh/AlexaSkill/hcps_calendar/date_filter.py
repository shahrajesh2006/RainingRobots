from datetime import date
import datetime


# Using readlines() 
file1 = open('Rajesh/hcps_calendar.txt', 'r') 
Lines = file1.readlines() # this list of all the lines from the file

search_query="holiday"
lines_matched=""

for line in Lines:
        if line.lower().find(search_query) != -1:
            lines_matched = lines_matched + line

#print(lines_matched)

today = date.today()#today's date object
print("Today's date:", today)

date_str = '11/28/2020' # The date - 29 Dec 2017
format_str = '%m/%d/%Y' # The format
datetime_obj = datetime.datetime.strptime(date_str, format_str).date()
print(datetime_obj)


# Check the dates 
if today == datetime_obj: 
    print("Both dates are equal") 
      
elif today > datetime_obj: 
    print("Today is greater than date from calendar") 
      
else: 
    print("Today is before the date from calendar") 


