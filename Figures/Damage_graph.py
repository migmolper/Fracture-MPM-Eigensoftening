import numpy as np
import matplotlib.pyplot as plt

xi = np.linspace(0,1)
f = 1 - xi

fig, ax = plt.subplots()
ax.set_xlim(0,1.2)
ax.set_ylim(0,1.2)
ax.plot(xi,f)

plt.show()

