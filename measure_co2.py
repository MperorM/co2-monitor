import mh_z19
import time
import serial


#!/usr/bin/env python3
"""PyBluez simple example rfcomm-server.py
Simple demonstration of a server application that uses RFCOMM sockets.
Author: Albert Huang <albert@csail.mit.edu>
modified by Mathias Bonde
$Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $
"""

import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            # protocols=[bluetooth.OBEX_UUID]
                            )

print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

try:
    while True:
        log = open('log.txt', 'a+')
        for i in range(0,5):
            mh_z19.read_all()
            time.sleep(0.5)
            reading = mh_z19.read_all()
            timestamp = time.localtime()
            # log.write(str(timestamp.tm_hour) + '.' + str(timestamp.tm_min) + ": " + str(reading) + '\n')
            time.sleep(1)
            client_sock.send(str(reading['co2']))
            #data = client_sock.recv(1024)
        log.close()
except OSError:
    pass

print("Disconnected.")

client_sock.close()
server_sock.close()
print("All done.")
