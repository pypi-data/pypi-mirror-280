import logging
from typing import Union
import pandas as pd

from ..transform_data import APIModels, TransformationStrategyFactory
from ..api.query import (
    get_v1_databases,
    post_v1_databases_datasource_query_instant,
    post_v1_databases_datasource_query_latest,
    post_v1_databases_datasource_query_range,
)
from ..models import (
    Instant,
    Latest,
    Range,
    ResponseWithMetricDataWithAnnotationsList,
)
from ..client import APIClient
from ..errors import UnexpectedStatus, unexpected_status_handler
from ..types import UNSET


DATABASES_STRATEGY = TransformationStrategyFactory.create_strategy(APIModels.DATABASES)


QUERY_STRATEGY = TransformationStrategyFactory.create_strategy(APIModels.QUERY)


@unexpected_status_handler
def get_databases(client: APIClient) -> pd.DataFrame:
    """Get databases as pandas DataFrame"""
    http_response = get_v1_databases.sync(client=client)

    return DATABASES_STRATEGY.extract_dataframe(http_response)


@unexpected_status_handler
def get_values(
    client: APIClient,
    datasource: str,
    metric_name: str,
    start: str,
    end: str,
    timezone: str = "Europe/Paris",
    limit: int = 50000,
    aggregation: Union[dict, str] = "none",
    filter: str = UNSET,
    **kwargs,
) -> pd.DataFrame:
    """Retrieve metric values in given range as pandas DataFrame"""

    range_dict = {
        "start": start,
        "end": end,
        "metric": {"name": metric_name},
        "timezone": timezone,
        "limit": limit,
        "showAnnotation": False,
        "aggregation": aggregation,
        "filter": filter,
    }

    for key, value in kwargs.items():
        range_dict[key] = value

    if range_dict["limit"] > 50000 or range_dict["limit"] < 0:
        message = "The “limit” argument value must be between 0 and 50000."
        raise UnexpectedStatus(status_code=400, content=message.encode())

    range_data = Range.from_dict(range_dict)

    http_response = post_v1_databases_datasource_query_range.sync(
        client=client, datasource=datasource, body=range_data
    )

    if not isinstance(http_response, ResponseWithMetricDataWithAnnotationsList):
        return pd.DataFrame()

    if not http_response.is_response_complete:
        logging.warning(
            "Not all values has been retrieved from get_range_values() HTTP response because of the limit given (max 50000)."
        )

    return QUERY_STRATEGY.extract_dataframe(http_response)


@unexpected_status_handler
def get_values_at(
    client: APIClient,
    datasource: str,
    instant_data: Union[
        Instant,
        dict,
    ],
) -> pd.DataFrame:
    """Retrieve metric values from one or multiple time series at a specific point in time as pandas DataFrame"""
    if isinstance(instant_data, dict):
        instant_data = Instant.from_dict(instant_data)

    http_response = post_v1_databases_datasource_query_instant.sync(
        client=client, datasource=datasource, body=instant_data
    )
    metrics_dataframes = []
    for item in http_response:
        metrics_dataframes.append(QUERY_STRATEGY.extract_dataframe(item))
    if metrics_dataframes:
        return pd.concat(metrics_dataframes)
    else:
        return pd.DataFrame()


@unexpected_status_handler
def get_latest_value(
    client: APIClient,
    datasource: str,
    latest_data: Union[
        Latest,
        dict,
    ],
) -> pd.DataFrame:
    """Retrieve latest metric value from one or multiple time series as pandas DataFrame"""
    if isinstance(latest_data, dict):
        latest_data = Latest.from_dict(latest_data)

    http_response = post_v1_databases_datasource_query_latest.sync(
        client=client, datasource=datasource, body=latest_data
    )
    metrics_dataframes = []
    for item in http_response:
        metrics_dataframes.append(QUERY_STRATEGY.extract_dataframe(item))
    if metrics_dataframes:
        return pd.concat(metrics_dataframes)

    # No values found, return empty dataframe
    else:
        return pd.DataFrame()


@unexpected_status_handler
def get_range_values(
    client: APIClient,
    datasource: str,
    range_data: Union[
        Range,
        dict,
    ],
) -> pd.DataFrame:
    """Retrieve metric values in given range as pandas DataFrame"""
    if isinstance(range_data, dict):
        range_data = Range.from_dict(range_data)

    http_response = post_v1_databases_datasource_query_range.sync(
        client=client, datasource=datasource, body=range_data
    )

    if not isinstance(http_response, ResponseWithMetricDataWithAnnotationsList):
        return pd.DataFrame()

    if not http_response.is_response_complete:
        logging.warning(
            "Not all values has been retrieved from get_range_values() HTTP response because of the limit given in range_data."
        )

    return QUERY_STRATEGY.extract_dataframe(http_response)
