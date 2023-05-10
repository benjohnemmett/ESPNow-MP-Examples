import network

mac_address_a = b'\xa4\xcf\x12u?D'
mac_address_b = b'$o(\x9d\x93\xf4'

def activate_wlan():
    wlan_sta = network.WLAN(network.STA_IF)
    wlan_sta.active(True)
    wlan_sta.disconnect()


def get_mac():
    wlan_sta = network.WLAN(network.STA_IF)
    wlan_sta.active(True)
    wlan_mac = wlan_sta.config('mac')
    return wlan_mac

def print_stats(esp_device):
    stats = esp_device.stats()
    print("Stats:")
    print(f"  tx_pkts {stats[0]}") 
    print(f"  tx_responses {stats[1]}") 
    print(f"  tx_failures {stats[2]}")
    print(f"  rx_packets {stats[3]}")
    print(f"  rx_dropped_packets {stats[4]}")