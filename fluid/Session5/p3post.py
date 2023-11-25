import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('result3.csv')
x = np.arange(0,3.01, 0.01)
dt = 0.001
print(int(2/dt))
plt.figure(figsize=(8,6))
for i in range(0,int(2/dt), 200):
	plt.plot(x, df.iloc[i], label=str(i*dt)+'s')

plt.legend(loc='upper right')
plt.title('Variation in temperature with time (dt={})'.format(dt))
plt.xlabel('x')
plt.ylabel('Temperature')
plt.savefig('figures/p31.png')

error = np.zeros((x.size, 10))

for i in range(10):
	ana = x;
	t = 0.2*i
	for n in range(1,100):
		ana = ana + 32*(1-(-1)**n)/n**3 * np.exp(-n*n*np.pi*np.pi*t/9) * np.sin(n*np.pi*x/3)/(np.pi**3)
	print(int(t/dt))
	plt.figure(figsize=(8,6))
	plt.plot(x, df.iloc[int(t/dt)], color='r', marker='o', label='FreeFEM')
	plt.plot(x, ana, color='k', label='Analytical')
	plt.plot(x, 4*x-x**2, label='Initital Condition')
	plt.legend()
	plt.title('Comparision of Analytical Solution with FreeFEM solution (t={} and dt={})'.format(t,dt))
	plt.xlabel('x')
	plt.ylabel('Temperature')
	plt.savefig('figures/p32{}.png'.format(i))
	error[:,i] = np.abs(df.iloc[int(t/dt)]-ana)

plt.figure(figsize=(8,6))
for i in range(10):
	t = 0.2*i
	plt.plot(x, error[:,i], label=str(np.round(t,1))+'s')
plt.legend()
plt.xlabel('x')
plt.title('Variation of error in FreeFEM Solution as compared to analytical solution with time')
plt.ylabel('Error')
plt.savefig('figures/p3error.png')