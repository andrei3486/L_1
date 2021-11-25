# courses = ['Math', 'Physics', 'History', 'Progrm', "Liter"]
# numbers = [4, 5, 23, 1, 9, 84]
# print(courses)
# print(numbers)

# courses.append('Art') #добавление в конец списка
# print(courses)
#
# courses.insert(0, 'art') #вставляет на конкретну. позицию
# print(courses)

# courses2 = ['art', 'english'] # добавление нескольких элементов
# courses.extend(courses2)
# print(courses)

# courses.remove("Math") #удаляет конкретный элемент
# print(courses)

# courses.pop() # удаляет индекс Ю можно по номеру
# print(courses)
# a = courses.remove("Math") # remove удаляет навсегда
# b = courses.pop() # pop удаляет с сохранением
# print(a)
# print(b)
# print(courses)

# courses.reverse() # меняет наооборот
# print(courses)
# print(list(reversed(courses)))

# courses.sort() #сортирует в алфавит порядке unikod таблица знаки препинания, цифры , буквы
# courses.sort()
# print(courses)
# print(sorted(courses))

# print(min(numbers)) #мин и макс числа с буквами также по unikod
# print(max(numbers))
# print(sum(numbers)) # все сумирует

# print(courses.index('Math')) # индекс- номер в строке
# print(courses.index('History', 1)) #ограничивает поиск
# print('Math' in courses) # проверяет элемент в списке

# sample = 'Hello World'
# courses_str = '**'.join(courses) # сохранение с элементом в кавычках Math**Physics**History**Progrm**Liter
# print(courses_str)
# print(sample.split(' ')) #['Hello', 'World']

# a, b, c, d = 'Hello world world'.split(' ') ###
# print(a)
# print(b)
# print(c)
# print(d)
# new_list = courses + numbers
# print(new_list)
#
# courses2 = courses.copy()
# courses2[0] = 'Art'   # замена по индексам
# courses[3] = 'english'
# print(courses)
# print(courses2)

courses = ('Math', 'Math', 'Physics', 'History', 'Progrm', "Liter") # заменены скобки
numbers = (4, 5, 23, 1, 9, 84)
# print(courses.count('Liter'))
# tuple1 = tuple()
# tuple2 = ()
# print(type(tuple1))
# print(type(tuple2))
#
# lst = [1]
# print(type(lst))

# set1 = set()
# set2 = {}
# print(type(set1))
# print(type(set2))

# set1 = {1, 4, 2, 5, 5, 5, 5, 5}
# print(set1)

set1 = {'Art', 'English', "Biology", 'Physics'}
set2 = {'Prog', 'Biology', 'Art', 'Math'}
print(set2.intersection(set1))    #находит общее

print(set1.difference(set2)) # находит схожее и уникальное
print(set2.difference(set1))

print(set1.union(set2)) # удаляет дубликаты
set1.add('Russian')    #добавляет элемент
print(set1)

set1.update(set2) # обновляет одно в другое
print(set1)