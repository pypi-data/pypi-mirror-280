# DataServices Module

The DataServices Module is a Python library that is common module for Financials , MarketData and Authentication. 



## Features

- Provides data services for Financials and MarketData SDKs
- Provides common proxy object for Authentication, Financials, DataServices
- Errors are well handled at every method.

## Installation

You can install the package using pip. Ensure you have Python 3.12+ installed.

```sh
pip install dataservicestestdistribution==1.0.4
```

## Basic Usage
Here's a brief example of how to use this package:

```sh
from DataServices.model.sdk_data_input import SDKDataInput
from DataServices.model.sdk_data_request import SDKDataRequest
from DataServices.services.impl.sdk_data_services_impl import SDKDataServices
from DataServices.model.sdk_proxy import SDKProxy

# Create an instance of main class
data_services = SDKDataServices()

# Define proxy settings
sdk_proxy_object = SDKProxy(proxy_username="", proxy_password="", proxy_host=None, proxy_port=None, proxy_domain="")

# invoke the entry point method i.e. invoke_data_service by passing SDKDataInput like: 
sdk_data_request = SDKDataRequest(function="GDSP",properties={},identifiers=["aAPL:","IBM"],mnemonics=["IQ_FILINGDATE_IS","IQ_EBITDA"])
sdk_data_input = SDKDataInput(token, sdk_proxy_object, sdk_data_request)

response = data_services.invoke_data_service(sdk_data_input)
print(response)
```
