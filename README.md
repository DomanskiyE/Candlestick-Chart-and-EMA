# Candlestick Chart and EMA


This project is a chart plotter that reads data from a CSV file, aggregates the data into candlestick intervals, calculates the Exponential Moving Average (EMA), and plots a candlestick chart with the EMA line.
## Getting started

To use this project, follow the steps below:

- [ ] Clone the repository: git clone https://github.com/your-username/project.git
- [ ] Install the required dependencies from requirements: pip install requirements.txt
- [ ] Run tests before the start: pytest -s -v
- [ ] Run the main.py file: python main.py

## Project Structure

The project is structured as follows:

- main.py: The main entry point of the program. It imports the necessary modules and executes the main function.
- chart.py: Contains the ChartPlotter class, which handles reading data, aggregating candles, calculating EMA, and plotting the chart.
- ema.py: Contains the ema_calculation function, which calculates the Exponential Moving Average.
- file_selector.py: Contains the select_file function, which opens a file dialog to select a CSV file.

 > There is also a **sample** folder containing example images of charts

## Usage

1. Run the main.py file.
2. A file dialog will open. Select the CSV file containing the data you want to plot.
3. Enter the desired candlestick interval (e.g., '5Min', '1H', '1D').
4. Enter the length of the EMA (number of periods).
5. The candlestick chart with the EMA line will be displayed.
6. Choose a save location and filename for the chart image.

