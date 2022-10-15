import calendar,sys

year=int(sys.argv[1])
month=int(sys.argv[2])
day=int(sys.argv[3])

weekday=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
idx=calendar.weekday(year, month, day)
print '%s'%weekday[idx]
