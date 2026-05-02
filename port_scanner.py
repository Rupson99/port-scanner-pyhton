import socket

target = input("Enter target IP (default: 127.0.0.1): ")
if target == "":
    target = "127.0.0.1"

start_port = int(input("Enter start port (e.g., 1): "))
end_port = int(input("Enter end port (e.g., 1024): "))

print("\n----------------------------------------")
print(f"Scanning Target: {target}")
print(f"Port Range: {start_port} - {end_port}")
print("----------------------------------------\n")

open_ports = 0  

for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05)  # Fast timeout

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(f"[OPEN] Port {port:<7} Service: {service}")
            open_ports += 1

        s.close()

    except:
        pass

print("\n----------------------------------------")
print("Scan Completed")
print(f"Total Open Ports Found: {open_ports}")
print("----------------------------------------")