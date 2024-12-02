import socket
import argparse


def scan(ip, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)  
    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"Port {port} up in IP {ip}")

    sock.close()


def scans(ip, start_port, end_port, timeout):
    for port in range(start_port, end_port + 1):
        scan(ip, port, timeout)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan ports on a given IP or domain.")
    parser.add_argument("ip", help="The IP address or domain to scan.")
    parser.add_argument("start_port", type=int, help="The starting port to scan.")
    parser.add_argument("end_port", type=int, help="The ending port to scan.")
    parser.add_argument("--timeout", type=int, default=1, help="The timeout for each connection attempt (default is 1 second).")

    args = parser.parse_args()

  
    scans(args.ip, args.start_port, args.end_port, args.timeout)
