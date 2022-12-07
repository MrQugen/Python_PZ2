import matplotlib.pyplot as plt
import numpy as np

import matplotlib.lines as mlines
fig12 = plt.figure(num=12, figsize=(10, 5))
ax12 = fig12.add_subplot(1, 1, 1)
ax12.set_xlim(left=-2*np.pi, right=2*np.pi)
ax12.set_ylim(bottom=-1.1, top=1.1)
xdata = np.linspace(-2*np.pi, 2*np.pi, 200)
ydata = np.sin(xdata)
line = mlines.Line2D(xdata, ydata,linewidth = 5, solid_joinstyle = 'bevel')
ax12.add_line(line)

fig12.savefig('img10.png', dpi=300, format='png')
