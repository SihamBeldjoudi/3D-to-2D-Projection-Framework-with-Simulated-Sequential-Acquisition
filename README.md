**3D-to-2D Projection Framework with Simulated Sequential Acquisition**  

#### **Detailed Description**  

This project provides a Python-based simulation tool designed to project 3D point cloud data into 2D space, replicating the behavior of sequential acquisition systems, such as those found in rolling shutter cameras. The simulation employs a series of virtual cameras positioned along a circular trajectory to create pixel-like horizontal bands in the 2D projection.  

The framework supports any 3D point cloud dataset and is highly customizable, offering users the ability to modify parameters such as focal length, camera radius, number of pixel lines, and the angular increments between virtual camera positions.  

### **Features**  

1. **3D-to-2D Projection**  
   - Converts 3D point cloud data into 2D space using mathematical transformations.  
   - Each 2D projection is divided into horizontal bands, mimicking pixel rows.  

2. **Dynamic Camera Simulation**  
   - Virtual cameras are arranged in a circular trajectory around the dataset.  
   - Cameras capture the 3D data sequentially, introducing motion-like transformations.  

3. **Visualization Tools**  
   - **3D Plot**: Displays the original 3D point cloud along with camera positions.  
   - **2D Plot**: Shows the sequentially projected 2D points, organized into pixel bands.  

4. **Customizable Parameters**  
   - Adjustable focal length, number of bands, and camera angular increments.  
   - Allows users to adapt the simulation to various scenarios and datasets.  

5. **Distinct Band Coloring**  
   - Each horizontal band is assigned a unique color for clarity in the 2D visualization.  

### **How It Works**  

1. **Input Data**:  
   - A CSV file containing 3D point cloud data with columns `X`, `Y`, and `Z`.  

2. **Circular Camera Path**:  
   - Virtual cameras are placed along a circle of configurable radius (`R`).  
   - Cameras capture the dataset from different angles, with their positions defined by angular increments (`alpha`).  

3. **Transformations**:  
   - The tool uses homogeneous coordinates and transformation matrices to project 3D points onto 2D planes.  
   - Each 3D point is translated and scaled based on the current camera's position.  

4. **Pixel Bands**:  
   - The 2D plane is divided into horizontal pixel-like bands, with points grouped and filtered by their vertical position (`y`).  

5. **Translation**:  
   - Projected points are further translated in 2D to simulate motion-like effects.  

### **Applications**  

- **Sequential Acquisition Simulation**:  
   - Emulates how real-world sensors capture 3D data sequentially, like rolling shutter systems.  

- **3D Data Analysis**:  
   - Provides a visual representation of 3D datasets under different projection parameters.  

- **Educational Tool**:  
   - Helps users understand key concepts in geometric transformations and camera projections.  

### **Requirements**  

- **Python Libraries**:  
  - `pandas`: For reading and handling CSV data.  
  - `numpy`: For numerical computations and matrix operations.  
  - `matplotlib`: For creating 3D and 2D visualizations.  

- **Input File**:  
  - A CSV file containing 3D point data in columns `X`, `Y`, and `Z`.  

### **How to Use**  

1. **Prepare Data**:  
   - Format your dataset as a CSV file with `X`, `Y`, and `Z` columns.  

2. **Adjust Parameters**:  
   - Modify constants in the script such as `f` (focal length), `R` (radius), and `nombre_lignes` (number of pixel lines) to fit your dataset and goals.  

3. **Run the Code**:  
   - Execute the script to generate both 3D and 2D visualizations.  

4. **Interpret the Results**:  
   - Use the 3D plot to understand the spatial distribution of points and camera positions.  
   - Analyze the 2D plot to see how the dataset is captured sequentially and grouped into pixel bands.  

### **Customization Options**  

- **`f` (focal length)**: Adjusts the scaling of the perspective projection.  
- **`R` (radius)**: Sets the distance of the cameras from the dataset.  
- **`alpha` (angular increment)**: Controls the density of camera positions around the circle.  
- **`nombre_lignes` (number of pixel bands)**: Defines the vertical resolution of the 2D projection.  
- **`ligne_h` (band height)**: Configures the vertical size of each band in 2D.  

### **Future Enhancements**  

- Add support for time-dependent point clouds to simulate dynamic motion.  
- Extend the framework to include other acquisition modes, such as global shutter.  
- Enable advanced visual effects like motion blur or depth of field.  
- Support for non-circular camera trajectories and irregular point cloud geometries.  
