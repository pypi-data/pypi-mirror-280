from Financials.constants.mnemonics_constants import MnemonicConstants
from Financials.constants.functions_constants import FunctionConstants


class DataConfig:
    def get_income_statement_mnemonics(self):
        return MnemonicConstants._income_statement_mnemonics

    def get_income_statement_pit_function(self):
        return FunctionConstants._income_statement_pit_function

    def get_income_statement_historical_function(self):
        return FunctionConstants._income_statement_historical_function

    def get_balance_sheet_mnemonics(self):
        return MnemonicConstants._balance_sheet_mnemonics

    def get_balance_sheet_pit_function(self):
        return FunctionConstants._balance_sheet_pit

    def get_balance_sheet_historic_function(self):
        return FunctionConstants._balance_sheet_historical

    def get_cash_flow_mnemonics(self):
        return MnemonicConstants._cash_flow_mnemonics

    def get_cash_flow_pit_function(self):
        return FunctionConstants._cash_flow_pit_function

    def get_cash_flow_historical_function(self):
        return FunctionConstants._cash_flow_historical_function

    def get_all_financial_data_mnemonics(self):
        return MnemonicConstants._all_financial_data_mnemonics

    def get_financials_pit_function(self):
        return FunctionConstants._financials_pit_function

    def get_financials_historical_function(self):
        return FunctionConstants._financials_historical_function