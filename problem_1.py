def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None
    if number == 0 or number == 1:
        return number
    start_num = 1
    end_num = number
    while start_num <= end_num:
        mid_num = (start_num + end_num) // 2
        mid_num_sqr = mid_num ** 2
        
        if mid_num_sqr == number:
            return mid_num
        elif mid_num_sqr < number:
            start_num = mid_num + 1
            sqrt_num = mid_num
        else:
            end_num = mid_num - 1
    return sqrt_num


###### TEST CASES ######

# General Cases
print('General Cases:')
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge cases
print('Edge Cases:')
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (77665 == sqrt(6031852225)) else "Fail")