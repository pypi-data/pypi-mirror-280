from enum import StrEnum

from .transformation_strategy import (
    MetricsTransformation,
    DatabasesTransformation,
    AccessZoneTransformation,
    StorageRulesTransformation,
    QueryTransformation,
)


class APIModels(StrEnum):
    DATABASES = "DATABASES"
    QUERY = "QUERY"
    METRICS = "METRICS"
    ACCESS_ZONES = "ACCESS_ZONES"
    STORAGE_RULES = "STORAGE_RULES"


class TransformationStrategyFactory:
    @staticmethod
    def create_strategy(model: APIModels):
        match (model):
            case APIModels.DATABASES:
                return DatabasesTransformation()

            case APIModels.QUERY:
                return QueryTransformation()

            case APIModels.METRICS:
                return MetricsTransformation()

            case APIModels.ACCESS_ZONES:
                return AccessZoneTransformation()

            case APIModels.STORAGE_RULES:
                return StorageRulesTransformation()

            case _:
                raise ValueError("Unsupported model transformation")
