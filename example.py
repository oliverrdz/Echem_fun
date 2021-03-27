import numpy as np

import echem
import plotting as p

k0 = 1e-0
alpha = 0.5

E = np.linspace(-0.5, 0.5, 100)
t = np.linspace(0.001, 1, 1001)
tsqrt = 1/np.sqrt(t)

cv = echem.Voltammetry(E=E)
cv.reversible()
cv.quasireversible(k0=k0, alpha=alpha)

E1 = -1
E2 = -0.2
ca1 = echem.Chronoamperometry(t=t, E=E1)
ca2 = echem.Chronoamperometry(t=t, E=E2)

p.plot2(E, cv.i_rev*1e9, 'Reversible', '-',
        E, cv.i_qrev*1e9, 'Quasi reversible', '-',
        '$E$ / V', '$i$ / nA', fig=1)

p.plot2(tsqrt, ca1.i*1e9, 'E = ' + '{:.1f}'.format(E1) + 'V', '-',
        tsqrt, ca2.i*1e9, 'E = ' + '{:.1f}'.format(E2) + 'V', '-',
        '$t^{-1/2}$ / s$^{-1/2}$', '$i$ / nA', fig=2)



