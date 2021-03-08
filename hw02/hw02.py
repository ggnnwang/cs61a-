from operator import sub, mul
HW_SOURCE_FILE = __file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    # def divide_number(x):
    #""" template """
    #assert x >= 0 and type(x) == int
    #remaining_parts, last = x // 10, x % 10
    # return (remaining_parts, last)
    #remaining_parts, last = divide_number(x)

    if x < 10 and x == 8:
        return 1
    elif x < 10 and x != 8:
        return 0
    else:
        return num_eights(x//10) + (1 if x % 10 == 8 else 0)
        # if x % 10 == 8:
        #    return num_eights(x // 10) + 1
        # else:
        #    return num_eights(x // 10) + 0


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    # if n <= 2:
    #     return n
    # else:
    #     if (n-1) % 8 == 0 or num_eights((n-1)) > 0:
    #         # pingpong(n-1) -  ( pingpong(n-1) - pingpong(n-2) )
    #         return pingpong(n-2)
    #     else:
    #         # pingpong(n-1) + ( pingpong(n-1) - pingpong(n-2) )
    #         return pingpong(n-1) * 2 - pingpong(n-2)

    def helper(index,ppn,direction):
        if index == n:
            return ppn
        if index % 8 == 0 or num_eights(index) > 0: 
            return helper (index+1,ppn-direction,-direction)
        else:
            return helper (index+1,ppn+direction,direction)
        
    return helper(1,1,1)

    #递归是不断往下找base case ，这道题开眼界啦，也可以把base case 往上找，终止条件是外层函数输入的n 。


    #both work
    # def helper(n):  # return direction, val
    #     if n == 1:
    #         return 1, 1
    #     return (lambda d, v: (-d, v + d) if num_eights(n) > 0 or n % 8 == 0 else (d, v + d))(*helper(n-1))
    # return helper(n)[1]


    # def helper(index, ppn, dir):
    #     if n == 1:
    #         return 1
    #     elif index != n:
    #         if num_eights(index) > 0 or index % 8 == 0:
    #             return helper(index+1, ppn-dir, -dir)
    #         else:
    #             return helper(index+1, ppn+dir, dir)
    #     else:
    #         return ppn
    # return helper(1, 1, 1)



def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    if n < 10:
        return 0
    else:
        if (n % 10)- ((n // 10) % 10) <= 1:
            return missing_digits(n // 10)
        else:
            return missing_digits(n // 10) + (n % 10) - ((n // 10) % 10) - 1


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
 
def next_smaller_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"

    # def max_num(x):
    #     if x <= 1:
    #         return 0        
    #     else:
    #         i = x
    #         while  not next_largest_coin(i):
    #             i = i - 1
    #         if next_largest_coin(i) > x:
    #             return i
    #         if next_largest_coin(i) <= x:
    #             return next_largest_coin(i)

    # def using_num(m , n):
    #     if m == 1 or m == 0:
    #         return 1
    #     elif m < 0:
    #         return 0
    #     elif n <= 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         with_max = using_num(m - max_num(n), max_num(n))
    #         without_max = using_num(m, max_num(n-1))
    #         return without_max + with_max
    # return using_num(total, max_num(total))
 

    def count_coins_exclude(total, excludes):
        """Return the number of ways using coins of value 
        excluding any coins >=  "excludes" from (1, 5, 10, 25)"""

        current_largest_coin = next_smaller_coin(excludes)

        if total <= 4 and total >= 0:
            return 1
        elif total < 0:
            return 0
        elif current_largest_coin == 1:
            return 1
        elif current_largest_coin == None:
            return 0
        else:
            return count_coins_exclude(total - current_largest_coin, excludes) + count_coins_exclude(total, current_largest_coin)

    def largest_func(total):
        if total >= 25:
            return 25
        elif total >= 10 and total < 25:
            return 10
        elif total >= 5 and total < 10:
            return 5
        elif total >= 1 and total <5:
            return 1

    largest_coin = largest_func(total)
    
    if total <= 4 and total >= 0:
        return 1
    elif total < 0:
        return 0
    elif largest_coin == 1:
        return 1
    elif largest_coin == None:
        return 0
    else:
        return count_coins(total - largest_coin) + count_coins_exclude(total, largest_coin)




            
            

 
    


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.
    should return a function that takes n


    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return  lambda n : (         (lambda f : f(n,f))   (lambda n, f : 1 if n == 1 else n * f(n-1,f))         )  

# https://youtu.be/WwHQS2_VH2Y?list=PL6BsET-8jgYWjZJMtCKJCdEBGUg2wZEgd&t=1006

# Write an expression that computes n factorial 
# using only call expressions, conditional expressions, and lambda expressions (no assignment or def statements). 
# Note in particular that you are not allowed to use make_anonymous_factorial in your return expression. 
# The sub and mul functions from the operator module are the only built-in functions required to solve this problem:



#python3 ok -q make_anonymous_factorial 