import matplotlib.pyplot as plt
import numpy as np

fig01 = plt.figure(num=2, figsize = (10, 4.8) )
ax01 = fig01.add_subplot(1, 2, 1)
ax02 = fig01.add_subplot(1, 2, 2)
t = np.linspace(-4*np.pi, 4*np.pi, 400)
x = np.sin(t)
y = np.cos(t)
ax01.plot(t, x)
ax02.plot(t, y)
fig01.subplots_adjust(wspace=0.5)

fig01.savefig('img2.png', dpi=300, format='png')
