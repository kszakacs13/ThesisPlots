import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd

lettersFontsize = 24

import matplotlib
matplotlib.rcParams.update({'font.size': 16})

# Read CSV file (assuming it has headers)
df = pd.read_csv('Modositott/Bodipy493Abeta42ResourceRPC.csv', sep = "\t", encoding='utf-16')

# Extract X and Y values
timeUV280 = df['UV 1_280'] + 174.407364 - 174.410156 # First addition is for the data to start from zero, second subtraction is to set the injection point to zero
uv280 = df['UV 1_280 Val']
timeUV493 = df['UV 3_493'] + 174.407364 - 174.410156
uv493 = df['UV 3_493 Val']
timeCond = df['Cond'] + 174.407364 - 174.410156
cond = df['Cond Val'] * 100
timeUV220 = df['UV 2_220'] + 174.407364 - 174.410156
uv220 = df['UV 2_220 Val']
timeConcB = df['Conc B'] + 174.407364 - 174.410156
ConcB = df['Conc B Val']

# Set the axis numbers
fig, ax = plt.subplots(figsize=(10, 8))
# major_ticks_x = np.arange(0, 350, 10)
# major_ticks_y = np.arange(0, 300, 50)
# minor_ticks_x = np.arange(0, 350, 5)
# minor_ticks_y = np.arange(0, 300, 25)

# ax.set_xticks(major_ticks_x)
# ax.set_xticks(minor_ticks_x, minor=True)
# ax.set_yticks(major_ticks_y)
# ax.set_yticks(minor_ticks_y, minor=True)

# Create a simple line plot
# ax.plot(timeUV280, uv280, 'g', label='Absorbance at 280 nm (mAU)')
ax.plot(timeUV220, uv220, 'r', label='Absorbance at 220 nm (mAU)')
ax.plot(timeUV493, uv493, 'k', label='Absorbance at 493 nm (mAU)')
ax.legend(loc='upper left')

ax.set_xlabel("Volume (ml)", fontsize = lettersFontsize)
ax.set_ylabel("Absorbance (mAU)", fontsize = lettersFontsize)

# Second Y-axis
ax2 = ax.twinx()
ax2.plot(timeConcB, ConcB, 'm', label='Buffer B %')
ax2.legend(loc='upper right')

ax2.set_ylabel("B %", fontsize = lettersFontsize)

# Tick frequency
ax.yaxis.set_major_locator(ticker.MultipleLocator(40))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(25))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

#plt.title("Chromatography")  # Add title
#plt.grid(True)
#plt.grid(True, which='both')
plt.xlim(0, 250 - 174.410156) # Show only a specific part
plt.show()
