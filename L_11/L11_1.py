import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
example*com
example@com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc

ball mall hall wall tall
'''
sentence = 'Start a sentence and then bring it to an end Start'

# print('\tTab')  # Tab
# print(r'\tTab')  # r сырая строка \tTab

pattern = re.compile(r'\bStart')



matches = pattern.finditer(sentence)
for match in matches:
    print(match)
    # print(text_to_search[match.start():match.end()])
    # print(match.start())
    # print(match.end())
    # print(match.group())
    #
