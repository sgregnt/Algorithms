import datetime
print(datetime.datetime.today())
print(datetime.datetime.today().weekday())

# convert integer to a data
from datetime import datetime
dt = datetime.fromordinal(733828)
print(dt)
print(dt.weekday())

integer_date = datetime(2012, 10, 1, 0, 0)
print(integer_date.toordinal())
print(integer_date.month)

integer_date1 = datetime(2012, 10, 1, 0, 0)
integer_date2 = datetime(2012, 12, 31, 0, 0)
integer_date3 = datetime(2013, 12, 31, 0, 0)
print(integer_date1.toordinal())
print(integer_date2.toordinal())
print(integer_date3.toordinal())
print(integer_date2.toordinal() - integer_date1.toordinal())
print(integer_date3.toordinal() - integer_date2.toordinal())