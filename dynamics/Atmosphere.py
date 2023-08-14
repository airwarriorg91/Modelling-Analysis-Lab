import numpy as np

def atmParam(h, v):
    """
    Calculates the atomspheric parameters using the Standard Atmosphere Model.

    Input:
        1. h: height at which the atmospheric parameters are to be calculated. Range: [0,11km]
    Output:
        1. T: Temperature
        2. rho: Density
        3. nu: Kinematic Viscosity
        4. M : Mach number
        5. log(Re) : natural log of reynolds number
    """
    def Temp(h):
        T = -(6.5*h)/1000 + 288.19
        return T
    
    def Density(h):
        T = Temp(h)
        g0 = 9.81
        R = 287
        a = -0.0065
        k = g0/(a*R)
        rho = 1.225*(T/288.19)**(-(k+1))
        return rho
        
    def Viscosity(h):
        b = 1.458e-06
        c = 110.4
        T = Temp(h)
        rho = Density(h)
        mu = (b*(T**(1.5)))/(T+c)
        return mu/rho

    def Mach(h,v):
        R = 287
        Y = 1.4
        T = Temp(h)
        A = np.sqrt(R*Y*T)
        return v/A

    def logRe(h,v):
        nu = Viscosity(h)
        d = 0.155
        re = (v*d)/nu
        return np.log(re)

    def Cd(h, v):
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16 = 0.0000641, -0.0006166, -0.0075524, 0.1175224, -0.0009032, 0.0136069, 0.0086353, -1.0093621, 0.0041238, -0.0858483, 0.4289429, 1.5431515, -0.0064570, 0.1778755, -1.5559375, 4.0394577
        M = Mach(h,v)
        R = logRe(h,v)
        cd = (c1*R**3 + c2*R**2 + c3*R + c4)*M**3 + (c5*R**3 + c6*R**2 + c7*R + c8)*M**2 + (c9*R**3 + c10*R**2 + c11*R + c12)*M + (c13*R**3 + c14*R**2 + c15*R + c16)
        return cd
    return Temp(h), Density(h) , Viscosity(h), Mach(h,v), logRe(h,v), Cd(h,v)