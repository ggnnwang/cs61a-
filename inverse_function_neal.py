def square(x):
	return x*x

def search(f,y):
	x=0
	while f(x) != y:
		x +=1
	return x

def inverse(f):

	def inverse_of_f(y): # 这个的作用是创建了一个叫inverse_of_f的object，只不过这个object比较特殊，有人call他的时候会返回值
		return search(f,y)  #中间多搞一层nested的是为了context里记住f
                            # 也可以inverse_of_f = lambda y: search(f,y) 创建了一个叫inverse_of_f的object
	return inverse_of_f

sqrt = inverse(square)
print(sqrt(16))