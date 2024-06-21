from DataServices.model.sdk_data_input import SDKDataInput
from DataServices.model.sdk_data_request import SDKDataRequest
from DataServices.services.impl.sdk_data_services_impl import SDKDataServicesImpl
from Financials.constants.data_config import DataConfig
from Financials.services.helper.data_transform import DataFormat
from Financials.services.financial_services_interface import FinancialServicesInterface
from Financials.util.property_utils import PropertyUtils
from Financials.constants.sdk_constants import SDKConstants
from Financials.config.logging_config import LOGGING_CONFIG
import logging.config
# Configure logging
logging.config.dictConfig(LOGGING_CONFIG)
# Get the logger
logger = logging.getLogger('main')

class SDKFinancialServices(FinancialServicesInterface):
    def __init__(self):
        self.data_services = SDKDataServicesImpl()
        self.data_config = DataConfig()

    def get_income_statement_pit(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_income_statement_pit_function()
        mnemonics = self.data_config.get_income_statement_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_pit(final_output,properties)
        return df


    def get_income_statement_historical(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_income_statement_historical_function()
        mnemonics = self.data_config.get_income_statement_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_gdshe(final_output, properties)
        return df


    def get_balance_sheet_pit(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_balance_sheet_pit_function()
        mnemonics = self.data_config.get_balance_sheet_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_pit(final_output, properties)
        return df


    def get_balance_sheet_historical(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_balance_sheet_historic_function()
        mnemonics = self.data_config.get_balance_sheet_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_gdshe(final_output, properties)
        return df


    def get_cash_flow_pit(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_cash_flow_pit_function()
        mnemonics = self.data_config.get_cash_flow_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_pit(final_output, properties)
        return df



    def get_cash_flow_historical(self, token, identifiers, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        function = self.data_config.get_cash_flow_historical_function()
        mnemonics = self.data_config.get_cash_flow_mnemonics()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_gdshe(final_output, properties)
        return df


    def get_financials_pit(self, token, identifiers, mnemonics, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        mnemonics_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.MNEMONICS_SIZE)
        if len(mnemonics) > int(mnemonics_size):
            raise ValueError("The 'mnemonics' list should not contain more than 10 items.")
        function = self.data_config.get_financials_pit_function()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_pit(final_output,properties)
        return df




    def get_financials_historical(self, token, identifiers, mnemonics, properties={}, proxy=None):
        identifiers_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.IDENTIFIERS_SIZE)
        if len(identifiers) > int(identifiers_size):
            raise ValueError("The 'identifiers' list should not contain more than 10 items.")
        mnemonics_size = PropertyUtils.get_property(SDKConstants.SDK, SDKConstants.MNEMONICS_SIZE)
        if len(mnemonics) > int(mnemonics_size):
            raise ValueError("The 'mnemonics' list should not contain more than 10 items.")
        function = self.data_config.get_financials_historical_function()
        sdk_data_request = self.__create_sdk_data_request(identifiers, function, properties, mnemonics)
        sdk_input_request = self.__create_sdk_data_input(token, proxy, sdk_data_request)
        final_output = self.data_services.invoke_data_service(sdk_input_request)
        df = DataFormat.convert_to_dataframe_generic(final_output,properties)
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