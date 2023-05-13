import network

mac_address_a = b'\xa4\xcf\x12u?D'
mac_address_b = b'$o(\x9d\x93\xf4'

def activate_wlan():
    '''
    Required to activate the radio hardware before doing any ESP-Now operations.
    '''
    wlan_sta = network.WLAN(network.STA_IF)
    wlan_sta.active(True)
    wlan_sta.disconnect()


def get_mac():
    '''
    Returns the MAC address of this device.
    '''
    wlan_sta = network.WLAN(network.STA_IF)
    wlan_sta.active(True)
    wlan_mac = wlan_sta.config('mac')
    return wlan_mac

def print_stats(esp_device):
    '''
    Prints ESP-Now stats to stdout.
    '''
    stats = esp_device.stats()
    print("Stats:")
    print(f"  tx_pkts {stats[0]}") 
    print(f"  tx_responses {stats[1]}") 
    print(f"  tx_failures {stats[2]}")
    print(f"  rx_packets {stats[3]}")
    print(f"  rx_dropped_packets {stats[4]}")

def print_rssi(esp_device):
    '''
    Prints the RSSI of the last received message of each peer to stdout.
    '''
    peers_table = esp_device.peers_table
    print("RSSI Table:")
    for peer in peers_table:
        print(f"  {peer} : {peers_table[peer][0]}")
