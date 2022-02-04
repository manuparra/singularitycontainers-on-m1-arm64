import numpy as np
import sys
from scipy.interpolate import splprep, splev

import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

plotname = sys.argv[1] if len(sys.argv)>1 else "example.png"

N = 400
t = np.linspace(0, 3 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel("X value")
plt.ylabel("Y value")
plt.savefig(plotname)
print("-----------------------------------------------")
print("SKA training: Git and Containers")
print("Plot generated in " + plotname + " file.")
print("-----------------------------------------------")
