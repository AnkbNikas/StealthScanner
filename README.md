# StealthScanner

StealthScanner is a Python-based reconnaissance tool designed for ethical hacking and penetration testing. It performs various scanning and enumeration tasks in a stealthy manner to minimize detection. Here's a brief summary of its functionalities:

Get Target IP: Converts a given domain name to its corresponding IP address.

Stealth Port Scanning: Uses Nmap to perform a stealth port scan on the target IP, identifying open ports.

Service Enumeration: Uses Nmap to identify services running on the target IP's open ports.

OS Identification: Uses Nmap to identify the operating system of the target host.

Subdomain Enumeration: Uses Sublist3r to passively enumerate subdomains of the target domain.

DNS Records Verification: Uses nslookup to verify DNS records of the target domain.

Technology Detection: Uses WhatWeb to passively detect technologies used on the target website.

The main function combines all these tasks to provide a comprehensive overview of the target domain and its associated IP address. This information can be useful for penetration testers to identify potential vulnerabilities and plan further actions.

Here’s how you can get StealthScanner up and running:

Install Required Tools: Ensure you have the necessary tools installed on your system.

Nmap

Sublist3r

WhatWeb

You can install them using the following commands:

sudo apt-get install nmap
sudo apt-get install sublist3r
sudo apt-get install whatweb

Install Python Packages: Make sure you have Python and the required packages installed.

nmap

socket

You can install the nmap package using pip:

pip install python-nmap

Prepare the Script: Copy the StealthScanner script to a Python file, for example, stealth_scanner.py.

Set Target Domain: In the script, replace the placeholder domain with the actual domain you want to scan:

if __name__ == '__main__':
    domain = "example.com"  # Replace with the target domain
    enumerate_target(domain)

Run the Script: Execute the script in your terminal:

python stealth_scanner.py

This will start the scanning process and output the results of the target domain enumeration.
