import matplotlib.pyplot as plt
import numpy as np

fig09 = plt.figure(num=9)
ax09 = fig09.add_subplot(1, 1, 1)
t = np.linspace(-4*np.pi, 4*np.pi, 200)
y = np.sin(t)
ax09.plot(t, y)

ax09.spines['top'].set_visible(False)
ax09.spines['right'].set_visible(False)

ax09.spines['bottom'].set_position('zero')
ax09.spines['left'].set_position('zero')

ax09.xaxis.set_tick_params(direction='inout', length=10)
ax09.yaxis.set_tick_params(direction='inout', length=10)

fig09.savefig('img6.png', dpi=300, format='png')
