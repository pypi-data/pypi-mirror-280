"""A client library for accessing IndasuiteApi"""

from .client import AuthenticatedClient
from .auth.authentication import refresh_access_token

from .ressources import (
    get_access_zones,
    get_access_zones_me,
    add_new_access_zone,
    get_metrics,
    add_new_metric,
    get_metric_by_id,
    update_metric,
    rename_metric,
    get_databases,
    get_values_at,
    get_latest_value,
)
from .models import (
    Instant,
    Latest,
    Range,
    MetricUpset,
    MetricRename,
    MetricPatch,
)


__all__ = (
    "AuthenticatedClient",
    "refresh_access_token",
    "get_access_zones",
    "get_access_zones_me",
    "add_new_access_zone",
    "get_metrics",
    "add_new_metric",
    "get_metric_by_id",
    "update_metric",
    "rename_metric",
    "get_databases",
    "get_values_at",
    "get_latest_value",
    "Instant",
    "Latest",
    "Range",
    "MetricUpset",
    "MetricRename",
    "MetricPatch",
)
