#!/usr/bin/env python3
"""
Fast Multi-threaded Port Scanner
=================================
"""

import socket
import concurrent.futures
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

class PortScanner:
    def __init__(self, target, ports, threads=100):
        self.target = target
        self.ports = ports
        self.threads = threads
        self.open_ports = []
        
    def scan_port(self, port):
        """Scan single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                self.open_ports.append((port, service))
                print(f"{Fore.GREEN}[+] Port {port}/tcp OPEN ({service}){Style.RESET_ALL}")
            sock.close()
        except:
            pass
    
    def run(self):
        """Execute scan"""
        print(f"{Fore.BLUE}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Port Scanning: {self.target}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Ports: {self.ports[0]}-{self.ports[-1]}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{'='*60}{Style.RESET_ALL}\n")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.scan_port, self.ports)
        
        print(f"\n{Fore.GREEN}[+] Scan complete!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Open ports: {len(self.open_ports)}{Style.RESET_ALL}")
        return self.open_ports

def main():
    parser = argparse.ArgumentParser(description='Fast Port Scanner')
    parser.add_argument('-t', '--target', required=True, help='Target IP/domain')
    parser.add_argument('-p', '--ports', default='1-1000', help='Port range (e.g., 1-1000)')
    parser.add_argument('--threads', type=int, default=100, help='Thread count')
    parser.add_argument('-o', '--output', help='Output file')
    
    args = parser.parse_args()
    
    # Parse port range
    if '-' in args.ports:
        start, end = map(int, args.ports.split('-'))
        ports = range(start, end + 1)
    else:
        ports = [int(args.ports)]
    
    scanner = PortScanner(args.target, ports, args.threads)
    results = scanner.run()
    
    if args.output:
        with open(args.output, 'w') as f:
            for port, service in results:
                f.write(f"{port},{service}\n")

if __name__ == "__main__":
    main()
