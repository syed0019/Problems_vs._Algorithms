def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args:
    ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    
    min_int = ints[0]
    max_int = ints[0]
    for integer in ints:
        if integer > max_int:
            max_int = integer
        if integer < min_int:
            min_int = integer

    return (min_int, max_int)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# other test cases
print(get_min_max([3]))
# prints (3, 3)
print(get_min_max([8, 12, 10, 3, 7, 1]))
# prints (1, 12)
print(get_min_max([2, 90, 21, 8, 6]))
# prints (2, 90)
print(get_min_max([12, 8, 9, 6, 0,  2, 20, 4, 4, 1, 22, 5]))
# prints (0, 22)
print(get_min_max([]))
# prints (None)