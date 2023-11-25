import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('result4.csv')
x = np.arange(0,1.01, 0.01)
dt = 0.01
print(int(1/dt))
plt.figure(figsize=(8,6))
for i in range(0,int(1/dt),20):
	plt.plot(x, df.iloc[i], label=str(i*dt)+"s")

plt.legend(loc='upper right')
plt.title('Variation in temperature with time (dt={})'.format(dt))
plt.xlabel('x')
plt.ylabel('Temperature')
plt.savefig('figures/p41.png')

# At t = 0.2s
t = 0.2
ana = 0.5*(x**2 + 2*t) - x + 1/3;
for n in range(1,50):
	ana = ana - 2*np.exp(-n*n*np.pi*np.pi*t)*np.cos(n*np.pi*x)/np.pi**2
print(int(t/dt))
plt.figure(figsize=(8,6))
plt.plot(x, df.iloc[int(t/dt)], color='r', marker='o', label='FreeFEM')
plt.plot(x, ana, color='k', label='Analytical')
plt.plot(x, np.zeros_like(x), label='Initital Condition')
plt.legend()
plt.title('Comparision of Analytical Solution with FreeFEM solution (dt={})'.format(dt))
plt.xlabel('x')
plt.ylabel('Temperature')
plt.savefig('figures/p42.png')