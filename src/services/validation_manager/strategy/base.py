from abc import ABC, abstractmethod
from typing import Dict


class Base(ABC):
    @abstractmethod
    def validate(self, payload: Dict) -> bool:
        pass
