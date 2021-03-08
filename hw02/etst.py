def num_eights(x):
    if x < 10 and x == 8:
        return 1
    elif x < 10 and x != 8:
        return 0
    else:
        return num_eights(x//10) + (1 if x % 10 == 8 else 0)

def pingpong(n):
    if n <= 2:
        return n

    else:
        if (n-1) % 8 == 0 or num_eights((n-1)) > 0:
            return pingpong(n-2)   #pingpong(n-1) -  ( pingpong(n-1) - pingpong(n-2) )
        else:
            return pingpong(n-1) * 2 - pingpong(n-2)   #pingpong(n-1) + ( pingpong(n-1) - pingpong(n-2) )
            

a = pingpong(8)
print (a)