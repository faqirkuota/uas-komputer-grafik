print("\033c")
import numpy as np
from matplotlib import pyplot as plt

# User Entries #
nama_file = "last"
threshold = 15
alfa_start = 30;beta_start = 30
delta_alfa = 30;delta_beta = 30
no_of_rotations = 1


pic = plt.imread(nama_file+".jpg")
pic = pic.astype(int)
plt.figure(1)
plt.imshow(pic)

# Creatin 3D from 2D Picture #
print("Creating a 3D Model");print("")

# User Decide The Size 3D Room and 2D Screen #
ROW,COL,DEPTH=pic.shape
LENGTH = COL
row = ROW-1; col = COL-1; length = LENGTH-1; depth = DEPTH-1
half_length = round(length/2)
print(ROW,COL,LENGTH,DEPTH)

# Creating the template matrix for 3D Model #
voxel = np.zeros(shape=(row,col,length,3),dtype=np.uint8) #Template for 3D Model
buffer = np.zeros(shape=(row,col,length,3),dtype=np.uint8) #Template for 3D Buffer
slice = np.zeros(shape=(row,col,3),dtype=np.uint8) #Template for Slice cut

# Photocopying #
voxel[0:row,0:col,200, :]=pic[0:row, 0:col, :]
for k in range (190,210):
    voxel[0:row,0:col,k, 0:]=voxel[0:row,0:col,200, 0:]

# Visualizing the cross slice at the half length #
slice[:,:,:] = voxel[half_length,:,:,:]
plt.figure("Horizontal Cross-cut (1)");plt.imshow(slice)

# Visualizing the cross slice at the half length #
slice[:,:,:] = voxel[:,half_length,:, :]
plt.figure("Vertical Cross-cut (1)"); plt.imshow(slice)

# Visualizing the cross slice at the half length #
slice[:,:,:]=voxel[:,:,half_length, :]
plt.figure("Vertical Cross-cut (2)"); plt.imshow(slice)

plt.ion()
plt.show()
plt.pause(2)

np.save(nama_file+".npy",voxel)
np.save(nama_file+"_0_0.npy",voxel)

#===Defining Function For Degree conversion and rotation===#
# Converting degree unit of alfa and beta radiant unit#
def degree_to_rad(alfa, beta):
    alfa_rad = (alfa / 100) * np.pi
    beta_rad = (beta / 100) * np.pi
    return alfa_rad, beta_rad


# Function to rotate voxel (xx,xv,vz) about a defined center (cx,cy,cz) as much as alfa rad
# Around Z-Axis then as much as beta rad around X-Axis
def rotate(vx, vy, vz, cx, cy, cz, alfa_rad, beta_rad):
    # Converting point's coordinate to be relative to the rotation center
    # So that the rotation matrix can be applied correctly.
    vx = vx - cx;vy = vy - cy;vz = vz - cz

    k = 0.6  # Correction Factor
    # Rotation 1 - Rotating the point as much as alfa around Z-Axis
    vx = int(np.cos(alfa_rad * k) * vx + np.sin(alfa_rad * k) * vy)
    vz = int(-np.sin(alfa_rad * k) * vx + np.cos(alfa_rad * k) * vy)
    vz = vz  # The Z-Coordinate of the voxel does not change

    # Rtation 2 - Rotating the point as much as beta around X-Axis
    vz = int(np.cos(beta_rad * k) * vz + np.sin(beta_rad * k) * vy)
    vz = int(-np.sin(beta_rad * k) * vz + np.cos(beta_rad * k) * vy)
    vz = vz  # The X-Coordinate of the voxel does not change

    # Converting point's coordinate back, relative to(8,0,8)
    vx = vx + cx;vy = vy + cy;vz = vz + cz
    return vx, vy, vz


# ===Main Program To Rotate The 3D Object===#
# The object is rotated with the same angle over and over again acc. to number of rotations#
cx = round(col / 2);cy = round(row / 2);cz = round(length / 2)  # Center of 3D Object rotation

alfa = alfa_start
beta = beta_start

for r in range(1, no_of_rotations + 1):
    alfa_rad, beta_rad = degree_to_rad(alfa, beta)  # Convert degree to rad
    voxel = np.load(nama_file + ".npy")  # always read original model

    for i in range(0, col):
        print('alfa=', alfa, 'beta=', beta, ', now rotating voxels in coloumn', i, '.')
        for j in range(0, row):
            for k in range(0, length):
                cek1 = int(voxel[i, j, k, 0])
                cek2 = int(voxel[i, j, k, 1])
                cek3 = int(voxel[i, j, k, 2])
                if (cek1 + cek2 + cek3) > threshold:
                    u, v, w = rotate(i, j, k, cx, cy, cz, alfa_rad, beta_rad)  # Rotate every voxel
                    buffer[u, v, w, :] = voxel[i, j, k, :]
                    voxel[i, j, k, :] = 0
    # Result of one time rotation of object is ready for next rotation
    np.save(nama_file + "_" + str(alfa) + "_" + str(beta) + ".npy", buffer)
    voxel[:, :, :] = 0  # Must be put back to black
    buffer[:, :, :] = 0  # Must be put back to black
    alfa = alfa + delta_alfa
    beta = beta + delta_beta

plt.show()
