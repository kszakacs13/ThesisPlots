import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd

lettersFontsize = 16

# Read CSV file (assuming it has headers)
df = pd.read_csv('Modositott/BODIPYTMR-X_Abeta42_HiTrap-Desaltin_Kristof.csv', sep = "\t", encoding='utf-16')

# Extract X and Y values
timeUV280 = df['UV 1_280'] + 60.727486 - (60.727486 + 33.298927) # First addition is for the data to start from zero, second subtraction is to set the injection point to zero
uv280 = df['UV 1_280 Val']
timeUV544 = df['UV 3_544'] + 60.727486 - (60.727486 + 33.298927)
uv544 = df['UV 3_544 Val']
timeCond = df['Cond'] + 60.727486 - (60.727486 + 33.298927)
cond = df['Cond Val'] * 100
timeUV214 = df['UV 2_214'] + 60.727486 - (60.727486 + 33.298927)
uv214 = df['UV 2_214 Val']

# Set the axis numbers
fig, ax = plt.subplots(figsize=(10, 8))
# major_ticks_x = np.arange(0, 180, 10)
# major_ticks_y = np.arange(0, 3000, 200)
# minor_ticks_x = np.arange(0, 180, 5)
# minor_ticks_y = np.arange(0, 3000, 100)

# ax.set_xticks(major_ticks_x)
# ax.set_xticks(minor_ticks_x, minor=True)
# ax.set_yticks(major_ticks_y)
# ax.set_yticks(minor_ticks_y, minor=True)

# Create a simple line plot
ax.plot(timeUV280, uv280, 'g', label='Absorbance at 280 nm (mAU)')
ax.plot(timeUV214, uv214, 'r', label='Absorbance at 214 nm (mAU)')
ax.plot(timeUV544, uv544, 'k', label='Absorbance at 544 nm (mAU)')
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
plt.xlim(0, 125 - (60.727486 + 33.298927))
plt.show()
