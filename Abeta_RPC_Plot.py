import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

# Read CSV file (assuming it has headers)
df = pd.read_csv('Modositott/Abeta_source15rpc_231017.csv', sep = "\t", encoding='utf-16')

# Extract X and Y values
timeUV280 = df['UV 1_280'] + 224.247726  # Replace 'X_column_name' with the actual column name
uv280 = df['UV 1_280 Val']  # Replace 'Y_column_name' with the actual column name
timeCond = df['Cond'] + 224.247726
cond = df['Cond Val'] * 100
timeUV220 = df['UV 2_220'] + 224.247726
uv220 = df['UV 2_220 Val']

# Set the axis numbers
fig, ax = plt.subplots(figsize=(10, 8))
major_ticks_x = np.arange(0, 500, 25)
major_ticks_y = np.arange(0, 3500, 250)
minor_ticks_x = np.arange(0, 500, 12.5)
minor_ticks_y = np.arange(0, 3500, 125)

ax.set_xticks(major_ticks_x)
ax.set_xticks(minor_ticks_x, minor=True)
ax.set_yticks(major_ticks_y)
ax.set_yticks(minor_ticks_y, minor=True)

# Create a simple line plot
plt.plot(timeUV280, uv280, 'g', label='Absorbance at 280 nm (mAU)')
plt.plot(timeUV220, uv220, 'r', label='Absorbance at 220 nm (mAU)')
plt.plot(timeCond, cond, 'b', label='Conductance (100 mS/cm)')
plt.legend()

plt.ylabel("Absorbance (mAU) and Conductance (100 mS/cm)")  # Add X-axis label
plt.xlabel("Volume (ml)")  # Add Y-axis label
#plt.title("Chromatography")  # Add title
plt.grid(True)
#plt.grid(True, which='both')
plt.show()