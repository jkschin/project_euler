import calendar
a = [calendar.monthrange(year,month)[0] for year in range(1901,2001) for month in range(1,13)].count(6)