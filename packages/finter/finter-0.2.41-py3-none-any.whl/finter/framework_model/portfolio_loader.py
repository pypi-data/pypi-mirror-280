from __future__ import print_function

import finter
from finter.settings import logger, get_api_client
from finter.rest import ApiException


class PortfolioPositionLoader:
    def __init__(self, start, end, exchange, universe, instrument_type, freq, position_type, portfolio_set):
        self.start = start
        self.end = end
        self.exchange = exchange
        self.universe = universe
        self.instrument_type = instrument_type
        self.freq = freq
        self.position_type = position_type
        self.portfolio_set = list(portfolio_set)

    def to_dict(self):
        return {
            'start': self.start,
            'end': self.end,
            'exchange': self.exchange,
            'universe': self.universe,
            'instrument_type': self.instrument_type,
            'freq': self.freq,
            'position_type': self.position_type,
            'portfolio_set': self.portfolio_set
        }

    def get_portfolio(self, identity_name):
        params = {**self.to_dict(), 'identity_name': identity_name}
        body = finter.BaseFlexibleFundGetPortfolio(**params)
        try:
            api_response = finter.FlexibleFundApi(get_api_client()).flexiblefund_base_portfolio_get_portfolio_create(body)
            return finter.to_dataframe(api_response.pm, api_response.column_types)
        except ApiException as e:
            logger.error("Exception when calling PortfolioPositionLoader->get_portfolio: %s\n" % e)
        return
