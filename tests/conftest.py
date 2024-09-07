import pytest
from unittest.mock import Mock
from src.alert_services.opsgenie import AlertService
from src.common.configs.base import (
    DataSchemeMonitorConfig,
    OpsgenieAlertServiceConfig,
    ElasticDataSourceConfig,
)


@pytest.fixture
def mock_alert_service() -> AlertService:
    return Mock(spec=AlertService)


@pytest.fixture
def mock_data_scheme_config():
    return DataSchemeMonitorConfig(file="test_config.yaml")


@pytest.fixture
def mock_opsgenie_alert_service_config():
    return OpsgenieAlertServiceConfig(api_key="test")


@pytest.fixture
def mock_elastic_data_source_config():
    return ElasticDataSourceConfig(
        url="http://localhost:9200", basic_auth=("user", "pass"), indices=["test"]
    )


def pytest_itemcollected(item):
    node = item.obj
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if suf:
        fpath = item.location[0].split("/")
        test_name = f"{fpath[-2]}/{fpath[-1][:-3]}"
        item._nodeid = f"{test_name}: {suf}"
