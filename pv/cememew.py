import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import random

def update_bars(num, bars):
    i = random.randint(0, 2)
    dz[i] += 0.1
    bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['r', 'g', 'b']))
    return bars

fig = plt.figure()
ax = p3.Axes3D(fig)
xpos = [1, 1, 3, 3]
ypos = [1, 3, 1, 3]
zpos = [0, 0, 0, 0]
dx = [1, 1, 1, 1]
dy = [1, 1, 1, 1]
dz = []

# add bars
bars = []
for i in range(1):
    if(dz[i]>=0 and dz[i]<=5):
        bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color='r'))
    elif(dz[i]>=5 and dz[i]<=7):
        bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color='b'))
    elif (dz[i] >= 7 and dz[i] <= 10):
        bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color='g'))
ax.set_title('Matrix Penilaian Siswa')

line_ani = animation.FuncAnimation(fig, update_bars, 20, fargs=[bars], interval=100, blit=False)
plt.show()