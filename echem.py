import numpy as np

F = 96485 # C/mol
R = 8.3145 # J/(mol K)
T = 298 # K


class Disc:
    '''
    Written for a reduction.
    Assumes only O is present in solution at t=0
    '''
    
    def __init__(self, a=5e-4, n=1, DO=1e-5, CO=1e-6):
        self.a = a
        self.n = n
        self.DO = DO
        self.CO = CO
        
        self.iLim = 4*self.n*F*self.DO*self.CO*self.a

class Voltammetry(Disc):
    '''
    '''

    def __init__(self, E, a=5e-4, n=1, CO=1e-6, DO=1e-5, DR=1e-5, E0=0, k0=1e8, alpha=0.5, noise=0):
        super().__init__(a, n, DO, CO)
        self.E = E
        self.E0 = E0
        self.DR = DR
        self.noise = noise
        self.cv(k0, alpha)

    def cv(self, k0, alpha):
        self.k0 = k0
        self.kappa0 = np.pi*self.k0*self.a/(4*self.DO)
        self.alpha = alpha
        self.Theta = 1 + (self.DO/self.DR)*np.exp(self.n*F*(self.E-self.E0)/(R*T))
        self.kappa = self.kappa0*np.exp(-self.alpha*self.n*F*(self.E-self.E0)/(R*T))
        i = -(self.iLim/self.Theta)/(1+(np.pi/(self.kappa*self.Theta))*((2*self.kappa*self.Theta+3*np.pi)/(4*self.kappa*self.Theta+3*np.pi**2)))
        self.i = i + np.random.normal(size=self.E.size, scale=self.noise)



class Chronoamperometry(Disc):

    def __init__(self, t, E=-1, a=5e-4, n=1, CO=1e-6, DO=1e-5, DR=1e-5, E0=0, k0=1e8, alpha=0.5, noise=0):
        super().__init__(a, n, DO, CO)
        self.t = t
        self.E = E
        self.DR = DR
        self.E0 = E0
        self.noise = noise
        self.ca(k0, alpha)

    def fun(self, D):
        s = D*self.t/self.a**2
        f1 = 1/np.sqrt(np.pi*s) + 1 + np.sqrt(s/(4*np.pi)) - 3*s/25 + 3*s**(3/2)/226
        f2 = 4/np.pi + 8/np.sqrt(s*np.pi**5) + 25/(2792*s**(3/2)) - 1/(3880*s**(5/2)) - 1/(4500*s**(7/2))
        # Fancy if statement using boolean operations:
        return (s<1.281)*f1 + (s>=1.281)*f2

    def ca(self, k0, alpha):
        fO = self.fun(self.DO)
        fR = self.fun(self.DR)
        Theta = 1 + (self.DO*fO/(self.DR*fR))*np.exp(self.n*F*(self.E-self.E0)/(R*T))
        kappa = (k0*self.a/(self.DO*fO))*np.exp(-alpha*self.n*F*(self.E-self.E0)/(R*T))
        i = -(np.pi*self.n*F*self.DO*self.CO*self.a*fO/Theta)/(1+(np.pi/(kappa*Theta))*((2*kappa*Theta+3*np.pi)/(4*kappa*Theta+3*np.pi**2)))
        self.i = i + np.random.normal(size=self.t.size, scale=self.noise)
