salary = 1000
# text = 'Johns salary is {}' # 1 sposob
# text = 'Johns salary is {2}, {0}, some text{1}'

# print(text.format(salary)) # конвертирует фигурные скопки 2 sposob
# print(text.format(salary, True , 123.23))

# price_string = "This {product:} costs {price:} eur"  # 3 sposob
# price_string = "This {product:} costs {price:1f} eur" # tsifra f
# print(price_string.format(product='Computer', price=1000))

a = 1000
b = 'john'
c = 2021
d = 1988
print(f'Hi, my name is {b.capitalize()}. I am {c-d} years old . My salary is {a} eur.')  #лучший способ(в начале f)
t = "hello\nworld'" #перенос строки \n
print(t)
r = 'that\'s' # \ знак сохранения кавычки
print(r)
# """ тройные кавычки перенос текста