from DataServices.model.sdk_data_input import SDKDataInput
from DataServices.model.sdk_data_request import SDKDataRequest
from DataServices.services.impl.sdk_data_services_impl import SDKDataServicesImpl

from MarketData.constants.data_config import DataConfig
from MarketData.constants.config_constants import ConfigConstants
from MarketData.services.helper.data_transform import DataFormat
from MarketData.services.sdk_marketdata_interface import MarketDataServicesInterface
from MarketData.util.property_utils import PropertyUtils
from MarketData.config.logging_config import LOGGING_CONFIG
import logging.config
# Configure logging
logging.config.dictConfig(LOGGING_CONFIG)
# Get the logger
logger = logging.getLogger('main')



class SDKMarketDataServices(MarketDataServicesInterface):

    def __init__(self):
        self.data_services = SDKDataServicesImpl()
        self.data_config = DataConfig()

    def get_pricing_info_pit(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(ConfigConstants.SDK, ConfigConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_pricing_info_pit_function()
        mnemonics = self.data_config.get_pricing_info_pit_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_pit(final_output, properties)
        return df

    def get_pricing_info_time_series(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(ConfigConstants.SDK, ConfigConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_pricing_info_time_series_function()
        mnemonics = self.data_config.get_pricing_info_time_series_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_gdst(final_output, properties)
        return df

    def get_dividend_pit_info(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(ConfigConstants.SDK, ConfigConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_dividend_info_pit_function()
        mnemonics = self.data_config.get_dividend_info_pit_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_pit(final_output, properties)
        return df

    def get_dividend_info_time_series(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(ConfigConstants.SDK, ConfigConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_dividend_info_time_series_function()
        mnemonics = self.data_config.get_dividend_info_time_series_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_gdst(final_output, properties)
        return df

    def get_market_info_pit(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(ConfigConstants.SDK, ConfigConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_market_info_pit_function()
        mnemonics = self.data_config.get_market_info_pit_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_pit(final_output, properties)
        return df

    def get_market_info_time_series(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(ConfigConstants.SDK, ConfigConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_market_info_time_series_function()
        mnemonics = self.data_config.get_market_info_time_series_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_gdst(final_output, properties)
        return df

    def __create_sdk_data_request(self, identifiers, function, properties={}, mnemonics=None):
        request = SDKDataRequest(
            function=function,
            properties=properties,
            identifiers=identifiers,
            mnemonics=mnemonics
        )
        return request

    def __create_sdk_data_input(self, token, proxy, sdk_data_request):
        data_input = SDKDataInput(
            sdk_proxy=proxy,
            bearer_token=token,
            data_requests=sdk_data_request
        )
        return data_input
