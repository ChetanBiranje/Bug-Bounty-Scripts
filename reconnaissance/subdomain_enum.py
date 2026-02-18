#!/usr/bin/env python3
"""
Subdomain Enumeration Tool
===========================
Discovers subdomains using multiple techniques
"""

import requests
import dns.resolver
import concurrent.futures
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

class SubdomainEnum:
    def __init__(self, domain, wordlist=None, threads=10):
        self.domain = domain
        self.wordlist = wordlist or self.default_wordlist()
        self.threads = threads
        self.found_subdomains = set()
        
    def default_wordlist(self):
        """Default subdomain list"""
        return [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 
            'webdisk', 'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 
            'api', 'dev', 'staging', 'test', 'admin', 'blog', 'shop', 'forum',
            'vpn', 'remote', 'secure', 'portal', 'mail2', 'help', 'support'
        ]
    
    def dns_brute_force(self, subdomain):
        """Brute force DNS lookup"""
        target = f"{subdomain}.{self.domain}"
        try:
            answers = dns.resolver.resolve(target, 'A')
            if answers:
                ip = answers[0].to_text()
                self.found_subdomains.add((target, ip))
                print(f"{Fore.GREEN}[+] Found: {target} -> {ip}{Style.RESET_ALL}")
                return target
        except:
            pass
        return None
    
    def check_crt_sh(self):
        """Check certificate transparency logs"""
        print(f"{Fore.YELLOW}[*] Checking crt.sh...{Style.RESET_ALL}")
        url = f"https://crt.sh/?q=%.{self.domain}&output=json"
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                data = response.json()
                for entry in data:
                    name = entry.get('name_value', '')
                    if name and '*' not in name:
                        self.found_subdomains.add((name, 'crt.sh'))
                        print(f"{Fore.CYAN}[+] crt.sh: {name}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] crt.sh error: {e}{Style.RESET_ALL}")
    
    def run(self):
        """Main execution"""
        print(f"{Fore.BLUE}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Subdomain Enumeration for: {self.domain}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{'='*60}{Style.RESET_ALL}\n")
        
        # Certificate transparency
        self.check_crt_sh()
        
        # DNS brute force
        print(f"\n{Fore.YELLOW}[*] Starting DNS brute force...{Style.RESET_ALL}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.dns_brute_force, self.wordlist)
        
        print(f"\n{Fore.GREEN}[+] Total subdomains found: {len(self.found_subdomains)}{Style.RESET_ALL}")
        return self.found_subdomains

def main():
    parser = argparse.ArgumentParser(description='Subdomain Enumeration Tool')
    parser.add_argument('-d', '--domain', required=True, help='Target domain')
    parser.add_argument('-w', '--wordlist', help='Custom wordlist file')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Thread count')
    parser.add_argument('-o', '--output', help='Output file')
    
    args = parser.parse_args()
    
    wordlist = None
    if args.wordlist:
        with open(args.wordlist, 'r') as f:
            wordlist = [line.strip() for line in f]
    
    enum = SubdomainEnum(args.domain, wordlist, args.threads)
    results = enum.run()
    
    if args.output:
        with open(args.output, 'w') as f:
            for subdomain, ip in results:
                f.write(f"{subdomain},{ip}\n")
        print(f"\n{Fore.GREEN}[+] Results saved to: {args.output}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
