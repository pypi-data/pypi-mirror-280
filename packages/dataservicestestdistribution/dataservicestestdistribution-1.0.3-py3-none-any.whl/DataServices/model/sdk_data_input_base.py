from DataServices.model.sdk_proxy import SDKProxy


class SDKDataInputBase:
    def __init__(self, bearer_token, sdk_proxy=None):
        self.sdk_proxy = sdk_proxy
        self.bearer_token = bearer_token


    @property
    def bearer_token(self):
        return self._bearer_token

    @bearer_token.setter
    def bearer_token(self, bearer_token):
        self._bearer_token = bearer_token

    @property
    def sdk_proxy(self):
        return self._sdk_proxy

    @sdk_proxy.setter
    def sdk_proxy(self, sdk_proxy):
        if sdk_proxy is not None and not isinstance(sdk_proxy, SDKProxy):
            raise ValueError("sdk_proxy must be an instance of SDKProxy or None")
        self._sdk_proxy = sdk_proxy

    def __str__(self):
        return f"SDKDataInputBase(bearer_token={self.bearer_token}, sdk_proxy={self.sdk_proxy})"
