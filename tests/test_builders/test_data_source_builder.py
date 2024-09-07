import pytest
from common.configs.base import DataSourceConfig, ElasticDataSourceConfig
from data_sources import create_data_source
from alert_services import AlertService


def test_register_data_source():
    """Register a new data source"""

    from data_sources.base import (
        __DATA_SOURCES,
        register_data_source,
        DataSource,
    )

    @register_data_source
    class TestDataSource(DataSource):
        pass

    assert "Test" in __DATA_SOURCES
    assert __DATA_SOURCES["Test"] == TestDataSource
    assert issubclass(TestDataSource, DataSource)


def test_register_invalid_data_source():
    """Register an invalid data source"""

    from data_sources.base import register_data_source

    with pytest.raises(AssertionError):

        @register_data_source
        class TestDataSource:
            pass


def test_create_data_source(
    mock_alert_service: AlertService,
    mock_elastic_data_source_config: ElasticDataSourceConfig,
):
    """Create a valid data source"""

    src = create_data_source(
        DataSourceConfig(type="Elastic", config=mock_elastic_data_source_config),
        mock_alert_service,
    )

    assert src.__class__.__name__ == "ElasticDataSource"


def test_create_invalid_data_source(mock_alert_service: AlertService):
    """Create an invalid data source"""
    c = DataSourceConfig(type="Unknown", config=None)

    with pytest.raises(Exception):
        create_data_source(c, mock_alert_service)
