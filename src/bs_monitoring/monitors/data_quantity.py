from typing import Any
from bs_monitoring.alert_services import alert, AlertService
from bs_monitoring.common.utils import MonitoringServiceError
import pytz
from datetime import datetime, timedelta

from bs_monitoring.monitors import Monitor, register_monitor


class DataQuantityError(MonitoringServiceError):
    def __init__(self, message: str) -> None:
        """Exception raised when data quantity is 0.

        Args:
            message (str): The error message.
        """
        super().__init__(message)


@register_monitor
class DataQuantityMonitor(Monitor):
    def __init__(
        self,
        alert_service: AlertService,
        config: None = None,
        db_name: str | None = None,
    ) -> None:
        """Monitor to check the quantity of data.

        Args:
            alert_service (AlertService): The alert service to use.
            config (None, optional): No purpose, required because of the factory method. Defaults to None.
        """
        super().__init__(alert_service, db_name)

    async def process(self, data: dict[str, Any]) -> None:
        """Process the data.

        Args:
            data (dict[str, Any]): The data to process.
        """
        start_date = datetime.now(pytz.utc) - timedelta(days=1)
        if start_date.weekday() >= 5:
            return

        for k, v in data.items():
            await self._process(k, v)

    @alert(message="Data quantity error")
    async def _process(self, key: str, value: list[Any]) -> None:
        """Process the data for a given key.

        Args:
            key (str): The key of the data to process.
            value (list[Any]): The data to process.

        Raises:
            DataQuantityError: Raised if the data quantity is 0.
        """
        if len(value) == 0:
            raise DataQuantityError(f"Data quantity for {key} is 0")

