import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.patches import Circle 

v = 0.5 ## Speed of wavefront propogation [m/s]
t_tot = 5 ## Total time of simulation [s]
n = 50 * t_tot ## Number of frames

## Creates necessary time, position, wavefront, and intensity arrays, and creates plot

t = np.linspace(0, t_tot, n)

waves = []
intensity = []

def particle_pos(t):
    x = 3 * np.sin(t)
    y = 3 * np.cos(t)
    return x, y

fig, axis = plt.subplots()

x, y = particle_pos(t)

lim = max(max(abs(x)), max(abs(y)))

axis.set_xlim(-1.5 * lim, 1.5 * lim)
axis.set_ylim(-1.5 * lim, 1.5 * lim)

moving_point, = axis.plot([], [], 'o', markersize = 10, color = 'blue')

## Updates data for each frame

def update_data(frame):

    x_pos, y_pos = particle_pos(t[frame])
    moving_point.set_data([x_pos], [y_pos])
    if (frame % int(n/250) == 0):
        waves.append(axis.add_artist(Circle((x_pos, y_pos)
                                    , radius = 0
                                    , fill = False
                                    , ec = 'black'))) ## Creates each wavefront
        
    if (frame != 0):
        for i in range(0, len(waves) - 1):
            dt = t_tot/n
            waves[i].set_radius(waves[i].get_radius() + v * dt) ## Updates wave radius based off of time passed in the simulation
            
        for wave in waves: 
            if (wave.get_radius() != 0):
                intensity.append(1/wave.get_radius()) ## Tracks intensity of each wave, which varies by 1/r for 2d wavefronts 

        I_max = max(intensity)
        I_min = min(intensity)

    for wave in waves[:]:
        if ((wave.get_radius() != 0) and (frame != 0)):
            I = 1/(wave.get_radius()) 
            if I_max != I_min:
                alpha = (np.log(I) - np.log(I_min))/(np.log(I_max) - np.log(I_min)) ## Uses logarithmic scale to set alpha values to display intensity of wavefronts
            else:
                alpha = 1
            wave.set_edgecolor((0, 0, 0, alpha))
            if wave.get_radius() > lim:
                wave.remove()
                waves.remove(wave) ## Removes wavefronts if too large to save computational time 

    intensity.clear() ## Clears intensity array for each update

    return [moving_point, *waves]

animation_system = FuncAnimation(fig = fig
                                  , func = update_data
                                  , frames = len(t)
                                  , interval = 15
                                  , repeat = False
                                  , blit = True)

plt.show()




