import espnow
import time

def send_and_listen_forever(echoer_mac_address):
    '''
    Sends messages to the given peer address and listens for a response
    '''
    e = espnow.ESPNow()
    e.active(True)
    e.add_peer(echoer_mac_address)

    while True:
        print("Starting send & listen loop...")
        for i in range(100):
            msg = "Echo this: {}".format(i)
            e.send(echoer_mac_address, msg, True)
            time.sleep(0.5)
            host, bytes_back = e.recv()
            str_back = bytes_back.decode('utf-8')
            if (msg != str_back):
                print("Failed to get echo. {} != {}".format(msg, bytes_back))
            else:
                print("Successfully received echo of '{}'".format(str_back))

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
            if msg == b'end':
                break
            e.send(sender_mac_address, msg, True) # send the same message back again

