# Indasuite-api-client

A client library for accessing Indasuite API.

## Getting started

First, create a client to communicate with API :

```python
from indasuite_api_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.example.com",
    access_token="mySuperSecretAccessToken",
)
```

Now use methods from ressources module :

```python
import pandas as pd
from indasuite_api_client import ModelX
from indasuite_api_client.ressources import get_X, add_new_X

with client as client:
    my_X_df: pd.DataFrame = get_X(client=client, x_id = x_id)

    new_X : ModelX = Model(attribute1= "attr1", ...)
    # or new_X : dict = {attribute1: "attr1", ...}
    add_new_X(client, new_X)
```

The models used in the methods are available in the base module. In this example : *from indasuite_api_client import ModelX*.


## Refreshing token

If you're using a device access token, you will have to refresh it everytime you need to use it.
This SDK provides a method to refresh it.

```python
from indasuite_api_client import refresh_access_token

access_token, refresh_token = refresh_access_token(
    device_auth_base_url="https://myFavouriteCompany.device-auth.SomeExtension.com", 
    api_key = "superSecretTokenLikeBearer"
    client_id="deviceX", 
    refresh_token="myOldRefreshToken"
)
```

> ## ⚠️ CAUTION ⚠️
> **YOU NEED TO REGISTER THE NEW REFRESH TOKEN IN YOUR PREFERRED SECRETS MANAGER**. As a reminder, each "refresh token" can only be used once. If you re-use a refresh token, the associated device will be blocked and you will have to repeat the procedure to register a new device with the help of the administrator.


# Available methods

The API provides 3 main types of resources:

+ Query : Databases list and metric values (instant, latest and range).
+ Write : Ingest and update metric values.
+ Metrics : Getting, adding, renaming, updating and deleting metrics.

Each following method is detailed in next sections.

+ ### Query
  + **get_databases** : Retrieve databases list.
  + **get_values_at** :  Retrieve metric values from one or multiple time series at a specific point in time.
  + **get_latest_value** : Retrieve latest metric value from one or multiple time series.
  + **get_values** : Retrieve metric values corresponding to given arguments.

+ ### Write
  + **update_values** : Update ingested values of metric. 
  + **write_values** : Ingest values of non existent metric. 


+ ### Metrics
  + **get_metrics** : Get metric list.
  + **get_metric_by_id** : Get a single metric by its id
  + **add_new_metric** : Add new metric.
  + **update_metric** : Update metric information.
  + **update_metric_az_sr** : Update access zones or storage rule of a metric.
  + **rename_metric** : Rename metric.
  + **delete_metric** : Delete metric.



## Query

### get_databases

**Aim** : Retrieve databases list.

```python
from indasuite_api_client.ressources import get_databases

with client as client:
    databases_df = get_databases(client)
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
+ This methods returns database list as pandas DataFrame.

### get_values_at

**Aim** : Retrieve metric values from one or multiple time series at a specific point in time as pandas DataFrame.

```python
from indasuite_api_client import AuthenticatedClient, Instant
from indasuite_api_client.ressources import get_values_at

with client as client:
    datasource = "test"
    instant_data = {
        "moment": "2024-03-11T11:00:00+01:00",
        "metrics": [
            {"name": "maquette_prod_totale"},
            {"name": "maquette_prod_solaire"},
        ],
        "queryDirection": "Before_moment",
        "timezone": "Europe/Paris",
    }
    instant = Instant.from_dict(instant_data)
    metrics_instant_df = get_values_at(client, "test", instant)
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **datasource** (*str*) : the datasource name.
  + **instant** (*Instant* or *dict*) : Structure that contains information of
    + metrics to retrieve values from.
    + specific point/moment.
    + query direction.

+ This methods returns a pandas DataFrame containing found value for each metric.

### get_latest_value

**Aim** : Retrieve latest metric value from one or multiple time series as pandas DataFrame.

```python
from indasuite_api_client import AuthenticatedClient, Latest
from indasuite_api_client.ressources import get_latest_value

with client as client:
    datasource = "test"
    latest_data = {
        "metrics": [
            {"name": "maquette_prod_totale"},
            {"name": "maquette_prod_solaire"},
        ],
        "timezone": "Europe/Paris",
        "returnUnit": True,
    }
    latest = Latest.from_dict(latest_data)
    metrics_latest_df = get_latest_value(client, "test", latest)
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **datasource** (*str*) : the datasource name.
  + **latest** (*Latest* or *dict*) : Structure that contains information of
    + metrics to retrieve values from.
    + timezone.
    + whether you want the unit or not.

+ This methods returns a pandas DataFrame containing found value for each metric.

### get_values

**Aim** : Retrieve metric values in given range parameters as pandas DataFrame.

```python
from indasuite_api_client import AuthenticatedClient
from indasuite_api_client.ressources import get_values

with client as client:
    metrics_range_df = get_values(
        client=client,
        datasource="test",
        metric_name="maquette_prod_totale",
        start="1924-03-11T10:26:00+01:00",
        end="2224-03-11T11:26:00+01:00",
    )
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **datasource** (*str*) : the datasource name.
  + **metric_name** (*str*) : the metric name to retrieve values from.
  + **start** (*str*) : the range start.
  + **end** (*str*) : the range end.

  + **Optional** :
    + *timezone* (*str*) : the timezone. Default : "Europe/Paris".
    + *limit* (*int*) : maximum number of values to retrieve (must be between 0 and 50000). Default : 50000.
    + *aggregation* (*dict* or *str*) : the definition of aggregation you want. Default : "none".
    + *filter* (*str*) : the filter you want to apply to values. Default : UNSET.

+ This methods returns a pandas DataFrame containing raw or calculated/aggregated values.


## Write

### update_values

**Aim** : Update already ingested values. Add an auto generated annotation.

```python
from indasuite_api_client.ressources import update_values

# Example DataFrame
values_df = pd.DataFrame({
    'timestamp': ["2014-02-28T01:07:21+01:00", "2014-02-28T01:07:21+01:00", "2014-02-28T01:07:21+01:00"],
    'value': [25.6, 26.6, 27.6],
})

with client as client:
    update_values(
        client=client,
        datasource="test",
        metric_name="test_metric",
        values=values_df,
        message="test_message",
    )
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **datasource** (*str*) : the datasource name.
  + **metric_name** (*str*) : the metric name to update.
  + **values** (*pd.DataFrame*) : the values to update as pandas DataFrame.

  + **Optional**:
    + *message* (*str*) : the message associated (maximum length : 250 characters). Default : None.

### write_values

**Aim** : Ingest values. Automatically creates non existent time series. Beware: only send points if you are **absolutely certain** they should be persisted.

```python
from indasuite_api_client.ressources import write_values

# Example DataFrame
values_df = pd.DataFrame({
    'timestamp': ["2014-02-28T01:07:21+01:00", "2014-02-28T01:07:21+01:00", "2014-02-28T01:07:21+01:00"],
    'value': [22.6, 23.6, 24.6],
})

with client as client:
    write_values(
        client=client,
        datasource="test",
        metric_name="test_metric",
        values=values_df
    )
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **datasource** (*str*) : the datasource name.
  + **metric_name** (*str*) : the metric name to save.
  + **values** (*pd.DataFrame*) : the values to ingest as pandas DataFrame.

  + **Optional**:
    + *site* (*str*) : the metadata site. Default : UNSET/None.
    + *device* (*str*) : the metadata device. Default : UNSET/None.
    + *prefix* (*str*) : the metadata prefix. Default : UNSET/None.

## Metrics

### get_metrics

**Aim** : Get metric list.

```python
from indasuite_api_client.ressources import get_databases

with client as client:
    databases_df = get_metrics(client, datasource="test")
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **datasource** (*str*) : the datasource name.
+ This methods returns metrics list as pandas DataFrame.

### get_metric_by_id

**Aim** : Retrieve a single metric data by its id.

```python
from indasuite_api_client import AuthenticatedClient
from indasuite_api_client.ressources import get_metric_by_id

with client as client:
    one_metric = get_metric_by_id(client, "test@maquette_prod_totale")
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **metric_id** (*str*) : the metric id.

+ This methods returns a pandas DataFrame containing a single metric data.

### add_new_metric

**Aim** : Retrieve a single metric data by its id.

```python
from indasuite_api_client import AuthenticatedClient, MetricUpset
from indasuite_api_client.ressources import add_new_metric

with client as client:
    new_metric_data = {
        "storageRuleId": "5a663587-475a-402b-b204-d7e41ce1fed8",
        "accessZones": [
            "f03b8481-1dba-48d7-bbc1-187d7fb10104",
            "09c21936-2709-4ce2-adf9-79ad5f056656"
        ],
        "name": "cip_60",
        "datasource": "main",
        "description": "short description",
        "unit": "m2",
        "source": "Telex",
        "type": "Raw"
    }
    new_metric = MetricUpset.from_dict(new_metric_data)

    add_new_metric(client, new_metric)
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **new_metric** (*MetricUpset* or *dict*) : Structure that contains all information of a metric.

### update_metric 

**Aim** : Update metric information.

```python
from indasuite_api_client import AuthenticatedClient, MetricUpset
from indasuite_api_client.ressources import update_metric

with client as client:
    metric_id = "main@cip_60"

    updated_metric_data = {
        "storageRuleId": "7520dff8-8697-49ae-9d7e-f2f3477252ac",
        "accessZones": [
            "83a36c56-ac0d-4198-91aa-f03f6c8283d5",
            "c7c5be8b-db58-4fce-882f-46e3a2d4347a"
        ],
        "name": "cip_60",
        "datasource": "main",
        "description": "short description",
        "unit": "m2",
        "source": "Telex",
        "type": "Raw"
    }

    updated_metric = MetricUpset.from_dict(updated_metric_data)

    update_metric(client, metric_id, updated_metric)
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **metric_id** (*str*) : the metric id to update.
  + **update_metric** (*MetricUpset* or *dict*) : Structure that contains all updated information of metric.


  
### update_metric_az_sr 

**Aim** : Update access zones or storage rule of a metric.

```python
from indasuite_api_client import AuthenticatedClient, MetricPatch
from indasuite_api_client.ressources import update_metric_az_sr

with client as client:
    metric_id = "main@cip_60"

    updated_metric_data = {
        "accessZonesId": [
            "ef27d903-aa6c-41cf-abb3-b5dd686e3a73",
            "a370e10b-17f6-4d9e-a880-bfb164d5c3c1"
        ],
        "storageRuleId": "dcb8a50e-f4c7-47a3-9a68-34e01dffc65e"
    }
    metric_patch = MetricPatch.from_dict(updated_metric_data)

    update_metric_az_sr(client, metric_id, metric_patch)
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **metric_id** (*str*) : the metric id to update.
  + **metric_patch** (*MetricPatch* or *dict*) : Structure that contains updated access zones and/or storage rule of metric.

### rename_metric

**Aim** : Rename metric.

```python
from indasuite_api_client import AuthenticatedClient
from indasuite_api_client.ressources import rename_metric

with client as client:
    rename_metric(client=client, metric_id="main@cip_60", new_name="TEST_NAME")
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **metric_id** (*str*) : the metric id to rename.
  + **new_name** (*str*) : the new name.

### delete_metric

**Aim** : Delete metric.

```python
from indasuite_api_client import AuthenticatedClient
from indasuite_api_client.ressources import delete_metric

with client as client:
    delete_metric(client=client, metric_id="main@cip_60")
```

+ Parameters :
  + **client** (*AuthenticatedClient*) : HTTP client.
  + **metric_id** (*str*) : the metric id to delete.
