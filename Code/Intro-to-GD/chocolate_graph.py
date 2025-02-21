import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 10, 500)  # x ranges from 0.01 to 10, with 500 points
y = np.log(x) + 4.6 # The natural logarithm of x

plt.plot(x, y, color="#8B4513")
plt.title("A plot of Bob's utility")
plt.xlabel("Chunks of chocolate eaten")
plt.ylabel("Utility")
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()