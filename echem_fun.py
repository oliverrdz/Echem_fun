'''
Electrochemistry functions
It requires numpy installed

Units of the parameters:
F [C/mol]
D [cm2/s]
C [mol/cm3]
a [cm]
i [A]
'''
import numpy as np

F = 96485 # C/mol

def ilim_disc(n=1, D=1e-5, C=1e-6, a=12.5e-4):
    ilim = 4*n*F*D*C*a
    return ilim

def shoup_Szabo(t, n=1, D=1e-5, C=1e-6, a=12.5e-4):
    tau = D*t/a**2
    iNorm = 0.7854 + 0.4431/np.sqrt(tau) + 0.2146*np.exp(-0.3911/np.sqrt(tau))
    i = 4*n*F*D*C*a
    return i

def mahon_Oldham(t, n=1, D=1e-5, C=1e-6, a=12.5e-4):
    s = D*t/a**2
    f1 = 1/np.sqrt(np.pi*s) + 1 + np.sqrt(s/(4*np.pi)) - 3*s/25 + 3*s**(3/2)/226
    f2 = 4/np.pi + 8/np.sqrt(s*np.pi**5) + 25/(2792*s**(3/2)) - 1/(3880*s**(5/2)) - 1/(4500*s**(7/2))
    # Fancy if statement using boolean algebra:
    iNorm = (s<1.281)*f1 + (s>=1.281)*f2
    i = np.pi*n*F*D*C*a*iNorm
    return i


