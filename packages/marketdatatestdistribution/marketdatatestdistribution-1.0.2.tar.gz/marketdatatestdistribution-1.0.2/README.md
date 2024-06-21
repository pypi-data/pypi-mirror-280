# MarketData Module

The MarketData SDK is a Python library that is used to retrieve market data. The module has various functions exposed :

- get_pricing_info_pit (token, identifiers, properties={}, proxy=None)
- get_pricing_info_time_series (token, identifiers, properties={}, proxy=None)
- get_market_info_pit (token, identifiers, properties={}, proxy=None)
- get_market_info_time_series (token, identifiers, properties={}, proxy=None)
- get_dividend_pit_info (token, identifiers, properties={}, proxy=None)
- get_dividend_info_time_series (token, identifiers, properties={}, proxy=None)


## Pre-requisite
To access financial data, you must install the authentication and dataservices libraries, as they are essential for obtaining authentication tokens and retrieving the data. Please use the following commands:
```sh
! pip install authtestdistribution==1.0.2
! pip install dataservicestestdistribution==1.0.2
```
Ensure these libraries are installed before attempting to fetch Market data. The authentication library is required to obtain the necessary token, and the dataservices library is needed to access the actual data.



## Features

- The above 6 functions are the entry points for the MarketData module.
- The MarketData SDK provides tools to access real-time and historical market data. 
- It includes functions for retrieving stock prices, trading volumes, indices, and other market-related information. 
- This SDK is crucial for applications requiring current market data for analysis, trading strategies, or financial reporting.
- Errors are well handled at every method.

## Installation

You can install the package using pip. Ensure you have Python 3.12+ installed.

```sh
pip install marketdatatestdistribution==1.0.2
```

## Basic Usage
Here's a brief example of how to Initialize required instances and use this package:
### Required Instances

```sh
from MarketData.services.impl.sdk_marketdata_services_impl import SDKMarketDataServices
from Authentication.services.impl.sdk_authenticate_service_impl import User
from DataServices.model.sdk_proxy import SDKProxy

#Authentication service for getting token
user = User()
username = "your_username"
password = "your password"

# Initialize proxy settings (if needed) 
sdk_proxy_object = SDKProxy(proxy_username="", proxy_password="", proxy_host=None, proxy_port=None, proxy_domain="")
token_response = user.get_token(username, password, proxy=sdk_proxy_object)
bearer_token = token_response.get("access_token")

market_data_services = SDKMarketDataServices()
```


## Fetching MarketData
Use the following methods from the SDKMarketDataServices class to fetch market data:

Note: All these functions of the MarketData services will accept identifiers with a maximum of 10. Additionally, if you need to use a proxy, provide the “data_services_proxy” object as a parameter; otherwise, you can ignore the proxy parameter.

### get_pricing_info_pit
Fetches pricing information for a given point in time.
```sh
response = market_data_services.get_pricing_info_pit(token=bearer_token, identifiers=["I_US5949181045","2588173","EG1320","CSP_594918104","IQT2630413"], properties={}, proxy=sdk_proxy_object) 
display(response.data)
```

### get_pricing_info_time_series
Fetches historical pricing information over a specified time period. 
```sh
response = market_data_services.get_pricing_info_time_series(token=bearer_token, identifiers=["CSP_594918104","IQT2630413","GV012141","MSFT:NasdaqGS","DB649496569","RX309198","MMM:"], properties={}, proxy=sdk_proxy_object) 
display(response.data)
```

### get_dividend_pit_info
Fetches dividend information for a given point in time. 
```sh
response = market_data_services.get_dividend_pit_info(token=bearer_token, identifiers=["CSP_594918104","IQT2630413","GV012141","MSFT:NasdaqGS"], properties={}, proxy=sdk_proxy_object) 
display(response.data)
```

### get_dividend_info_time_series
Fetches historical dividend information over a specified time period 
```sh
response = market_data_services.get_dividend_info_time_series(token=bearer_token, identifiers=["GV012141","MSFT:NasdaqGS","DB649496569","RX309198","MMM:"], properties={}, proxy=sdk_proxy_object) 
display(response.data)
```

### get_market_info_pit
Fetches market information for a given point in time. 
```sh
response = market_data_services.get_market_info_pit(token=bearer_token, identifiers=["IQT2630413","GV012141","MSFT:NasdaqGS","DB649496569","RX309198"], properties={}, proxy=sdk_proxy_object) 
display(response.data)
```
### get_market_info_time_series
Fetches historical market information over a specified time period.
```sh 
response = market_data_services.get_market_info_time_series(token=bearer_token, identifiers=["AAPL:"], properties={}, proxy=sdk_proxy_object) 
display(response.data)
```
By using these methods and the IPython.display.display function, you can efficiently retrieve and display various types of market data in a human-readable format, whether you need information for PIT or TIMESERIES.