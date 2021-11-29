# dictionary
# x = {} # пустой словарь
# print(type(x))
x = 5
sample_lst = {'one', 'teo', 'three'}
student = {'name': 'John', 'age': 30, 'courses': ['math', 'bio', 'art'], 1: 'int_key',
           0.2: 'float_key', x: 'variable', 'var_key': x, True: 'Hello world', False: 'Hello world'}

# print(student[1]) # идексировать можно только если есть цифры, не порядок
# print(student[x]) # переменная х также и 5
# print(student.get('job'))
# print(student.get('courses')[1])
# print(student['courses'].append('Hello world'))

# print(student.get('job', 'Empty')) # указать что вернуть если символа нет в словаре(empty)
# print(student['name'])
# student['age'] = 25 # изменение в словаре
# student['phone'] = '555-555-5555'
student.update({'name': 'Jack', 'age': 25, 'phone': '555-555-5555'}) #можно обновить несколько элементов в словаре

# del student['age'] # удаление из словаря , также del удаляет переменную из кода


# age = student.pop('age') # удляет только ключ(age), остаеться значение(25)
#
# print(student.keys()) # выводит только ключи dict_keys
# # print(list(student.keys()) # можно конвертировать и после этого индексировать
#
# print(student.values())
# print(student.items())
# print(list(student.items()))
