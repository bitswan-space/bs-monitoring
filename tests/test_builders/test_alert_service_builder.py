import pytest
from common.configs.base import OpsgenieAlertServiceConfig, AlertServiceConfig
from alert_services import create_alert_service


def test_register_alert_service():
    """Register a new alert service"""

    from alert_services.base import (
        __ALERT_SERVICES,
        register_alert_service,
        AlertService,
    )

    @register_alert_service
    class TestAlertService(AlertService):
        pass

    assert "Test" in __ALERT_SERVICES
    assert __ALERT_SERVICES["Test"] == TestAlertService
    assert issubclass(TestAlertService, AlertService)


def test_register_invalid_alert_service():
    """Register an invalid alert service"""

    from alert_services.base import register_alert_service

    with pytest.raises(AssertionError):

        @register_alert_service
        class TestAlertService:
            pass


def test_create_alert_service(
    mock_opsgenie_alert_service_config: OpsgenieAlertServiceConfig,
):
    """Create a valid alert service"""

    svc = create_alert_service(
        AlertServiceConfig(type="Opsgenie", config=mock_opsgenie_alert_service_config)
    )

    assert svc.__class__.__name__ == "OpsgenieAlertService"


def test_create_invalid_alert_service():
    """Create an invalid alert service"""
    c = AlertServiceConfig(type="Unknown", config=None)

    with pytest.raises(Exception):
        create_alert_service(c)
