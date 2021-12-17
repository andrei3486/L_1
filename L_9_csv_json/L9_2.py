import csv

# with open('test.csv', 'r', encoding='utf8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     with open ('test_copy.csv', 'w', encoding='utf8') as csv_wfile:
#         csv_writer = csv.writer(csv_wfile, delimiter='-', lineterminator='\n')      # delimeter чем разделять #lineterminator перенос строки
#
#         for line in csv_reader:
#             csv_writer.writerow(line)
#
with open('test_copy.csv', 'r', encoding='utf8') as csv_file2:
    csv_reader = csv.reader(csv_file2)
    for line in csv_reader:
        print(line)
#     # next(csv_reader)   # пропуск первой строки
#     # # print(csv_reader)    #csv.reader object at 0x000001E2E3F2D420>
#     # for line in csv_reader:
#     #     # print(line)        #   ['Name', 'Date of birth', 'Town']
#     #     print(f'Hello {line[0]}. You are from {line[2]}. You were born on {line[1]}')
#
# # sample_list = [1, 2, 3, 4, 5, 6, 7]
# # sample_list = iter(sample_list)
# # # print(sample_list)   # <list_iterator object at 0x000001E2E3F43070>
# # print(next(sample_list))
# # next(sample_list)
# # print(next(sample_list))
#
# with open('test_copy.csv', 'r', encoding='utf8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         print(line)
#     #
#     # for line in csv_reader:         # {'Name-Date of birth-Town': 'John Black-16.03.1988-Tallinn'}
#     #     print(f'Hello {line['Name']}')
#     #
#     with open('test2.csv', 'w', encoding='utf8') as csv_wfile:
#         fieldnames = ['Name', 'DOB', 'Town']
#         csv_writer = csv.DictWriter(csv_wfile, fieldnames=fieldnames)
#         csv_writer.writeheader()
#
#         for line in csv_reader:
#             csv_writer.writerow(line)