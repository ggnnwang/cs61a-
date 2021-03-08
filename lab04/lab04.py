LAB_SOURCE_FILE = __file__



this_file = __file__

def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    #Write a function skip_add that takes a single argument n and computes the sum of every other integer between 0 and n. Assume n is non-negative.

    "*** YOUR CODE HERE ***"

    if n <= 0:
        return 0
    else:
        return n + skip_add(n-2)


def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(1)
    else:
        return summation(n-1,term) + term(n)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"

#Consider an insect in an M by N grid. The insect starts at the bottom left corner, (0, 0), and wants to end up at the top right corner, (M-1, N-1). 
# The insect is only capable of moving right or up. 
# Write a function paths that takes a grid length and width and returns the number of different paths the insect can take from the start to the goal.
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m-1,n) + paths(m,n-1)


def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    if n//(10 ** t) == 0:
        return n
    elif t == 1:
        return int(max([digstr for digstr in str(n)]))
    else:
        max_less1digit = max_subseq(n//10, t-1)
        last_digit = max_subseq(n % (10**(len(str(n))-1)),t-1) % 10
        return max_less1digit * 10 + last_digit



    # if n//(10 ** t) == 0:
    #     return n
    # elif t == 1:
    #     return int(max([digstr for digstr in str(n)]))
    # else:
    #     list = []
    #     n_string = str(n)
    #     for digits in n_string:
    #         list = list + [digits + str(max_subseq(int(n_string[1:]),t-1))]
    #     return int(max(list))

#应该是取一个digit，然后对后面的digit作t-1的recursion
# 然后全部digit都这样搞一遍返回最大值
#9+f(586524,t-1),  5+f(86524,t-1), 这里面求最大值



# 我的思路是。。假如求 #     9586524  t=4   要得到的结果是 9865
# 那我就求 958652  t=3 ，得到986
# 以及 586524  t=3  得到，865
# 然后就是986 * 10 + （865的个位数）。 就是9865 。 感觉好蠢哦qwq

    #You need to split into the cases where the ones digit is used and the one where it is not. 
    #In the case where it is, we want to reduce t since we used one of the digits, and in the case where it isn't we do not.
    #In the case where we are using the ones digit, you need to put the digit back onto the end, and the way to attach a digit d to the end of a number n is 10 * n + d.


# 也可以用monotone stack来解
# 如果新放进去的数字，比数组里最后一个数字大
# 就删掉数组里的最后一个数字
# 最多删掉n-t个数字


#叫回溯法
#对每个数字
#用了这个数字就t-1的递归，没用就t的递归
#然后下一个数字
#f(x,t)=max (s[x]+10*f(x+1,t-1), f(x+1,t))

#f(x,t)= s[x]+10*f(x+1,t-1), f(x+1,t)





def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")   #("coy", "cacophony")# 对齐。 #("fin", "effusion")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    "*** YOUR CODE HERE ***"


    if w2 == "":
        return ""

    digw1 = w1[:1]  #即使digw1是""，也不会出错。保证可以取到第一个字符  better than w1[0]
    digw2 = w2[:1]

    if digw1 != digw2:
        return digw2 + add_chars(w1[0:], w2[1:])
    elif digw1 == digw2:
        return add_chars(w1[1:], w2[1:])
    

#w1 want ; t      ""
#w2 wanton ; ton "on"

# oy acophony
# a+  oy cophony

# a+ c+   oy ophony
# a+c+  y + phony
# a+c+ p ; y + hony
# a+c+ p+h ; y + ony
# a+c+ p+h o n ; y + y



def count_equal(k): #k=9
    """ k == n """
    result = 0
    for i in range(k):
        result = result + combination(k-1,i)
    return result



def combination(n,m): #n>m
    """ """
    return fact(n) // (fact(n-m) * fact(m))

    # n 9  m 2; 
    # comb ()


def fact(n):
    """ """
    if n == 0:
        return 1
    elif n<0 or type(n) != int:
        return None
    else:
        return fact(n-1) * n



def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """

#Consider a special version of the count_stairways problem,
#where instead of taking 1 or 2 steps, we are able to take up to and including
#k steps at a time.
#Write a function count_k that figures out the number of paths for this scenario. Assume n and k are positive
# solution https://www.youtube.com/watch?v=oGBcPguM9vo&list=PLx38hZJ5RLZd35oDi3TGz5p9DyyxU3WwA&index=5


    if n == 0:
        return 1
    elif n<0:
        return 0 
    else:
        i = 1
        result = 0
        while i<=k:
            result += count_k(n-i,k)
            i+=1
        return result

