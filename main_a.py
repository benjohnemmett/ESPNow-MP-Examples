import util
import example_unidirectional as unidirectional
import example_echo as echo
import example_broadcast_async as bcast
import example_hall_effect_blinker as hall_blinker

'''
This is the main.py file for device A. Copy to device A and rename main.py
Uncomment the example that you would like to run, as well as the matching
example on device B.
'''

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
# print(f"Broadcasting to everyone")
# bcast.broadcast_forever()

## Hall Effect Blink
print("Listening for hall effect data and blinking...")
hall_blinker.receive_value_and_blink_loop()
