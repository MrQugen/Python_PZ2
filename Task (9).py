import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

fig11 = plt.figure(num=11, figsize = (10, 6))
ax11 = fig11.add_subplot(1, 1, 1)
ax11.set_xlim(left=-8, right=3.1)
ax11.set_ylim(bottom=-1.5, top=3.1)
ax11.set_aspect('equal')
circle = mpatches.Circle(xy=(-6, 2), radius = 0.5, color='blue', linestyle='--', fill=False)

elipse = mpatches.Ellipse(xy=(-4, 2), color='red', width=2, height=1, fill=False)

rectangle = mpatches.Rectangle(xy=(-1, 1.5), width=1, height=1.5, angle=130, fill=False)

arc = mpatches.Arc(xy=(0, 2), width=2, height=1, angle=0, theta1=0, theta2=180)

wedge = mpatches.Wedge(center=(2.2, 2), r=1, theta1=90, theta2=180, fill=False)

polygon = mpatches.Polygon(xy=np.array([[-7, -1], [-6.5, 0], [-5.5, 0], [-5, -1]]),
                           closed=True, fill=False)

arrow = mpatches.Arrow(x=-4, y=0, dx=1, dy=0, color = 'red')

farrow = mpatches.FancyArrow(x=-2, y=0, dx=1, dy=0, width=0.01, head_width=0.1)

fbox = mpatches.FancyBboxPatch(xy=(0, -1), width=1, height=1.0, fill=False)
fbox2 = mpatches.FancyBboxPatch(xy=(0.12, -0.88), width=0.75, height=0.75, fill=False)
fbox3 = mpatches.FancyBboxPatch(xy=(0.24, -0.76), width=0.5, height=0.5, fill=False)

ax11.add_patch(circle); ax11.add_patch(elipse); ax11.add_patch(rectangle); ax11.add_patch(arc)
ax11.add_patch(wedge); ax11.add_patch(polygon);
ax11.add_patch(arrow); ax11.add_patch(farrow);
ax11.add_patch(fbox); ax11.add_patch(fbox3); ax11.add_patch(fbox2)

fig11.savefig('img9.png', dpi=300, format='png')
