def combo(a, b):
    """Return the smallest integer with all of the digits of a and b (in order).
    >>> combo(531, 432)
    45312
    >>> combo(531, 4321)
    45321
    >>> combo(1234, 9123)
    91234
    >>> combo(0, 321)
    321
    # 45312 contains both _531_ and 4_3_2.
    # 45321 contains both _53_1 and 4_321.
    # 91234 contains both _1234 and 9123_.
    # The number 0 has no digits, so 0 is not in the result.
    """

#Implement combo, which takes two non-negative integers a and b. It returns the smallest integer that
#contains all of the digits of a in order, as well as all of the digits of b in order

    if a == 0 or b == 0:
        return a + b

    if a % 10 == b % 10:
        return combo(a//10, b//10) * 10 + a % 10

    combo_result1 = (combo(a//10, b) * 10 + a % 10)
    combo_result2 = (combo(a, b//10) * 10 + b % 10) 
    
    return min(combo_result1, combo_result2)



#     elif ___________________________________________________________________________________:
#         return combo(___________________, __________________)_______________________________
        
#     return ________(________________________________________________________________________,
#                     ________________________________________________________________________)

 
# 什么时候用9 , (a % 100) ,39 或 (b % 10 * 10 + a % 10) 29 是最小的;   min( (a % 100)  ,  (b % 10 * 10 + a % 10) )
# 什么时候用2  92(b % 100)  或 32 是最小的 (a % 10 * 10 + b % 10)    min(   ,    )

# # 539 432
# # 45329

# 什么时候用9 , (a % 100) ,39 或 (b % 10 * 10 + a % 10) 29 是最小的;   min( (a % 100)  ,  (b % 10 * 10 + a % 10) ) #elif 最小
# 什么时候用2  92(b % 100)  或 32 是最小的 (a % 10 * 10 + b % 10)    min(  (b % 100)  ,  (a % 10 * 10 + b % 10)  )

    # if a == 0 or b == 0:
    #     return a + b

    # elif min( (a % 100)  ,  (b % 10 * 10 + a % 10) ) <= min(  (b % 100)  ,  (a % 10 * 10 + b % 10)  ):
    #     return combo( a //10 , b) * 10 + a % 10

    # return combo (________________________________________________________________________,
    #                 ________________________________________________________________________)
