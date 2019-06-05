import datetime, calendar

for year in range(1006, 1996, 10):
    date = datetime.date(year, 1, 26)
    if date.isoweekday() == 1 & calendar.isleap(year):
        print(date)
