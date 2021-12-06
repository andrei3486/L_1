numbers = [7, 1, 7, 9, 2, 9, 7, 3, 0]
counter = []

for num in range(10):
    n = numbers.count(num)
    counter.append(n)

largest = max(counter)
print((numbers), '→', (counter.index(largest)))