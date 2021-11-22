string_sample1 = "hello world world"
string_sample2 = 'first letteR is loWErcase'
string_sample3 = ' extral whitespace string '
string_sample4 = 'der Fluß'
simple_string = 'hello'
              # '01234'
               # '-5-4-3-2-1'

# print(len(string_sample1))
# print(len('243535353'))

#[start_index:stop_index:step]

# print(string_sample1[1:10])
# print(string_sample1[:10])
# print(string_sample1[:])
# print(string_sample1[1:10:2])
# print(string_sample1[::2])
# print(string_sample1[-1])
# print(string_sample1[-5:-1])
# print(string_sample1[-5:])
#
# sliced_string = string_sample1[6:11]
# print(sliced_string)

# print('hello world'[2:10])

# print('world' in string_sample1)   #true
# print('World' in string_sample1) #false

# print(string_sample1.upper()) #big letters
# print(string_sample1)
# string_sample1 = string_sample1.upper()
# print(string_sample4.lower()) # der fluß
# print(string_sample4.casefold()) # der fluss

# print(string_sample2.capitalize()) # 1 capital big ,all another small
# user_input = input('Please ener your name')
# print(user_input.capitalize())

string_sample3 = ' extral whitespace string '

# print(string_sample3.strip())  #обрезает по краям пробелы
# print(string_sample3.strip(' e'))# удяляет пробел и букву е
# print(string_sample3.strip('est'))
# print(string_sample3.lstrip()) # l-left r-right
# print(string_sample3.lstrip().rstrip())

string_sample1 = "hello world world"

# print(string_sample1.replace('world', 'planet')) #замена слова
# print(string_sample1.replace('world', 'planet', 1)) # замена количества слов
# print(string_sample1.replace(' ','')
# print(string_sample1.split())  #['hello', 'world', 'world']

# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)
# a, b, c = string_sample1.split()

# print(string_sample1.count('w')) # считает количество символов
# print(string_sample1.count('o', 5, 10))
print(string_sample1.find('world')) #поиск слова один раз индекс слова (цифра)
print(string_sample1[6:11])
print(string_sample1[string_sample1.find('world'):])
print(string_sample1.rfind('world')) #ищет с права
