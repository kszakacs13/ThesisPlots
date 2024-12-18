import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd

lettersFontsize = 24

import matplotlib
matplotlib.rcParams.update({'font.size': 16})

# Read CSV file (assuming it has headers)
df = pd.read_csv('Modositott/Bodipy493Abeta42DeSalt.csv', sep = "\t", encoding='utf-16')

# Extract X and Y values
timeUV280 = df['UV 1_280'] + 66.010132 - (66.010132 + 0.001205) # First addition is for the data to start from zero, second subtraction is to set the injection point to zero
uv280 = df['UV 1_280 Val']
timeUV493 = df['UV 3_493'] + 66.010132 - (66.010132 + 0.001205)
uv493 = df['UV 3_493 Val']
timeCond = df['Cond'] + 66.010132 - (66.010132 + 0.001205)
cond = df['Cond Val'] * 100
timeUV220 = df['UV 2_220'] + 66.010132 - (66.010132 + 0.001205)
uv220 = df['UV 2_220 Val']

# Set the axis numbers
fig, ax = plt.subplots(figsize=(10, 8))
# major_ticks_x = np.arange(0, 160, 10)
# major_ticks_y = np.arange(0, 3800, 250)
# minor_ticks_x = np.arange(0, 160, 5)
# minor_ticks_y = np.arange(0, 3800, 125)

# ax.set_xticks(major_ticks_x)
# ax.set_xticks(minor_ticks_x, minor=True)
# ax.set_yticks(major_ticks_y)
# ax.set_yticks(minor_ticks_y, minor=True)

# Create a simple line plot
ax.plot(timeUV280, uv280, 'g', label='Absorbance at 280 nm (mAU)')
ax.plot(timeUV220, uv220, 'r', label='Absorbance at 220 nm (mAU)')
ax.plot(timeUV493, uv493, 'k', label='Absorbance at 493 nm (mAU)')
# ax.plot(timeCond, cond, 'b', label='Conductance (0.01 mS/cm)')
ax.legend(loc='upper right')

ax.set_ylabel("Absorbance (mAU)", fontsize = lettersFontsize)  # Add X-axis label
ax.set_xlabel("Volume (ml)", fontsize = lettersFontsize)  # Add Y-axis label

# Tick frequency
ax.yaxis.set_major_locator(ticker.MultipleLocator(400))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(200))
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2.5))

#plt.title("Chromatography")  # Add title
#plt.grid(True)
#plt.grid(True, which='both')
plt.xlim(0, 100 - (66.010132 + 0.001205))
plt.show()
