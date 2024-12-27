from abc import ABC, abstractmethod
from typing import TypeVar, Generic

PT = TypeVar("PT")  # Params type
OT = TypeVar("OT")  # Output type

class NLPModule(ABC, Generic[PT, OT]):
    """
    Abstract base class for all NLP modules
    """
    @abstractmethod
    def process(self, input_text: str, params: PT) -> OT:
        """
        Process input data and return the output.

        Args:
            input_text (str): The input data to process.
            params (PT): Additional parameters for the module.

        Returns:
            OT: The processed output.
        """
        pass
