import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
print(x)

sin_y = np.sin(x)
cos_y = np.cos(x)


# Plot the graph
plt.figure(figsize=(12, 5))
plt.style.use("fivethirtyeight")

plt.plot(x, sin_y, label="sin(x)")
plt.plot(x, cos_y, label="cos(x)")

# Add labels, title, and grid
plt.title("Trigonometry Functions", fontsize=16)
plt.xlabel("x (radians)", fontsize=12)
plt.ylabel("sin(x)", fontsize=12)

# show origin
plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")
plt.axvline(0, color="gray", linewidth=0.8, linestyle="--")
plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig("plots/sin_cos.png")
plt.show()
