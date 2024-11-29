import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 500)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='Sine', color='blue', linewidth=2)
plt.plot(x, y_cos, label='Cosine', color='red', linestyle='--', linewidth=2)

plt.title('Sine and Cosine Graph', fontsize=16)
plt.xlabel('x (radians)', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Add horizontal axis
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Add vertical axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()
