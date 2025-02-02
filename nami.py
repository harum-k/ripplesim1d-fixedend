# fixed end refrections
# 固定端反射

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

BOXWIDTH = 100

fig, ax = plt.subplots(figsize=(12.8, 7.2))

y = np.zeros(BOXWIDTH)

line, = ax.plot(y)
ax.set_ylim(-1,1)

y1 = y.copy()
k = y.copy()
y[20] = 4.0
y[70] = -2.0

def update(i):
    global y,y1,k
    for j in range(1,BOXWIDTH-1):
        y1[j] = np.average(y[j-1:j+2]) + k[j]
    if i > 4:
        k = y1 - y
    y = y1.copy()
    line.set_ydata(y)
    filbet = ax.fill_between(np.arange(BOXWIDTH), y, -1.0, animated=True, facecolor='C0')
    return line,filbet

ani = animation.FuncAnimation(fig, update, interval=50, blit=True, save_count=1400)
#ani.save("nami.mp4")
plt.show()
