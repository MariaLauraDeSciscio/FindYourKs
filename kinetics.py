
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

T = 300 #K
k_B = 1.380649e-23  # (J/K)
h = 6.62607015e-34  # (J.s)
R = 8.314462618     # (J/mol/K)

def calc_dg(k,T = 300 ):
    
    delta_G = -R * T * np.log((k * h) / (k_B * T))  # ΔG in J/mol
    return delta_G / 1000 / 4.184  # kcal/mol

def plot_solution_residuals(t, A, D, E, sol, K, k2, k_2, k3, k4, K_opt, k2_opt, k_2_opt, k3_opt, k4_opt, RMSE, idx):
    fig = plt.figure(figsize=(15.5, 10.5))
    gs = GridSpec(2, 1, height_ratios=[4, 1])
    axs = [plt.subplot(gs[0]), plt.subplot(gs[1])]

    axs[0].plot(t / (60 * 60 * 24), A, 'o', label='Asn (exp)')
    axs[0].plot(t / (60 * 60 * 24), D, 'o', label='Suc (exp)')
    axs[0].plot(t / (60 * 60 * 24), E, 'o', label='Asp (exp)')
    axs[0].plot(t / (60 * 60 * 24), sol.y[0], '-', label='Asn (model)')
    axs[0].plot(t / (60 * 60 * 24), sol.y[2], '-', label='Suc (model)')
    axs[0].plot(t / (60 * 60 * 24), sol.y[3], '-', label='Asp (model)')

    axs[1].plot(t / (60 * 60 * 24), sol.y[0]-A, '-', label='Asn residual')
    axs[1].plot(t / (60 * 60 * 24), sol.y[2]-D, '-', label='Suc residual')
    axs[1].plot(t / (60 * 60 * 24), sol.y[3]-E, '-', label='Asp residual')

    for i in range(2):
        axs[i].set_xlabel('Time (days)')
    axs[0].set_ylabel('Concentration')
    axs[1].set_ylabel('Residuals')
    axs[0].legend()
    axs[1].legend()
    axs[0].set_title(
        f' K={K}, k2={k2}, k_2={k_2}, k3={k3}, k4={k4} \n'
        f'OPT:  K = {K_opt}, k2 = {k2_opt}, k_2 = {k_2_opt}, k3 = {k3_opt}, k4 = {k4_opt} \n'
        f'RMSE={RMSE}'
    )
    plt.tight_layout()
    plt.show()

