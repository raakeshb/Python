import datetime as dt
a=dt.datetime.now()
print(a.strftime("%B"),a.strftime("%A"),a)
if a.strftime("%A")=="Monday":
   print("Today is MONDAY: Here is the Time table")
elif a.strftime("%A")=="Tuesday":
   print("Today is TUESDAY: Here is the Time table")
elif a.strftime("%A")=="Wednesday":
   print("Today is WEDNESDAY: Here is the Time table")
elif a.strftime("%A")=="Thursday":
   print("Today is THURSDAY: Here is the Time table")
elif a.strftime("%A")=="Friday":
   print("Today is FRIDAY: Here is the Time table")
elif a.strftime("%A")=="Saturday":
   print("Today is SATURDAY: Here is the Time table")
