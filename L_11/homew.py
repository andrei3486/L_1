import re
# #1
# pattern = re.compile(r'[#A-F|0-9]+[A-F|0-9]')
#
# #2
# pattern = re.compile(r'[0-9][^+]')
#
# #3
# pattern = re.compile(r'[0-2][0-9]:[0-5][0-9]')

#4
with open('people.txt', 'r', encoding='utf8') as file:
    file_content = file.read()
    # pattern = re.compile(r'[A-Z]+[a-z]+\s[A-Z]+[a-z]{3,}')
    pattern = re.compile(r'\d\d\d\s\D{2,}\d\d\d\d')
    matches = pattern.finditer(file_content)
    for match in matches:
        print(match)

#5
pattern = re.compile(r'[a-z][A_Z][0-9]')

#6
# pattern = re.compile(r'[1-8][0-9][0-9][0-1][0-9][0-3][0-9][0-9][0-9][0-9][0-9]')