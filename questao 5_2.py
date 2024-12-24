import numpy as np
import matplotlib.pyplot as plt


N_TIME_STEPS = 100000
TOLERANCE = 1.0e-6


nx = 22
ny = 22

a = 1.0
b = 1.0

delta_x = 10*a/(nx-2)
delta_y = b/(ny-2)


x = np.linspace(1,a-1,nx-2)
y = np.linspace(1,b-1,ny-2)



phi_BC_e = 0.0
phi_BC_w = 0.0
phi_BC_n = np.sin(np.pi * x / a)
phi_BC_s = 0.0
phi = 0.0
phi_values = np.zeros((nx, ny), dtype = float)
#phi_values[...] = phi



RES = np.zeros((nx, ny), dtype = float)

for iteration in range(N_TIME_STEPS):
    phi_old = phi_values.copy()


    phi_values[0, 1: nx - 1] = - phi_values[1, 1:nx - 1] + (2 * phi_BC_n)
    phi_values[1:ny - 1, -1] = - phi_values[1:ny - 1, -2]
    phi_values[-1, 1:nx - 1] = - phi_values[-2, 1:nx - 1]
    phi_values[1:ny - 1, 0] = - phi_values[1:ny - 1, 1]


    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            phi_values[i, j] = (phi_values[i + 1, j] + phi_values[i - 1, j]) * delta_y ** 2
            phi_values[i, j] += (phi_values[i, j + 1] + phi_values[i, j - 1]) * delta_x ** 2
            phi_values[i, j] /= (2 * (delta_x ** 2 + delta_y ** 2))
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            RES[i, j] = (phi_values[i + 1, j] + phi_values[i - 1, j]) * delta_y ** 2
            RES[i, j] += (phi_values[i, j + 1] + phi_values[i, j - 1]) * delta_x ** 2
            RES[i, j] -= (2 * phi_values[i, j] * (delta_x ** 2 + delta_y ** 2))
    residuo = np.linalg.norm(RES)
    print(residuo)

    plt.clf()
    plt.imshow(phi_values[1:-1,1:-1], extent=[0,a,0,b] , origin='upper', cmap='hot', vmin=0, vmax=1)
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
