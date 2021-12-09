# numbers = [7, 1, 7, 9, 2, 9, 7, 3, 0]
# counter = []
#
# for num in range(10):
#     n = numbers.count(num)
#     counter.append(n)
#
# largest = max(counter)
# print((numbers), '→', (counter.index(largest)))

test_list = [1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8]
empty_dict = {}
for num in test_list:
    empty_dict[num] = test_list.count(num)

result_list = []
for x in empty_dict.keys():
    if empty_dict[x] == max(empty_dict.values()):
        result_list.append(x)

print(result_list)