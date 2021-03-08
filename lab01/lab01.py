def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    
    product = 1

    if k == 0:
        return product

    while k != 0:
        product = product * n
        n= n- 1
        k= k -1
    return product

        





def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"

    sum = 0
    while y !=0:
        digit_value = y % 10 
        sum = sum + digit_value
        y = y // 10
    return sum
    

def get_dig_value(n,k):
    """get the value of digit k from number n
    >>> get_dig_value(543,1)
    3
    >>> get_dig_value(543,2)
    4
    >>> get_dig_value(543,3)
    5
    >>> get_dig_value(543,0)
    >>> get_dig_value(543,4)
    >>> get_dig_value(55843,3)
    8
    """
    if k <= len(str(n)) and k >= 1:
        n = n % (10 ** k)
        dig_value = n // (10 **(k-1))
    else: 
        return None

    return dig_value




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"

    dig1 = 1
    dig2 = 2

    while (get_dig_value(n,dig1) != None) and (get_dig_value(n,dig2) !=None):
        if get_dig_value(n,dig1) ==8 and get_dig_value(n,dig2) ==8:
            return True
        dig1 += 1
        dig2 += 1
    return False
    

def double_eights_ver1(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"

    dig1 = 1
    dig2 = 2
    
    while get_dig_value(n,dig1) !=8 or get_dig_value(n,dig2) !=8:
        if get_dig_value(n,dig1) ==None or get_dig_value(n,dig2) ==None:
            return False
        dig1 += 1
        dig2 += 1
    return True


