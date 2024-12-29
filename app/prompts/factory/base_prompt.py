from abc import ABC, abstractmethod


class BasePrompt(ABC):
    """
    Abstract base class to handle prompts.
    """

    @abstractmethod
    def get_system_prompt(self):
        """
        Returns the system prompt for specific
        """
        ...

    @abstractmethod
    def get_user_prompt(self):
        """
        Returns the user prompt for specific
        """
        ...
