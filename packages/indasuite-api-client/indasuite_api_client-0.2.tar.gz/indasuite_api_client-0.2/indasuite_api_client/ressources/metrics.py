import logging
from typing import Union
import pandas as pd

from ..transform_data import APIModels, TransformationStrategyFactory
from ..api.metrics import (
    get_v1_metrics,
    post_v1_metrics,
    get_v_1_metrics_metric_id,
    put_v_1_metrics_metric_id_rename,
    put_v_1_metrics_metric_id,
    delete_v_1_metrics_metric_id,
    patch_v_1_metrics_metric_id,
)
from ..models import MetricUpset, MetricRename, MetricPatch
from ..client import APIClient
from ..errors import unexpected_status_handler
from ..types import UNSET

METRICS_STRATEGY = TransformationStrategyFactory.create_strategy(APIModels.METRICS)


@unexpected_status_handler
def get_metrics(
    client: APIClient,
    datasource: str = None,
    name: str = None,
    access_zone_id: str = None,
) -> pd.DataFrame:
    """Get metric list data as pandas DataFrame

    Args:
        client (APIClient): The API client.
        name (str): The metric name. Default: None.
        datasource (str): The datasource name. Default: None.
        access_zone_id (str): The access zone id. Default : None.

    Returns:
       pandas.DataFrame
    """
    is_complete = False
    pagination_key = UNSET
    http_dataframes = []
    while not is_complete:
        http_response = get_v1_metrics.sync(
            client=client,
            name=name,
            datasource=datasource,
            access_zone_id=access_zone_id,
            pagination_key=pagination_key,
            limit=5000,
        )
        pagination = http_response.pagination_info
        is_complete = pagination.is_complete
        pagination_key = pagination.pagination_key

        http_dataframes.append(METRICS_STRATEGY.extract_dataframe(http_response))
    return pd.concat(http_dataframes, ignore_index=True)


@unexpected_status_handler
def get_metric_by_id(
    client: APIClient,
    metric_id: str,
) -> pd.DataFrame:
    """Get a single metric by its id as pandas DataFrame

    Args:
        client (APIClient): The API client.
        metric_id (str): The metric id to get.

    Returns:
       pandas.DataFrame
    """
    http_response = get_v_1_metrics_metric_id.sync(client=client, metric_id=metric_id)

    return METRICS_STRATEGY.extract_dataframe(http_response)


@unexpected_status_handler
def add_new_metric(
    client: APIClient,
    new_metric: Union[
        MetricUpset,
        dict,
    ],
) -> None:
    """Add new metric following given data"""
    if isinstance(new_metric, dict):
        new_metric = MetricUpset.from_dict(new_metric)

    http_response = post_v1_metrics.sync(client=client, body=new_metric)


@unexpected_status_handler
def rename_metric(client: APIClient, metric_id: str, new_name: str) -> None:
    """Rename given metric with given name"""
    metric_rename: MetricRename = MetricRename.from_dict({"newName": new_name})
    http_response = put_v_1_metrics_metric_id_rename.sync(
        client=client, metric_id=metric_id, body=metric_rename
    )


@unexpected_status_handler
def update_metric(
    client: APIClient,
    metric_id: str,
    update_metric: Union[
        MetricUpset,
        dict,
    ],
) -> None:
    """Update given metric with given information"""
    if isinstance(update_metric, dict):
        update_metric = MetricUpset.from_dict(update_metric)

    http_response = put_v_1_metrics_metric_id.sync(
        client=client, metric_id=metric_id, body=update_metric
    )


@unexpected_status_handler
def delete_metric(client: APIClient, metric_id: str) -> None:
    """Delete given metric"""
    http_response = delete_v_1_metrics_metric_id.sync(
        client=client, metric_id=metric_id
    )


@unexpected_status_handler
def update_metric_az_sr(
    client: APIClient,
    metric_id: str,
    metric_patch: Union[
        MetricUpset,
        dict,
    ],
) -> None:
    """Update access zones or storage rule to specified metric"""
    metric_patch = MetricPatch.from_dict(metric_patch.to_dict())
    http_response = patch_v_1_metrics_metric_id.sync(
        client=client, metric_id=metric_id, body=metric_patch
    )
