import re
#
# text_to_search = '''
# abcdefghijklmnopqurtuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa HaHaH
# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )
# example.com
# example*com
# example@com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800-555-1234
# 900-555-1234
# Mr. Jones
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T
# abc
#
# ball mall hall wall tall
# '''
# sentence = 'Start a sentence and then bring it to an end Start'
#
# pattern = re.compile(r'M(rs|s|r)\.? [A-Z][a-z]*')
#
#
#
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
38606184214
'''

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+') # email

# pattern = re.compile(r'(https://|http://)?(www\.)?([\w-]+)(\.\w+)')   # URLS

#
matches = pattern.finditer(urls)
for match in matches:
    print(match)

# matches = pattern.finditer(urls)
# for match in matches:
#     print(match)
#     print(match.group(3) + match.group(4))   # <re.Match object; span=(1, 23), match='https://www.google.com'>
# subbed_urls = pattern.sub(r'\2\3\4', urls)  # www.google.com
# print(subbed_urls)

# pattern = re.compile(r'(\d)[^+]')