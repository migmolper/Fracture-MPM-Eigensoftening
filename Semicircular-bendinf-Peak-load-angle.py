import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig, ax = plt.subplots()

# Total plot
# # ax.set_xlim(0.00, 0.0002)
# ax.set_xticks([0, 0.01, 0.02])
# ax.set_yticks([-0.01, 0.0, 0.01, 0.02, 0.03, 0.04, 0.05])
# ax.xaxis.set_minor_locator(AutoMinorLocator())
# ax.yaxis.set_minor_locator(AutoMinorLocator())

Experimental_data = pd.read_csv("Semicircular-bending-Experimental-results.txt",header=0,names=['angle','load'])
# Experimental_data.boxplot(ax=ax,by='angle')
ExpDat_angles = Experimental_data['angle'].to_numpy()
ExpDat_P = Experimental_data['load'].to_numpy()

Simulation_data   = pd.read_csv("Semicircular-bending-Simulation-results.txt", header=None)
SimDat_angles = Simulation_data[0].to_numpy()
SimDat_P = Simulation_data[1].to_numpy()

plt.scatter(ExpDat_angles,ExpDat_P,marker='D',label=r'Experiment Lim \textit{et al.}')

ax.plot(SimDat_angles,SimDat_P,':',marker='s',fillstyle='none',color='k',label=r'Simulation')

# ED_1 = np.array([234,187,193,183,235])
# ED_2 = np.array([268,220,236,211,212])
# ED_3 = np.array([312,334,280,326,310,332])

# ax.boxplot([ED_1,ED_2,ED_3],positions=[0,30,60])


ax.set_xlabel(r'Notch inclination angle ($^{\circ}$)', fontsize=16)
ax.set_ylabel(r'Force ($N$)', fontsize=16)
plt.legend()
plt.show()

