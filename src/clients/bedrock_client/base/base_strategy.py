from abc import ABC, abstractmethod


class BedrockBaseStrategy(ABC):
    """
    Abstract base class for Bedrock strategies.
    Defines methods that specific strategies must implement.
    """

    @abstractmethod
    def execute(self, *args, **kwargs) -> dict:
        """
        Executes the Bedrock operation.
        """
        pass
