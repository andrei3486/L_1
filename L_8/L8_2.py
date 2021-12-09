# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r' - read and write

# file = open('text.txt', 'r', encoding='UTF8')  # если в той же пвпке
# print(file.encoding)  #UTF8
# print(file.name)   # text.txt
# print(file.mode)    # 'r'
# print(file.closed)   # False  файл открыт
# file.close()
# print(file.closed)   # true файл закрыт

# with open('text.txt', 'r', encoding='UTF8') as file:    #print(rfile.closed)  # False файл открыт with автоматический управляет времеено файл не нужно закрывать
    # file_content = file.read()         # выводит файд целиком   str
    # print(file_content)
    # print(type(file_content))

    # file_content = file.readline() # любой текст до переноса строки
    # print(file_content)

    # file_content = file.readlines()
    # print(file_content)
    # print(type(file_content))


    # for line in file:
    #     print(line)

    # size_to_read = 500
    # file_content = file.read(size_to_read)
    # while len(file_content) > 0:
    #     print(file_content, end='')
    #     print(f'\n{len(file_content)}')
    #     file_content = file.read(size_to_read)

# with open('test_text.txt', 'w', encoding='UTF8') as wfile:  #  'w' создание файла и перезапись существующего
#     wfile.write('TEST')
#

# with open('test_text.txt', 'x', encoding='UTF8') as wfile:  # 'x' создание файла не перезаписывет существующий
#     wfile.write('TEST')

# with open('test_text.txt', 'w', encoding='UTF8') as wfile:
#     wfile.write('TEST3')
#     wfile.seek(2)
#     wfile.write('test2')
#
# with open('text.txt', 'r') as file:
#     data1 = file.read()
#     print(data1)
#     print()
#     file.seek(0)
#     data2 = file.read()
#     print(data2)

# with open('python.jpg', 'rb') as file:
#     with open('python_copy,jpg', 'wb') as wfile:
#         chunk_size = 4096
#         file_content = file.read(chunk_size)     # сохранение части картинки
#         cnt = 0
#         while cnt < :
#             wfile.write(file_content)
#             file_content = file.read(chunk_size)
#             cnt += 1


# with open('python_copy.jpg', 'wb') as wfile: # пересохранение
#     wfile.write(file_content)