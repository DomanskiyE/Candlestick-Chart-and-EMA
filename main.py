from file_selector import select_file
from chart import ChartPlotter


def main():
    file_path = select_file()
    chart_plotter = ChartPlotter(file_path)
    chart_plotter.read_data()
    chart_plotter.aggregate_candles()
    chart_plotter.calculate_ema()
    chart_plotter.plot_chart()


if __name__ == "__main__":
    main()
