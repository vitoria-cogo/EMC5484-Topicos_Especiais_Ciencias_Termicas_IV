import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iterations = 10

N_x = [5,31,101]
L_x = 1.0

x5 = np.linspace(0, L_x, N_x[0])
x31 = np.linspace(0, L_x, N_x[1])
x101 = np.linspace(0, L_x, N_x[2])

delta_x5 = L_x/(N_x[0]-1)
delta_x31 = L_x/(N_x[1]-1)
delta_x101 = L_x/(N_x[2]-1)

T_x5 = np.sin(np.pi * x5) + 0.1 * np.sin(N_x[0] * np.pi * x5)
T_x31 = np.sin(np.pi * x31) + 0.1 * np.sin(N_x[1] * np.pi * x31)
T_x101 = np.sin(np.pi * x101) + 0.1 * np.sin(N_x[2] * np.pi * x101)

# Guardando a distribuição inicial para plotagem
T_x5_initial = T_x5.copy()
T_x31_initial = T_x31.copy()
T_x101_initial = T_x101.copy()

# Condição na esquerda
T_x5[0] = np.sin(np.pi * x5[0]) + 0.1 * np.sin(N_x[0] * np.pi * x5[0])
T_x31[0] = np.sin(np.pi * x31[0]) + 0.1 * np.sin(N_x[1] * np.pi * x31[0])
T_x101[0] = np.sin(np.pi * x101[0]) + 0.1 * np.sin(N_x[2] * np.pi * x101[0])

# Condição na direita
T_x5[-1] = np.sin(np.pi * x5[-1]) + 0.1 * np.sin(N_x[0] * np.pi * x5[-1])
T_x31[-1] = np.sin(np.pi * x31[-1]) + 0.1 * np.sin(N_x[1] * np.pi * x31[-1])
T_x101[-1] = np.sin(np.pi * x101[-1]) + 0.1 * np.sin(N_x[2] * np.pi * x101[-1])

# Cálculo dos volumes internos
for j in range(iterations):
    for i in range(1, N_x[0]-1):
        T_x5[i] = (T_x5[i+1] + T_x5[i-1])/2

    for i in range(1, N_x[1]-1):
        T_x31[i] = (T_x31[i+1] + T_x31[i-1])/2

    for i in range(1, N_x[2]-1):
        T_x101[i] = (T_x101[i+1] + T_x101[i-1])/2


# N_x = 5
plt.plot(x5, T_x5_initial, '--', label='Inicial (N=5)')
plt.plot(x5, T_x5, label=f'Apos {iterations} iteracoes (N=5)')
plt.xlabel('x')
plt.ylabel('Temperatura T(x)')
plt.title('Distribuição de Temperatura Inicial e após 10 Iterações')
plt.legend()
plt.grid()
plt.show()
# N_x = 31
plt.plot(x31, T_x31_initial, '--', label='Inicial (N=31)')
plt.plot(x31, T_x31, label=f'Apos {iterations} iteracoes (N=31)')
plt.xlabel('x')
plt.ylabel('Temperatura T(x)')
plt.title('Distribuição de Temperatura Inicial e após 10 Iterações')
plt.legend()
plt.grid()
plt.show()
# N_x = 101
plt.plot(x101, T_x101_initial, '--', label='Inicial (N=101)')
plt.plot(x101, T_x101, label=f'Apos {iterations} iteracoes (N=101)')
plt.xlabel('x')
plt.ylabel('Temperatura T(x)')
plt.title('Distribuição de Temperatura Inicial e após 10 Iterações')
plt.legend()
plt.grid()
plt.show()