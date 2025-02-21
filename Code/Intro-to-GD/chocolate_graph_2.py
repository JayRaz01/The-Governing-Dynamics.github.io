import numpy as np
import matplotlib.pyplot as plt

# Define the custom function
def custom_function(x):
    a = 4  # Controls the steepness of the fall after the peak
    return np.log(x+36) + 5.35 - (x - 6)**2 / a

# Generate x values
x = np.linspace(0.01, 10, 500)
# Calculate y values using the custom function
y = custom_function(x)

# Plot the function
plt.plot(x, y, color="#8B4513")
plt.title("A plot of Mary's utility")
plt.xlabel("Chunks of chocolate eaten")
plt.ylabel("Utility")
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()