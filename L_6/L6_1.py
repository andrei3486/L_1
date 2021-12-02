# # def squares():
# #     x = 10             # обдпсть функцмм ограничена самой функцией
# #     print(x ** 2)
# #
# # squares()
# # print(x)
#
# # def squares():
# #     x = 10
# #     return x ** 2
#
# # def squares2():
# #     x = 10
# #     print(x **2)
# #
# # print(squares())
# # print(squares2())
# #
# # lst = []
# # lst.append('hello world')
#
# def squares(x):
#     return x ** 2
#
# def no_argument():
#     number = 25** 0.5
#     return number
#
# def sqrt(number):                # функция возведения в квадратный корень
#     return number ** 0.5
#
# def print_message(name, age, profession):
#     return print(f' Hi my name is {name}, I am {age} years old. I works as a {profession} ')
# # print_message('JAck', 25, "progger")
# #
# # emp_list = [('JAck s', 25, "progger"), ('Mary', 18, 'Teacher'), ('Bob', 30, 'Builder')]
# # for emploee in emp_list:
# #     print_message(emploee[0], emploee[1], emploee[2])
# #                                     # одно и то же
# # for name, age, profession in emp_list:
# #     print_message(name, age, profession)
#
# user_name, usere_age, user_prof = input('Enter name, age, prof: ').split(', ')
# print_message(user_name, usere_age, user_prof)
# # sample_string = "hello world planet"    # split делит до пробела ['hello', 'world', 'planet']
# # print(sample_string.split())
#
# # print(print_message('Jack', 25, 'Progger'))
# # y = 200
# # # print(squares(5))
# # # result = squares(5)
# # result = squares(y)
# # result2 = no_argument()
# # print(result)
# # print(result2)

# def double(x):
#     y = x * 2
#     # return f'Double from {x} is {y}'
#     return y
#
# def triple(x):
#     y = x * 3
#     # return f'Triple from{x} is {y}'
#     return double(y)
# number = 5
# print(triple(number))


# emp_list = ('jack', 'smith', 25, 2500, '555-555-5555', 'jack.smith@example.com')
# def print_message(emp_info):
#     return f'Hello {emp_info[0]} {emp_info[1]}. You are {emp_info[2]} years old. '


def fizz_buzz(start_num, end_num):
    for num in range(start_num, end_num):
        if num % 3 == 0 and num % 5 == 0:
            print(f'{num} FizzBuzz')
        elif num % 3 == 0:
            print(f'{num} Fizz')
        elif num % 5 == 0:
            print(f'{num} Buzz')

fizz_buzz(50, 1000 )