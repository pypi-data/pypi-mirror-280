from MarketData.constants.mnemonics_constants import MnemonicConstants
from MarketData.constants.functions_constants import FunctionConstants
class DataConfig:
    def get_pricing_info_pit_mnemonics(self):
        return MnemonicConstants.pricing_info_pit_mnemonics

    def get_pricing_info_time_series_mnemonics(self):
        return MnemonicConstants.pricing_info_time_series_mnemonics

    def get_dividend_info_pit_mnemonics(self):
        return MnemonicConstants.dividend_info_pit_mnemonics

    def get_dividend_info_time_series_mnemonics(self):
        return MnemonicConstants.dividend_info_time_series_mnemonics

    def get_market_info_pit_mnemonics(self):
        return MnemonicConstants.market_info_pit_mnemonics

    def get_market_info_time_series_mnemonics(self):
        return MnemonicConstants.market_info_time_series_mnemonics

    def get_pricing_info_pit_function(self):
        return FunctionConstants.pricing_info_pit_function

    def get_pricing_info_time_series_function(self):
        return FunctionConstants.pricing_info_time_series_function

    def get_dividend_info_pit_function(self):
        return FunctionConstants.dividend_info_pit_function

    def get_dividend_info_time_series_function(self):
        return FunctionConstants.dividend_info_time_series_function

    def get_market_info_pit_function(self):
        return FunctionConstants.market_info_pit_function

    def get_market_info_time_series_function(self):
        return FunctionConstants.market_info_time_series_function