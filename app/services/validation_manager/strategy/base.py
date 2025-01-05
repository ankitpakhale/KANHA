from abc import ABC, abstractmethod
from typing import Dict
from app.control_panel import control_panel_manager


class Base(ABC):
    def __init__(self):
        self.control_panel_manager = control_panel_manager

    @abstractmethod
    def validate(self, payload: Dict) -> bool:
        pass
