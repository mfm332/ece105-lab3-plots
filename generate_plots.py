import numpy as np
import matplotlib.pyplot as plt

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.


def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    # Set random seed for reproducibility
    np.random.seed(seed)
    
    n = 200
    # Generate timestamps uniformly from 0 to 10 seconds
    timestamps = np.linspace(0, 10, n)
    t = timestamps
    
    # Sensor A: base 20 C + 0.5 A sine wave (0.05 Hz) + 0.005*t drift + Gaussian noise
    sensor_a = 20 + 0.5*np.sin(2*np.pi*0.05*t) + 0.005*t + 0.2*np.random.randn(n)
    
    # Sensor B: base 50 C + 1.0 A sine wave (0.02 Hz, phase shift) + 0.01*t drift + Gaussian noise
    sensor_b = 50 + 1.0*np.sin(2*np.pi*0.02*t + 0.7) + 0.01*t + 0.4*np.random.randn(n)
    
    # Add random spikes (~30 samples) to both sensors
    num_spikes = 30
    spike_idx = np.random.choice(n, num_spikes, replace=False)
    sensor_a[spike_idx] += np.random.choice([+8, -8], size=num_spikes) * np.random.rand(num_spikes)
    sensor_b[spike_idx] += np.random.choice([+8, -8], size=num_spikes) * np.random.rand(num_spikes)
    
    # Add missing values (~2% of samples)
    missing_idx = np.random.choice(n, size=int(0.02*n), replace=False)
    sensor_a[missing_idx] = np.nan
    sensor_b[missing_idx] = np.nan
    
    return sensor_a, sensor_b, timestamps


def plot_scatter(ax, timestamps, sensor_a, sensor_b):
    """Plot sensor data as scatter points on an Axes object.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to plot on. Modified in place.
    timestamps : numpy.ndarray
        Time values in seconds, shape (200,).
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).

    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, color='blue', s=4, alpha=0.6, label='Sensor A')
    ax.scatter(timestamps, sensor_b, color='orange', s=4, alpha=0.6, label='Sensor B')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Scatter Plot: Synthetic Temperature Sensor Data')
    ax.legend()
    ax.grid(True, alpha=0.3)

# Create a function plot_histogram(ax, sensor_a, sensor_b) that plots histograms
# of both sensors on an Axes object, modified in place, returning None.


def plot_histogram(ax, sensor_a, sensor_b):
    """Plot histogram distributions of sensor data on an Axes object.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to plot on. Modified in place.
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).

    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color='blue', label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, color='orange', label='Sensor B')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram: Temperature Distribution')
    ax.legend()
    ax.grid(True, alpha=0.3)




# Create a main() function that generates synthetic data, prints statistics,
# and creates two plots (line plot and scatter/histogram plots) using the
# plot_scatter and plot_histogram functions.


def main():
    """Generate synthetic sensor data and create visualization plots.

    This function generates synthetic temperature sensor data using the
    generate_data function, prints summary statistics, and creates a single
    figure with four subplots arranged in a 2×2 grid: line plot, scatter plot,
    histogram, and summary statistics.

    Returns
    -------
    None
    """
    # Generate synthetic data
    sensor_a, sensor_b, timestamps = generate_data(seed=2332)

    # Print statistics
    print(f"sensor_a shape: {sensor_a.shape}, dtype: {sensor_a.dtype}")
    print(f"sensor_b shape: {sensor_b.shape}, dtype: {sensor_b.dtype}")
    print(f"timestamps shape: {timestamps.shape}, dtype: {timestamps.dtype}")
    print(f"\nFirst 5 sensor_a values: {sensor_a[:5]}")
    print(f"First 5 sensor_b values: {sensor_b[:5]}")
    print(f"\nMissing values in sensor_a: {np.isnan(sensor_a).sum()}")
    print(f"Missing values in sensor_b: {np.isnan(sensor_b).sum()}")

    # Create 2x2 grid of subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    # Subplot 1: Line plot
    ax1.plot(timestamps, sensor_a, label='sensor_a', alpha=0.8)
    ax1.plot(timestamps, sensor_b, label='sensor_b', alpha=0.8)
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel('Temperature (°C)')
    ax1.set_title('Line Plot: Temperature Over Time')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Subplot 2: Scatter plot
    plot_scatter(ax2, timestamps, sensor_a, sensor_b)

    # Subplot 3: Histogram
    plot_histogram(ax3, sensor_a, sensor_b)

    # Subplot 4: Summary statistics (text box)
    ax4.axis('off')
    stats_text = (
        f"Data Summary Statistics\n"
        f"{'='*35}\n"
        f"Sample Count: {len(sensor_a)}\n"
        f"Time Range: {timestamps[0]:.1f}–{timestamps[-1]:.1f} seconds\n\n"
        f"Sensor A:\n"
        f"  Mean: {np.nanmean(sensor_a):.2f}°C\n"
        f"  Std Dev: {np.nanstd(sensor_a):.2f}°C\n"
        f"  Min: {np.nanmin(sensor_a):.2f}°C\n"
        f"  Max: {np.nanmax(sensor_a):.2f}°C\n"
        f"  Missing: {np.isnan(sensor_a).sum()} ({100*np.isnan(sensor_a).sum()/len(sensor_a):.1f}%)\n\n"
        f"Sensor B:\n"
        f"  Mean: {np.nanmean(sensor_b):.2f}°C\n"
        f"  Std Dev: {np.nanstd(sensor_b):.2f}°C\n"
        f"  Min: {np.nanmin(sensor_b):.2f}°C\n"
        f"  Max: {np.nanmax(sensor_b):.2f}°C\n"
        f"  Missing: {np.isnan(sensor_b).sum()} ({100*np.isnan(sensor_b).sum()/len(sensor_b):.1f}%)"
    )
    ax4.text(0.1, 0.5, stats_text, transform=ax4.transAxes, fontsize=10,
             verticalalignment='center', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    fig.tight_layout()
    fig.savefig('sensor_plots_grid.png', dpi=100)
    print("\nAll plots saved as 'sensor_plots_grid.png'")


if __name__ == '__main__':
    main()
