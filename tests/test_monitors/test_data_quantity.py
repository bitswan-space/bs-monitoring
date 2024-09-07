from typing import Callable
import pytest
from unittest.mock import patch
from datetime import datetime
from monitors.data_quantity import DataQuantityMonitor
from alert_services.base import AlertService


@pytest.fixture
def data_quantity_monitor(mock_alert_service) -> DataQuantityMonitor:
    return DataQuantityMonitor(mock_alert_service)


@patch("monitors.data_quantity.datetime")
def test_process_empty_data_weekday(
    mock_datetime: Callable,
    data_quantity_monitor: DataQuantityMonitor,
    mock_alert_service: AlertService,
):
    """Empty data on a weekday"""
    mock_datetime.now.return_value = datetime(2023, 8, 15)  # A Tuesday
    data_quantity_monitor.process({"test_key": []})
    mock_alert_service.send_alert.assert_called()


def test_process_non_empty_data(
    data_quantity_monitor: DataQuantityMonitor, mock_alert_service: AlertService
):
    """Non-empty data"""
    data_quantity_monitor.process({"test_key": [1, 2, 3]})
    mock_alert_service.send_alert.assert_not_called()


@patch("monitors.data_quantity.datetime")
def test_process_weekend(
    mock_datetime,
    data_quantity_monitor: DataQuantityMonitor,
    mock_alert_service: AlertService,
):
    """Empty data on a weekend"""
    mock_datetime.now.return_value = datetime(2023, 8, 13)  # A Sunday
    data_quantity_monitor.process({"test_key": []})

    mock_alert_service.send_alert.assert_not_called()


@patch("monitors.data_quantity.datetime")
def test_process_multiple_keys(
    mock_datetime,
    data_quantity_monitor: DataQuantityMonitor,
    mock_alert_service: AlertService,
):
    """Multiple keys with one empty"""
    mock_datetime.now.return_value = datetime(2023, 8, 15)  # A Tuesday
    data_quantity_monitor.process({"non_empty_key": [1, 2, 3], "empty_key": []})

    mock_alert_service.send_alert.assert_called()
