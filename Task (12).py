import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

r = 1
circle = mpatches.Circle(xy=(0, 0), radius=r, color='blue', linestyle='--', fill=False)
fi = np.linspace(0, 2 * np.pi, 360)
x = r * np.cos(fi)
y = r * np.sin(fi)
dx = x
dy = np.cos(x)

fig15 = plt.figure(15, figsize=(10, 10))
ax15 = fig15.add_subplot(1, 1, 1)
ax15.quiver(x[::4], y[::4], dx[::4], dy[::4], units='xy',
            angles='xy', label='Касательные векторы')

ax15.add_patch(circle)
ax15.set_xlabel(r'Ось $Ox$')
ax15.set_ylabel(r'Ось $Oy$')

ax15.set_aspect('equal')

fig15.savefig('img12.png', dpi=300, format='png')
