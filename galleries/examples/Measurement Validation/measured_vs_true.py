"""Measurement vs. True Values with Uncertainty Band.

This example demonstrates how to plot measured data against true values,
fit a linear model, and visualize measurement uncertainty using a shaded
±1σ confidence band. Useful for validating sensor accuracy and quantifying
systematic error and noise.
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate data: true values and noisy measurements
rng = np.random.default_rng(seed=42)
x = np.linspace(0, 10, 30)
y = 2*x + 1 + rng.normal(0, 0.3, x.size)

# Fit linear model
slope, icpt = np.polyfit(x, y, 1)
y_fit = slope*x + icpt

# Calculate residuals and uncertainty (±1σ)
residuals = y - y_fit
sigma = np.std(residuals)
uncertainty = 1.0 * sigma

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot of measured values
ax.scatter(x, y, color='blue', s=50, alpha=0.6, label='Measured values', edgecolors='navy')

# Best-fit line
ax.plot(x, y_fit, color='red', linewidth=2, label=f'Best fit: y={slope:.2f}x+{icpt:.2f}')

# Uncertainty band (±1σ)
ax.fill_between(x, y_fit - uncertainty, y_fit + uncertainty, 
                 color='red', alpha=0.2, label=f'±1σ uncertainty (σ={sigma:.3f})')

# Labels and formatting
ax.set_xlabel('True Value')
ax.set_ylabel('Measured Value')
ax.set_title('Measurement Accuracy: Measured vs. True Values')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
