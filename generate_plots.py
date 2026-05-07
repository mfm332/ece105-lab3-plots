"""Generate synthetic sensor data and create visualization plots.

This module provides functions to generate synthetic temperature sensor data
and create various visualization plots including scatter, histogram, and boxplot.
"""

import matplotlib.pyplot as plt
import numpy as np


def generate_data(seed):
    """Generate synthetic temperature sensor data.

    Creates realistic sensor readings with noise, drift, and missing values
    to simulate real-world sensor characteristics.

    Parameters
    ----------
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    time : ndarray
        Time values (0 to 10 seconds, 200 samples).
    sensor_a : ndarray
        Temperature readings from Sensor A (°C) with noise and drift.
    sensor_b : ndarray
        Temperature readings from Sensor B (°C) with noise and drift.
    """
    np.random.seed(seed)
    time = np.linspace(0, 10, 200)

    base_a = 20 + 0.5 * np.sin(2 * np.pi * 0.05 * time) + 0.005 * time
    base_b = 50 + 1.0 * np.sin(2 * np.pi * 0.02 * time + 0.7) + 0.01 * time

    noise_a = 0.2 * np.random.normal(size=200)
    noise_b = 0.4 * np.random.normal(size=200)

    sensor_a = base_a + noise_a
    sensor_b = base_b + noise_b

    spike_indices = np.random.choice(200, 5, replace=False)
    sensor_a[spike_indices] += np.random.uniform(2, 5, 5)

    missing_indices = np.random.choice(200, 10, replace=False)
    sensor_a[missing_indices] = np.nan
    sensor_b[missing_indices] = np.nan

    return time, sensor_a, sensor_b


def plot_scatter(ax, time, sensor_a, sensor_b):
    """Plot scatter visualization of sensor data over time.

    Modifies the given axes in place to display sensor readings as scatter points.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to modify.
    time : ndarray
        Time values.
    sensor_a : ndarray
        Temperature readings from Sensor A.
    sensor_b : ndarray
        Temperature readings from Sensor B.

    Returns
    -------
    None
    """
    valid_mask = ~(np.isnan(sensor_a) | np.isnan(sensor_b))
    ax.scatter(time[valid_mask], sensor_a[valid_mask], color='blue', s=4, alpha=0.6, label='Sensor A')
    ax.scatter(time[valid_mask], sensor_b[valid_mask], color='orange', s=4, alpha=0.6, label='Sensor B')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Scatter Plot: Sensor Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3)


def plot_histogram(ax, sensor_a, sensor_b):
    """Plot histogram distribution of sensor data.

    Modifies the given axes in place to display overlaid histograms for both sensors.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to modify.
    sensor_a : ndarray
        Temperature readings from Sensor A.
    sensor_b : ndarray
        Temperature readings from Sensor B.

    Returns
    -------
    None
    """
    valid_mask_a = ~np.isnan(sensor_a)
    valid_mask_b = ~np.isnan(sensor_b)
    ax.hist(sensor_a[valid_mask_a], bins=30, alpha=0.5, color='blue', label='Sensor A')
    ax.hist(sensor_b[valid_mask_b], bins=30, alpha=0.5, color='orange', label='Sensor B')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram: Temperature Distribution')
    ax.legend()
    ax.grid(True, alpha=0.3)


def plot_boxplot(ax, sensor_a, sensor_b):
    """Plot boxplot comparison of sensor data distributions.

    Modifies the given axes in place to display boxplots for both sensors.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to modify.
    sensor_a : ndarray
        Temperature readings from Sensor A.
    sensor_b : ndarray
        Temperature readings from Sensor B.

    Returns
    -------
    None
    """
    valid_mask_a = ~np.isnan(sensor_a)
    valid_mask_b = ~np.isnan(sensor_b)
    data = [sensor_a[valid_mask_a], sensor_b[valid_mask_b]]
    ax.boxplot(data, labels=['Sensor A', 'Sensor B'])
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Boxplot: Sensor Comparison')
    ax.grid(True, alpha=0.3, axis='y')


def main():
    """Generate data and create visualization plots.

    Creates a 2x2 grid of plots showing scatter, histogram, boxplot,
    and calibration metrics for synthetic sensor data.

    Returns
    -------
    None
    """
    time, sensor_a, sensor_b = generate_data(seed=42)

    valid_mask = ~(np.isnan(sensor_a) | np.isnan(sensor_b))
    differences = sensor_a[valid_mask] - sensor_b[valid_mask]
    correlation = np.corrcoef(sensor_a[valid_mask], sensor_b[valid_mask])[0, 1]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

    ax1.plot(time, sensor_a, label='Sensor A', alpha=0.8, linewidth=1.5)
    ax1.plot(time, sensor_b, label='Sensor B', alpha=0.8, linewidth=1.5)
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel('Temperature (°C)')
    ax1.set_title('Sensor Readings Over Time')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    plot_scatter(ax2, time, sensor_a, sensor_b)
    plot_histogram(ax3, sensor_a, sensor_b)

    plot_boxplot(ax4, sensor_a, sensor_b)

    fig.suptitle('Sensor Data Analysis', fontsize=14, fontweight='bold')
    fig.tight_layout()

    plt.savefig('sensor_plots_grid.png', dpi=150, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()
