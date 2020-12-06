class FuncionesMatematicas:
	"""Math Functions Class"""

	def average(self, a, b):
		"""Average between two numbers"""
		return (a + b) / 2
	
	def max(self, a):
		"""Max value from list"""
		if a:
			max = a[0]
			for num in a:
				if num > max:
					max = num
			return max
		else:
			return a
	
	def min(self, a):
		"""Min value from list"""
		if a:
			min = a[0]
			for num in a:
				if num < min:
					min = num
			return min
		else:
			return a
	
	def repeated(self, a):
		"""Show repeated values in list"""
		return sorted(set([num for num in a if a.count(num) > 1]))
	
	def unique(self, a):
		"""Show unique values in list"""
		return sorted(set([num for num in a if a.count(num) == 1]))
	
	def fibo(self, a):
		"""Calculate Fibonacci Sucession from a given quantity of digits"""
		if a == 0:
			return 0
		elif a == 1:
			return 1
		else:
			return self.fibo(a - 1) + self.fibo(a - 2)
			
#Tests

function = FuncionesMatematicas()

print(function.average(3, 1)) #2.0
print(function.max([1, 2, 3])) #3
print(function.min([3, 1, 2])) #1
print(function.repeated([1, 1, 1])) #[1]
print(function.unique([1, 1, 1])) #[]
print(function.fibo(7))
