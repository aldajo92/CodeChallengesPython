def binary_search(array, target):
    return binary_search_recursive(array, target, 0, len(array) - 1)


def binary_search_recursive(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        binary_search_recursive(array, target, start_index, mid_index - 1)
    else:
        binary_search_recursive(array, target, start_index + 1, mid_index)


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)
