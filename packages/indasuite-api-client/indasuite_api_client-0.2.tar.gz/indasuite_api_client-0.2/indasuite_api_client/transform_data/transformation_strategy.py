from abc import ABC, abstractmethod
import logging
from typing import List, Union

from attr import define
import pandas as pd

from ..types import Response, UNSET
from ..models import (
    ResponseWithMetricList,
    ResponseWithDatabaseList,
    ResponseWithAccessZoneList,
    ResponseWithStorageRuleList,
    ResponseWithMetricDataList,
    ResponseWithMetricDataWithAnnotationsList,
)


@define
class TransformationStrategy(ABC):
    @abstractmethod
    def extract_series(self, response: Response) -> pd.Series:
        """Extract list from HTTP Response to a pandas Series."""
        pass

    @abstractmethod
    def extract_dataframe(self, response: Response) -> pd.DataFrame:
        """Extract data list from HTTP Response to a pandas Dataframe."""
        pass


@define
class MetricsTransformation(TransformationStrategy):
    def extract_series(self, response: ResponseWithMetricList) -> pd.Series:
        """Transform HTTP Response of metric list to a pandas Series of metrics ids."""
        return pd.Series(
            [metric.get("id") for metric in response.to_dict()["data"]]
        )

    def extract_dataframe(
        self, response: ResponseWithMetricList
    ) -> pd.DataFrame:
        """Transform HTTP Response of metric list to a pandas DataFrame of metrics info."""
        metrics = response.to_dict()["data"]

        # Several metrics in 'data'
        if isinstance(metrics, list):
            # Replacing accessZones attribute with a list of access zones ids (prev. list of AccessZone objects as str).
            for metric in metrics:
                metric["accessZones"] = [
                    access_zone["id"] for access_zone in metric["accessZones"]
                ]

            return pd.DataFrame(metrics)

        # Only one metric in 'data'
        elif isinstance(metrics, dict):
            metrics["accessZones"] = [
                access_zone["id"] for access_zone in metrics["accessZones"]
            ]

            return pd.DataFrame([metrics])

        return pd.DataFrame()


@define
class DatabasesTransformation(TransformationStrategy):
    def extract_series(self, response: ResponseWithDatabaseList) -> pd.Series:
        """Transform HTTP Response of database list to a pandas Series of databases names."""
        return pd.Series(response.data)

    def extract_dataframe(
        self, response: ResponseWithDatabaseList
    ) -> pd.DataFrame:
        """Transform HTTP Response of database list to a pandas DataFrame of databases names."""
        return pd.DataFrame(response.data)


@define
class QueryTransformation(TransformationStrategy):
    def extract_series(
        self,
        response: Union[
            ResponseWithMetricDataList,
            ResponseWithMetricDataWithAnnotationsList,
        ],
    ) -> None:
        """Unable to transform response to pandas Series"""
        return None

    def extract_dataframe(
        self,
        response: Union[
            ResponseWithMetricDataList,
            ResponseWithMetricDataWithAnnotationsList,
        ],
    ) -> pd.DataFrame:
        """Transform HTTP Response of metric data list to a pandas DataFrame of metric data, adding metric name column to values, and unit if it exists."""
        values_list = response.to_dict()["values"]
        if isinstance(response, ResponseWithMetricDataWithAnnotationsList):
            for value in values_list:
                if value.get("annotations"):
                    value["annotations"] = [
                        annotation.get("id")
                        for annotation in value.get("annotations")
                    ]

        # Flatten value dict for aggregate/calculated values
        for timestamp in values_list:
            if isinstance(timestamp["value"], dict):

                # Create a key:value entry in dict for each aggregated/calculated value
                for key, val in timestamp.get("value", {}).items():
                    timestamp[key] = val

                # Delete old 'value' key
                timestamp.pop("value", None)

        values_df = pd.DataFrame(values_list)
        values_df["name"] = response.name
        if response.unit is not UNSET:
            values_df["unit"] = response.unit

        return values_df


@define
class AccessZoneTransformation(TransformationStrategy):
    def extract_series(self, response: ResponseWithAccessZoneList) -> pd.Series:
        """Transform HTTP Response of access zone list to a pandas Series of access zones ids."""
        return pd.Series(
            [
                access_zone.get("id")
                for access_zone in response.to_dict()["data"]
            ]
        )

    def extract_dataframe(
        self, response: ResponseWithAccessZoneList
    ) -> pd.DataFrame:
        """Transform HTTP Response of access zone list to a pandas DataFrame of access zones."""
        return pd.DataFrame(response.to_dict()["data"])


@define
class StorageRulesTransformation(TransformationStrategy):
    def extract_series(
        self, response: ResponseWithStorageRuleList
    ) -> pd.Series:
        """Transform HTTP Response of access zone list to a pandas Series of storage rules ids."""
        return pd.Series(
            [
                storage_rule.get("id")
                for storage_rule in response.to_dict()["data"]
            ]
        )

    def extract_dataframe(
        self, response: ResponseWithStorageRuleList
    ) -> pd.DataFrame:
        """Transform HTTP Response of access zone list to a pandas DataFrame of storage rules."""
        return pd.DataFrame(response.to_dict()["data"])
