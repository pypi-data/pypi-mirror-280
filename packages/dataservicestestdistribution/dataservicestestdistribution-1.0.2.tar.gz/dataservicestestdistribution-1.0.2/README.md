# DataServices Module

The DataServices Module is a Python library that is common module for Financials , MarketData and Authentication. 


## Pre-requisite
To access dataservices with Proxy, authentication library is required. Use the following library to install the necessary authentication service:
```sh
pip install authtestdistribution==1.0.2
```

## Features

- Provides services Financials and MarketData service
- Provides common proxy object for Authentication, Financials, DataServices
- Errors are well handled at every method.

## Installation

You can install the package using pip. Ensure you have Python 3.12+ installed.

```sh
pip install dataservicestestdistribution==1.0.2
```

## Basic Usage
Here's a brief example of how to use this package:

```sh
from DataServices.model.sdk_data_input import SDKDataInput
from DataServices.model.sdk_data_request import SDKDataRequest
from DataServices.services.impl.sdk_data_services_impl import SDKDataServicesImpl
from Authentication.model.sdk_proxy import SDKProxy

# Create an instance of main class
sdk_data_services_impl = SDKDataServicesImpl()

# Define proxy settings
sdk_proxy = SDKProxy(proxy_username=None, proxy_password=None, proxy_host='proxy_host', proxy_port=8080)

# invoke the entry point method i.e. invoke_data_service by passing SDKDataInput like: 
sdk_data_request = SDKDataRequest(function="GDSP",properties={},identifiers=["aAPL:","IBM"],mnemonics=["IQ_FILINGDATE_IS","IQ_EBITDA"])
sdk_data_input = SDKDataInput(token, proxy, sdk_data_request)

response = sdk_data_services_impl.invoke_data_service(sdk_data_input)
print(response)


```