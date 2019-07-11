def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (end_index - start_index) // 2

        mid_element = array[mid_index]

        if mid_element == target:
            return mid_index

        elif target < mid_element:
            end_index = mid_element - 1
        else:
            start_index = mid_element + 1

    return -1


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)
