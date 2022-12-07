import matplotlib.pyplot as plt
import numpy as np

fig05 = plt.figure(num=4, figsize=(10, 10))
axs05 = [fig05.add_subplot(3, 1, i) for i in range(1,4)]
x = np.linspace(-2,2,100)
funcs = [x, x**2, x**3]
y_min = np.min(funcs)
y_max = np.max(funcs)
for (f, ax) in zip(funcs, axs05):
    ax.plot(x, f)
    ax.set_ylim(bottom=y_min, top=y_max)
for ax in axs05[0:2]:
    ax.set_xticklabels([])
fig05.subplots_adjust(hspace=0)

fig05.savefig('img4.png', dpi=300, format='png')
