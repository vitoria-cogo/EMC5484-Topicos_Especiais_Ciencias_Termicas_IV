import numpy as np
import matplotlib.pyplot as plt


N_TIME_STEPS = 100000
TOLERANCE = 1.0e-6


N_x = 20
N_y = 20

a = 1.0
b = 0.1

delta_x = a/(N_x-1)
delta_y = b/(N_y-1)


x = np.linspace(0,a,N_x)
y = np.linspace(0,b,N_y)



phi_BC_e = 0.0
phi_BC_w = 0.0
phi_BC_n = np.sin(np.pi * x / a)
phi_BC_s = 0.0
phi = 0.0
phi_values = np.zeros((N_x, N_y), dtype = float)
#phi_values[...] = phi


phi_values[:, 0] = phi_BC_w
phi_values[:, -1] = phi_BC_e
phi_values[-1, :] = phi_BC_s
phi_values[0, :] = phi_BC_n
RES = np.zeros((N_x, N_y), dtype = float)

for iteration in range(N_TIME_STEPS):
    phi_old = phi_values.copy()
    for i in range(1, N_x - 1):
        for j in range(1, N_y - 1):
            phi_values[i, j] = (phi_values[i + 1, j] + phi_values[i - 1, j]) * delta_y ** 2
            phi_values[i, j] += (phi_values[i, j + 1] + phi_values[i, j - 1]) * delta_x ** 2
            phi_values[i, j] /= (2 * (delta_x ** 2 + delta_y ** 2))
    for i in range(1, N_x - 1):
        for j in range(1, N_y - 1):
            RES[i, j] = (phi_values[i + 1, j] + phi_values[i - 1, j]) * delta_y ** 2
            RES[i, j] += (phi_values[i, j + 1] + phi_values[i, j - 1]) * delta_x ** 2
            RES[i, j] -= (2 * phi_values[i, j] * (delta_x ** 2 + delta_y ** 2))
    residuo = np.linalg.norm(RES)
    print(residuo)

    plt.clf()
    plt.imshow(phi_values, extent=[0, a, 0, b], origin='upper', cmap='hot', vmin=0, vmax=1)
    plt.colorbar(label='Phi')
    plt.title(f'Iteração {iteration + 1}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.pause(0.1)

    res = np.linalg.norm(phi_values - phi_old, ord=np.inf)
    if res < TOLERANCE:
        print(f"Convergiu em {iteration} iterações com erro {res}")
        break
plt.show()
