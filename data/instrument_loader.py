import pandas as pd


class InstrumentLoader:

    def __init__(self, instruments_file):
        self.instruments_file = instruments_file

    def load(self):
        df = pd.read_csv(self.instruments_file)
        # convert expiry column to datetime
        df["expiry"] = pd.to_datetime(df["expiry"])
        return df

