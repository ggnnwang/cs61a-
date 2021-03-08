# #Tutorial: Write a function that takes a list s and returns a new list
# that keeps only the even-indexed elements of s and multiplies them by their
# corresponding index.

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [  s[i]*i for i in range(len(s)) if i % 2 ==0 ]

# Write a function that takes in a list and returns the maximum product that
# can be formed using nonconsecutive elements of the list. 
# The input list will contain only numbers greater than or equal to 1.

def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    >>> max_product([2,10,8,5,9,2,8]) 10* 9* 8  ; 2*8*9*8 = 1152 ;  10*5*2
    1152
    """
    if s ==[]:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        largest,i = 0,0
        for element in s:
            current = element * max_product(s[2+i:])
            i+=1
            if current > largest:
                largest = current
        return largest

#挨个拿出一个digit 然后做剩下的递归。然后比较挨个，取最大值
print(max_product([10,3,1,9,2]))
print(max_product([5,10,5,10,5]))
print(max_product([2,10,8,5,9,2,8]))