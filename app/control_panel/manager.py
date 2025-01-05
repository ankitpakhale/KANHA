from app.control_panel import CONTROL_PANEL_SETTINGS
from app.config import GeneralConfig
from app.utils import logger


class ControlPanelManager:
    @staticmethod
    def get_setting(setting: str) -> bool:
        """
        Get the value of a particular setting
        """
        current_environment = GeneralConfig.ENV
        if current_environment == "prod":
            logger.error(
                "Current Environment is Prod, control panel will not work. :<("
            )
            setting = True
        else:
            setting = CONTROL_PANEL_SETTINGS.get(setting, True)
        return setting


# singleton instance of ControlPanelManager
control_panel_manager = ControlPanelManager
