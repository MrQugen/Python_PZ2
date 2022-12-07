import matplotlib.pyplot as plt
import numpy as np

fig13 = plt.figure(num=13, figsize=(10, 5))
ax13 = fig13.add_subplot(1, 1, 1)
ax13.set_xlim(0, 1.5)
ax13.set_ylim(0, 1.5)
points = [(0.25, 0.25), (0.50, 0.50), (0.75, 0.75), (1.0, 1.0), (1.25, 1.25)]
xs = [p for (p, _) in points]
ys = [p for (_, p) in points]
ax13.plot(xs, ys, marker='o', markersize=6, linestyle='None')
x, y = points[0]
ax13.annotate(text='Точка No1', xy=(x, y+0.1,), color='gray')
x, y = points[1]
ax13.annotate(text='Точка No2', xy=(x, y+0.1,), rotation_mode='anchor', rotation=90)
x, y = points[2]
ax13.annotate(xy=(x, y+0.1,), text='Точка No3',
              horizontalalignment='center', fontstyle='italic', fontsize=14)
x, y = points[3]
ax13.annotate(xy=(x, y+0.1,), text='Точка No4', fontweight='extra bold')
x, y = points[4]
ax13.annotate(xy=(x, y+0.1,), text=r'$\mathscr{{P}}({0}, {1})$'.format(x, y))
ax13.annotate(xy=(0.2, 1.2,),
              text=r'$\lim_{x \to + \infty}\left(\frac{\pi(x)}{x/\ln x}\right)=1$', fontsize=20)

fig13.savefig('img11.png', dpi=300, format='png')
