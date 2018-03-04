import numpy as np
import random


class oper(object):
	def __init__(self,a,op):
		self.a = a
		self.op = op

		if op == 0:
			self.b = random.randint(10,80)
			self.res = oper.sum(a,self.b)
			self.symb = "+"
		elif op == 1:
			self.b = random.randint(2,a)
			self.res = oper.diff(a,self.b)
			self.symb = "-"
		elif op == 2:
			self.b = random.randint(2,10)
			self.res = oper.mult(a,self.b)
			self.symb = "x"
		else:
			self.b = random.choice(list(list_divisors(a)))
			self.res = oper.div(a,self.b)
			self.symb = "/"

	def sum(a,b):
		return int(a + b)

	def diff(a,b):
		return int(a - b)

	def mult(a,b):
		return int(a * b)

	def div(a,b):
		return int(a / b)

def list_divisors(n):
	divisors = []
	for i in range(2,int(np.sqrt(n) + 1)):
		if n % i == 0:
			yield i
			if i*i != n:
				divisors.append(n / i)
	for div in reversed(divisors):
		yield int(div)

def check(a):
	if a > 180:
		return False
	elif a < 3:
		return False
	elif not isinstance(a,int):
		return False
	else:
		return True

def check_div(a):
	if len(list(list_divisors(a))) == 0:
		return False
	else:
		return True
