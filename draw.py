import random
from math import *
from decimal import *
import numpy as np
import matplotlib.pyplot as plt
# print(getcontext())


n = 1000	 # Number of vertices

ratio = 0.99  # Precision of Estimation

c = (4 - 2 * sqrt(3)) / 3

def f1(x):
	return 1 - exp(- x - x ** 2 / 2 - c * x ** 3)

def f2(x):
	return min(x, 1)

def get_prob(mu, n):
	# Given the number of vertices and mu,
	# compute the probability that vertex i has a type t_i
	x = 1 - mu
	x = log(x)
	x /= n
	x = exp(x)
	prob = 1 - x
	return prob

def calc(mu, type):
	# Estimate E[g(y)] given mu

	# When type = 0, we are considering about integral matching
	# When type = 1, we are computing the worst ratio of fractional matching
	print(mu)
	if mu > 1:
		print("mu TOO Large")
		exit(0)

	T = int(floor((1 / (1 - ratio)) ** 2 / mu * 10))

	# Choose T so that w.h.p. 
	# the ratio has a multiplicative error of at most 1 - ratio

	if mu == 1:
		p = 0.01
	else:
		p = get_prob(mu, n)


	pw = [(1 - p) ** i for i in range(n + 1)]


	sumy = 0
	sumgy = 0

	for x in range(T):
		cury = 0
		for i in range(1, n + 1):
			if random.random() < p:
				# Vertex i is "active"
				
				# The value of the estimator is exactly (1 - p)^{i - 1}
				Estimator = pw[i - 1]

				sumy += Estimator
				cury += Estimator

		# Till now, we draw an sample of y
		if type == 0:
			sumgy += f1(cury)
		else:
			sumgy += f2(cury)

	# print(sumy / T)
	return sumgy / T / mu

K = 100 
x = [float(i) / K for i in range(1, K + 1)]

print("===== Start To Calculate the Ratio of Integral Matching =====")
y = [calc(x[i], 0) for i in range(K)]

print("===== Start To Calculate the Ratio of Fractional Matching =====")
z = [calc(x[i], 1) for i in range(K)]

print(x)
print(y)
print(z)

plt.plot(x, z, linewidth = 2.8,  label = "Fractional Matching")
plt.plot(x, y, linewidth = 2.8,  label = 'Rounding with OCS')

plt.xlabel('E[y]')
plt.ylabel('Competitive Ratio')
plt.legend(loc = "best")

my_x_ticks = np.arange(0.6, 1.01, 0.04)
plt.yticks(my_x_ticks)
plt.grid(axis = 'y', which = "major")
# plt.ylim(0, 1)
# plt.xlim(0, 1)


plt.show()