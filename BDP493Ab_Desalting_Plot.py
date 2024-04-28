import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

# Read CSV file (assuming it has headers)
df = pd.read_csv('Modositott/Bodipy493Abeta42DeSalt.csv', sep = "\t", encoding='utf-16')

# Extract X and Y values
timeUV280 = df['UV 1_280'] + 66.010132
uv280 = df['UV 1_280 Val']
timeUV493 = df['UV 3_493'] + 66.010132
uv493 = df['UV 3_493 Val']
timeCond = df['Cond'] + 66.010132
cond = df['Cond Val'] * 100
timeUV220 = df['UV 2_220'] + 66.010132
uv220 = df['UV 2_220 Val']

# Set the axis numbers
fig, ax = plt.subplots(figsize=(10, 8))
major_ticks_x = np.arange(0, 160, 10)
major_ticks_y = np.arange(0, 3800, 250)
minor_ticks_x = np.arange(0, 160, 5)
minor_ticks_y = np.arange(0, 3800, 125)

ax.set_xticks(major_ticks_x)
ax.set_xticks(minor_ticks_x, minor=True)
ax.set_yticks(major_ticks_y)
ax.set_yticks(minor_ticks_y, minor=True)

# Create a simple line plot
plt.plot(timeUV280, uv280, 'g', label='Absorbance at 280 nm (mAU)')
plt.plot(timeUV220, uv220, 'r', label='Absorbance at 220 nm (mAU)')
plt.plot(timeUV493, uv493, 'k', label='Absorbance at 493 nm (mAU)')
plt.plot(timeCond, cond, 'b', label='Conductance (100 mS/cm)')
plt.legend()

plt.ylabel("Absorbance (mAU) and Conductance (100 mS/cm)")  # Add X-axis label
plt.xlabel("Volume (ml)")  # Add Y-axis label
#plt.title("Chromatography")  # Add title
plt.grid(True)
#plt.grid(True, which='both')
plt.show()
