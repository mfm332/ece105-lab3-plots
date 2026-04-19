# ECE 105 Lab 3: Sensor Plots

## Overview

This project generates synthetic temperature sensor data and creates visualization plots. The `generate_plots.py` script is a standalone Python implementation that was converted from a Jupyter notebook. It simulates realistic temperature measurements from two sensors over a 10-second time window with 200 samples, including noise, drift, anomalies, and missing values.

## Features

- **Synthetic Data Generation**: Creates realistic temperature sensor readings with:
  - Gaussian measurement noise
  - Low-frequency oscillations (sine waves at different frequencies)
  - Linear drift over time
  - Random spikes (~30 anomalies per sensor)
  - Missing values (~2% of samples set to NaN)

- **Three Visualization Plots**:
  - Line plot showing temperature trends over time
  - Scatter plot of data points for both sensors
  - Histogram showing temperature distribution

## Installation

### Prerequisites
- Python 3.7+
- Conda or Mamba package manager

### Setup

1. Activate the ece105 conda environment:
```bash
conda activate ece105
```

2. Install required packages (if not already installed):
```bash
conda install numpy matplotlib
```

Or using mamba:
```bash
mamba install numpy matplotlib
```

## Usage

Run the script from the command line:

```bash
python generate_plots.py
```

The script will:
1. Generate synthetic temperature data using seed 2332
2. Print summary statistics (data shapes, dtypes, sample values, missing value counts)
3. Create three PNG visualization files

## Output Files

The script generates three PNG image files in the same directory:

1. **sensor_data_plot.png**: Line plot showing temperature readings from both sensors over time (12" × 5")
2. **sensor_scatter.png**: Scatter plot visualization of individual data points for both sensors (12" × 5")
3. **sensor_histogram.png**: Histogram showing temperature distributions for both sensors with 30 bins (12" × 5")

## Script Structure

### Functions

- **`generate_data(seed)`**: Generates synthetic temperature sensor readings
  - Parameters: `seed` (int) - random seed for reproducibility
  - Returns: `sensor_a`, `sensor_b`, `timestamps` (all numpy arrays of shape (200,))

- **`plot_scatter(ax, timestamps, sensor_a, sensor_b)`**: Creates scatter plot on an Axes object
  - Modifies the Axes in place, returns None

- **`plot_histogram(ax, sensor_a, sensor_b)`**: Creates histogram on an Axes object
  - Modifies the Axes in place, returns None

- **`main()`**: Main entry point that orchestrates data generation and plot creation
  - Generates data, prints statistics, and saves all three plots

## Data Specifications

- **Sample Count**: 200 samples per sensor
- **Time Range**: 0 to 10 seconds (uniformly spaced)
- **Sensor A**: Base temperature ~20°C, oscillation amplitude 0.5°C, noise σ=0.2°C
- **Sensor B**: Base temperature ~50°C, oscillation amplitude 1.0°C, noise σ=0.4°C
- **Anomalies**: ~30 random spikes per sensor (±8°C magnitude)
- **Missing Data**: ~2% (approximately 4 samples per sensor set to NaN)

## AI tools used and disclosure

[Insert information about AI tools used in development and any relevant disclosures here.]
