import datetime

# d = datetime.date(2018, 7, 11) # 2018-07-11
#
# today = datetime.date.today() # сегодн. дата
# # print(today.year)
# # print(today.day)
# print(today - d)
# # print(type(today))
# # print(type(d))
# # print(today.weekday())  # день недели по стандартам пайтона для расчетов и алгоритмов
# # print(today.isoweekday()) # день недели стандартный для людей
#
# print(today - d) #  'datetime.timedelta' разница во времеени б дельта времени date1 - date2 = timedelta
# # tdelta = datetime.timedelta(days=(5 * 365.25))
# # print(tdelta)
#
# tdelta = datetime.timedelta(days=57) # расчет даты
# print(d + tdelta)

# d = datetime.time(13, 17, 52)  # 13:17:52
# print(d.hour)
# print(d.minute)
# print(d.second)
# print(d.microsecond)

# d = datetime.datetime(2020, 7, 11, 14, 17, 52, 1000)  # 2020-07-11 14:17:52.001000
# print(d.date())
# print(d.time())
#
# # d_tdelta + datetime.timedelta(days=7, hours=4, minutes=15)
# # print(d - d_tdelta)
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# print(dt_today)
# print(dt_now)

# работа со с строкой
today = datetime.datetime.today()

print(today.strftime('%B %d, %Y')) # по директиве в документации December 06, 2021

dt_str = 'November 30, 2021'
new_date = datetime.datetime.strptime(dt_str, '%B %d, %Y')  # 2021-11-30 00:00:00
print(new_date)