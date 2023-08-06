import numpy as np

def EulerMethod(y0,t0,tf,h,yprime, n=1):
    '''
    Implementation of Euler's Method in python to solve ODE.

    Inputs:
        1. y0: Initial value of function y.
        2. t0: Initial value of time
        3. tf: Final value of time
        4. h: time-step
        5. yprime: Derivative function of the y
        6. n: dimension of the y vector

    Outputs:
        1. y: approximate solution of the ODE using euler method
        2. t: time vector
    '''

    l = int((tf-t0)/h)
    t=np.reshape(np.arange(t0,tf,h), (l,-1))
    shape = (np.size(t),n)
    y = np.zeros(shape)
    y[0] = y0
    for i in range(0, np.size(t)-1):
        #print(yprime(t[i],y[i]))
        y[i + 1] = y[i] + h*yprime(t[i],y[i])

    return y, t

def RK4Method(y0,t0,tf,h,yprime, n=1):
    '''
    Implementation of Runge-Kutta 4 Method in python to solve ODE.

    Inputs:
        1. y0: Initial value of function y.
        2. t0: Initial value of time
        3. tf: Final value of time
        4. h: time-step
        5. yprime: Derivative function of the y
        6. n: dimension of the y vector

    Outputs:
        1. y: approximate solution of the ODE using euler method
        2. t: time vector
    '''
    l = int((tf-t0)/h)
    t=np.reshape(np.arange(t0,tf,h), (l,-1))
    shape = (np.size(t),n)
    y = np.zeros(shape)
    y[0] = y0
    for i in range(0, np.size(t)-1):
        k1 = yprime(t[i],y[i])
        k2 = yprime(t[i]+0.5*h, y[i]+k1*0.5*h)
        k3 = yprime(t[i]+0.5*h, y[i]+k2*0.5*h)
        k4 = yprime(t[i]+h, y[i]+k3*h)        
        y[i + 1] = y[i] + h*(k1+2*k2+2*k3+k4)/6

    return y, t