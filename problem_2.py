def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_search_recursive(input_list, number, 0, len(input_list) - 1)

def rotated_search_recursive(array, target, start_index, end_index):
    
    if start_index > end_index:
        return -1
        
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
        
    if target == mid_element:             
        return mid_index
        
    left_search_array = rotated_search_recursive(array, target, start_index, mid_index - 1)
    right_search_array = rotated_search_recursive(array, target, mid_index + 1, end_index)
    
    max_value = max(left_search_array, right_search_array)
    
    return max_value
    
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

##### Test Cases #####
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# edge cases #
print('Edge Cases:')
test_function([[1], 0])
test_function([[], -1])
test_function([[4,5,2], -1])
test_function([[1,2,3,4,5,6,7,8], 5])