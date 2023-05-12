# ESPNow-MP-Examples
Examples of ESP-Now with Micropython on ESP32. These examples use only two ESP32 devices.

The current stable release, v1.20.0, does not yet have ESP-Now support. For now, use the most recent nightly build from here https://micropython.org/download/esp32/. I tested this code using esp32-20230504-unstable-v1.20.0-50-g786013d46.bin.

# Setup
Running these examples requires two ESP32 devices (called device A and device B below). I used an ESP32 DevKtV1 for device A and ESP32 DevKitC V4 for device B. I used the [Thonny IDE](https://thonny.org/) to transfer, rename, and run files on the devices.

1. Install a version of Micropython that supports ESP-Now on device A
1. Copy all *.py files in the repository to ESP32 device A
1. Change (or Save As) the main_a.py on device A to main.py
1. Uncomment the example you would like to run in main.py
2. Run main.py and note the mac address of the device displayed in the console
3. Update `mac_address_a` in util.py 
4. Repeat previous steps for ESP32 device B

Make sure that `mac_address_a` and `mac_address_b` are match your device MAC addresses on both devices.
