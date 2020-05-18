import numpy as np
import matplotlib.pyplot as plt

Mass_hummer = 120E-3 # Tons
L_1 = 38 # mm
rho_1 = 7.85E-9 # Tons/mm^3
E = 210E3 # N/mm^2
R = 14
B = 28
H = 100
T_end = 550E-6 # sg

rho_2 = np.linspace(1E-8,3E-7,100)

# Restriction 1 (Celerity)
L_R1 = (2*L_1*(np.sqrt(rho_2) - np.sqrt(rho_1)) + T_end*np.sqrt(E))/(2*np.sqrt(rho_2))

# Restriction 2 (Mass)
L_R2 = (Mass_hummer - B*H*rho_1*(L_1-R) - 0.5*np.pi*R*R*H*rho_1 + B*H*L_1*rho_2)/(B*H*rho_2)


plt.plot(rho_2,L_R1,label='Celerity restriction')
plt.plot(rho_2,L_R2,label='Mass restriction')
plt.legend()
plt.show()
