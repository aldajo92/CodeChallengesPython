def return_operator(value1, value2):
    if value1 > value2:
        return ">"
    elif value1 < value2:
        return "<"
    else:
        return "="


entries_size = input("Enter the number of entries\n")

list_values = []

for _ in range(int(entries_size)):
    values = input()
    list_values.append([int(x) for x in values.split(" ")])

for values in list_values:
    print(return_operator(values[0], values[1]))
