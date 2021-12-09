with open('trimushketera.txt', 'r', encoding='UTF8') as file:
    file_content = len(file.read())

    print('total words: ', file_content)

with open("trimushketera.txt", "r", encoding='UTF8') as file:
    lines = file.read().splitlines()
    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")