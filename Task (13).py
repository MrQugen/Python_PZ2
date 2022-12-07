import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import os


def cycloid(t, R=3.0):
    '''Уравнение циклоиды'''
    return np.array([R * (t - np.sin(t)), R * (1 - np.cos(t))])


FOLDER = 'cycloid'
try:
    os.mkdir(FOLDER)
except FileExistsError:
    pass

fig18 = plt.figure(1)
ax01 = fig18.add_subplot(1, 1, 1)
ax01.set_aspect('equal')

R = 2.0
final_t = 10
final_x, _ = cycloid(final_t, R=R)
range_before = np.arange(0.0, final_t + 0.1, 0.1)
reversed_range = range_before[::-1]
for counter, last_t in enumerate(reversed_range):

    ax01.clear()
    T = np.linspace(last_t, 10.0, 1000)
    X, Y = cycloid(T, R=R)

    last_x, last_y = cycloid(T[0], R=R)

    circ = mpatches.Circle((R * T[0], R), R, fill=False, color='black')

    last_point = mpatches.Circle((last_x, last_y), 0.1, color='black')

    ax01.set_xlim(right=final_x + 2 * R)
    ax01.set_ylim(top=2 * R)

    ax01.plot(X, Y, linestyle='--')

    ax01.add_patch(last_point)
    ax01.add_patch(circ)
    fig18.savefig('{0}/{1:03d}.png'.format(FOLDER, counter), dpi=300, format='png')
