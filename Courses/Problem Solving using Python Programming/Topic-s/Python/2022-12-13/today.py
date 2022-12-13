import testfunction
from datetime import datetime

dt = datetime.now()

print(testfunction.calculate(3))
print('The current weekday is:', dt.strftime('%a'),'(short form)')
print('The current weekday is:', dt.strftime('%A'),'(full form)')
print('The current weekday no. is:', dt.strftime('%w'),'(weekday as a number)')
print('The current day of month is:', dt.strftime('%d'),'(day of month)')
print('The current month name is:', dt.strftime('%b'),'(short form)')
print('The current month name is:', dt.strftime('%B'),'(full form)')
print('The current year is:', dt.strftime('%y'),'(without century)')
print('The current year is:', dt.strftime('%Y'),'(full version)')
print('The current hour is:', dt.strftime('%H'))
print('The current hour is:', dt.strftime('%I'))
print('If AM/PM:', dt.strftime('%p'))
print('The current minutes are:', dt.strftime('%M'))
print('The current seconds are:', dt.strftime('%S'))
print('The current microseconds are:', dt.strftime('%f'))
print('The UTC offset is:', dt.strftime('%z'))
print('The Timezone is: ', dt.strftime('%Z'))
print('The Day number of year:', dt.strftime('%j'))
print('The Weeknumber of year:', dt.strftime('%U'), '(Sunday as the first day)')
print('The Weeknumber of year:', dt.strftime('%W'), '(Monday as the first day)')
print('The Local version  of date and time:', dt.strftime('%c'))
print('The current century:', dt.strftime('%C'))
print('The Local version of date:', dt.strftime('%x'))
print('The Local version of time:', dt.strftime('%X'))
print('The ISO 8601 year:', dt.strftime('%G'))
print('The ISO 8601 weekday:', dt.strftime('%u'))
print('The ISO 8601 weeknumber:', dt.strftime('%V'))

