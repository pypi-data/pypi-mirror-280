import requests


class RestGatewaySupport:
    @staticmethod
    def create_rest_template(proxy):

        session = requests.Session()

        if proxy and proxy.proxy_host:
            if proxy.proxy_username and proxy.proxy_password:
                session.proxies = {
                    'http': f'http://{proxy.proxy_username}:{proxy.proxy_password}@{proxy.proxy_host}:{proxy.proxy_port}',
                    'https': f'http://{proxy.proxy_username}:{proxy.proxy_password}@{proxy.proxy_host}:{proxy.proxy_port}'
                }
            else:
                session.proxies = {
                    'http': f'http://{proxy.proxy_host}:{proxy.proxy_port}',
                    'https': f'http://{proxy.proxy_host}:{proxy.proxy_port}'
                }

        return session
