with open("trimushketera.txt", "r", encoding='UTF8') as file:
    file_content = len(file.read())
    lines = file.read().splitlines()
    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    a = ('total words: ', file_content)
    b = (f"Unique words: {len(uniques)}")
    print(a, b)