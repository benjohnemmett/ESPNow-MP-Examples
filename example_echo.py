import espnow
import time
import util

def send_and_listen_forever(echoer_mac_address):
    '''
    Sends messages to the given peer address and listens for a response
    '''
    e = espnow.ESPNow()
    e.active(True)
    e.add_peer(echoer_mac_address)

    timeout_ms = 1000

    while True:
        print("Starting send & listen loop...")
        for i in range(100):
            msg = f"Echo this: {i}"
            e.send(echoer_mac_address, msg, True)
            time.sleep(0.5)
            host, bytes_back = e.recv(timeout_ms)
            if host is None:
                print("Timed out waiting for echo")
            else:
                str_back = bytes_back.decode('utf-8')
                if (msg != str_back):
                    print(f"Message received did not match sent. {msg} != {bytes_back}")
                else:
                    print(f"Successfully received echo of '{str_back}'")
                    
            util.print_stats(e)

def echo_forever(sender_mac_address):
    '''
    Sends messages to the given peer address and listens for a response
    '''
    e = espnow.ESPNow()
    e.active(True)

    peer = sender_mac_address
    e.add_peer(peer)

    print("Starting echo loop...")
    while True:
        host, msg = e.recv()
        if msg:
            print(host, msg)
            e.send(sender_mac_address, msg, True) # send the same message back again
            util.print_stats(e)


