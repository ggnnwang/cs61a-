
ok = 3

def my_func(x, y):
    return x,y,ok

a = my_func(3,4)
print(a)

#直接打印出了 ok = 3
#3, 4, 3)


print("下一个例子")

ok = 3

def my_func(x, y):
    c = ok + 3
    return x,y,ok,c

print(ok)
a = my_func(3,4)
print(a)

# 3
#(3, 4, 3, 6)




print("下一个例子")

ok = 3

def my_func(x, y):
    ok = x + y
    return x,y,ok

print(ok)
a = my_func(3,4)
print(a)

#打印出了 ok = 7， 因为return时候，@寻找name连接哪个object的过程@，寻找到的是最近的那个ok。parent的ok比较远。
# 离开f1之后，所以name消失。此时global frame的ok还是最上面的那个ok



print("下一个例子")

ok = 3

def my_func(x, y):
    ok = ok +1     
                    #重要！！！！！：在f1里面，所有创建的variable object（bind），都是只针对f1的。以后会消失。所以一旦要创建name object,一定是f1 local
                    #的，所以这里是两个ok都是local的。然后右边的local没有被initilized，所以出错。
    return x,y,ok
#
#To fix this, you have two options:
#1) Rather than reassigning [var] to its new value, create a new variable to hold that new value. 
# Use that new variable in future calculations.
#2) For this problem specifically, avoid this issue entirely by not using assignment statements at all. 
# Instead, pass new values in as arguments to a call to announce_highest.


a = my_func(3,4)
print(a)
