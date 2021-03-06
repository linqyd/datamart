from abc import ABC, abstractmethod
import pandas as pd
import typing


class MaterializerBase(ABC):
    """Abstract class of Materializer, should be extended for every Materializer dealing with different data source.

    """

    @abstractmethod
    def get(self, metadata: dict = None, variables: typing.List[int] = None, constrains: dict = None) -> pd.DataFrame:
        """API for Materialize, every Materializer should implement `get` method, returns a pandas dataframe.

        """
        pass
