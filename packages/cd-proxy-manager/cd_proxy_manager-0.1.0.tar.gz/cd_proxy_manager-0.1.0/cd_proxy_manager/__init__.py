from .format_proxy import ProxyFormatter
from .proxy_dealer import ProxyDealer
from .set_env_proxy import EnvProxyManager
from .set_global_proxy import SysProxy
from cd_proxy_manager import http_judges
from cd_proxy_manager import browser_judges


def format_proxy(proxy_string, delimiter=':', http=False):
    """
    Formats proxy for requests and selenium libs.

    :param delimiter: default is a colon
    :param proxy_string: proxy:port or proxy:port:user:pass
    :param http: Default is set for selenium, http=False.
    :return: proxy dictionary for both types.
    """
    proxy_formatter = ProxyFormatter(delimiter=delimiter)
    if http:
        return proxy_formatter.format_for_requests(proxy_string)
    else:
        return proxy_formatter.format_for_selenium(proxy_string)
