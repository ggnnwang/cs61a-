class Student:
    haha = 1

    def __init__(self, name):
        self.name = name

    

class Student1(Student):

    def __init__(self,age):
        self.age = age



#理解 class attribute 和 instance attribute
>>> baozi.name
'baozi'
>>> baozi.haha
1
>>> Student.haha = 2
>>> baozi.haha
2
>>> baozi.haha = 5
>>> baozi.haha
5
>>> Student.haha
2
>>> Student1.haha
2
>>> neal = Student1(30)
>>> neal.age
30
>>> neal.haha
2
>>> neal.haha = 90
>>> neal.haha
90
>>> baozi.haha
5
>>> Student.haha
2
>>> Student1.haha
2


#甚至可以现场写入 不同的attributes
>>> baozi.wuwa = 3
>>> baozi.wuwa
3
>>> Student.ok = 3
>>> Student1.ok
3
>>> neal.ok
3
>>> Student.wuwa = 1
>>> baozi.wuwa
3
>>> neal.wuwa
1