def search(f):
	"""return the smallest non-negtive integer x for which f(x) is a true value"""
	x = 0
	while True:
		if f(x):
			return x
		x += 1

def square(x):
	return x * x


def inverse(f):
	"""return a fucnftion g(y) that returns x such that f(x) == y.
	
	>>> sqrt = inverse(square)
	>>> sqrt(16)
	4
	"""
	def inverse_of_f(y):          
		def is_inverse_of_y(x):
			return f(x) == y
		return search(is_inverse_of_y)
	return inverse_of_f

	#return lambda y: search(lambda x: f(x) ==y)

print (inverse(square)(16))
#sqrt = inverse(square)
#print (sqrt(16))
