import pytest
from alert_services.base import AlertService
from common.configs.base import MonitorConfig, DataSchemeMonitorConfig
from monitors import create_monitors
from unittest.mock import mock_open, patch

SAMPLE_YAML = """
field1:
  type: string
  required: true
field2:
  type: integer
  min: 0
  max: 100
"""


def test_register_monitor():
    """Register a new monitor class"""
    from monitors.base import __MONITORS, register_monitor, Monitor

    @register_monitor
    class TestMonitor(Monitor):
        pass

    assert "Test" in __MONITORS
    assert __MONITORS["Test"] == TestMonitor
    assert issubclass(TestMonitor, Monitor)


def test_register_invalid_monitor():
    """Register an invalid monitor"""
    from monitors.base import register_monitor

    with pytest.raises(AssertionError):

        @register_monitor
        class TestMonitor:
            pass


def test_create_monitors(
    mock_alert_service: AlertService, mock_data_scheme_config: DataSchemeMonitorConfig
):
    """Create valid monitors"""
    with patch("builtins.open", mock_open(read_data=SAMPLE_YAML)):
        configs = [
            MonitorConfig(type="DataQuantity", config=None),
            MonitorConfig(type="DataScheme", config=mock_data_scheme_config),
        ]

        ms = create_monitors(configs, mock_alert_service)

    assert len(ms) == 2
    assert ms[0].__class__.__name__ == "DataQuantityMonitor"
    assert ms[1].__class__.__name__ == "DataSchemeMonitor"


def test_create_invalid_monitor(mock_alert_service: AlertService):
    """Create invalid monitor"""
    configs = [MonitorConfig(type="InvalidMonitor", config=None)]

    with pytest.raises(KeyError):
        create_monitors(configs, mock_alert_service)
