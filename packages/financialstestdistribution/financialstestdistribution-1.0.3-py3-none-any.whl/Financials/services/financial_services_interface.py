from abc import ABC, abstractmethod
import pandas as pd

class FinancialServicesInterface(ABC):

    @abstractmethod
    def get_income_statement_pit(self, token, identifiers, properties={}, proxy=None) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_income_statement_historical(self, token, identifiers, properties={}, proxy=None):
        pass

    @abstractmethod
    def get_balance_sheet_pit(self, token, identifiers, properties={}, proxy=None):
        pass

    @abstractmethod
    def get_balance_sheet_historical(self, token, identifiers, properties={}, proxy=None):
        pass

    @abstractmethod
    def get_cash_flow_pit(self, token, identifiers, properties={}, proxy=None) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_cash_flow_historical(self, token, identifiers, properties={}, proxy=None) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_financials_pit(self,token, identifiers, mnemonics, properties={}, proxy=None):
        pass

    @abstractmethod
    def get_financials_historical(self, token, identifiers, mnemonics, properties={}, proxy=None):
        pass