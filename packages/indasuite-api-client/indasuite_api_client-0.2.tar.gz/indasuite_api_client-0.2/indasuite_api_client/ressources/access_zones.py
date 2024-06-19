import pandas as pd

from ..transform_data import APIModels, TransformationStrategyFactory
from ..api.access_zones import get_v1_access_zones, get_v1_access_zones_me, post_v1_access_zones
from ..models import AccessZoneAdd
from ..client import APIClient
from ..errors import unexpected_status_handler

ACCESS_ZONES_STRATEGY = TransformationStrategyFactory.create_strategy(APIModels.ACCESS_ZONES)


@unexpected_status_handler
def get_access_zones(client: APIClient) -> pd.DataFrame:
    """Get all access zones data as pandas DataFrame"""
    http_response = get_v1_access_zones.sync(client=client)
    return ACCESS_ZONES_STRATEGY.extract_dataframe(http_response)


@unexpected_status_handler
def get_access_zones_me(client: APIClient) -> pd.DataFrame:
    """Get the connected user access zones data as pandas DataFrame"""
    http_response = get_v1_access_zones_me.sync(client=client)
    return ACCESS_ZONES_STRATEGY.extract_dataframe(http_response)


@unexpected_status_handler
def add_new_access_zone(client: APIClient, new_access_zone: pd.Series) -> None:
    """Add new access zone following given pandas Series"""
    new_access = AccessZoneAdd.from_dict(new_access_zone.to_dict())
    http_response = post_v1_access_zones.sync(client=client, body=new_access)
