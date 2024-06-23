from cd_proxy_manager import EnvProxyManager


proxy = "10.07.80:8080"
env_proxy = EnvProxyManager()

# sets proxy for this file and any file opened by this file.
env_proxy.set_proxy(http_proxy=proxy, https_proxy=proxy)

# disable proxy
env_proxy.set_proxy(no_proxy=True)

# prints set env variables
env_proxy.proxy_vars()
