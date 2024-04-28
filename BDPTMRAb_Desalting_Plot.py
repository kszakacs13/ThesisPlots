import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

# Read CSV file (assuming it has headers)
df = pd.read_csv('Modositott/BODIPYTMR-X_Abeta42_HiTrap-Desaltin_Kristof.csv', sep = "\t", encoding='utf-16')

# Extract X and Y values
timeUV280 = df['UV 1_280'] + 60.727486
uv280 = df['UV 1_280 Val']
timeUV544 = df['UV 3_544'] + 60.727486
uv544 = df['UV 3_544 Val']
timeCond = df['Cond'] + 60.727486
cond = df['Cond Val'] * 100
timeUV214 = df['UV 2_214'] + 60.727486
uv214 = df['UV 2_214 Val']

# Set the axis numbers
fig, ax = plt.subplots(figsize=(10, 8))
major_ticks_x = np.arange(0, 180, 10)
major_ticks_y = np.arange(0, 3000, 200)
minor_ticks_x = np.arange(0, 180, 5)
minor_ticks_y = np.arange(0, 3000, 100)

ax.set_xticks(major_ticks_x)
ax.set_xticks(minor_ticks_x, minor=True)
ax.set_yticks(major_ticks_y)
ax.set_yticks(minor_ticks_y, minor=True)

# Create a simple line plot
plt.plot(timeUV280, uv280, 'g', label='Absorbance at 280 nm (mAU)')
plt.plot(timeUV214, uv214, 'r', label='Absorbance at 214 nm (mAU)')
plt.plot(timeUV544, uv544, 'k', label='Absorbance at 544 nm (mAU)')
plt.plot(timeCond, cond, 'b', label='Conductance (100 mS/cm)')
plt.legend()

plt.ylabel("Absorbance (mAU) and Conductance (100 mS/cm)")  # Add X-axis label
plt.xlabel("Volume (ml)")  # Add Y-axis label
#plt.title("Chromatography")  # Add title
plt.grid(True)
#plt.grid(True, which='both')
plt.show()
