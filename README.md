# portscanner
Bad and inefficient port scanner. Just learning some networking :)
--- 
It works by scanning in a given ip adress all the open ports in the given port range.

To run, its simple: `python3 porscanner.py <ip> <first-port> <last-port>`
```sh
$ python3 porscanner.py 254.254.0.1 50 100
```
This will scan for all open ports between 50 and 100 in the given ip `254.254.0.1`
