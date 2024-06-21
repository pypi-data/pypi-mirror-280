from abc import ABC, abstractmethod

class MarketDataServicesInterface(ABC):

    @abstractmethod
    def get_pricing_info_pit(self, token, identifiers, properties={}, proxy=None):
        pass

    @abstractmethod
    def get_pricing_info_time_series(self, token, identifiers, properties={}, proxy=None):
        pass

    @abstractmethod
    def get_dividend_pit_info(self, token, identifiers, properties={}, proxy=None):
        pass

    @abstractmethod
    def get_dividend_info_time_series(self, token, identifiers, properties={}, proxy=None):
        pass

    @abstractmethod
    def get_market_info_pit(self, token, identifiers, properties={}, proxy=None):
        pass

    @abstractmethod
    def get_market_info_time_series(self, token, identifiers, properties={}, proxy=None):
        pass
