import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load 3D point cloud data from a CSV file
data = pd.read_csv('rabbit_pc.csv')

# Constants
f = 2  # Focal length
v = 2  # Scaling factor for the z-axis in transformations
R = 0.1  # Radius of the circular camera trajectory
alpha = 0.3  # Angular increment for camera positions
nombre_lignes = 110  # Number of horizontal pixel lines
y_min, y_max = -0.75, 0.75  # Vertical limits for the 2D projection
ligne_h = (y_max - y_min) / nombre_lignes  # Height of each pixel-like band

# Load distinct colors for each line
colors = plt.get_cmap('tab20').colors

# Extract 3D points from the data
points = np.array([data['X'], data['Y'], data['Z']]).T

# Create a figure for visualization
fig = plt.figure(figsize=(40, 40))

# 3D visualization of the point cloud
fig1 = fig.add_subplot(121, projection='3d')
fig1.set_title('3D')
fig1.set_xlabel('X')
fig1.set_ylabel('Y')
fig1.set_zlabel('Z')
fig1.scatter(points[:, 0], points[:, 1], points[:, 2], color='blue', marker='p', s=1)

# Convert 3D points to homogeneous coordinates for matrix operations
points_3D_homogenes = np.hstack((points, np.ones((points.shape[0], 1))))

# Create a subplot for 2D projection visualization
fig2 = fig.add_subplot(122)
fig2.set_title('2D')
fig2.set_xlabel('x')
fig2.set_ylabel('y')

# Loop through each pixel-like horizontal line
for Vi in range(nombre_lignes):
    # Compute the angular position of the virtual camera
    theta = Vi / alpha

    # Compute the position of the camera on the circular path
    Ax = R * np.cos(np.radians(theta))
    Ay = R * np.sin(np.radians(theta))
    bx = Ax  # x-offset for translation
    by = Ay  # y-offset for translation

    # Visualize the camera position in the 3D plot
    fig1.scatter(Ax, Ay, 0, color='red', marker='p', s=10, label=f'Camera Pos {Vi}')

    # Transformation matrices
    # Translation matrix for the camera
    Mai1 = np.array([[1, 0, 0, Ax], 
                     [0, 1, 0, Ay], 
                     [0, 0, 1, 0], 
                     [0, 0, 0, 1]])
    
    # Projection matrix with scaling
    Mtl1 = np.array([[1, 0, 0, 0], 
                     [0, 1, 0, 0], 
                     [0, 0, 1, 0], 
                     [0, 0, -1/v, 1]])
    
    # Combined transformation matrix
    Mul1 = np.dot(Mtl1, Mai1)

    # Apply transformations to compute 2D projections
    points_2D_homogenes = []
    for point in points_3D_homogenes:
        z = point[2]  # Extract z-coordinate
        if z != 0:
            # Perspective projection matrix
            Mpp1 = np.array([[-f / z, 0, -bx, 0], 
                             [0, -f / z, -by, 0], 
                             [0, 0, -1 / z, 0]])
            # Combine with other transformations
            M1 = np.dot(Mpp1, Mul1)
            point_2D_homogene = np.dot(M1, point)  # Transform the point
            points_2D_homogenes.append(point_2D_homogene)
        else:
            # Handle cases where z = 0
            points_2D_homogenes.append(np.zeros(4))

    points_2D_homogenes = np.array(points_2D_homogenes)

    # Convert from homogeneous to Cartesian coordinates
    x_2D = points_2D_homogenes[:, 0] / points_2D_homogenes[:, 2]
    y_2D = points_2D_homogenes[:, 1] / points_2D_homogenes[:, 2]

    # Determine the range for the current horizontal line
    ligne_y_min = y_min + Vi * ligne_h
    ligne_y_max = ligne_y_min + ligne_h
    
    # Filter points that fall within the current line
    bande = (y_2D >= ligne_y_min) & (y_2D < ligne_y_max)
    x_2D_ligne = x_2D[bande]
    y_2D_ligne = y_2D[bande]

    # Apply translation to the filtered points
    translation_matrix = np.array([[1, 0, bx], 
                                    [0, 1, by], 
                                    [0, 0, 1]])
    points_2D = np.vstack((x_2D_ligne, y_2D_ligne, np.ones_like(x_2D_ligne)))
    points_2D_translated = translation_matrix @ points_2D

    # Extract translated coordinates
    x_2D_translated = points_2D_translated[0, :]
    y_2D_translated = points_2D_translated[1, :]

    # Assign a distinct color to the current line
    color = colors[Vi % len(colors)]
    fig2.scatter(x_2D_translated, y_2D_translated, color=color, marker='+', s=10)

# Add gridlines and adjust the visualizations
fig2.axhline(0, color='black', linewidth=0.5)
fig2.axvline(0, color='black', linewidth=0.5)
fig2.set_aspect('equal', adjustable='box')
fig2.grid()

# Improve layout and display the plots
plt.tight_layout()
plt.show()
