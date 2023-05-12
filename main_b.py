import example_unidirectional as unidirectional
import example_echo as echo
import util

util.activate_wlan()
print("Device B")
print(util.get_mac())

# print("Sending forever to {}".format(util.mac_address_a))
# unidirectional.send_forever(util.mac_address_a)

print("Ready to echo back messages to {}".format(util.mac_address_a))
echo.echo_forever(util.mac_address_a)
