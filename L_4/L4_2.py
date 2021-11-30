# numbers = [1, 2, 3, 4, 5]
# numbers2 = range(0, 100) # от и до числовой диапазон
# # for num in numbers:
# #     print(num)
#
# for num in numbers:
#     print(num ** 2) # каждый элемент в квадрате
#     # num = num ** 2 # быстрее работате без вывода (print)

people = [('Jack', 'Smith', 20, 'Tallinn', 'male'), ('Mary', 'Gold', 25, 'London', 'female'),
          ('Pierre', 'Summere', 30, 'Milan', 'male'), ('Sarah', 'Simpson', 30, 'New-york', 'female')]

# for person in people:

    # if person[4] =='male':
    #     print(f'This is {person[0]} {person[1]}. He is {person[2]} years old. He lives in {person[3]}')
    # elif person[4] =='female':
    #     print(f'This is {person[0]} {person[1]}. He is {person[2]} years old. He lives in {person[3]}')
    # print('Hello world')

# for person in people:
#     print(person)

# for name, surname, age, town, gender in people:
#     print(name)
#     print(surname)
#     print(age)
#     print(town)
#     print(gender)
#
# for person in people:
#     cnt = 0
#     cnt += 1
#     print(cnt)

# for letter in 'Hello wolrd':
#     print(letter)

# some_dict = {'name': 'Jack', 'surname': 'Smith', 'age': 30}
# print(some_dict.items())
# for key, value in some_dict.items():
#     print(key)
#     print(value)
#     print(key, value)
#
# for num1 in range(0, 10):
#     for num2 in range(0, 10):
#         for num3 in range(0, 10):
#             for num4 in range(0, 10):
#                 print(num1, num2, num3, num4)

''''''''''''''
# Fiz bas в числовом диапазоне от 0 до 100:
         #если число делиться на 3 без остатка, написать число +Fizz
          #если число делиться на 5 без остатка, написать число +Buzz
          #если число делиться на 3 и на5 без остатка, написать число +FizzBuzz
''''''''''''''
# for num in range(0, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, 'FizzBuzz')
#     elif num % 5 == 0:
#         print(num, 'Buzz')
#     elif num % 3 == 0:
#         print(num, 'Fizz')
#
chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
id = [3, 8, 6, 0, 6, 1, 8, 4, 2, 1, 4]
print((1 * 3 + 2 * 8 + 3 * 6 + 4 * 0 + 5 * 6 + 6 * 1 + 7 * 8 + 8 * 4 + 9 * 2 + 1 * 1) % 11)

print((3 * 3 + 8 * 4 + 6 * 5 + 0 * 6 + 6 * 7 + 1 * 8 + 8 * 9 + 4 * 1 + 2 * 2 + 1 * 3) % 11)

# while True:
#     print('I can\'t stop')

# condition = True
# while condition:
#     print('Hello')
#     condition = False

# x = 0
# while x < 200:
#     print(x)
#     x += 1

# condition = True
# while condition:
#     user_input = input('Enter id')
#     if len(user_input) != 11:
#         print('Wrong number')
#     else:
#         condition = False
#         print(user_input)

# distance_to_target = input('Please enter distance in meters: ')
# current_position = 0
# step = 0.5
#
# cnt = 0
# while current_position < int(distance_to_target):
#     cnt += 1
#     current_position += step
#
# print('Done')
# print(f'{cnt} steps')

# if ((1 * 3 + 8 * 2 + 8 * 3 + 3 * 5 + 6 + 6 * 7 + 2* 9 + 7) % 11) == id[10]:
#     print(True)
# elif ((3 * 3 + 8 * 4 + 8 * 5 + 3 * 7 + 8 + 6 * 9 + 4 + 7 * 3) % 11) == id[10]:
#     print(True)