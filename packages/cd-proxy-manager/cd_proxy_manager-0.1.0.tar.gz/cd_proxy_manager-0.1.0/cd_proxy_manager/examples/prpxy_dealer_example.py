from cd_proxy_manager import ProxyDealer


# Fake list of proxies
proxies = [
    "proxy1:port1",
    "proxy2:port2",
    "proxy3:port3",
    "proxy4:port4",
    "proxy5:port5",
    "proxy6:port6",
    "proxy7:port7",
    "proxy8:port8",
    "proxy9:port9",
    "proxy10:port10"
]

# Create ProxyDealer instance
proxy_dealer = ProxyDealer(proxies)

# Example usage of ProxyDealer methods
print("Initial proxies:")
proxy_dealer.print_proxies()

print("\nCycling through proxies with shuffle:")
for _ in range(20):  # Simulate 20 URL requests
    print("Next proxy:", proxy_dealer.get_next_proxy_with_shuffle())

print("\nCycling through proxies without shuffle:")
for _ in range(10):  # Simulate 10 URL requests
    print("Next proxy:", proxy_dealer.get_next_proxy_no_shuffle())

print("\nShuffling proxies:")
proxy_dealer.shuffle_proxies()
proxy_dealer.print_proxies()

print("\nRandom proxy:", proxy_dealer.get_random_proxy())
