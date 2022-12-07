import matplotlib.pyplot as plt
import numpy as np

fig10 = plt.figure(num=10, figsize=(3,3))
ax10 = fig10.add_subplot(1, 1, 1, projection='polar')
phi = np.linspace(0.0, 10, 100)
r = 0.5*phi
ax10.plot(phi, r, linewidth=1)

fig10.savefig('img8.png', dpi=300, format='png')
