import socket
import termcolor


def scan(targets, ports):
    print(termcolor.colored(f"\nStarting Scan For {targets}", "green"))
    for port in range(1, ports):
        scan_port(targets, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port Opened {port}")
        sock.close()
    except:
        pass


targets = input("[*] Enter Target To Scan(split them by ','): ")
ports = int(input("[*] How Many Ports You Want To Scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr, ports)
else:
    scan(targets, ports)
