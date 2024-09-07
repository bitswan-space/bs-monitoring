from typing import Callable
from unittest.mock import mock_open, patch
from monitors.data_scheme import DataSchemeMonitor, DataSchemeMonitorConfig

# Sample YAML content for testing
SAMPLE_YAML = """
field1:
  type: string
  required: true
field2:
  type: integer
  min: 0
  max: 100
"""


def test_valid_data(
    mock_alert_service: Callable, mock_data_scheme_config: DataSchemeMonitorConfig
):
    with patch("builtins.open", mock_open(read_data=SAMPLE_YAML)):
        data_scheme_monitor = DataSchemeMonitor(
            mock_alert_service, mock_data_scheme_config
        )

    valid_data = {
        "test_key": [
            {"field1": "test", "field2": 50},
            {"field1": "another test", "field2": 75},
        ]
    }
    data_scheme_monitor.process(valid_data)

    mock_alert_service.send_alert.assert_not_called()


def test_invalid_data(
    mock_alert_service: Callable, mock_data_scheme_config: DataSchemeMonitorConfig
):
    with patch("builtins.open", mock_open(read_data=SAMPLE_YAML)):
        data_scheme_monitor = DataSchemeMonitor(
            mock_alert_service, mock_data_scheme_config
        )

    invalid_data = {
        "test_key": [
            {"field1": "test", "field2": 150},  # field2 > max
            {"field1": 123, "field2": 75},  # field1 should be string
            {"field2": 74},  # field1 is missing
        ]
    }
    data_scheme_monitor.process(invalid_data)

    mock_alert_service.send_alert.assert_called()
