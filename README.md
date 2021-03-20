# Echem_fun
Electrochemistry functions that I use on my day to day. It requires numpy and matplotlib installed. The functions have default parameters, for more info see the code or type:

```python
from echem_fun import *
# To get help of any function:
help(ilim)
```

# Usage
```python

from echem_fun import *
from plotting import *

import numpy as np

t = np.linspace(1e-3, 1, 1000)
tsqrt = 1/np.sqrt(t)

i = mahon_Oldham(t, a=10e-4)

plot(tsqrt, i*1e9, '$t^{-1/2}$ / s$^{-1/2}$', '$i$ / nA')
```
