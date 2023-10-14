#!/bin/python3

import socket
import sys
from datetime import datetime 

if len(sys.argv) != 4:
    print("Invalid amount of arguments.")
    print("Syntax: python3 portscanner.py <ip> <first-port> <last-port>")
    sys.exit()

target = socket.gethostbyname(sys.argv[1])
first_port = int(sys.argv[2])
last_port = int(sys.argv[3])
ports_number = 0

print("-" * 50)
print("| Scanning target: " + target)
print("| Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range (first_port,last_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            ports_number = ports_number + 1 
            print(f"Port {port} is open!")
        
        s.close()

except KeyboardInterrupt:
    print("\nExiting program...")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to the server.")
    sys.exit()

finally:
    print(f"Finished with {ports_number} open doors!")