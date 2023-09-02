import pytest
from chart import ChartPlotter


@pytest.fixture
def chart_plotter():
    file_path = "prices.csv"  # Path to test file
    return ChartPlotter(file_path)


def test_read_data_invalid_file(chart_plotter):
    chart_plotter.file_path = "invalid_file.csv"  # Invalid path to test file
    with pytest.raises(Exception):
        chart_plotter.read_data()


def test_read_data(chart_plotter):
    chart_plotter.read_data()
    assert len(chart_plotter.df) > 0


@pytest.mark.parametrize("invalid_interval", ["invalid_interval", False])
def test_aggregate_candles(chart_plotter, invalid_interval):
    chart_plotter.read_data()
    chart_plotter.interval = invalid_interval
    if invalid_interval is False:
        chart_plotter.aggregate_candles()
        assert chart_plotter.interval is not None
        assert len(chart_plotter.ohlc) > 0
    else:
        with pytest.raises(Exception):
            chart_plotter.aggregate_candles()


@pytest.mark.parametrize("invalid_length", ["invalid_length", False])
def test_calculate_ema(chart_plotter, invalid_length):
    chart_plotter.read_data()
    chart_plotter.interval = '1D'  # valid value of interval
    chart_plotter.aggregate_candles()
    chart_plotter.length = invalid_length
    if invalid_length is False:
        chart_plotter.calculate_ema()
        assert chart_plotter.length is not None
        assert chart_plotter.ema is not False
    else:
        with pytest.raises(Exception):
            chart_plotter.calculate_ema()


@pytest.mark.parametrize("length", ["length", '1'])
def test_calculate_ema_no_data(chart_plotter, length):
    chart_plotter.read_data()
    chart_plotter.length = length
    with pytest.raises(Exception):
        chart_plotter.calculate_ema()
