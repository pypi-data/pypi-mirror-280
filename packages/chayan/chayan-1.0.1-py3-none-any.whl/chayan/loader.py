import csv
import logging
from datetime import datetime, timedelta
from io import StringIO

import requests


class CuratedStocks:

    def __init__(self, url='https://raw.githubusercontent.com/sharmaak/curated/main/curated_stocks.csv',
                 refresh_delay_min: float = 15):
        self.url = url
        self.refresh_delay_min = refresh_delay_min
        self.updated_time = datetime.now() - timedelta(days=1)
        self.curated_stock = []
        self._logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

    def load_curated_stocks(self):
        """
        Loads symbols from a CSV file at the specified URL. Extracts 'nse_symbol' and 'isin'
        from the CSV file and returns them as a list of dictionaries.
        :return: list of dicts with keys 'nse_symbol' and 'isin'
        """

        now = datetime.now()
        threshold_time = self.updated_time + timedelta(minutes=self.refresh_delay_min)
        if now < threshold_time:
            return self.curated_stock

        self._logger.debug(f'updated_time={self.updated_time}, now={now}. Loading curated stocks from {self.url} ...')
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an error for bad status codes

        curated_stocks = []
        content = StringIO(response.text)
        reader = csv.DictReader(content)

        for row in reader:
            nse_symbol = row['nse_symbol'].strip()
            isin = row['isin'].strip()
            if nse_symbol and isin:  # Ensure both nse_symbol and isin are present
                curated_stocks.append(Stock(nse_symbol, isin,
                                            row['bse_id'].strip(),
                                            row['name'].strip(),
                                            row['sector'].strip()))

        # Assign the loaded socks to cached value and update the timestamp
        self.curated_stock = curated_stocks
        self.updated_time = datetime.now()

        self._logger.debug(f'Loaded {len(curated_stocks)} curated stocks.')
        return curated_stocks


class Stock:
    def __init__(self, nse_symbol, isin, bse_id, name, sector):
        self.nse_symbol = nse_symbol
        self.isin = isin
        self.bse_id = bse_id
        self.name = name
        self.sector = sector

    def __repr__(self):
        return (f"Stock(nse_symbol='{self.nse_symbol}', isin='{self.isin}', "
                f"bse_id='{self.bse_id}', name='{self.name}', sector='{self.sector}')")

    def __eq__(self, other):
        return isinstance(other, Stock) and self.nse_symbol == other.nse_symbol

    def display_info(self):
        return (f"Stock Information:\n"
                  f"Name: {self.name}\n"
                  f"NSE Symbol: {self.nse_symbol}\n"
                  f"ISIN: {self.isin}\n"
                  f"BSE ID: {self.bse_id}\n"
                  f"Sector: {self.sector}")
