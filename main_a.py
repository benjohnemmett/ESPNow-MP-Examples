import util
import example_unidirectional as unidirectional
import example_echo as echo
import example_broadcast_async as bcast

util.activate_wlan()
print("Device A")
print(util.get_mac())

## Unidirectional Example
# print("Sending forever to {}".format(util.mac_address_b))
# unidirectional.send_forever(util.mac_address_b)

## Echo Example
# print(f"Sending & Listening to {util.mac_address_b}")
# echo.send_and_listen_forever(util.mac_address_b)

## Broadcast + Async Listen Example
print(f"Broadcasting to everyone")
bcast.broadcast_forever()
