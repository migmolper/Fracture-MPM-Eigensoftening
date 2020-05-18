import numpy as np
import matplotlib.pyplot as plt

E = 210E3 # N/mm^2
rho1 = 7.85E-9 # Tons/mm^3
rho2 = 1.2E-7 # Tons/mm^3
L = 390 # mm
L1 = 38 # mm
L2 = L-L1 # mm
V_hummer = [881,1760,2640] # mm/s 
CFL = 0.1
Cel1 = np.sqrt(E/rho1) # mm/s
Cel2 = np.sqrt(E/rho2) # mm/s
DeltaX = np.linspace(0.1,1.0,100)
# DeltaX = np.array([0.1,0.5,1.0])
DeltaT = (CFL/Cel1)*DeltaX

for i in range(0,3):
    Tend = DeltaX/V_hummer[i] + 2*L1/Cel1 + 2*L2/Cel2
    Nsteps = Tend/DeltaT
    plt.plot(Tend,Nsteps, label="Hummer vel : %f"%V_hummer[i])
plt.legend()
plt.show()
