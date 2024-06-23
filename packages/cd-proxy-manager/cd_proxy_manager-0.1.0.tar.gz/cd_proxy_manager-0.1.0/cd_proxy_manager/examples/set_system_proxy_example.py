from cd_proxy_manager import SysProxy

# Example usage
proxy = "proxy.example.com:8080"

sys_proxy = SysProxy()
sys_proxy.set_proxy(proxy)
sys_proxy.set_no_proxy()
