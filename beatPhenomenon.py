import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

delta = 0.01 ## Difference in wavelength [m]
alpha = 0.3 ## Wave dispersion coefficient [m^2] 
v = 0.005 ## Speed of wave
l_1, l_2 = 0.1, 0.1 + delta ## Wavelengths of both superposed waves [m]
A_1, A_2 = 4, 4 ## Amplitudes of both superposed waves [m]  (for best display of beat phenomenon, use waves close in both wavelength and amplitude)

k_1 = 2 * np.pi / l_1 ## Wave numbers for both superposed waves [1/m]
k_2 = 2 * np.pi / l_2

w_1 = v * k_1 * np.sqrt(1 + alpha * k_1 ** 2) ## Angular frequencies for both superposed waves [1/s]
w_2 = v * k_2 * np.sqrt(1 + alpha * k_2 ** 2)

## Creates both position and time arrays, and creates plot

x_lim = 3 * (2 * np.pi / np.abs(k_1 - k_2))

x = np.linspace(-x_lim, x_lim, int((2 * x_lim / min(l_1, l_2)) * 10))
t = np.linspace(0, 50, 500)

fig, axis = plt.subplots()

axis.set_xlim(-x_lim, x_lim)
axis.set_ylim(-1.5 * (A_1 + A_2), 1.5 * (A_1 + A_2))

superposition, = axis.plot([], []) ## The sum of both waves
envelope, = axis.plot([], [], color = 'green')
envelope_2, = axis.plot([], [], color = 'green') ## The two sinusoids that 'envelope' the superposed waves

## Updates plot for each frame

def update_data(frame):

    superposition.set_data(x, A_1 * np.sin(k_1 * x - w_1 * t[frame]) + A_2 * np.sin(k_2 * x - w_2 * t[frame]))
    envelope.set_data(x, 2 * A_1 * np.cos((k_1 - k_2)/2 * x - (w_1 - w_2)/2 * t[frame]))
    envelope_2.set_data(x, -2 * A_1 * np.cos((k_1 - k_2)/2 * x - (w_1 - w_2)/2 * t[frame]))

    return superposition, envelope, envelope_2

animation = FuncAnimation(fig = fig, func = update_data, frames = len(t), interval = 15, repeat = False, blit = True)

plt.show()


