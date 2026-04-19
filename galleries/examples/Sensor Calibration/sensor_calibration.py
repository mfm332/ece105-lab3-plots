"""Sensor Calibration Comparison.

This example demonstrates how to generate synthetic temperature sensor data
and compare calibration characteristics between two sensors using visualization
and statistical metrics. Useful for understanding sensor accuracy and drift.
"""

import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path

# Import generate_plots module
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
from generate_plots import generate_data, plot_scatter, plot_histogram

# Generate synthetic sensor data
sensor_a, sensor_b, timestamps = generate_data(seed=2332)

# Compute calibration metrics
valid_mask = ~(np.isnan(sensor_a) | np.isnan(sensor_b))
differences = sensor_a[valid_mask] - sensor_b[valid_mask]
correlation = np.corrcoef(sensor_a[valid_mask], sensor_b[valid_mask])[0, 1]

# Create 2x2 grid visualization
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Line plot
ax1.plot(timestamps, sensor_a, label='Sensor A', alpha=0.8, linewidth=1.5)
ax1.plot(timestamps, sensor_b, label='Sensor B', alpha=0.8, linewidth=1.5)
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Temperature (°C)')
ax1.set_title('Sensor Readings Over Time')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Scatter plot
plot_scatter(ax2, timestamps, sensor_a, sensor_b)

# Histogram
plot_histogram(ax3, sensor_a, sensor_b)

# Calibration metrics summary
ax4.axis('off')
metrics_text = (
    f"Calibration Metrics\n{'='*30}\n"
    f"Mean Diff (A-B): {np.mean(differences):.3f}°C\n"
    f"Std Dev Diff: {np.std(differences):.3f}°C\n"
    f"Max Diff: {np.max(np.abs(differences)):.3f}°C\n"
    f"Correlation: {correlation:.4f}"
)
ax4.text(0.1, 0.5, metrics_text, transform=ax4.transAxes, fontsize=11,
         fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

fig.suptitle('Sensor Calibration Analysis', fontsize=14, fontweight='bold')
fig.tight_layout()

plt.show()
