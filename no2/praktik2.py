print("\033c")
import numpy as np
from matplotlib import pyplot as plt

# ===User Entries===#
nama_file = "last"
threshold = 15

# User decide the rotation angles in degree #
alfa_start = 30;beta_start = 30
delta_alfa = 30;delta_beta = 30
no_of_rotations = 1

cam_focal = 400

# User decides the cam positions considering that 3D room Border
# Z = 8 and at the leftmost 3D Voxel, Z = Lengthe
# E.G CAM_z = -5 * LENGTH mean that the Cam resides far behind The 3D Room border
cam_z = -120
print("cam_z =", cam_z)

# ===Preparation===#
voxel = np.load(nama_file + "_0_0.npy")
print("voxel.shape =", voxel.shape)
maks = max(voxel.shape)
col, row, length = maks, maks, maks  # Be ensure making a cubic 3D Space and a square 2D Screen

# Preparing the template for 2D Screen (Black) #
pixel = np.zeros(shape=(row, col, 3), dtype=np.uint8)

print('col, row, length =', col, ',', row, ',', length)
cx = round(0.5 * col);
cy = round(0.5 * row)
print('cx, cy =', cx, ',', cy)

# The 2D Screen positions is fixed, that is, analogous the real sensor residing at the cam's focal #
room_border_z = 0  # The z positions of the 3D room's border its 0.
print('room_border_z =', room_border_z)

# Deciding the size of the 2D Screen
col = col;row = row

# ===Defining the function for backward projection===#
def projection(cx, cy, cam_z, screen_z, px, py, vz):
    pz = screen_z
    vx = round(cx + (cx - px) * ((vz - cam_z) / (cam_z - pz)))
    vy = round(cy + (cy - py) * ((vz - cam_z) / (cam_z - pz)))
    return vx,vy


# ===Main Program===#
cam_z = -280  # -420
alfa = alfa_start
beta = beta_start
for i in range(1, no_of_rotations + 1):
    pixel[:, :, :] = 0  # Put the 2D Screen back to black
    voxel = np.load(nama_file + "_" + str(alfa) + "_" + str(beta) + ".npy")
    screen_z = cam_z - cam_focal
    print('cam_z =', cam_z);print('screen_z =', screen_z)
    print('NOW PROJECTING: FROM 2D SCREEN CAM TO 3D OBJECT')
    print('Finding vx and vy of the 3D Object that coralates with every pixel of 2D Screen')
    for px in range(0, col):  # x of a pixel of the 2D Screen
        print('alfa =', alfa, ', beta =', beta, ', px =', px)
        for py in range(0, row):  # y of that pixel
            for vz in range(0, length):  # z of voxel of the corelating 3D object
                # Starting from 3D room's border(right to left)
                vx, vy = projection(cx, cy, cam_z, screen_z, px, py, vz)  # Projection
                if (vy >= 0 and vy < row and vx >= 0 and vx < col) and \
                        (int(voxel[vy, vx, vz, 0]) + int(voxel[vy, vx, vz, 1]) + int(voxel[vy, vx, vz, 2]) > threshold):
                    pixel[row - py - 1, col - px - 1, :] = voxel[vy, vx, vz, :]
                    break
    plt.imsave(nama_file + "_" + str(alfa) + ("_") + str(beta) + ("_") + str(cam_z) + ".jpg", pixel)
    alfa = alfa + delta_alfa
    beta = beta + delta_beta

plt.figure(1)
plt.imshow(pixel)
plt.show()
