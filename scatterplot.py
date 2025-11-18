import matplotlib.pyplot as plt
import numpy as np

# Generate random data for scatterplot
x = np.random.rand(200)
y = np.random.rand(200)

# Create scatterplot
plt.scatter(x, y)
plt.title('Devica\'s Scatterbrain!')
plt.xlabel('X values go away')
plt.ylabel('Y values go up')

# Save the plot to a file
plt.savefig('scatterplot.png')
print("Scatterplot saved as scatterplot.png")

plt.show()