import espnow
import time
import util
import esp32
from machine import Pin

led_pin_number = 2
global blink_time_seconds

def send_hall_effect_data(receiver_mac_address):
    '''
    Sends hall effect sensor data to peer in infinite loop.
    '''
    espnow_device = espnow.ESPNow()
    espnow_device.active(True)

    peer = receiver_mac_address
    espnow_device.add_peer(peer)

    while True:
        print("Starting hall effect loop...")
        for i in range(100):
            hall_effect_value = esp32.hall_sensor()
            print(f"Sending {hall_effect_value}")
            msg = f"{hall_effect_value}"
            espnow_device.send(peer, msg, True)
            util.print_stats(espnow_device)
            util.print_rssi(espnow_device)
            time.sleep(0.1)


def receive_value_and_blink_loop():
    '''
    Blinks builtin LED based on blink_time_seconds which is set based on data received.
    '''
    global blink_time_seconds
    espnow_device = espnow.ESPNow()
    espnow_device.active(True)
    espnow_device.irq(receive_irq)

    print("Listening")
    led_pin = Pin(led_pin_number, Pin.OUT)
    blink_time_seconds = 0.3
    while True:
        led_pin.on()
        time.sleep(blink_time_seconds)
        led_pin.off()
        time.sleep(blink_time_seconds)
    

def receive_irq(espnow_device):
    '''
    Set blink_time_seconds based on data received.
    '''
    global blink_time_seconds
    try:
        sender, msg = espnow_device.irecv(0)
        value = int(msg.decode())
        print(f"Got Hall Effect value: {value}")
        if value < -100:
            blink_time_seconds = 0.1
        elif value < -50:
            blink_time_seconds = 0.2
        elif value < 0:
            blink_time_seconds = 0.3
        elif value < 50:
            blink_time_seconds = 0.4
        elif value < 100:
            blink_time_seconds = 0.5
        else:
            blink_time_seconds = 0.6
    except:
        print("Failed to parse incoming data")

