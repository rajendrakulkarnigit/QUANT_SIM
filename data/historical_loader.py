import pandas as pd

class HistoricalLoader:
    def __init__(self, client):
        self.client = client

    def fetch(self, token):
        data = self.client.get_historical(token)
        df = pd.DataFrame(data)
        df["returns"] = df["close"].pct_change()
        return df