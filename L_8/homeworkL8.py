# with open('trimushketera.txt', 'r', encoding='UTF8') as file:
#     file_content = len(file.read())
#
#     print('total words: ', file_content)
#
# with open("trimushketera.txt", "r", encoding='UTF8') as file:
#     lines = file.read().splitlines()
#     uniques = set()
#     for line in lines:
#         uniques |= set(line.split())
#
#     print(f"Unique words: {len(uniques)}")

with open('trimushketera.txt', 'r', encoding='UTF8') as file:
    data = file.read()
    symbols = ['.', ',', '!', '?', '(', ')', ':', '"']
    for sym in symbols:
        data = data.replace(sym, '')
    data = data.lower()
    word_list = data.split()
    unique_word_list = list(set(word_list))
    with open('trimushketera_copy.txt', 'w', encoding='utf8') as wfile:
        wfile.write(f'There are {len(word_list)} words in {file.name}.\n')
        wfile.write(f'There are {len(unique_word_list)} unique words in {file.name}.\n')
        for word in sorted (unique_word_list):
            if word.isalpha() == True:
                wfile.write(word + '\n')