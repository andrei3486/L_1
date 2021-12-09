import calendar

# x = (calendar.month(2021, 7, w=0, l=0))
# print(type(x))
# print(calendar.calendar(2021, w=2, l=1, c=2, m=3))

# print(calendar.weekday(2021, 12, 6))

# print(calendar.isleap(2020))   # високлсный год
# print(calendar.isleap(2021))
#
# print(calendar.leapdays(2000, 2020)) # количество високосных лет


# import time
#
#
# # print(time.time())   # unix timestamp
#
# start = time.time()
#
# time.sleep(7)              #сколько секунд прога будет спать
#
# # print(time.asctime())  # Mon Dec  6 19:26:18 2021 можно индексировать
#
# print(time.gmtime()) # time.struct_time(tm_year=2021, tm_mon=12, tm_mday=6, tm_hour=17, tm_min=29, tm_sec=2, tm_wday=0, tm_yday=340, tm_isdst=0)
#
# now = time.gmtime()
# print(now[0])
#
# stop = time.time()
# print(stop - start)