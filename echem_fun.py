'''
Electrochemistry functions
It requires numpy installed
All the functions have default parameters

Units of the parameters:
F [C/mol]
D [cm2/s]
C [mol/cm3]
a [cm]
i [A]
'''
import numpy as np

F = 96485 # C/mol
R = 8.3145 # J/molK
T = 298 # K

def ilim_disc(n=1, D=1e-5, C=1e-6, a=12.5e-4):
'''
    Returns the limiting current in A of a microdisc with a=10 um and default parameters:

    from echem_fun import *
    ilim = ilim_disc(a=10e-4)
'''
    ilim = 4*n*F*D*C*a
    return ilim

def shoup_Szabo(t, n=1, D=1e-5, C=1e-6, a=10e-4):
'''
    Returns the current of a microdisc electrode of a=10 um according to the Shoup and Szabo equation. It also accepts numpy arrays for the time.
    Chronoamperometric current at finite disk electrodes
    Shoup and Szabo, Journal of Electroanalytical Chemistry, 1982, 140, 237-245

    from echem_fun import *
    t = 1 # [s], time to calculate the current
    i = shoup_Szabo(t, a=10e-4)
'''
    tau = D*t/a**2
    iNorm = 0.7854 + 0.4431/np.sqrt(tau) + 0.2146*np.exp(-0.3911/np.sqrt(tau))
    i = 4*n*F*D*C*a
    return i

def mahon_Oldham(t, n=1, D=1e-5, C=1e-6, a=10e-4):
'''
    Returns the current of a microdisc electrode of a=10 um according to the Mahon and Oldham equaiton. It also accepts numpy arrays for the time.
    Diffusion-controlled chronoamperometry at a disk electrode
    Mahon and Oldham, Analytical Chemistry, 2005, 77, 6100-6101

    from echem_fun import *
    t = 1 # [s], time to calculate the current
    i = mahon_Oldham(t, a=10e-4)
'''

    # Written for a reduction
    s = D*t/a**2
    f1 = 1/np.sqrt(np.pi*s) + 1 + np.sqrt(s/(4*np.pi)) - 3*s/25 + 3*s**(3/2)/226
    f2 = 4/np.pi + 8/np.sqrt(s*np.pi**5) + 25/(2792*s**(3/2)) - 1/(3880*s**(5/2)) - 1/(4500*s**(7/2))
    # Fancy if statement using boolean operations:
    iNorm = (s<1.281)*f1 + (s>=1.281)*f2
    i = np.pi*n*F*D*C*a*iNorm
    return i

def perry_Denuault(t, n=1, E0=0, E=-0.5, DO=1e-5, DR=1e-5, C=1e-6, a=10e-4, k0=1e-3, alpha=0.5):
    '''
    Returns the current of a microdisc electrode of a=10 um and E=-0.5 V according to the Perry and Denuault equation. It also accepts numpy arrays for the time.
    Sampled-Current Voltammetry at Microdisk Electrodes: Kinetic Information from Pseudo Steady State Voltammograms
    Perry, Al Shandoudi, Denuault, Analytical Chemistry, 2014, 86, 9917-9923
    doi: 10.1021/ac502645e

    from echem_fun import *
    t = 1 # [s], time to calculate the current
    i = perry_Denuault(t, E=-0.5, a=10e-4)
    '''
    fO = mahon_Oldham(t, n, DO, C, a)/(np.pi*n*F*DO*C*a)
    fR = mahon_Oldham(t, n, DR, C, a)/(np.pi*n*F*DR*C*a)
    Theta = 1 + (DO*fO/(DR*fR))*np.exp(n*F*(E-E0)/(R*T))
    kappa = (k0*a/(DO*fO))*np.exp(-alpha*n*F*(E-E0)/(R*T))
    i = (np.pi*n*F*DO*C*a*fO/Theta)/(1+(np.pi/(kappa*Theta))*((2*kappa*Theta+3*np.pi)/(4*kappa*Theta+3*np.pi**2)))
    return i





