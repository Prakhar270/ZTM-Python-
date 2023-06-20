some_list = ['a', 'b', 'b', 'p', 'q', 'm', 'm', 'n']

duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)