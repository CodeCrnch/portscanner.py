import socket

def port_scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    try:
        s.connect((host, port))
        print(f"Port {port} is open")
    except:
        pass

    s.close()

host = "192.168.0.1"
port_range = range(1, 100)

for port in port_range:
    port_scan(host, port)
