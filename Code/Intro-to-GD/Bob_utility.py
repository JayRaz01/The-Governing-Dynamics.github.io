import matplotlib.pyplot as plt
import numpy as np

# Define the number of chocolate bites (x-axis)
bites = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Define Bob's utility function
bob_utility = np.array([0, 2, 4, 6, 8, 7, 5, 3, 1])

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(bites, bob_utility, marker='o', linestyle='-', color='blue', label="Bob's Utility")

# Customize the plot
plt.xlabel("Bites Eaten")
plt.ylabel("Utility")
plt.title("Bob's Utility Function")
plt.xticks(bites)
plt.yticks(range(0, 11, 2))
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Show the plot
plt.show()
