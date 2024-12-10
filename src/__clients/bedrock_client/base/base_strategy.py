from abc import ABC, abstractmethod
from typing import Any


class BedrockBaseStrategy(ABC):
    """
    Abstract base class for OpenAI strategies.
    """

    @abstractmethod
    # flake8: noqa: F821
    def execute(self, client: "BedrockBaseClient", **kwargs: Any) -> Any:
        """
        Execute the strategy logic.
        """
        raise NotImplementedError("Subclasses must implement the `execute` method.")
