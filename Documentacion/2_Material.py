import glob,os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from matplotlib.ticker import FixedLocator
from matplotlib.ticker import FormatStrFormatter

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def Get_Riemann_I(Stress_I,Velocity_I,nu):
    R_I = (0.5/nu)*(- Stress_I + Velocity_I*nu)
    return R_I

def Get_Riemann_II(Stress_II,Velocity_II,nu):
    R_II = (0.5/nu)*(Stress_II + Velocity_II*nu)
    return R_II

def Dyka_Riemann(CFL,T_END,i_RES):
                     
    # Material properties
    L = 380
    x_a = 0
    x_b = L*0.1
    x_c = L
    
    E_ab = 210*10**3 # MPa
    rho_ab = 7.8*10**(-9) # Tn/mm³
    CEL_ab = np.sqrt(E_ab/rho_ab)
    E_bc = 210*10**3 # MPa
    rho_bc = 1.2*10**(-7) # Tn/mm³
    CEL_bc = np.sqrt(E_bc/rho_bc)

    CEL = max(CEL_ab,CEL_bc)

    # Discretize domain
    DeltaX = 1
    N_nodes = int(L/DeltaX)
    X = np.linspace(x_a,x_c,N_nodes)
    I_a = find_nearest(X,x_a)
    I_b = find_nearest(X,x_b)
    I_c = find_nearest(X,x_c)    

    # Discretize time
    N_steps = int(T_END/(1*CFL/CEL))
    DeltaT = CFL*DeltaX/CEL
    T = np.linspace(0.0,T_END,int(N_steps/i_RES))

    # Initial conditions
    v0 = -500
    Stress = np.zeros([int(N_steps/i_RES),N_nodes])
    Velocity = np.zeros([int(N_steps/i_RES),N_nodes])
    for x in range(0,N_nodes):
        if X[x] <= 10 :
            Velocity[0,x] = v0
        else :
            Velocity[0,x] = 0
        
        
    # Get the static viscosity
    nu_ab = np.sqrt(E_ab*rho_ab)
    nu_bc = np.sqrt(E_bc*rho_bc)

    ################################################################
    ####################### Loop in time ###########################
    ################################################################
    for t in range(1,int(N_steps/i_RES)):
    
        ############################################################    
        ################### Solve domain ab ########################
        ############################################################
        for x in range(1,I_b):

            # Get boundary values through characteristics lines
            t_I = T[t] - X[x]/CEL_ab
            t_II = T[t] - (x_b-x_a-X[x])/CEL_ab
    
            # Get stress and velocity values in I and II
            if(t_I>0):
                t_i = find_nearest(T, t_I)
                Stress_I = 0
                Velocity_I = Velocity[t_i,I_a]
            else:
                x_i = find_nearest(X, X[x] - T[t]*CEL_ab)
                Stress_I = Stress[0,x_i]
                Velocity_I = Velocity[0,x_i]
            if(t_II>0):
                t_i = find_nearest(T, t_II)
                Stress_II = Stress[t_i,I_b]
                Velocity_II = Velocity[t_i,I_b]
            else:
                x_i = find_nearest(X, X[x] + T[t]*CEL_ab)
                Stress_II = Stress[0,x_i]
                Velocity_II = Velocity[0,x_i]
            
            # Rimman invariants
            R_I = Get_Riemann_I(Stress_I,Velocity_I,nu_ab)
            R_II = Get_Riemann_II(Stress_II,Velocity_II,nu_ab)
        
            # Stress-velocity actualization
            Stress[t,x] = nu_ab*(R_II - R_I) 
            Velocity[t,x] = R_I + R_II

            
        ############################################################    
        ################### Solve domain bc ########################
        ############################################################
        for x in range(I_b+1,I_c):

            # Get boundary values through characteristics lines
            t_I = T[t] - (X[x]-x_b)/CEL_bc
            t_II = T[t] - (x_c-X[x])/CEL_bc
    
            # Get stress and velocity values in I and II
            if(t_I>0):
                t_i = find_nearest(T, t_I)
                Stress_I = Stress[t_i,I_b]
                Velocity_I = Velocity[t_i,I_b]
            else:
                x_i = find_nearest(X, X[x] - T[t]*CEL_bc)
                Stress_I = Stress[0,x_i]
                Velocity_I = Velocity[0,x_i]
            if(t_II>0):
                t_i = find_nearest(T, t_II)
                Stress_II = Stress[t_i,I_c]
                Velocity_II = 0
            else:
                x_i = find_nearest(X, X[x] + T[t]*CEL_bc)
                Stress_II = Stress[0,x_i]
                Velocity_II = Velocity[0,x_i]
            
            # Rimman invariants
            R_I = Get_Riemann_I(Stress_I,Velocity_I,nu_bc)
            R_II = Get_Riemann_II(Stress_II,Velocity_II,nu_bc)
        
            # Stress-velocity actualization
            Stress[t,x] = nu_bc*(R_II - R_I) 
            Velocity[t,x] = R_I + R_II



        ############################################################
        ################## Solve the interfase #####################
        ############################################################
        
        # Get boundary values through characteristics lines
        t_I = T[t] - x_b/CEL_ab
        t_II = T[t] - (L-x_b)/CEL_bc
    
        # Get stress and velocity values in I and II
        if(t_I>0):
            t_i = find_nearest(T, t_I)
            Stress_I = 0
            Velocity_I = Velocity[t_i,I_a]
        else:
            x_i = find_nearest(X, x_b - T[t]*CEL_ab)
            Stress_I = Stress[0,x_i]
            Velocity_I = Velocity[0,x_i]
        if(t_II>0):
            t_i = find_nearest(T, t_II)
            Stress_II = Stress[t_i,I_c]
            Velocity_II = 0
        else:
            x_i = find_nearest(X, x_b + T[t]*CEL_bc)
            Stress_II = Stress[0,x_i]
            Velocity_II = Velocity[0,x_i]
            
        # Rimman invariants
        R_I_ab = Get_Riemann_I(Stress_I,Velocity_I,nu_ab)
        R_II_bc = Get_Riemann_II(Stress_II,Velocity_II,nu_bc)
        
        # Stress-velocity actualization
        Stress[t,I_b] = nu_bc*R_II_bc - nu_ab*R_I_ab 
        Velocity[t,I_b] = 2*(nu_ab*R_I_ab + nu_bc*R_II_bc)/(nu_ab+nu_bc)

    
        ############################################################
        ################### Solve left boundary ####################
        ############################################################

        # Get time in the right boundary
        t_II = T[t] - x_b/CEL_ab

        # Get stress and velocity values in I and II 
        if(t_II>0):
            t_i = find_nearest(T, t_II)
            Velocity_II = Velocity[t_i,I_b]
            Stress_II = Stress[t_i,I_b]
        else:
            x_i = find_nearest(X, T[t]*CEL_ab)
            Velocity_II = Velocity[0,x_i]
            Stress_II = Stress[0,x_i]

        # Get Riemann II
        R_II = Get_Riemann_II(Stress_II,Velocity_II,nu_ab)
    
        # Get the value in the boundary
        Stress[t,0] = 0
        Velocity[t,0] = 2*R_II
            
        ############################################################
        ################### Solve right boundary ###################
        ############################################################

        # Get time in the left boundary
        t_I = T[t] - (x_c-x_b)/CEL_bc
    
        # Get stress and velocity values in I and II
        if(t_I>0):
            t_i = find_nearest(T, t_I)
            Stress_I = Stress[t_i,I_b]
            Velocity_I = Velocity[t_i,I_b]
        else:
            x_i = find_nearest(X, x_c-T[t]*CEL_bc)
            Stress_I = Stress[0,x_i]
            Velocity_I = Velocity[0,x_i]

        # Get Riemann I
        R_I = Get_Riemann_I(Stress_I,Velocity_I,nu_bc)

        # Get the value in the boundary
        Stress[t,I_c] = - 2*nu_bc*R_I
        Velocity[t,I_c] = 0

    # np.save('2_Material/Velocity_%i'%(100*CFL), Velocity)
    # np.save('2_Material/Stress_%i'%(100*CFL), Stress)
    np.save('Velocity_%i'%(100*CFL), Velocity)
    np.save('Stress_%i'%(100*CFL), Stress)


################################################################
############### Print results in x-t diagram ###################
################################################################

# Material properties

# Material properties
L = 380
x_a = 0
x_b = L*0.1
x_c = L
    
E_ab = 210*10**3 # MPa
rho_ab = 7.8*10**(-9) # Tn/mm³
CEL_ab = np.sqrt(E_ab/rho_ab)
E_bc = 210*10**3 # MPa
rho_bc = 1.2*10**(-7) # Tn/mm³
CEL_bc = np.sqrt(E_bc/rho_bc)

CEL = max(CEL_ab,CEL_bc)

# Discretize domain
DeltaX = 1
CFL = 0.5
T_END = 600E-6
i_RES = 100

 # Discretize domain
N_nodes = int(L/DeltaX)
X = np.linspace(x_a,x_c,N_nodes)
# Discretize time
N_steps = int(T_END/(DeltaX*CFL/CEL))
DeltaT = CFL*DeltaX/CEL
T = np.linspace(0.0,T_END,int(N_steps/i_RES))

Dyka_Riemann(CFL, T_END, i_RES)

# Generate mesh
XX, TT = np.meshgrid(X,T)

# Velocity = np.load('2_Material/Velocity_%i.npy'%(CFL*100))
# Stress = np.load('2_Material/Stress_%i.npy'%(CFL*100))
Velocity = np.load('Velocity_%i.npy'%(CFL*100))
Stress = np.load('Stress_%i.npy'%(CFL*100))

min_vel = np.min(np.min(Velocity))
max_vel = np.max(np.max(Velocity))
min_str = np.min(np.min(Stress))
max_str = np.max(np.max(Stress))

# ################################################################
# ################### Velocity 3D Figure  ########################
# ################################################################

fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.grid(False)
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
for line in ax.xaxis.get_ticklines():
    line.set_visible(False)
for line in ax.yaxis.get_ticklines():
    line.set_visible(False)


surf = ax.plot_surface(XX, TT, Velocity, rstride=1,
                       cstride=1, cmap=cm.jet,
                       linewidth=0, antialiased=False)

ax.set_zlim3d(min_vel, max_vel)
ax.set_zticks([min_vel, 0.5*min_vel, 0, 0.5*max_vel, max_vel])
plt.tight_layout()
fig.colorbar(surf)

ax.set_xlabel('X')
ax.set_ylabel('Time')
ax.set_zlabel('Velocity')
# plt.savefig("Analytical_3D_Velocity.%s"%(format_fig))  
# if Show_grafs:
plt.show()
    
fig.clear()


# ################################################################
# ################### Proyections Velocity #######################
# ################################################################

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# # ax.grid(False)
# ax.xaxis.pane.set_edgecolor('black')
# ax.yaxis.pane.set_edgecolor('black')
# ax.zaxis.pane.set_edgecolor('black')
# ax.xaxis.pane.fill = False
# ax.yaxis.pane.fill = False
# ax.zaxis.pane.fill = False
# ax.axes.xaxis.set_ticklabels([])
# ax.axes.yaxis.set_ticklabels([])
# for line in ax.xaxis.get_ticklines():
#     line.set_visible(False)
# for line in ax.yaxis.get_ticklines():
#     line.set_visible(False)

# cset_z = ax.contour(XX, TT, Velocity, zdir='z', offset=min_vel, cmap=cm.coolwarm)
# cset_x = ax.contour(XX, TT, Velocity, zdir='x', offset=0, cmap=cm.coolwarm)
# cset_y = ax.contour(XX, TT, Velocity, zdir='y', offset=T_end, cmap=cm.coolwarm)

# ax.set_zlim3d(min_vel, max_vel)
# ax.set_zticks([min_vel, 0.5*min_vel, 0, 0.5*max_vel, max_vel])
# plt.tight_layout()
# fig.colorbar(cset_z)

# ax.set_xlabel('X')
# ax.set_ylabel('Time')
# ax.set_zlabel('Velocity')
# plt.savefig("Analytical_contour_Velocity.%s"%(format_fig))
# if Show_grafs:
#     plt.show()
# fig.clear()


# ################################################################
# ################## 1D results of velocity ######################
# ################################################################

fig, ax = plt.subplots()
ax.plot(T,Velocity[:,0])
ax.set_xlabel('Time')
ax.set_ylabel('Velocity')
plt.title('Left side velocity evolution')
plt.tight_layout()
plt.grid()
plt.show()
fig.clear()


# ################################################################
# ##################### Stress 3D Figure #########################
# ################################################################

fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.grid(False)
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
for line in ax.xaxis.get_ticklines():
    line.set_visible(False)
for line in ax.yaxis.get_ticklines():
    line.set_visible(False)
        
surf = ax.plot_surface(XX, TT, Stress, rstride=1,
                       cstride=1, cmap=cm.jet,
                       linewidth=0, antialiased=False)
ax.set_zlim3d(min_str, max_str)
ax.set_zticks([min_str,0.5*min_str,0, 0.5*max_str, max_str])
plt.tight_layout()
fig.colorbar(surf)

ax.set_xlabel('X')
ax.set_ylabel('Time')
ax.set_zlabel('Stress')
plt.show()

fig.clear()

# ################################################################
# #################### Proyections Stress ########################
# ################################################################

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# # ax.grid(False)
# ax.xaxis.pane.set_edgecolor('black')
# ax.yaxis.pane.set_edgecolor('black')
# ax.zaxis.pane.set_edgecolor('black')
# ax.xaxis.pane.fill = False
# ax.yaxis.pane.fill = False
# ax.zaxis.pane.fill = False
# ax.axes.xaxis.set_ticklabels([])
# ax.axes.yaxis.set_ticklabels([])
# for line in ax.xaxis.get_ticklines():
#     line.set_visible(False)
# for line in ax.yaxis.get_ticklines():
#     line.set_visible(False)

# cset_z = ax.contour(XX, TT, - Stress, zdir='z',
#                         offset=min_str, cmap=cm.coolwarm)
# cset_x = ax.contour(XX, TT, - Stress, zdir='x',
#                         offset=0, cmap=cm.coolwarm)
# cset_y = ax.contour(XX, TT, - Stress, zdir='y',
#                         offset=T_end, cmap=cm.coolwarm)

# ax.set_zlim3d(min_str, max_str)
# ax.set_zticks([min_str,0.5*min_str,0, 0.5*max_str, max_str])
# plt.tight_layout()
# fig.colorbar(cset_z)

# ax.set_xlabel('X')
# ax.set_ylabel('Time')
# ax.set_zlabel('Stress')
# plt.savefig("Analytical_contour_Stress.%s"%(format_fig))
# if Show_grafs:
#     plt.show()

# fig.clear()

# ################################################################
# ################## 1D results of stress ########################
# ################################################################

fig, ax = plt.subplots()
ax.plot(T,Stress[:, find_nearest(X, 0.25*L)])
ax.set_xlabel('Time')
ax.set_ylabel('Stress')
plt.title('3/4 L point stress evolution')
plt.tight_layout()
plt.grid()
plt.show()
fig.clear()
