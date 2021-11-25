## x = 5
# print(x)

# print(x == 5) # true
# print(x != 5)

# x = 100
#
# if x != 100:
#     print('X is not equal to 100') # s otstupom vypoljaet IF срабатывает ппервое условие
# elif x == 100:
#     print('X is equal to 100')
# elif x > 500:
#     print('X is greater than 50') # если убрать else  сработает все
# else:
#     print(x)


# id_code = input('PLease enter ID: ')
# if len(id_code) == 11:
#      print('ID code is correct')
# elif len(id_code) >11:
#      print('ID code is to long')
# else:
#      print('ID code is to short')

# id_code = input('PLease enter ID: ')
# if len(id_code) == 11:
#      print('ID code is correct')
# else:
#     if len(id_code) > 11:
#         print('ID code is to long')
#         if len(id_code >15):
#             print('ID is more than 15 symbols')
#     else:
#         print('ID code is to short')

# sample_list =list()
# sample_list2 = []
# print(type(sample_list))
# print(type(sample_list2))

# world = "world"
# sample_list = [123, 0.2323, 'Hello', world, True, None, [1, 2, 3, 4, 5, 6,['one', 'two', 'tree']]]
# print(sample_list)
#
# print(len(sample_list))
# print(type(sample_list[-1]))
# print(sample_list[-1][2:4]) #первые суобуи выбор элемениа Ювторые скобки выбор из элемента
# print(sample_list[-1][-1][0][0])

courses = ['Math', 'Physics', 'History', 'Progrm', "Liter"]
numbers = [4, 5, 23, 1, 9, 84]

print(courses)
courses[0] = 'Bio' # изменение индекса
courses[0:2] = 'Bio' #'B', 'i', 'o'
courses[0:2] = 'Bio', 'art', 'rus' #'Bio', 'art', 'rus', 'o', 'History'
print(courses)