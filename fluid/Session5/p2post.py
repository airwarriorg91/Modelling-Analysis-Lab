import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('result2.csv')
x = np.arange(0,2.01, 0.01)
dt = 0.001
print(int(1/dt))
plt.figure(figsize=(8,6))
for i in range(0,int(1/dt),200):
	plt.plot(x, df.iloc[i], label=str(i*dt)+"s")

plt.legend(loc='upper right')
plt.title('Variation in temperature with time (dt={})'.format(dt))
plt.xlabel('x')
plt.ylabel('Temperature')
plt.savefig('figures/p21.png')

ana = np.zeros_like(x);

# At t = 0.2s
t = 0.2
for n in range(1,50):
	ana = ana + (32/(np.pi**2))*(np.sin((2*n-1)*np.pi/4)*(1-np.cos((2*n-1)*np.pi/4))*np.sin((2*n-1)*np.pi*x/4)*np.exp((-t/16)*(np.pi**2)*(2*n-1)**2))/((2*n-1)**2)
print(int(t/dt))
plt.figure(figsize=(8,6))
plt.plot(x, df.iloc[int(t/dt)], color='r', marker='o', label='FreeFEM')
plt.plot(x, ana, color='k', label='Analytical')
plt.plot([0, 1, 2], [0,1,0], label='Initital Condition')
plt.legend()
plt.title('Comparision of Analytical Solution with FreeFEM solution (dt={})'.format(dt))
plt.xlabel('x')
plt.ylabel('Temperature')
plt.savefig('figures/p22.png')