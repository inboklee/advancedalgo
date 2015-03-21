import math
import random

def random_in_place(L):
	n = len(L)
	for i in xrange(n):
		temp_index = int(random.random()*(n-i))+ i
		temp = L[temp_index]
		L[temp_index] = L[i]
		L[i] = temp
	
def secretary(L):
	n = len(L)
	temp = max(L) + 1
	for i in xrange(n):
		if (i < n / math.exp(1)):
			if (L[i] < temp):
				temp = L[i]
		else:
			if (L[i] < temp):
				return L[i]
	return -1
	
def compute_pi(n, r):
	occur = 0
	for i in xrange(n):
		x = int(random.random() * r)
		y = int(random.random() * r)
		if (x * x + y * y <= r * r):
			occur = occur + 1
	return 4.0 * occur / n
