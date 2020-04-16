# helper function
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged

# helper function
def mergesort(array_items):
    if len(array_items) <= 1:
        return array_items

    mid_index = len(array_items) // 2
    left_items = array_items[:mid_index]
    right_items = array_items[mid_index:]

    left_items = mergesort(left_items)
    right_items = mergesort(right_items)

    return merge(left_items, right_items)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        return None

    if len(input_list) <= 1:
        return input_list

    merged_items = mergesort(input_list)
    
    first_list = []
    second_list = []

    for item in merged_items:
        if len(first_list) > len(second_list):
            second_list.append(str(item))
        else:
            first_list.append(str(item))
            
    first_sum = int(''.join(first_list))
    second_sum = int(''.join(second_list))
    
    list_of_max_sums = [first_sum, second_sum]
    
    return list_of_max_sums


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

###### Test Cases ######
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Edge Cases
print('Edge Cases:')
test_function([[], []])
test_function([[1,2,3], [32,1]])
test_function([[4,3,2], [43, 2]])