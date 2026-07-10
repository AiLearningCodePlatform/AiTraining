import socket

host = "127.0.0.1"
open_ports = []

print("Scanning ports...\n")

for port in range(1, 1025):  # common ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((host, port))
    if result == 0:
        open_ports.append(port)

    sock.close()

print("Open ports:", open_ports)

# Check if port 80 is open
if 80 in open_ports:
    print(" Port 80 is OPEN")
else:
    print(" Port 80 is NOT open")
