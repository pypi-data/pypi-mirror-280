import logging
from typing import List
import pandas as pd

from ..api.write import (
    post_v1_databases_datasource_values,
    put_v1_databases_datasource_values,
)
from ..models import (
    Writer,
    WriterMetric,
    WriterMetricData,
    WriterMetadata,
    WriterMetricUpdate,
    OkResponse,
)
from ..client import APIClient
from ..errors import UnexpectedStatus, unexpected_status_handler
from ..types import UNSET


@unexpected_status_handler
def write_values(
    client: APIClient,
    datasource: str,
    metric_name: str,
    values: pd.DataFrame,
    site: str = UNSET,
    device: str = UNSET,
    prefix: str = UNSET,
) -> None:
    """Ingest values. Automatically creates non existent time series. Beware: only send points if you are absolutely certain they should be persisted."""

    if values is None or not (
        "timestamp" in values.columns and "value" in values.columns
    ):
        message = "The “values” dataframe must have these two columns : 'timestamp' and 'value'."
        raise UnexpectedStatus(status_code=400, content=message.encode())

    # Transform values dataframe to list of dict where timestamp and value are dict keys.
    values_dict_list: List[dict] = values[["timestamp", "value"]].to_dict(
        orient="records"
    )

    # Transform list of dict to list of WriterMetricData
    writer_metric_data: list[WriterMetricData] = [
        WriterMetricData.from_dict(item) for item in values_dict_list
    ]

    # Instanciate WriterMetric with given metric name and values
    writer_metric: WriterMetric = WriterMetric(
        name=metric_name, values=writer_metric_data
    )

    # Instanciate WriterMetadata with given kwargs
    writer_metadata: WriterMetadata = WriterMetadata(
        site=site, device=device, prefix=prefix
    )

    # Instanciate HTTP Body (Writer)
    writer_instance: Writer = Writer(body=[writer_metric], metadata=writer_metadata)

    logging.info(
        f"Ingesting {len(writer_metric_data)} values for metric {metric_name}..."
    )
    http_response = post_v1_databases_datasource_values.sync(
        client=client, datasource=datasource, body=writer_instance
    )
    return http_response


@unexpected_status_handler
def update_values(
    client: APIClient,
    datasource: str,
    metric_name: str,
    values: pd.DataFrame,
    message: str = UNSET,
) -> None:
    """Update an already ingested value. Add an auto generated annotation."""

    if values is None or not (
        "timestamp" in values.columns and "value" in values.columns
    ):
        message = "The “values” dataframe must have these two columns : 'timestamp' and 'value'."
        raise UnexpectedStatus(status_code=400, content=message.encode())

    # Transform values dataframe to list of dict where timestamp and value are dict keys.
    values_dict_list: List[dict] = values[["timestamp", "value"]].to_dict(
        orient="records"
    )

    # Transform list of dict to list of WriterMetricData
    writer_metric_data: list[WriterMetricData] = [
        WriterMetricData.from_dict(item) for item in values_dict_list
    ]

    logging.info(
        f"Updating {len(writer_metric_data)} values in metric {metric_name}..."
    )
    # Call function update for each value
    for value_to_update in writer_metric_data:

        # Instanciate HTTP Body (WriterMetricUpdate)
        writer_metric_update: WriterMetricUpdate = WriterMetricUpdate(
            name=metric_name, value=value_to_update, message=message
        )

        http_response = put_v1_databases_datasource_values.sync(
            client=client, datasource=datasource, body=writer_metric_update
        )
        if not isinstance(http_response, OkResponse):
            return http_response
