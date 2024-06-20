import polars as pl

class Indicator:
    def __init__(self, name, window):
        self.name = name
        self.window = window

    def calculate(self, data):
        if self.name == 'SMA':
            return data.with_columns([pl.col('close').rolling_mean(self.window).alias(f'SMA_{self.window}')])
        # Add more indicators as needed
        raise ValueError(f"Unsupported indicator: {self.name}")
