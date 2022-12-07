import matplotlib.pyplot as plt
import numpy as np

fig08 = plt.figure(num=8)
ax08 = [
    fig08.add_axes([0.0, 0.0, 1.0, 1.0]),
    fig08.add_axes([0.20, 0.6, 0.2, 0.3], xlim=(-1.5, 0), ylim=(-3, 10)),
    fig08.add_axes([0.65, 0.6, 0.2, 0.3], xlim=(1.5, 2.1), ylim=(0, 10))
]

t = np.linspace(-2.0, 2.1, 500)
y = t**4 - t**3 + t**2 - t - 1
z = t**3 - t**2 + 3

for ax in ax08:
    ax.plot(t, y, linewidth=1.0)
    ax.plot(t, z, linewidth=1.0, markevery=10)

fig08.savefig('img5.png', dpi=300, format='png')
