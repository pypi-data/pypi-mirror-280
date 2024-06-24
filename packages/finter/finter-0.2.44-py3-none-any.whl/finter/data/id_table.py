import pandas as pd
from finter.api.quanda_data_api import QuandaDataApi


class IdTable:

    def __init__(self, vendor_name):
        self.vendor_name = vendor_name
        self.cache = {}

    def _get(self, id_type):
        df = self.cache.get(id_type)
        if df is None or df.empty:
            data = QuandaDataApi().quanda_data_id_table_retrieve(vendor=self.vendor_name, id_type=id_type)
            df = pd.read_json(data['data'])
            self.cache[id_type] = df
        return df

    def get_company(self):
        return self._get('company')

    def get_stock(self):
        return self._get('stock')
