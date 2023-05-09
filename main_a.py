import util
import example_unidirectional as unidirectional
import example_echo as echo

util.activate_wlan()
print(util.get_mac())

# print("Receiving forever...")
# unidirectional.receive_forever()

print("Sending & Listening to {}".format(util.mac_address_b))
echo.send_and_listen_forever(util.mac_address_b)
