# This is an exemple of how to use Numpy and MatplotLib
# Improting numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

#Creating 1000 numbers between 0 and 10
x = np.linspace(0, 10, 1000)

#Creating sine and cosine curves, using sin and cos function
y1 = np.sin(x)
y2 = np.cos(x)

#Plotting the curves and naming them
plt.plot(x, y1, "-b", label="sine")
plt.plot(x, y2, "-r", label="cosine")

#Legend
plt.legend(loc="upper left")
plt.ylim(-1.5, 2.0)

#Showing the graph
plt.show()