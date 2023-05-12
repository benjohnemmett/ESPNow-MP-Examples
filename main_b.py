import util
import example_unidirectional as unidirectional
import example_echo as echo
import example_broadcast_async as bcast
import example_hall_effect_blinker as hall_blinker


util.activate_wlan()
print("Device B")
print(util.get_mac())

## Unidirectional Receiver Example
# print("Receiving forever...")
# unidirectional.receive_forever()

## Echo Example
# print(f"Ready to echo back messages to {util.mac_address_a}")
# echo.echo_forever(util.mac_address_a)

## Broadcast + Async Listen Example
# print(f"Broadcasting to everyone")
# bcast.broadcast_forever()

## Hall Effect Blink
print(f"Sending Hall Effect Data to {util.mac_address_a}")
hall_blinker.send_hall_effect_data(util.mac_address_a)