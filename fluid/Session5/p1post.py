import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('result1.csv')
x = np.arange(0,1.01, 0.01)
dt = 0.001
print(int(1/dt))
plt.figure(figsize=(8,6))
for i in range(0,int(1/dt)):
	plt.plot(x, df.iloc[i])

#plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
plt.title('Variation in temperature with time (dt={})'.format(dt))
plt.xlabel('x')
plt.ylabel('Temperature')
plt.savefig('figures/p11001n.png')

ana = np.zeros_like(x);

# At t = 0.2s
t = 0.2
for n in range(1,50):
	ana = ana + 4*(1-(-1)**n)/n**3 * np.exp(-n*n*np.pi*np.pi*t) * np.sin(n*np.pi*x)/(np.pi**3)
print(int(t/dt))
plt.figure(figsize=(8,6))
plt.plot(x, df.iloc[int(t/dt)], color='r', marker='o', label='FreeFEM')
plt.plot(x, ana, color='k', label='Analytical')
plt.plot(x, x-x**2, label='Initital Condition')
plt.legend()
plt.title('Comparision of Analytical Solution with FreeFEM solution (dt={})'.format(dt))
plt.xlabel('x')
plt.ylabel('Temperature')
plt.savefig('figures/p12001n.png')