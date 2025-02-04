import nmap
import socket
import subprocess
import os
import time

def get_target_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

def scan_ports(target_ip):
    nm = nmap.PortScanner()
    nm.scan(target_ip, '1-65535', '-sS -T2 -Pn -n')
    open_ports = [(port, nm[target_ip]['tcp'][port]['name']) for port in nm[target_ip]['tcp'] if nm[target_ip]['tcp'][port]['state'] == 'open']
    return open_ports

def scan_services(target_ip):
    nm = nmap.PortScanner()
    nm.scan(target_ip, arguments='-sV -T2 -Pn -n')
    services = [(port, nm[target_ip]['tcp'][port]['product']) for port in nm[target_ip]['tcp'] if nm[target_ip]['tcp'][port]['state'] == 'open']
    return services

def identify_os(target_ip):
    nm = nmap.PortScanner()
    nm.scan(target_ip, arguments='-O -T2 -Pn -n')
    os_matches = nm[target_ip]['osmatch']
    return os_matches

def enumerate_subdomains(domain):
    subdomains = []
    command = f"sublist3r -d {domain} -o subdomains.txt"
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists('subdomains.txt'):
        with open('subdomains.txt', 'r') as file:
            subdomains = file.read().splitlines()
    return subdomains

def check_dns_records(domain):
    records = {}
    try:
        result = subprocess.run(['nslookup', '-type=any', domain], capture_output=True, text=True)
        records[domain] = result.stdout
    except Exception as e:
        records[domain] = str(e)
    return records

def detect_technologies(target_ip):
    technologies = []
    try:
        result = subprocess.run(['whatweb', target_ip], capture_output=True, text=True)
        technologies = result.stdout.splitlines()
    except Exception as e:
        technologies = [str(e)]
    return technologies

def enumerate_target(domain):
    target_ip = get_target_ip(domain)
    if not target_ip:
        print(f'[-] Unable to obtain IP address for domain: {domain}')
        return
    
    print(f'[+] Target IP: {target_ip}')
    
    print('[+] Stealth port scanning...')
    open_ports = scan_ports(target_ip)
    if open_ports:
        print(f'[+] Open ports: {open_ports}')
    else:
        print('[-] No open ports found.')

    print('[+] Stealth service enumeration...')
    services = scan_services(target_ip)
    if services:
        print(f'[+] Services found: {services}')
    else:
        print('[-] No services found.')

    print('[+] Stealth OS identification...')
    os_matches = identify_os(target_ip)
    if os_matches:
        print(f'[+] Possible operating systems: {os_matches}')
    else:
        print('[-] OS identification failed.')

    print('[+] Passive subdomain enumeration...')
    subdomains = enumerate_subdomains(domain)
    if subdomains:
        print(f'[+] Subdomains found: {subdomains}')
    else:
        print('[-] No subdomains found.')

    print('[+] Stealth DNS records verification...')
    dns_records = check_dns_records(domain)
    if dns_records:
        print(f'[+] DNS records: {dns_records}')
    else:
        print('[-] No DNS records found.')

    print('[+] Passive technology detection...')
    technologies = detect_technologies(target_ip)
    if technologies:
        print(f'[+] Technologies detected: {technologies}')
    else:
        print('[-] No technologies detected.')

if __name__ == '__main__':
    domain = "example.com"  # Replace with the target domain
    enumerate_target(domain)
