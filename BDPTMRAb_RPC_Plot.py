import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd

lettersFontsize = 16

# Read CSV file (assuming it has headers)
df = pd.read_csv('Modositott/BODIPYTMRXAbeta42ResourceRPC.csv', sep = "\t", encoding='utf-16')

# Extract X and Y values
timeUV280 = df['UV 1_280'] + 196.69931 - 497.947479 # First addition is for the data to start from zero, second subtraction is to set the injection point to zero
uv280 = df['UV 1_280 Val']
timeCond = df['Cond'] + 196.69931 - 497.947479
cond = df['Cond Val'] * 100
timeConcB = df['Conc B'] + 196.69931 - 497.947479
ConcB = df['Conc B Val']

# Set the axis numbers
fig, ax = plt.subplots(figsize=(10, 8))
# major_ticks_x = np.arange(0, 1000, 10)
# major_ticks_y = np.arange(0, 300, 40) # Ritkább osztásközök
# minor_ticks_x = np.arange(0, 1000, 5)
# minor_ticks_y = np.arange(0, 300, 20) # Ritkább osztásközök

# ax.set_xticks(major_ticks_x)
# ax.set_xticks(minor_ticks_x, minor=True)
# ax.set_yticks(major_ticks_y)
# ax.set_yticks(minor_ticks_y, minor=True)

# Create a simple line plot
ax.plot(timeUV280, uv280, 'g', label='Absorbance at 280 nm (mAU)')
ax.plot(timeCond, cond, 'b', label='Conductance (0.01 mS/cm)')
ax.legend(loc='upper left')

ax.set_xlabel("Volume (ml)", fontsize = lettersFontsize)
ax.set_ylabel("Absorbance (mAU) and Conductance (0.01 mS/cm)", fontsize = lettersFontsize)

# Second Y-axis
ax2 = ax.twinx()
ax2.plot(timeConcB, ConcB, 'm', label='Amount of buffer B (%)')
ax2.legend(loc='upper right')

ax2.set_ylabel("Amount of buffer B (%)", fontsize = lettersFontsize)

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
plt.xlim(0, 550 - 497.947479) # Show only a specific part
plt.show()
