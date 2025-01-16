from typing import Any
from bs_monitoring.common.utils import MonitoringServiceError, ConfigField
from bs_monitoring.alert_services import alert, AlertService
from cerberus import Validator
import yaml

from bs_monitoring.monitors.base import Monitor, register_monitor


class DataSchemeError(MonitoringServiceError):
    def __init__(self, message: str) -> None:
        """Exception raised when there is an error in the data scheme.

        Args:
            message (str): The error message.
        """
        super().__init__(message)


@register_monitor
class DataSchemeMonitor(Monitor):
    file = ConfigField(str)

    def __init__(
        self,
        alert_service: AlertService,
        db_name: str | None = None,
        config: Any = None,
    ) -> None:
        """Monitor to check the data scheme of the data.

        Args:
            alert_service (AlertService): The alert service to use.
            config (DataSchemeMonitorConfig): The configuration for the monitor.
        """
        super().__init__(alert_service, db_name, config)

        with open(self.file, "r") as f:
            self.validator_ = Validator(yaml.safe_load(f), allow_unknown=True)

    async def process(self, data: dict[str, Any]) -> None:
        """Process the data.

        Args:
            data (dict[str, Any]): The data to process.
        """
        for k, v in data.items():
            await self._process(k, v)

    @alert(message="Data scheme error")
    async def _process(self, key: str, value: list[Any]) -> None:
        """Process the data for a given key.

        Args:
            key (str): The key of the data to process.
            value (list[Any]): The data to process.
        """
        invalid_items = list(filter(lambda x: not self.validator_.validate(x), value))
        if len(invalid_items) > 0:
            raise DataSchemeError(
                f"Data scheme error {self.validator_.errors} for {key}, total invalid items: {len(invalid_items)}"
            )
