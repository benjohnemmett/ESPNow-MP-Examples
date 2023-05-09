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
