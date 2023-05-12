import espnow
import time
import util

def send_forever(receiver_mac_address):
    '''
    Sends messages to peer in infinite loop.
    '''
    e = espnow.ESPNow()
    e.active(True)

    peer = receiver_mac_address # MAC address of peer's wifi interface
    e.add_peer(peer)      # Must add_peer() before send()

    while True:
        print("Starting loop...")
        e.send(peer, "Starting...")
        for i in range(100):
            msg = f"Hello from the other ESP32 {i}"
            e.send(peer, msg, True)
            util.print_stats(e)
            util.print_rssi(e)
            time.sleep(0.5)

def receive_forever():
    '''
    Listens for incomming messages in infinite loop.
    '''
    e = espnow.ESPNow()
    e.active(True)

    print("Listening")
    while True:
        host, msg = e.recv() # Blocking call for default timeout (300,000 ms)
        if msg:
            print(host, msg)
            util.print_stats(e)
