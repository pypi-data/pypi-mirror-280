#programmed by ssskingsss for python
import subprocess
import sys

required_modules = [
    ('time', None),
    ('os', None),
    ('colored', '1.4.4'),
    ('concurrent.futures', None),
    ('colorama', None),
    ('warnings', None),
    ('ipaddress', None),
    ('socket', None),
    ('threading', None),
    ('re', None),
    ('urllib.request', None),
    ('itertools', None),
    ('subprocess', None),
    ('tqdm', None),
    ('bs4', None),
    ('retry', None),
    ('argparse', None),
    ('json', None),
    ('requests', None),
    ('ipcalc', None),
    ('colorama', None),
    ('datetime', None),
    ('six', None),
    ('ssl', None),
    ('socket', None),
    ('requests', None),
    ('ping3', None),
    ('aiohttp', None),
    ('termcolor', None),
    ('tldextract', None)
]

def install_module(module):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module, "--break-system-packages"])

def check_and_install_modules():
    for module, version in required_modules:
        try:
            imported_module = __import__(module)
            if version and getattr(imported_module, '__version__', None) != version:
                print(f"{module} version is not {version}. Installing...")
                install_module(f"{module}=={version}")
            else:
                print(f"{module} is already installed.")
        except ImportError:
            print(f"{module} is not installed. Installing...")
            install_module(module)

check_and_install_modules()

import time
import os
from colored import fg 
import concurrent.futures
from colorama import Fore, init
import warnings
import ipaddress
import socket
import threading
import re
import sys
import urllib.request
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style
import subprocess
from tqdm import tqdm
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from retry import retry
import argparse
import json
import requests,sys
import ipcalc
import colorama
from datetime import datetime, timedelta
import dns
import dns.message
import dns.query
import dns.resolver
import requests
import ssl
import socket
import requests
import dns.resolver
from urllib.parse import urlparse
import subprocess
import socket
import random

os.system('cls' if os.name == 'nt' else 'clear')
total_tasks = 0  # Global variable to store the total number of tasks
progress_counter = 0 

OKCYAN = '\033[96m'
FAIL = '\033[91m'
ENDC = '\033[0m'
UNDERLINE = '\033[4m'
OKPURPLE = '\033[92m'
WARNING = '\033[93m'
OKYELLOW = '\033[33m'
OKPURPLE = '\033[35m'
ORANGE = fg('#FFA500')
Magenta = fg('#FF00FF')
Olive = fg('#808000')
OKlime = fg('#00FF00')
OKBLUE = fg('#0000A5')
OKPINK = fg('#FF69B4')

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
        
banner_lines = [
    OKCYAN + "██████╗ ██╗   ██╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ ███████╗ ®" + ENDC,
    OKCYAN + "██╔══██╗██║   ██║██╔════╝ ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝" + ENDC,
    OKCYAN + "██████╔╝██║   ██║██║  ███╗███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝███████╗" + ENDC,
    OKPINK + "██╔══██╗██║   ██║██║   ██║██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗╚════██║" + ENDC,
    OKPINK + "██████╔╝╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║███████║" + ENDC,
    OKPINK + "╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝" + ENDC,
    Olive + "██████╗ ██████╗  ██████╗" + OKlime + "🚓This script is a tool used for creating and scanning domains" + ENDC,
    Olive + "██╔══██╗██╔══██╗██╔═══██╗" + OKlime + "single ips or cidr blocks for for testing purposes" + ENDC,
    Olive + "██████╔╝██████╔╝██║   ██║" + OKlime + "usage of this script is soley upto user discretion" + ENDC,
    Magenta + "██╔═══╝ ██╔══██╗██║   ██║" + OKlime + "user should understand that useage of this script may be" + ENDC,
    Magenta + "██║     ██║  ██║╚██████╔╝" + OKlime + "concidered an attack on a data network, and may violate terms" + ENDC,
    Magenta + "╚═╝     ╚═╝  ╚═╝ ╚═════╝" + OKlime + "of service, use on your own network or get permission first" + ENDC,
    OKPURPLE + "version@ 0.9.43 ®" + ENDC,
    ORANGE + "All rights reserved 2022-2024 ♛: ®" + ENDC,      
    OKYELLOW + "Programmed by King  https://t.me/ssskingsss12 ☏: " + OKYELLOW + "®" + ENDC,]

for line in banner_lines:
    print(line)

def script0():

    OKCYAN = '\033[96m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    WARNING = '\033[93m'
    OKYELLOW = '\033[33m'
    OKPURPLE = '\033[35m'
    ORANGE = '\033[38;5;208m'
    Magenta = '\033[38;5;201m'
    Olive = '\033[38;5;142m'
    OKlime = '\033[38;5;10m'
    OKBLUE = '\033[38;5;21m'
    OKPINK = '\033[38;5;219m'

    banner_lines = [        
        Magenta + "██████╗ ██╗   ██╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ ███████╗ ®" + ENDC,
        Magenta + "██╔══██╗██║   ██║██╔════╝ ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝" + ENDC,
        Magenta + "██████╔╝██║   ██║██║  ███╗███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝███████╗" + ENDC,
        Magenta + "██╔══██╗██║   ██║██║   ██║██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗╚════██║" + ENDC,
        Magenta + "██████╔╝╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║███████║" + ENDC,
        Magenta + "╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝" + ENDC,
        ORANGE + "██████╗ ██████╗  ██████╗" + OKPINK + "this script is a tool used for creating and scanning" + ENDC,
        ORANGE + "██╔══██╗██╔══██╗██╔═══██╗" + OKPINK + "domains, ips or ranges for for testing" + ENDC,
        ORANGE + "██████╔╝██████╔╝██║   ██║" + OKPINK + "usage of this script is soley upto user discretion" + ENDC,
        ORANGE + "██╔═══╝ ██╔══██╗██║   ██║" + OKPINK + "and should understand that useage of this script" + ENDC,
        ORANGE + "██║     ██║  ██║╚██████╔╝" + OKPINK + "may be concidered an attack on a data network" + ENDC,
        ORANGE + "╚═╝     ╚═╝  ╚═╝ ╚═════╝" + OKPURPLE + "use on your own network or get permission first" + ENDC,
        ORANGE + "All rights reserved 2022-2024 ♛: ®" + ENDC,      
        OKYELLOW + "Programmed by King  t.me/ssskingsss ☏: " + OKYELLOW + "®" + ENDC,
    ]
    
    for line in banner_lines:
        print(line)
        
def script1():
    print("\033[96m" + """
        ███████╗██╗   ██╗██████╗     ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
        ██╔════╝██║   ██║██╔══██╗    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
        ███████╗██║   ██║██████╔╝    ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
        ╚════██║██║   ██║██╔══██╗    ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
        ███████║╚██████╔╝██████╔╝    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
        ╚══════╝ ╚═════╝ ╚═════╝     ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ \033[0m""") 
    print("\033[91m" + """                                                                                             
                    ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
                    ██╔════╝████╗  ██║██║   ██║████╗ ████║
                    █████╗  ██╔██╗ ██║██║   ██║██╔████╔██║ 
                    ██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
                    ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
                    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝     \033[0m""") 

    def write_subs_to_file(subdomain, output_file):
        with open(output_file, 'a') as fp:
            fp.write(subdomain.replace("*.","") + '\n')

    def process_target(t, output_file, subdomains):
        global lock  # Declare lock as a global variable

        req = requests.get(f'https://crt.sh/?q=%.{t}&output=json')
        if req.status_code != 200:
            print(f'[*] Information available for {t}!')
            return

        for (key,value) in enumerate(req.json()):
            subdomain = value['name_value']
            with lock:
                write_subs_to_file(subdomain, output_file)
                subdomains.append(subdomain)

    def a():
        global lock  # Declare lock as a global variable

        subdomains = []
        target = ""

        while True:
            target_type = input("Enter '1' for file name or '2' for single IP/domain: ")
            if target_type == '1':
                file_name = input("Enter the file name containing a list of domains: ")
                try:
                    with open(file_name) as f:
                        target = f.readlines()
                    target = [x.strip() for x in target]
                    break
                except:
                    print("Error opening the file. Try again.")
            elif target_type == '2':
                target = input("Enter a single domain name or IP address: ")
                break
            else:
                print("Invalid input. Try again.")

        output_file = input("Enter a file to save the output to: ")

        num_threads = int(input("Enter the number of threads (1-255): "))
        if num_threads < 1 or num_threads > 255:
            print("Invalid number of threads. Please enter a value between 1 and 255.")
            return

        lock = threading.Lock()

        if isinstance(target, list):
            with ThreadPoolExecutor(max_workers=num_threads) as executor:
                futures = []
                for t in target:
                    futures.append(executor.submit(process_target, t, output_file, subdomains))

                for future in tqdm(futures, desc="Progress"):
                    future.result()
        else:
            process_target(target, output_file, subdomains)

        print(f"\n\n[**] Process is complete, {len(subdomains)} subdomains have been found and saved to the file.")

    if __name__ == '__main__':
        try:
            a()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()
            
def script6():
    import threading
    import requests
    import time
    import random
    from bs4 import BeautifulSoup
    from tqdm import tqdm
    print("\033[95m" + """
          
        ██████╗ ███████╗██╗   ██╗██╗   ██╗██╗  ████████╗██████╗  █████╗ 
        ██╔══██╗██╔════╝██║   ██║██║   ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗
        ██████╔╝█████╗  ██║   ██║██║   ██║██║     ██║   ██████╔╝███████║
        ██╔══██╗██╔══╝  ╚██╗ ██╔╝██║   ██║██║     ██║   ██╔══██╗██╔══██║
        ██║  ██║███████╗ ╚████╔╝ ╚██████╔╝███████╗██║   ██║  ██║██║  ██║
        ╚═╝  ╚═╝╚══════╝  ╚═══╝   ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝    
                        \033[0m""")

    def random_user_agent():
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.76",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/84.0.4316.140",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 OPR/84.0.4316.140",
        ]
        return random.choice(user_agents)

    def scrape_page(url, scraped_domains, lock):
        headers = {'User-Agent': random_user_agent()}
        retries = 13  # Number of retries
        for _ in range(retries):
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 500:
                    print("Hold 1 sec, error, retrying...")
                    time.sleep(1)  # Add a delay before retrying
                    continue  # Retry for 500 errors
                response.raise_for_status()  # Raise an error for other bad responses
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all <tr> tags containing data
                tr_tags = soup.find_all('tr')
                
                # Extract domain names and IPs
                has_domains = False
                for tr in tr_tags:
                    tds = tr.find_all('td')
                    if len(tds) >= 2:
                        domain = tds[0].text.strip()
                        ip = tds[1].text.strip()
                        # Add domain name and IP to the set of scraped domains
                        if domain and ip:  # Check if domain and IP are not empty
                            has_domains = True
                            with lock:
                                scraped_domains.add((domain, ip))
                            print(f"Grabbed domain: {domain}, IP: {ip}")  # Print the scraped domain and IP
                # If no domains found, exit early
                if not has_domains:
                    print("No domains found on this page.")
                    return False  # Return False if no domains were found
                return True  # Return True if domains were found
            except requests.RequestException as e:
                print("...Pressure....")
                print("...Retrying...")

        print("Max retries exceeded. Unable to fetch data")
        return False

    def scrape_rapiddns(domain, num_pages):
        base_url = "https://rapiddns.io/s/{domain}?page={page}"
        base_url2 = "https://rapiddns.io/sameip/{domain}?page={page}"
        scraped_domains = set()
        lock = threading.Lock()

        def scrape_for_page(page):
            found_domains = False  # Flag to track if any domains are found in any URL for this page
            for url_type in [base_url, base_url2]:  # Iterate over both URLs
                url = url_type.format(domain=domain, page=page)
                with tqdm(total=1, desc=f"Page {page}", leave=False) as pbar:
                    domains_found = scrape_page(url, scraped_domains, lock)
                    if domains_found:  # Check if any domains were scraped
                        found_domains = True  # Set the flag to True
                        pbar.set_description(f"Page {page} ({len(scraped_domains)} domains)")  # Update description with count of domains
                        pbar.update(1)
                    else:
                        print(f"No more data available for {domain}.")
                        break
            return found_domains

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(scrape_for_page, page) for page in range(1, num_pages + 1)]
            for future in as_completed(futures):
                future.result()  # Wait for all threads to complete

        return scraped_domains

    def ul():
        # Get user input
        domain_input = input("Enter the domain, IP/CDIR, or file name.txt: ")
        num_pages = int(input("Enter the number of pages to scan: "))

        # If input is a file
        if domain_input.endswith('.txt'):
            all_domains = set()
            with open(domain_input, 'r') as file:
                for line in file:
                    current_url = line.strip()
                    if current_url:
                        print(f"Finding data for URL: {current_url}")
                        domains = scrape_rapiddns(current_url, num_pages)
                        if domains:
                            all_domains |= domains  # Merge domains from all URLs
                        else:
                            print("No more domains found for this URL.")
                    else:
                        print("Empty line encountered in the file.")

            if all_domains:
                save_prompt = input("Do you want to save the scraped domains? (yes/no): ")
                if save_prompt.lower() == 'yes':
                    save_domains(all_domains)
                else:
                    print("Domains not saved.")
        else:  # If single domain input
            domains = scrape_rapiddns(domain_input, num_pages)
            if domains:
                save_prompt = input("Do you want to save the scraped domains? (yes/no): ")
                if save_prompt.lower() == 'yes':
                    save_domains(domains)
                else:
                    print("Domains not saved.")
            else:
                print("No domains found.")

    def save_domains(scraped_domains):
        # Get user input for the filename
        print(f"Total unique domains scraped: {len(scraped_domains)}")
        filename = input("Enter the name of the file to save domains (without extension): ")

        # Add '.txt' extension if not provided
        if not filename.endswith('.txt'):
            filename += '.txt'

        with open(filename, 'w') as file:
            for domain, ip in scraped_domains:
                file.write(f"{domain}\n{ip}\n")  # Write domain and IP on separate lines with an empty line between each pair

        print(f"Domains saved to {filename}")

    if __name__ == '__main__':
        try:
            ul()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()

def script2():
    print("\033[95m" + """
        
    ███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
    ██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
    ███████╗██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
    ╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
    ███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
    ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║                           
    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                    \033[0m""")
    def scan_date(domain, formatted_date, domains, ips, progress_bar):
        url = f"https://subdomainfinder.c99.nl/scans/{formatted_date}/{domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                tr_elements = soup.find_all("tr", {"onclick": "markChecked(this)"})

                if tr_elements:
                    unique_domains = set()
                    unique_ips = set()
                    for tr in tr_elements:
                        td_elements = tr.find_all("td")
                        for td in td_elements:
                            link = td.find("a", class_="link")
                            if link:
                                href_link = link["href"]
                                href_link = href_link.lstrip('/').replace('geoip/', '')
                                unique_domains.add(href_link)
                            
                            ip = td.find("a", class_="ip")
                            if ip:
                                href_ip = ip.text.strip()
                                href_ip = href_ip.lstrip('geoip/')
                                unique_ips.add(href_ip)
                    
                    domains.update(unique_domains)
                    ips.update(unique_ips)
        except (ConnectionResetError, requests.exceptions.ConnectionError):
            print("ConnectionResetError occurred. Retrying in 2 seconds...")
            time.sleep(2)
            scan_date(domain, formatted_date, domains, ips, progress_bar)
        finally:
            time.sleep(1)  # Add a delay to slow down the requests
            progress_bar.update(1)

    def c():
        current_date = datetime.now()
        start_date = current_date - timedelta(days=6*1)

        domain = input("Enter the domain name: ")
        domains = set()
        ips = set()
        total_days = (current_date - start_date).days + 1

        print(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
        print(f"End Date: {current_date.strftime('%Y-%m-%d')}")

        save_domains = input("Do you want to save domains (y/n)? ").lower()

        if save_domains == 'y':
            output_domains_filename = input("Enter the output file name for domains (e.g., domains.txt): ")

        save_ips = input("Do you want to save IPs (y/n)? ").lower()

        if save_ips == 'y':
            output_ips_filename = input("Enter the output file name for IPs (e.g., ips.txt): ")

        progress_bar = tqdm(total=total_days, desc="Scanning Dates", unit="day")
        current = start_date
        threads = []

        while current <= current_date:
            formatted_date = current.strftime("%Y-%m-%d")
            thread = threading.Thread(target=scan_date, args=(domain, formatted_date, domains, ips, progress_bar))
            thread.start()
            threads.append(thread)
            current += timedelta(days=1)
            time.sleep(0.5)  # Add a delay between starting threads

        for thread in threads:
            thread.join()

        progress_bar.close()

        if save_domains == 'y' and domains:
            with open(output_domains_filename, 'w') as domains_file:
                for domain in domains:
                    if domain is not None:  # Check for None values
                        domains_file.write(domain + '\n')
            print(f"{len(domains)} Domains saved to {output_domains_filename}")

        if save_ips == 'y' and ips:
            with open(output_ips_filename, 'w') as ips_file:
                for ip in ips:
                    if ip is not None:  # Check for None values
                        ips_file.write(ip + '\n')
            print(f" {len(ips)} IPs saved to {output_ips_filename}")

    if __name__ == '__main__':
        try:
            c()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()

def script3():
        
    print (''' 

    ██╗    ██╗███████╗██████╗ ███████╗ ██████╗  ██████╗██╗  ██╗███████╗████████╗
    ██║    ██║██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝
    ██║ █╗ ██║█████╗  ██████╔╝███████╗██║   ██║██║     █████╔╝ █████╗     ██║   
    ██║███╗██║██╔══╝  ██╔══██╗╚════██║██║   ██║██║     ██╔═██╗ ██╔══╝     ██║   
    ╚███╔███╔╝███████╗██████╔╝███████║╚██████╔╝╚██████╗██║  ██╗███████╗   ██║   
    ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝                     
    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗                 
    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗                
    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝                
    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗                
    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║                
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                

                    ''')

    colorama.init(autoreset=True)

    ipranges = {  "CLOUDFRONT_GLOBAL_IP_LIST": [
                "13.32.0.0/15", "52.46.0.0/18", "52.84.0.0/15", "52.222.128.0/17",
                "54.182.0.0/16", "54.192.0.0/16", "54.230.0.0/16", "54.239.128.0/18",
                "54.239.192.0/19", "54.240.128.0/18", "204.246.164.0/22 204.246.168.0/22",
                "204.246.174.0/23","204.246.176.0/20","205.251.192.0/19","205.251.249.0/24",
                "205.251.250.0/2","205.251.252.0/23","205.251.254.0/24","216.137.32.0/19",
                    ],
            "CLOUDFRONT_REGIONAL_EDGE_IP_LIST_1": [
                "13.54.63.128/26", "13.59.250.0/26", "13.113.203.0/24", "13.124.199.0/24", 
                "13.228.69.0/24", "18.216.170.128/25", "34.195.252.0/24", "34.216.51.0/25", 
                "34.226.14.0/24", "34.232.163.208/29", "35.158.136.0/24", "35.162.63.192/26", 
                "35.167.191.128/26", "52.15.127.128/26", "52.47.139.0/24", "52.52.191.128/26", 
                "52.56.127.0/25", "52.57.254.0/24", "52.66.194.128/26", "52.78.247.128/26", 
                "52.199.127.192/26", "52.212.248.0/26", "52.220.191.0/26", "54.233.255.128/26", 
                "2.57.12.0/24", "2.255.190.0/23", "3.0.0.0/15", "3.2.0.0/24", "3.2.2.0/23", 
                "3.2.8.0/21", "3.2.48.0/23", "3.2.50.0/24", "3.3.6.0/23", "3.3.8.0/21", 
                "3.3.16.0/20", "3.5.32.0/22", "3.5.40.0/21", "3.5.48.0/21", "3.5.64.0/21", 
                "3.5.72.0/23", "3.5.76.0/22", "3.5.80.0/21", "3.5.128.0/19", "3.5.160.0/21", 
                "3.5.168.0/23", "3.5.208.0/22", "3.5.212.0/23", "3.5.216.0/22", "3.5.220.0/23", 
                "3.5.222.0/24", "3.5.224.0/23", "3.5.226.0/24", "3.5.228.0/22", "3.5.232.0/21", 
                "3.5.240.0/20", "3.6.0.0/15", "3.8.0.0/13", "3.16.0.0/13", "3.24.0.0/14", "3.28.0.0/15", 
                "3.33.35.0/24", "3.33.44.0/22", "3.33.128.0/17", "3.34.0.0/15", "3.36.0.0/14", "3.64.0.0/12", 
                "3.96.0.0/14", "3.101.0.0/16", "3.104.0.0/13", "3.112.0.0/14", "3.120.0.0/13", "3.128.0.0/12", 
                "3.144.0.0/13", "3.248.0.0/13", "5.22.145.0/24", "5.183.207.0/24", "13.32.1.0/24", "13.32.2.0/23", 
                "13.32.4.0/22", "13.32.8.0/21", "13.32.16.0/20", "13.32.40.0/22", "13.32.45.0/24", "13.32.46.0/23", 
                "13.32.48.0/21", "13.32.56.0/23", "13.32.59.0/24", "13.32.60.0/23", "13.32.62.0/24", "13.32.64.0/23", 
                "13.32.66.0/24", "13.32.68.0/22", "13.32.72.0/21", "13.32.80.0/21", "13.32.88.0/22", "13.32.92.0/23", 
                "13.32.98.0/23", "13.32.100.0/22", "13.32.104.0/23", "13.32.106.0/24", "13.32.108.0/22", "13.32.112.0/20",
                "13.32.128.0/22", "13.32.132.0/24", "13.32.134.0/23", "13.32.136.0/23", 
                "13.32.140.0/24", "13.32.142.0/23", "13.32.146.0/24", "13.32.148.0/22", "13.32.152.0/22",
                "13.32.160.0/19", "13.32.192.0/20", "13.32.208.0/21", "13.32.224.0/23", "13.32.226.0/24", 
                "13.32.229.0/24", "13.32.230.0/23", "13.32.232.0/24", "13.32.240.0/23", "13.32.246.0/23",
                "13.32.249.0/24", "13.32.252.0/22", "13.33.0.0/19", "13.33.32.0/21", "13.33.40.0/23", "13.33.43.0/24", 
                "13.33.44.0/22", "13.33.48.0/20", "13.33.64.0/19", "13.33.96.0/22", "13.33.100.0/23", "13.33.104.0/21", "13.33.112.0/20", "13.33.128.0/21", "13.33.136.0/22", "13.33.140.0/23", "13.33.143.0/24",
                "13.33.144.0/21", "13.33.152.0/22", "13.33.160.0/21", "13.33.174.0/24", "13.33.184.0/23", "13.33.189.0/24", "13.33.197.0/24", "13.33.200.0/21", "13.33.208.0/21", "13.33.224.0/23", "13.33.229.0/24", "13.33.230.0/23", "13.33.232.0/21", "13.33.240.0/20", "13.35.0.0/21", "13.35.8.0/23", "13.35.11.0/24", "13.35.12.0/22", "13.35.16.0/21", "13.35.24.0/23", "13.35.27.0/24", "13.35.28.0/22", "13.35.32.0/21", "13.35.40.0/23", "13.35.43.0/24", "13.35.44.0/22", "13.35.48.0/21", "13.35.56.0/24", "13.35.63.0/24", "13.35.64.0/21", "13.35.73.0/24", "13.35.74.0/23", "13.35.76.0/22", "13.35.80.0/20", "13.35.96.0/19", "13.35.128.0/20", "13.35.144.0/21", "13.35.153.0/24", "13.35.154.0/23", "13.35.156.0/22", "13.35.160.0/21", "13.35.169.0/24", "13.35.170.0/23", "13.35.172.0/22", "13.35.176.0/21", "13.35.192.0/24", "13.35.200.0/21", "13.35.208.0/21", "13.35.224.0/20", "13.35.249.0/24", "13.35.250.0/23",
                "13.35.252.0/22", "13.36.0.0/14", "13.40.0.0/14", "13.48.0.0/13", "13.56.0.0/14", 
                "13.112.0.0/14", "13.124.0.0/14", "13.200.0.0/15", "13.208.0.0/13", "13.224.0.0/18", 
                "13.224.64.0/19", "13.224.96.0/21", "13.224.105.0/24", "13.224.106.0/23", "13.224.108.0/22", 
                "13.224.112.0/21", "13.224.121.0/24", "13.224.122.0/23", "13.224.124.0/22", "13.224.128.0/20", 
                "13.224.144.0/21", "13.224.153.0/24", "13.224.154.0/23", "13.224.156.0/22", "13.224.160.0/21", "13.224.185.0/24", "13.224.186.0/23", "13.224.188.0/22", "13.224.192.0/18", "13.225.0.0/21", "13.225.9.0/24", "13.225.10.0/23", "13.225.12.0/22", "13.225.16.0/21", "13.225.25.0/24", "13.225.26.0/23", "13.225.28.0/22", "13.225.32.0/19", "13.225.64.0/19", "13.225.96.0/21", "13.225.105.0/24", "13.225.106.0/23", "13.225.108.0/22", "13.225.112.0/21", "13.225.121.0/24", "13.225.122.0/23", "13.225.124.0/22", "13.225.128.0/21", "13.225.137.0/24", "13.225.138.0/23", "13.225.140.0/22", "13.225.144.0/20", "13.225.160.0/21", "13.225.169.0/24", "13.225.170.0/23", "13.225.172.0/22", "13.225.176.0/21", "13.225.185.0/24", "13.225.186.0/23", "13.225.188.0/22", "13.225.192.0/19", "13.225.224.0/20", "13.225.240.0/21", "13.225.249.0/24", "13.225.250.0/23", "13.225.252.0/22", "13.226.0.0/21", "13.226.9.0/24", "13.226.10.0/23", "13.226.12.0/22", "13.226.16.0/20", "13.226.32.0/20", "13.226.48.0/21", "13.226.56.0/24", "13.226.73.0/24", "13.226.77.0/24", "13.226.78.0/23", "13.226.84.0/24", "13.226.86.0/23", "13.226.88.0/21", "13.226.96.0/21", "13.226.112.0/22", "13.226.117.0/24", "13.226.118.0/23", "13.226.120.0/21", "13.226.128.0/17", "13.227.1.0/24", "13.227.2.0/23", "13.227.5.0/24", "13.227.6.0/23",
                "13.227.8.0/21", "13.227.16.0/22", "13.227.21.0/24", "13.227.22.0/23", "13.227.24.0/21", "13.227.32.0/20", "13.227.48.0/22", "13.227.53.0/24", "13.227.54.0/23", "13.227.56.0/21", "13.227.64.0/20", "13.227.80.0/22", "13.227.85.0/24", "13.227.86.0/23", "13.227.88.0/21", "13.227.96.0/19", "13.227.128.0/19", "13.227.160.0/22", "13.227.164.0/24", "13.227.168.0/21", "13.227.198.0/23", "13.227.208.0/22", "13.227.216.0/21", "13.227.228.0/24", "13.227.230.0/23", "13.227.240.0/20", "13.228.0.0/14", "13.232.0.0/13", "13.244.0.0/14", "13.248.0.0/19", "13.248.32.0/20", "13.248.48.0/21", "13.248.60.0/22", "13.248.64.0/21", "13.248.72.0/24", "13.248.96.0/19", "13.248.128.0/17", "13.249.0.0/17", "13.249.128.0/20", "13.249.144.0/24", "13.249.146.0/23", "13.249.148.0/22", "13.249.152.0/21", "13.249.160.0/24", "13.249.162.0/23", "13.249.164.0/22", "13.249.168.0/21", "13.249.176.0/20", "13.249.192.0/19", "13.249.224.0/20", "13.249.241.0/24", "13.249.242.0/23", "13.249.245.0/24", "13.249.246.0/23", "13.249.248.0/21", "13.250.0.0/15", "15.152.0.0/16", "15.156.0.0/15", "15.158.0.0/21", "15.158.8.0/22", "15.158.13.0/24", "15.158.15.0/24", "15.158.16.0/23", "15.158.19.0/24", "15.158.21.0/24", "15.158.22.0/23", "15.158.24.0/23", "15.158.27.0/24", "15.158.28.0/22", "15.158.33.0/24", "15.158.34.0/23", "15.158.36.0/22", "15.158.40.0/21", "15.158.48.0/21", "15.158.56.0/23", "15.158.58.0/24", "15.158.60.0/22", "15.158.64.0/22", "15.158.68.0/23", "15.158.70.0/24", "15.158.72.0/21", "15.158.80.0/21", "15.158.88.0/23", 
                "15.158.91.0/24", "15.158.92.0/22", "15.158.96.0/22", "15.158.100.0/24", "15.158.102.0/23", "15.158.104.0/23", "15.158.107.0/24", "15.158.108.0/22", "15.158.112.0/20", "15.158.128.0/24", "15.158.131.0/24", "15.158.135.0/24", "15.158.138.0/23", "15.158.140.0/23", "15.158.142.0/24", "15.158.144.0/22", "15.158.148.0/23", "15.158.151.0/24", "15.158.152.0/24", "15.158.156.0/22", "15.158.160.0/23", "15.158.162.0/24"
                    ],
            "CLOUDFRONT_REGIONAL_EDGE_IP_LIST_2": [
                "15.158.165.0/24", "15.158.166.0/23", "15.158.168.0/21", "15.158.176.0/22", "15.158.180.0/24", "15.158.182.0/24", "15.158.184.0/21", "15.160.0.0/15", "15.164.0.0/15", "15.168.0.0/16", "15.177.8.0/21", "15.177.16.0/20", "15.177.32.0/19", "15.177.66.0/23", "15.177.68.0/22", "15.177.72.0/21", "15.177.80.0/21", "15.177.88.0/22", "15.177.92.0/23", "15.177.94.0/24", "15.177.96.0/22", "15.181.0.0/17", "15.181.128.0/20", "15.181.144.0/22", "15.181.160.0/19", "15.181.192.0/19", "15.181.224.0/20", "15.181.240.0/21", "15.181.248.0/22", "15.181.252.0/23", "15.181.254.0/24", "15.184.0.0/15", "15.188.0.0/16", "15.190.0.0/22", "15.190.16.0/20", "15.193.0.0/22", "15.193.4.0/23", "15.193.7.0/24", "15.193.8.0/23", "15.193.10.0/24", "15.197.4.0/22", "15.197.12.0/22", "15.197.16.0/22", "15.197.20.0/23", "15.197.24.0/22", "15.197.28.0/23", "15.197.32.0/21", "15.197.128.0/17", "15.206.0.0/15", "15.220.0.0/19", "15.220.32.0/21", "15.220.40.0/22", "15.220.48.0/20", "15.220.64.0/21", "15.220.80.0/20", "15.220.112.0/20", "15.220.128.0/18", "15.220.192.0/20", "15.220.216.0/21", "15.220.224.0/19", "15.221.7.0/24", "15.221.8.0/21", "15.221.16.0/20", "15.221.36.0/22", "15.221.40.0/21", "15.221.128.0/22", "15.222.0.0/15", "15.228.0.0/15", "15.236.0.0/15", "15.248.8.0/22", "15.248.16.0/22", "15.248.32.0/21", "15.248.40.0/22", 
                "15.248.48.0/21", "15.253.0.0/16", "15.254.0.0/16", "16.12.0.0/23", "16.12.2.0/24", "16.12.4.0/23", "16.12.9.0/24", "16.12.10.0/23", "16.12.12.0/23", "16.12.14.0/24", "16.12.18.0/23", "16.12.20.0/24", "16.12.24.0/21", "16.12.32.0/21", "16.12.40.0/23", "16.16.0.0/16", "16.24.0.0/16", "16.50.0.0/15", "16.62.0.0/15", "16.162.0.0/15", "16.168.0.0/14", "18.34.32.0/19", "18.34.64.0/20", "18.34.240.0/20", "18.35.32.0/19", "18.35.64.0/20", "18.35.240.0/20", "18.60.0.0/15", "18.64.0.0/19", "18.64.32.0/21", "18.64.40.0/22", "18.64.44.0/24", "18.64.75.0/24", "18.64.76.0/22", "18.64.80.0/20", "18.64.96.0/20", "18.64.112.0/21", "18.64.135.0/24", "18.64.136.0/21", "18.64.144.0/20", "18.64.160.0/19", "18.64.192.0/20", "18.64.208.0/23", "18.64.225.0/24", "18.64.226.0/23", "18.64.228.0/22", "18.64.232.0/21", "18.64.255.0/24", "18.65.0.0/17", "18.65.128.0/18", "18.65.192.0/19", "18.65.224.0/21", "18.65.232.0/22", "18.65.236.0/23", "18.65.238.0/24", "18.65.254.0/23", "18.66.0.0/16", "18.67.0.0/18", "18.67.64.0/19", "18.67.96.0/20", "18.67.112.0/22", "18.67.116.0/24", "18.67.147.0/24", "18.67.148.0/22", "18.67.152.0/21", "18.67.160.0/23", "18.67.237.0/24", "18.67.238.0/23", "18.67.240.0/20", "18.68.0.0/20", "18.68.16.0/23", "18.68.19.0/24", "18.68.20.0/24", "18.68.64.0/20", "18.68.80.0/24", "18.68.82.0/23", "18.68.130.0/23", "18.68.133.0/24", "18.68.134.0/23", "18.68.136.0/22", "18.88.0.0/18", "18.100.0.0/15", "18.102.0.0/16", "18.116.0.0/14", "18.130.0.0/16", "18.132.0.0/14", 
                "18.136.0.0/16", "18.138.0.0/15", "18.140.0.0/14", "18.144.0.0/15", "18.153.0.0/16", "18.154.30.0/23", "18.154.32.0/20", "18.154.48.0/21", "18.154.56.0/22", "18.154.90.0/23", "18.154.92.0/22", "18.154.96.0/19", "18.154.128.0/20", "18.154.144.0/22", "18.154.148.0/23", "18.154.180.0/22", "18.154.184.0/21", "18.154.192.0/18", "18.155.0.0/21", "18.155.8.0/22", "18.155.12.0/23", "18.155.29.0/24", "18.155.30.0/23", "18.155.32.0/19", "18.155.64.0/21", "18.155.72.0/23", "18.155.89.0/24", "18.155.90.0/23", "18.155.92.0/22", "18.155.96.0/19", "18.155.128.0/17", "18.156.0.0/14", "18.160.0.0/18", "18.160.64.0/19", "18.160.96.0/22", "18.160.100.0/23", "18.160.102.0/24", "18.160.133.0/24", "18.160.134.0/23", "18.160.136.0/21", "18.160.144.0/20", "18.160.160.0/19", "18.160.192.0/19", "18.160.224.0/20", "18.160.240.0/21", "18.160.248.0/22", "18.160.252.0/24", "18.161.12.0/22", "18.161.16.0/20", "18.161.32.0/19", "18.161.64.0/21", "18.161.87.0/24", "18.161.88.0/21", "18.161.96.0/19", "18.161.128.0/19", "18.161.160.0/20", "18.161.176.0/24", "18.161.192.0/19", "18.161.224.0/20", "18.161.240.0/21", "18.161.248.0/22", "18.162.0.0/15", "18.164.15.0/24", "18.164.16.0/20", "18.164.32.0/19", "18.164.64.0/18", "18.164.128.0/17", "18.165.0.0/17", "18.165.128.0/22", "18.165.132.0/23", "18.165.149.0/24", "18.165.150.0/23", "18.165.152.0/21", "18.165.160.0/22", "18.165.179.0/24", "18.165.180.0/22", "18.165.184.0/21", "18.165.192.0/20", "18.165.208.0/24", "18.165.225.0/24", "18.165.226.0/23", "18.165.228.0/22", "18.165.232.0/21", "18.165.255.0/24", "18.166.0.0/15", "18.168.0.0/14", "18.172.86.0/23", "18.172.88.0/21", "18.172.96.0/22", "18.172.100.0/24", "18.172.116.0/22", "18.172.120.0/21", "18.172.128.0/19", "18.172.160.0/20", "18.172.206.0/23", "18.172.208.0/20", "18.172.224.0/21", "18.172.232.0/22", "18.172.251.0/24", "18.172.252.0/22", "18.173.0.0/21", "18.173.8.0/23", "18.173.40.0/22", "18.173.44.0/24", "18.173.49.0/24", "18.173.50.0/24", "18.173.55.0/24", "18.173.56.0/23", "18.173.58.0/24", "18.173.62.0/23", "18.173.64.0/23", "18.173.70.0/23", 
                "18.173.72.0/23", "18.173.74.0/24", "18.173.76.0/22", "18.173.81.0/24", "18.173.82.0/23", "18.173.84.0/24", "18.173.91.0/24", "18.173.92.0/23", "18.173.95.0/24", "18.173.98.0/23", "18.173.105.0/24", "18.173.106.0/23", "18.175.0.0/16", "18.176.0.0/13", "18.184.0.0/15", "18.188.0.0/14", "18.192.0.0/13", "18.200.0.0/14", "18.216.0.0/13", "18.224.0.0/13", "18.236.0.0/15", "18.238.0.0/21", "18.238.8.0/22", "18.238.12.0/23", "18.238.14.0/24", "18.238.121.0/24", "18.238.122.0/23", "18.238.124.0/22", "18.238.128.0/21", "18.238.161.0/24", "18.238.162.0/23", "18.238.164.0/22", "18.238.168.0/21", "18.238.200.0/23", "18.238.203.0/24", "18.238.204.0/23", "18.238.207.0/24", "18.238.209.0/24", "18.238.211.0/24", "18.238.235.0/24", "18.239.230.0/24", "18.244.111.0/24", "18.244.112.0/21", "18.244.120.0/22", "18.244.124.0/23", "18.244.131.0/24", "18.244.132.0/22", "18.244.136.0/21", "18.244.144.0/23", "18.244.151.0/24", "18.244.152.0/21", "18.244.160.0/22", "18.244.164.0/23", "18.244.171.0/24", "18.244.172.0/22", "18.244.176.0/21", "18.244.184.0/23", "18.244.191.0/24", "18.244.192.0/21", "18.244.200.0/22", "18.244.204.0/23", "18.245.229.0/24", "18.245.251.0/24", "18.246.0.0/16", "18.252.0.0/15", "18.254.0.0/16", "23.92.173.0/24", "23.92.174.0/24", "23.130.160.0/24", "23.131.136.0/24", "23.142.96.0/24", "23.144.82.0/24", "23.156.240.0/24", "23.161.160.0/24", "23.183.112.0/23", "23.191.48.0/24", "23.239.241.0/24", "23.239.243.0/24", "23.249.168.0/24", "23.249.208.0/23", "23.249.215.0/24", "23.249.218.0/23", "23.249.220.0/24", "23.249.222.0/23", "23.251.224.0/22", "23.251.232.0/21", "23.251.240.0/21", "23.251.248.0/22", "27.0.0.0/22", "31.171.211.0/24", "31.171.212.0/24", "31.223.192.0/20", "34.208.0.0/12", "34.240.0.0/12", "35.71.64.0/22", "35.71.72.0/22", "35.71.97.0/24", "35.71.100.0/24", "35.71.102.0/24", "35.71.105.0/24", "35.71.106.0/24", "35.71.111.0/24", "35.71.114.0/24", "35.71.118.0/23", "35.71.128.0/17", "35.72.0.0/13", "35.80.0.0/12", "35.152.0.0/16", "35.154.0.0/15", "35.156.0.0/14", "35.160.0.0/13", "35.176.0.0/13", "37.221.72.0/22", "43.198.0.0/15", "43.200.0.0/13", 
                "43.218.0.0/16", "43.247.34.0/24", "43.250.192.0/23", "44.224.0.0/11", "45.8.84.0/22", "45.10.57.0/24", "45.11.252.0/23", "45.13.100.0/22", "45.42.136.0/22", "45.42.252.0/22", "45.45.214.0/24", "45.62.90.0/23", "45.88.28.0/22", "45.91.255.0/24", "45.92.116.0/22", "45.93.188.0/24", "45.95.94.0/24", "45.95.209.0/24", "45.112.120.0/22", "45.114.220.0/22", "45.129.53.0/24", "45.129.54.0/23", "45.129.192.0/24", "45.136.241.0/24", "45.136.242.0/24", "45.138.17.0/24", "45.140.152.0/22", "45.143.132.0/24", "45.143.134.0/23", "45.146.156.0/24", "45.149.108.0/22", "45.152.134.0/23", "45.154.18.0/23", "45.155.99.0/24", "45.156.96.0/22", "45.159.120.0/22", "45.159.224.0/22", "45.223.12.0/24", "46.18.245.0/24", "46.19.168.0/23", "46.28.58.0/23", "46.28.63.0/24", "46.51.128.0/18", "46.51.192.0/20", "46.51.216.0/21", "46.51.224.0/19", "46.137.0.0/16", "46.227.40.0/22", "46.227.44.0/23", "46.227.47.0/24", "46.228.136.0/23", "46.255.76.0/24", "47.128.0.0/14", "50.18.0.0/16", "50.112.0.0/16", "50.115.212.0/23", "50.115.218.0/23", "50.115.222.0/23", "51.16.0.0/15", "51.149.8.0/24", "51.149.14.0/24", "51.149.250.0/23", "51.149.252.0/24", "52.8.0.0/13", "52.16.0.0/14", "52.24.0.0/13", "52.32.0.0/13", "52.40.0.0/14", "52.46.0.0/21", "52.46.8.0/24", "52.46.25.0/24", "52.46.34.0/23", "52.46.36.0/24", "52.46.43.0/24", "52.46.44.0/24", "52.46.46.0/23", "52.46.48.0/23", "52.46.51.0/24", "52.46.53.0/24", "52.46.54.0/23", "52.46.56.0/23", "52.46.58.0/24", "52.46.61.0/24", "52.46.62.0/23", "52.46.64.0/20", "52.46.80.0/21", "52.46.88.0/22", "52.46.96.0/19", "52.46.128.0/19", "52.46.172.0/22", "52.46.180.0/22", "52.46.184.0/22", "52.46.192.0/19", "52.46.240.0/22", "52.46.249.0/24", "52.47.0.0/16", "52.48.0.0/14", "52.52.0.0/15", "52.56.0.0/14", "52.60.0.0/16", "52.62.0.0/15", "52.64.0.0/14", "52.68.0.0/15", "52.74.0.0/15", "52.76.0.0/14",
                "52.84.2.0/23", "52.84.4.0/22", "52.84.8.0/21", "52.84.16.0/20", "52.84.32.0/23", "52.84.35.0/24", "52.84.36.0/22", "52.84.40.0/21", "52.84.48.0/21", "52.84.56.0/23", "52.84.58.0/24", "52.84.60.0/22", "52.84.64.0/22", "52.84.68.0/23", "52.84.70.0/24", "52.84.73.0/24", "52.84.74.0/23", "52.84.76.0/22", "52.84.80.0/22", "52.84.84.0/24", "52.84.86.0/23", "52.84.88.0/21", "52.84.96.0/19", "52.84.128.0/22", "52.84.132.0/23", "52.84.134.0/24", "52.84.136.0/21", "52.84.145.0/24", "52.84.146.0/23", "52.84.148.0/22", "52.84.154.0/23", "52.84.156.0/22", "52.84.160.0/19", "52.84.192.0/21", "52.84.212.0/22", "52.84.216.0/23", "52.84.219.0/24", "52.84.220.0/22", "52.84.230.0/23", "52.84.232.0/22", "52.84.243.0/24", "52.84.244.0/22", "52.84.248.0/23", "52.84.251.0/24", "52.84.252.0/22", "52.85.0.0/20", "52.85.22.0/23", "52.85.24.0/21", "52.85.32.0/21", "52.85.40.0/22", "52.85.44.0/24", "52.85.46.0/23", "52.85.48.0/21", "52.85.56.0/22", "52.85.60.0/23", "52.85.63.0/24", "52.85.64.0/19", "52.85.96.0/22", "52.85.101.0/24", "52.85.102.0/23", "52.85.104.0/21", "52.85.112.0/20", "52.85.128.0/19", "52.85.160.0/21", "52.85.169.0/24", "52.85.170.0/23", "52.85.180.0/24", "52.85.183.0/24", "52.85.185.0/24", "52.85.186.0/23", "52.85.188.0/22", "52.85.192.0/19", "52.85.224.0/20", "52.85.240.0/22", "52.85.244.0/24", "52.85.247.0/24", "52.85.248.0/22", "52.85.252.0/23", "52.85.254.0/24", "52.88.0.0/15", "52.92.0.0/22", "52.92.16.0/21", "52.92.32.0/21", "52.92.128.0/19", "52.92.160.0/21", "52.92.176.0/21", "52.92.192.0/21", "52.92.208.0/21", "52.92.224.0/21", 
                "52.92.240.0/20", "52.93.110.0/24", "52.94.0.0/21", "52.94.8.0/24", "52.94.10.0/23", "52.94.12.0/22", "52.94.16.0/22", "52.94.20.0/24", "52.94.22.0/23", "52.94.24.0/23", "52.94.28.0/23", "52.94.30.0/24", "52.94.32.0/19", "52.94.64.0/22", "52.94.68.0/23", "52.94.72.0/21", "52.94.80.0/20", "52.94.96.0/20", "52.94.112.0/22", "52.94.120.0/21", "52.94.128.0/20", "52.94.144.0/23", "52.94.146.0/24", "52.94.148.0/22", "52.94.160.0/19", "52.94.204.0/22", "52.94.208.0/20", "52.94.224.0/20", "52.94.240.0/22", "52.94.252.0/22", "52.95.0.0/20", "52.95.16.0/21", "52.95.24.0/22", "52.95.28.0/24", "52.95.30.0/23", "52.95.34.0/23", "52.95.48.0/22", "52.95.56.0/22", "52.95.64.0/19", "52.95.96.0/22", "52.95.104.0/22", "52.95.108.0/23", "52.95.111.0/24", "52.95.112.0/20", "52.95.128.0/20", "52.95.144.0/21", "52.95.152.0/22", "52.95.156.0/24", "52.95.160.0/19", "52.95.192.0/20", "52.95.212.0/22", "52.95.224.0/22", "52.95.228.0/23", "52.95.230.0/24", "52.95.235.0/24", "52.95.239.0/24", "52.95.240.0/22", "52.95.244.0/24", "52.95.246.0/23", "52.95.248.0/22", "52.95.252.0/23", "52.95.254.0/24", "52.119.41.0/24", "52.119.128.0/20", "52.119.144.0/21", "52.119.156.0/22", "52.119.160.0/19", "52.119.192.0/21", "52.119.205.0/24", "52.119.206.0/23", "52.119.210.0/23", "52.119.212.0/22", "52.119.216.0/21", "52.119.224.0/21", "52.119.232.0/22", "52.119.240.0/21", "52.119.248.0/23", "52.119.252.0/22", "52.124.130.0/24", "52.124.180.0/24", "52.124.199.0/24", "52.124.215.0/24", "52.124.219.0/24", "52.124.220.0/23", "52.124.225.0/24", "52.124.227.0/24", "52.124.228.0/22", "52.124.232.0/22", "52.124.237.0/24", "52.124.239.0/24", "52.124.240.0/21", "52.124.248.0/23", "52.124.251.0/24", "52.124.252.0/22", "52.128.43.0/24", "52.129.34.0/24", "52.129.64.0/24", "52.129.66.0/24", "52.129.100.0/22", "52.129.104.0/21", "52.144.61.0/24", "52.192.0.0/13", "52.208.0.0/13", "52.216.0.0/18", "52.216.64.0/21", "52.216.72.0/24", "52.216.76.0/22", "52.216.80.0/20", "52.216.96.0/19", "52.216.128.0/18", "52.216.192.0/22", "52.216.200.0/21", "52.216.208.0/20", "52.216.224.0/19", "52.217.0.0/16", "52.218.0.0/21", "52.218.16.0/20", "52.218.32.0/19", "52.218.64.0/22", "52.218.80.0/20", "52.218.96.0/19", "52.218.128.0/24", "52.218.132.0/22", "52.218.136.0/21", 
                "52.218.144.0/24", "52.218.148.0/22", "52.218.152.0/21", "52.218.160.0/24", "52.218.168.0/21", "52.218.176.0/21", "52.218.184.0/22", "52.218.192.0/18", "52.219.0.0/20", "52.219.16.0/22", "52.219.24.0/22", "52.219.32.0/20", "52.219.56.0/21", "52.219.64.0/21", "52.219.72.0/22", "52.219.80.0/20", "52.219.96.0/19", "52.219.128.0/20", "52.219.144.0/22", "52.219.148.0/23", "52.219.152.0/21", "52.219.160.0/23", "52.219.164.0/22", "52.219.168.0/21", "52.219.176.0/20", "52.219.192.0/21", "52.219.200.0/24", "52.219.202.0/23", "52.219.204.0/22", "52.219.208.0/22", "52.219.216.0/23", "52.219.218.0/24", "52.220.0.0/15", "52.222.128.0/18", "52.222.192.0/21", "52.222.200.0/22", "52.222.207.0/24", "52.222.211.0/24", "52.222.221.0/24", "52.222.222.0/23", "52.222.224.0/19", "52.223.0.0/17", "54.64.0.0/12", "54.92.0.0/17", "54.93.0.0/16", "54.94.0.0/15", "54.148.0.0/14", "54.153.0.0/16", "54.154.0.0/15", "54.168.0.0/14", "54.176.0.0/14", "54.180.0.0/15", "54.182.0.0/21", "54.182.134.0/23", "54.182.136.0/21", "54.182.144.0/20", "54.182.162.0/23", "54.182.166.0/23", "54.182.171.0/24", "54.182.172.0/22", "54.182.176.0/21", "54.182.184.0/23", "54.182.188.0/23", "54.182.190.0/24", 
                "54.182.195.0/24", "54.182.196.0/22", "54.182.200.0/22", "54.182.205.0/24", "54.182.206.0/23", "54.182.209.0/24", "54.182.211.0/24", "54.182.215.0/24", "54.182.216.0/21", "54.182.224.0/22", "54.182.228.0/23", "54.182.235.0/24", "54.182.240.0/23", "54.182.246.0/23", "54.182.248.0/22", "54.182.252.0/23", "54.182.254.0/24", "54.183.0.0/16", "54.184.0.0/13", "54.192.0.0/21", "54.192.8.0/22", "54.192.13.0/24", "54.192.14.0/23", "54.192.16.0/21", "54.192.28.0/22", "54.192.32.0/21", "54.192.41.0/24", "54.192.42.0/23", "54.192.48.0/20", "54.192.64.0/18", "54.192.128.0/22", "54.192.136.0/22", "54.192.144.0/22", "54.192.152.0/21", "54.192.160.0/20", "54.192.177.0/24", "54.192.178.0/23", "54.192.180.0/22", "54.192.184.0/23", "54.192.187.0/24", "54.192.188.0/23", "54.192.191.0/24", "54.192.192.0/21", "54.192.200.0/24", "54.192.202.0/23", "54.192.204.0/22", "54.192.208.0/22", "54.192.216.0/21", "54.192.224.0/20", "54.192.248.0/21", "54.193.0.0/16", "54.194.0.0/15", "54.199.0.0/16", "54.200.0.0/14", "54.206.0.0/15", "54.212.0.0/14", "54.216.0.0/14", "54.220.0.0/16", "54.228.0.0/15", "54.230.0.0/22", "54.230.6.0/23", "54.230.8.0/21", "54.230.16.0/21", "54.230.28.0/22", "54.230.32.0/21", "54.230.40.0/22", "54.230.48.0/20", "54.230.64.0/22", "54.230.72.0/21", "54.230.80.0/20", "54.230.96.0/22", "54.230.100.0/24", "54.230.102.0/23", "54.230.104.0/21", "54.230.112.0/20", "54.230.129.0/24", "54.230.130.0/24", "54.230.136.0/22", "54.230.144.0/22", 
                "54.230.152.0/23", "54.230.155.0/24", "54.230.156.0/22", "54.230.160.0/20", "54.230.176.0/21", 
                "54.230.184.0/22", "54.230.188.0/23", "54.230.190.0/24", "54.230.192.0/20", "54.230.208.0/22", "54.230.216.0/21", "54.230.224.0/19", "54.231.0.0/24", "54.231.10.0/23", "54.231.16.0/22", "54.231.32.0/22", "54.231.36.0/24", "54.231.40.0/21", "54.231.48.0/20", "54.231.72.0/21", "54.231.80.0/21", "54.231.88.0/24", "54.231.96.0/19", "54.231.128.0/17", "54.232.0.0/15", "54.238.0.0/16", "54.239.2.0/23", "54.239.4.0/22", "54.239.8.0/21", "54.239.16.0/20", "54.239.32.0/21", "54.239.48.0/20", "54.239.64.0/21", "54.239.96.0/24", "54.239.98.0/23", "54.239.108.0/22", "54.239.113.0/24", "54.239.116.0/22", "54.239.120.0/21"],
            "CLOUDFRONT_REGIONAL_EDGE_IP_LIST_3": [
                "144.81.144.0/21", "144.81.152.0/24", "144.220.1.0/24", "144.220.2.0/23", "144.220.4.0/23", "144.220.11.0/24", "144.220.12.0/22", "144.220.16.0/21", "144.220.26.0/24", "144.220.28.0/23", "144.220.31.0/24", "144.220.37.0/24", "144.220.38.0/24", "144.220.40.0/24", "144.220.49.0/24", "144.220.50.0/23", "144.220.52.0/24", "144.220.55.0/24", "144.220.56.0/24", "144.220.59.0/24", "144.220.60.0/22", "144.220.64.0/22", "144.220.68.0/23", "144.220.72.0/22", "144.220.76.0/24", "144.220.78.0/23", "144.220.80.0/23", "144.220.82.0/24", "144.220.84.0/24", "144.220.86.0/23", "144.220.90.0/24", "144.220.92.0/23", "144.220.94.0/24", "144.220.99.0/24", "144.220.100.0/23", "144.220.103.0/24", "144.220.104.0/21", "144.220.113.0/24", "144.220.114.0/23", "144.220.116.0/23", "144.220.119.0/24", "144.220.120.0/23", "144.220.122.0/24", "144.220.125.0/24", "144.220.126.0/23", "144.220.128.0/21", "144.220.136.0/22", "144.220.140.0/23", "144.220.143.0/24", "146.66.3.0/24", "146.133.124.0/24", "146.133.127.0/24", "147.124.160.0/22", "147.124.164.0/23", "147.160.133.0/24", "147.189.18.0/23", "148.5.64.0/24", "148.5.74.0/24", "148.5.76.0/23", "148.5.80.0/24", "148.5.84.0/24", "148.5.86.0/23", "148.5.88.0/24", "148.5.93.0/24", "148.5.95.0/24", "148.163.131.0/24", "149.19.6.0/24", "149.20.11.0/24", "150.242.68.0/24", "151.148.32.0/22", "151.148.37.0/24", "151.148.38.0/23", "151.148.40.0/23", "152.129.248.0/23", "152.129.250.0/24", "155.46.191.0/24", "155.46.192.0/23", "155.46.195.0/24", "155.46.196.0/23", "155.46.212.0/24", "155.63.85.0/24", "155.63.86.0/24", "155.63.90.0/23", "155.63.208.0/23", "155.63.210.0/24", "155.63.213.0/24", "155.63.215.0/24", "155.63.216.0/23", "155.63.221.0/24", "155.63.222.0/23", "155.226.224.0/20", "155.226.254.0/24", "156.70.116.0/24", "157.53.255.0/24", "157.84.32.0/23", "157.84.40.0/23", "157.166.132.0/22", "157.166.212.0/24", "157.167.134.0/23", "157.167.136.0/21", "157.167.144.0/21", "157.167.152.0/23", "157.167.155.0/24", "157.167.156.0/24", "157.167.225.0/24", "157.167.226.0/23", "157.167.228.0/22", "157.167.232.0/23", "157.175.0.0/16", "157.241.0.0/16", "157.248.214.0/23", "157.248.216.0/22", "158.51.9.0/24", "158.51.65.0/24", "158.115.133.0/24", "158.115.141.0/24", "158.115.147.0/24", "158.115.151.0/24", "158.115.156.0/24", "159.60.0.0/20", "159.60.192.0/19", "159.60.224.0/20", "159.60.240.0/21", "159.60.248.0/22", "159.112.232.0/24", "159.140.140.0/23", "159.140.144.0/24", "159.148.136.0/23", "160.202.21.0/24", "160.202.22.0/24", "161.38.196.0/22", "161.38.200.0/21", "161.69.8.0/21", "161.69.58.0/24", 
                "161.69.75.0/24", "161.69.76.0/22", "161.69.94.0/23", "161.69.100.0/22", "161.69.105.0/24", "161.69.106.0/23", "161.69.109.0/24", "161.69.110.0/23", "161.69.124.0/24", "161.69.126.0/23", "161.129.19.0/24", "185.206.120.0/24", "161.188.128.0/20", "161.188.144.0/22", "161.188.148.0/23", 
                "161.188.152.0/22", "161.188.158.0/23", "161.188.160.0/23", "161.188.205.0/24", "161.199.67.0/24", "162.33.124.0/23", "162.33.126.0/24", "162.136.61.0/24", 
                "162.212.32.0/24", "162.213.126.0/24", "162.213.205.0/24", "162.218.159.0/24", "162.219.9.0/24", "162.219.11.0/24", "162.219.12.0/24", "162.221.182.0/23", "162.247.163.0/24", "162.248.24.0/24", "162.249.117.0/24", "162.250.61.0/24", "162.250.63.0/24", "163.123.173.0/24", "163.123.174.0/24", "163.253.47.0/24", "164.55.233.0/24", "164.55.235.0/24", "164.55.236.0/23", "164.55.240.0/23", "164.55.243.0/24", "164.55.244.0/24", "164.55.255.0/24", "164.152.64.0/24", "164.153.130.0/23", "164.153.132.0/23", "164.153.134.0/24", "165.1.160.0/21", "165.1.168.0/23", "165.69.249.0/24", "165.84.210.0/24", "165.140.171.0/24", "165.225.100.0/23", "165.225.126.0/24", "167.88.51.0/24", "185.206.228.0/24", "168.87.180.0/22", "168.100.27.0/24", "168.100.65.0/24", "168.100.67.0/24", "168.100.68.0/22", "168.100.72.0/22", "168.100.76.0/23", "168.100.79.0/24", "168.100.80.0/21", "168.100.88.0/22", "168.100.93.0/24", "168.100.94.0/23", "168.100.97.0/24", "168.100.98.0/23", "168.100.100.0/22", "168.100.104.0/24", "168.100.107.0/24", "168.100.108.0/22", "168.100.113.0/24", "168.100.114.0/23", "168.100.116.0/22", "168.100.122.0/23", "168.100.164.0/24", "168.100.168.0/24", "168.149.242.0/23", "168.149.244.0/23", "168.149.247.0/24", "168.203.6.0/23", "168.238.100.0/24", "169.150.104.0/24", "169.150.106.0/24", "169.150.108.0/22", "170.39.131.0/24", "170.39.141.0/24", "170.72.226.0/24", "170.72.228.0/22", "170.72.232.0/24", "170.72.234.0/23", "170.72.236.0/22", "170.72.240.0/22", "170.72.244.0/23", "170.72.252.0/22", "170.89.128.0/22", "170.89.132.0/23", "170.89.134.0/24", "170.89.136.0/22", "170.89.141.0/24", "170.89.144.0/24", "170.89.146.0/23", "170.89.149.0/24", 
                "170.89.150.0/24", "170.89.152.0/23", "170.89.156.0/22", "170.89.160.0/24", "170.89.164.0/24", "170.89.173.0/24", "170.89.176.0/24", "170.89.178.0/24", "170.89.181.0/24", "170.89.182.0/23", "170.89.184.0/24", "170.89.189.0/24", "170.89.190.0/23", "170.114.16.0/20", "170.114.34.0/23", "170.114.37.0/24", "170.114.38.0/24", "170.114.40.0/23", "170.114.42.0/24", "170.114.44.0/24", "170.114.49.0/24", "170.114.53.0/24", "170.176.129.0/24", "170.176.135.0/24", "170.176.153.0/24", "170.176.154.0/24", "170.176.156.0/24", "170.176.158.0/24", "170.176.160.0/24", "170.176.200.0/24", "170.176.212.0/22", "170.176.216.0/23", "170.176.218.0/24", "170.176.220.0/22", "170.200.94.0/24", "172.86.224.0/24", "172.99.250.0/24", "173.199.36.0/23", "173.199.38.0/24", "173.199.56.0/23", "173.231.88.0/22", "173.240.165.0/24", "173.241.39.0/24", "173.241.44.0/23", "173.241.46.0/24", "173.241.82.0/24", "173.241.87.0/24", "173.241.94.0/24", "173.249.168.0/22", "174.34.225.0/24", "175.29.224.0/19", "175.41.128.0/17", "176.32.64.0/19", "176.32.96.0/20", "176.32.112.0/21", "176.32.120.0/22", "176.32.126.0/23", "176.34.0.0/16", "176.110.104.0/24", "176.116.14.0/24", "176.116.21.0/24", "176.124.224.0/24", "176.221.80.0/24", "176.221.82.0/23", "177.71.128.0/17", "177.72.240.0/21", "178.21.147.0/24", "178.21.148.0/24", "185.207.135.0/24", "178.213.75.0/24", "178.236.0.0/20", "178.239.128.0/23", "178.239.130.0/24", "179.0.17.0/24", "182.54.135.0/24", "184.72.0.0/18", "184.94.214.0/24", "184.169.128.0/17", "185.7.73.0/24", "185.20.4.0/24", "185.31.204.0/22", "185.36.216.0/22", "185.37.37.0/24", "185.37.39.0/24", "185.38.134.0/24", "185.39.10.0/24", "185.43.192.0/22", "185.44.176.0/24", "185.48.120.0/22", "185.49.132.0/23", "185.53.16.0/22", "185.54.72.0/22", "185.54.124.0/24", "185.54.126.0/24", "185.55.188.0/24", "185.55.190.0/23", "185.57.216.0/24", "185.57.218.0/24", "185.64.6.0/24", "185.64.73.0/24", "185.66.202.0/23", "185.68.58.0/23", "185.69.1.0/24", "185.75.61.0/24", "185.75.62.0/23", "185.79.75.0/24", "185.83.20.0/22", "185.88.184.0/23", "185.88.186.0/24", "185.95.174.0/24", "185.97.10.0/24", "185.98.156.0/24", "185.98.159.0/24", "185.107.197.0/24", "185.109.132.0/22", "185.118.109.0/24", "185.119.223.0/24", "185.120.172.0/22", "185.121.140.0/23", "185.121.143.0/24", "185.122.214.0/24", "185.127.28.0/24", "185.129.16.0/23", "185.133.70.0/24", "185.134.79.0/24", "185.135.128.0/24", "185.137.156.0/24", "185.143.16.0/24", "185.143.236.0/24", "185.144.16.0/24", 
                "185.144.18.0/23", "185.144.236.0/24", "185.145.38.0/24", "185.146.155.0/24", "185.150.179.0/24", "185.151.47.0/24", "185.166.140.0/22", "185.169.27.0/24", "185.170.188.0/23", "185.172.153.0/24", 
                "185.172.155.0/24", "185.175.91.0/24", "185.186.212.0/24", "185.187.116.0/22", "185.195.0.0/22",
                "185.195.148.0/24", "185.210.156.0/24", "185.212.105.0/24", "185.212.113.0/24", "185.214.22.0/23", "185.215.115.0/24", "185.219.146.0/23", "185.221.84.0/24", "185.225.252.0/24", "185.225.254.0/23", "185.226.166.0/24", "185.232.99.0/24", "185.235.38.0/24", "185.236.142.0/24", "185.237.5.0/24", "185.237.6.0/23", "185.253.9.0/24", "185.255.32.0/22", "185.255.54.0/24", "188.72.93.0/24", "188.95.140.0/23", "188.95.142.0/24", "188.116.35.0/24", "188.172.137.0/24", "188.172.138.0/24", "188.209.136.0/22", "188.241.223.0/24", "188.253.16.0/20", "191.101.94.0/24", "191.101.242.0/24", "192.35.158.0/24", "192.42.69.0/24", "192.64.71.0/24", "192.71.84.0/24", "192.71.255.0/24", "192.80.240.0/24", "192.80.242.0/24", "192.80.244.0/24", "192.81.98.0/24", "192.84.23.0/24", "192.84.38.0/24", "192.84.231.0/24", "192.101.70.0/24", "192.111.5.0/24", "192.111.6.0/24", "192.118.71.0/24", "192.132.1.0/24", "192.151.28.0/23", "192.152.132.0/23", "192.153.76.0/24", "192.161.151.0/24", "192.161.152.0/24", "192.161.157.0/24", "192.175.1.0/24", "192.175.3.0/24", "192.175.4.0/24", "192.184.67.0/24", "192.184.69.0/24", "192.184.70.0/23", "192.190.135.0/24", "192.190.153.0/24", "192.197.207.0/24", "192.206.0.0/24", "192.206.146.0/23", "192.206.206.0/23", "192.210.30.0/23", "192.225.99.0/24", "192.230.237.0/24", "192.245.195.0/24", "193.0.181.0/24", "193.3.28.0/24", "193.3.160.0/24", "193.9.122.0/24", "193.16.22.0/24", "193.17.68.0/24", "193.24.42.0/23", "193.25.48.0/24", "193.25.51.0/24", "193.25.52.0/23", "193.25.54.0/24", "193.25.60.0/22", "193.30.161.0/24", "193.31.111.0/24", "193.33.137.0/24", "193.35.157.0/24", "193.37.39.0/24", "193.37.132.0/24", "193.39.114.0/24", "193.47.187.0/24", "193.57.172.0/24", "193.84.26.0/24", "193.100.64.0/24", "193.104.169.0/24", "193.105.212.0/24", "193.107.65.0/24", "193.110.146.0/24", "193.111.200.0/24", "193.131.114.0/23", "193.138.90.0/24", "193.150.164.0/24", "193.151.92.0/24", "193.151.94.0/24", "193.160.155.0/24", "193.176.54.0/24", "193.200.30.0/24", "193.200.156.0/24", "193.207.0.0/24", "193.219.118.0/24", "193.221.125.0/24", "193.227.82.0/24", "193.234.120.0/22", "193.239.162.0/23", "193.239.236.0/24", "193.243.129.0/24", "194.5.67.0/24", "194.5.147.0/24", "194.29.54.0/24", "194.29.58.0/24", "194.30.175.0/24", "194.33.184.0/24", "194.42.96.0/23", "194.42.104.0/23", "194.53.200.0/24", "194.99.96.0/23", "194.104.235.0/24", "194.140.230.0/24", "194.165.43.0/24", "194.176.117.0/24", "194.195.101.0/24", "194.230.56.0/24", "194.247.26.0/23", "195.8.103.0/24", "195.42.240.0/24", "195.46.38.0/24", "195.60.86.0/24", "195.69.163.0/24", "195.74.60.0/24", "195.82.97.0/24", "195.85.12.0/24", "195.88.213.0/24", "195.88.246.0/24", "195.93.178.0/24", "195.191.165.0/24", "195.200.230.0/23", "195.234.155.0/24", "195.244.28.0/24", "195.245.230.0/23", "198.99.2.0/24", "198.137.150.0/24", "198.154.180.0/23", "198.160.151.0/24", "198.169.0.0/24", "198.176.120.0/23", "198.176.123.0/24", "198.176.124.0/23", "198.176.126.0/24", "198.183.226.0/24", "198.202.176.0/24", "198.204.13.0/24", "198.207.147.0/24", "198.212.50.0/24", "198.251.128.0/18", "198.251.192.0/19", "198.251.224.0/21", "199.43.186.0/24", "199.47.130.0/23", "199.59.243.0/24", "199.65.20.0/22", "199.65.24.0/23", "199.65.26.0/24", "199.65.242.0/24", "199.65.245.0/24", "199.65.246.0/24", "199.65.249.0/24", "199.65.250.0/24", "199.65.252.0/23", "199.68.157.0/24", "199.85.125.0/24", "199.87.145.0/24", "199.91.52.0/23", "199.115.200.0/24", "199.127.232.0/22", "199.165.143.0/24", "199.187.168.0/22", "199.192.13.0/24", "199.196.235.0/24", "199.250.16.0/24", "199.255.32.0/24", "199.255.192.0/22", "199.255.240.0/24", "202.8.25.0/24", "202.44.120.0/23", "202.44.127.0/24", "202.45.131.0/24", "202.50.194.0/24", "202.52.43.0/24", "202.92.192.0/23", "202.93.249.0/24", "202.128.99.0/24", "202.160.113.0/24", "202.160.115.0/24", "202.160.117.0/24", "202.160.119.0/24", "202.173.24.0/24", "202.173.26.0/23", "202.173.31.0/24", "203.12.218.0/24", "203.20.242.0/23", "203.27.115.0/24", "203.27.226.0/23", "203.55.215.0/24", "203.57.88.0/24", "203.83.220.0/22", "203.175.1.0/24", "203.175.2.0/23", "203.210.75.0/24", "204.10.96.0/21", "204.11.174.0/23", "204.15.172.0/24", "204.15.215.0/24", "204.27.244.0/24", "204.48.63.0/24", "204.77.168.0/24", "204.90.106.0/24", "204.110.220.0/23", "204.110.223.0/24", "204.154.231.0/24", "204.236.128.0/18", "204.239.0.0/24", "204.246.160.0/22", "204.246.166.0/24", "204.246.169.0/24", "204.246.175.0/24", "204.246.177.0/24", "204.246.178.0/24", "204.246.180.0/23", "204.246.182.0/24", "204.246.187.0/24", "204.246.188.0/22", "205.147.81.0/24", "205.157.218.0/23", "205.166.195.0/24", "205.201.44.0/23", "205.220.188.0/24", "205.235.121.0/24", "205.251.192.0/21", "205.251.200.0/24", "205.251.203.0/24", "205.251.206.0/23", "205.251.212.0/23", "205.251.216.0/24", 
                "205.251.218.0/23", "205.251.222.0/23", "205.251.224.0/21", "205.251.232.0/22", "205.251.240.0/22", "205.251.244.0/23", "205.251.247.0/24", "205.251.248.0/23", "205.251.251.0/24", "205.251.253.0/24", "206.108.41.0/24", "206.130.88.0/23", "206.166.248.0/23", "206.195.217.0/24", "206.195.218.0/24", "206.195.220.0/24", "206.198.37.0/24", "206.198.131.0/24", "206.225.200.0/23", "206.225.203.0/24", "206.225.217.0/24", "206.225.219.0/24", "207.2.117.0/24", "207.2.118.0/23", "207.34.11.0/24", "207.45.79.0/24", "207.90.252.0/23", "207.167.92.0/22", "207.167.126.0/23", "207.171.160.0/19", "207.189.185.0/24", "207.202.17.0/24", "207.202.18.0/24", "207.202.20.0/24", "207.207.176.0/22", "207.230.151.0/24", "207.230.156.0/24", "208.56.44.0/23", "208.56.47.0/24", "208.56.48.0/20", "208.71.22.0/24", "208.71.106.0/24", "208.71.210.0/24", "208.71.245.0/24", "208.73.7.0/24", "208.81.250.0/24", "208.82.220.0/22", "208.89.247.0/24", "208.90.238.0/24", "208.91.36.0/23", "208.95.53.0/24", "208.127.200.0/21", "209.51.32.0/21", "209.54.160.0/19", "209.94.75.0/24", "209.126.65.0/24", "209.127.220.0/24", "209.160.100.0/22", "209.163.96.0/24", "209.169.228.0/24", "209.169.242.0/24", "209.182.220.0/24", "209.222.82.0/24", "211.44.103.0/24", "212.4.240.0/22", "212.8.241.0/24", "212.19.235.0/24", "212.19.236.0/24", "212.104.208.0/24", "212.192.221.0/24", "213.5.226.0/24", "213.109.176.0/22", "213.170.156.0/24", "213.170.158.0/24", "213.217.29.0/24", "216.9.204.0/24", "216.24.45.0/24", "216.73.153.0/24", "216.73.154.0/23", "216.74.122.0/24", "216.75.96.0/22", "216.75.104.0/21", "216.99.220.0/24", "216.115.17.0/24", "216.115.20.0/24", "216.115.23.0/24", "216.120.142.0/24", "216.120.187.0/24", "216.122.176.0/22", "216.137.32.0/24", "216.137.34.0/23", "216.137.36.0/22", "216.137.40.0/21", "216.137.48.0/21", "216.137.56.0/23", "216.137.58.0/24", "216.137.60.0/23", "216.137.63.0/24", "216.147.0.0/23", "216.147.3.0/24", "216.147.4.0/22", "216.147.9.0/24", "216.147.10.0/23", "216.147.12.0/23", 
                "216.147.15.0/24", "216.147.16.0/23", "216.147.19.0/24", "216.147.20.0/23", "216.147.23.0/24", "216.147.24.0/22", "216.147.29.0/24", "216.147.30.0/23", "216.147.32.0/23", "216.157.133.0/24", "216.157.139.0/24", "216.169.145.0/24", "216.170.100.0/24", "216.182.236.0/23", "216.198.2.0/23", "216.198.17.0/24", "216.198.18.0/24", "216.198.33.0/24", "216.198.34.0/23", "216.198.36.0/24", "216.198.49.0/24", "216.211.162.0/24", "216.219.113.0/24", "216.238.188.0/23", "216.238.190.0/24", "216.241.208.0/20", "217.8.118.0/24", "217.117.65.0/24", "217.117.71.0/24", "217.117.76.0/24", "217.119.96.0/24", "217.119.98.0/24", "217.119.104.0/23", "217.169.73.0/24", "218.33.0.0/18" ],
            "CLOUDFRONT_REGIONAL_EDGE_IP_LIST_4": [
                "54.239.130.0/23", "54.239.132.0/23", "54.239.135.0/24", "54.239.142.0/23", "54.239.152.0/23", "54.239.158.0/23", "54.239.162.0/23", "54.239.164.0/23", "54.239.168.0/23", "54.239.171.0/24", "54.239.172.0/24", "54.239.174.0/23", "54.239.180.0/23", "54.239.186.0/24", "54.239.192.0/24", "54.239.195.0/24", "54.239.200.0/24", "54.239.204.0/22", "54.239.208.0/21", "54.239.216.0/23", "54.239.219.0/24", "54.239.220.0/23", "54.239.223.0/24", "54.240.0.0/21", "54.240.16.0/24", "54.240.24.0/22", "54.240.50.0/23", "54.240.52.0/22", "54.240.56.0/21", "54.240.80.0/20", "54.240.96.0/20", "54.240.112.0/21", "54.240.129.0/24", "54.240.130.0/23", "54.240.160.0/23", "54.240.166.0/23", "54.240.168.0/21", "54.240.184.0/21", "54.240.192.0/21", "54.240.200.0/24", "54.240.202.0/24", "54.240.204.0/22", "54.240.208.0/20", "54.240.225.0/24", "54.240.226.0/23", "54.240.228.0/22", "54.240.232.0/22", "54.240.244.0/22", "54.240.248.0/21", "54.241.0.0/16", "54.244.0.0/14", "54.248.0.0/13", "57.180.0.0/14", "58.181.95.0/24", "62.133.34.0/24", "63.32.0.0/14", "63.140.32.0/22", "63.140.36.0/23", "63.140.48.0/22", "63.140.52.0/24", "63.140.55.0/24", "63.140.56.0/23", "63.140.61.0/24", "63.140.62.0/23", "63.246.112.0/24", "64.35.162.0/24", "64.45.129.0/24", "64.45.130.0/23", "64.52.111.0/24", "64.56.212.0/24", "64.65.61.0/24", "64.69.212.0/24", "64.69.223.0/24", "64.186.3.0/24", "64.187.128.0/20", "64.190.110.0/24", "64.190.237.0/24", "64.207.194.0/24", "64.207.196.0/24", "64.207.198.0/23", "64.207.204.0/23", "64.234.115.0/24", "64.238.2.0/24", "64.238.5.0/24", "64.238.6.0/24", "64.238.14.0/24", "64.252.65.0/24", "64.252.70.0/23", "64.252.72.0/21", "64.252.80.0/21", "64.252.88.0/23", "64.252.98.0/23", "64.252.100.0/22", "64.252.104.0/21", "64.252.112.0/23", "64.252.114.0/24", "64.252.118.0/23", "64.252.120.0/22", "64.252.124.0/24", "64.252.129.0/24", "64.252.130.0/23", "64.252.132.0/22", "64.252.136.0/21", "64.252.144.0/23", "64.252.147.0/24", "64.252.148.0/23", "64.252.151.0/24", "64.252.152.0/24", "64.252.154.0/23", "64.252.156.0/24", "64.252.159.0/24", "64.252.161.0/24", "64.252.162.0/23", "64.252.164.0/24", "64.252.166.0/23", "64.252.168.0/22", "64.252.172.0/23", "64.252.175.0/24", "64.252.176.0/22", "64.252.180.0/24", "64.252.182.0/23", "64.252.185.0/24", "64.252.186.0/23", "64.252.188.0/23", "64.252.190.0/24", "65.0.0.0/14", "65.8.0.0/23", "65.8.2.0/24", "65.8.4.0/22", "65.8.8.0/23", "65.8.11.0/24", "65.8.12.0/24", "65.8.14.0/23", "65.8.16.0/20", "65.8.32.0/19", "65.8.64.0/20", "65.8.80.0/21", "65.8.88.0/22", "65.8.92.0/23", "65.8.94.0/24", "65.8.96.0/20", "65.8.112.0/21", "65.8.120.0/22", "65.8.124.0/23", "65.8.129.0/24", "65.8.130.0/23", "65.8.132.0/22", "65.8.136.0/22", "65.8.140.0/23", "65.8.142.0/24", "65.8.146.0/23", "65.8.148.0/23", "65.8.150.0/24", "65.8.152.0/23", "65.8.154.0/24", "65.8.158.0/23", "65.8.160.0/19", "65.8.192.0/18", "65.9.4.0/24", "65.9.6.0/23", "65.9.9.0/24", "65.9.11.0/24", "65.9.14.0/23", "65.9.17.0/24", "65.9.19.0/24", "65.9.20.0/22", "65.9.24.0/21", "65.9.32.0/19", "65.9.64.0/19", "65.9.96.0/20", "65.9.112.0/23", "65.9.129.0/24", "65.9.130.0/23", "65.9.132.0/22", "65.9.136.0/21", "65.9.144.0/20", "65.9.160.0/19", "65.20.48.0/24", "65.37.240.0/24", "65.110.52.0/23", "65.110.54.0/24", "66.22.176.0/24", "66.22.190.0/24", "66.37.128.0/24", "66.51.208.0/24", "66.51.210.0/23", "66.51.212.0/22", "66.51.216.0/23", "66.54.74.0/23", "66.81.8.0/24", "66.81.227.0/24", "66.81.241.0/24", "66.117.20.0/24", "66.117.22.0/23", "66.117.24.0/23", "66.117.26.0/24", "66.117.30.0/23", "66.129.247.0/24", "66.129.248.0/24", "66.159.226.0/24", "66.159.230.0/24", "66.178.130.0/24", "66.178.132.0/23", "66.178.134.0/24", "66.178.136.0/23", "66.178.139.0/24", "66.182.132.0/23", "66.187.204.0/23", "66.206.173.0/24", "66.232.20.0/23", "66.235.151.0/24", "66.235.152.0/22", "67.20.60.0/24", "67.199.239.0/24", "67.219.241.0/24", "67.219.247.0/24", "67.219.250.0/24", "67.220.224.0/19", "67.221.38.0/24", "67.222.249.0/24", "67.222.254.0/24", "67.226.222.0/23", "68.64.5.0/24", "68.66.112.0/20", "68.70.127.0/24", "69.10.24.0/24", "69.58.24.0/24", "69.59.247.0/24", "69.59.248.0/24", "69.59.250.0/23", "69.64.150.0/24", "69.64.152.0/24", "69.72.44.0/22", "69.80.226.0/23", "69.94.8.0/23", "69.166.42.0/24", "69.169.224.0/20", "70.132.0.0/20", "70.132.16.0/22", "70.132.20.0/23", "70.132.23.0/24", "70.132.24.0/23", "70.132.27.0/24", "70.132.28.0/22", "70.132.32.0/21", "70.132.40.0/24", "70.132.42.0/23", "70.132.44.0/24", "70.132.46.0/24", "70.132.48.0/22", "70.132.52.0/23", "70.132.55.0/24", "70.132.58.0/23", "70.132.60.0/22", "70.224.192.0/18", "70.232.64.0/20", "70.232.80.0/21", "70.232.88.0/22", "70.232.96.0/20", "70.232.112.0/21", "70.232.120.0/22", "71.141.0.0/21", "71.152.0.0/22", "71.152.4.0/23", "71.152.7.0/24", "71.152.8.0/24", "71.152.10.0/23", "71.152.13.0/24", "71.152.14.0/23", "71.152.16.0/21", "71.152.24.0/22", "71.152.28.0/24", "71.152.30.0/23", "71.152.33.0/24", "71.152.35.0/24", "71.152.36.0/22", "71.152.40.0/23", "71.152.43.0/24", "71.152.46.0/23", "71.152.48.0/22", "71.152.53.0/24", "71.152.55.0/24", "71.152.56.0/22", "71.152.61.0/24", "71.152.62.0/23", "71.152.64.0/21", "71.152.72.0/22", "71.152.76.0/23", "71.152.79.0/24", "71.152.80.0/21", "71.152.88.0/22", "71.152.92.0/24", "71.152.94.0/23", "71.152.96.0/22", "71.152.100.0/24", "71.152.102.0/23", "71.152.105.0/24", "71.152.106.0/23", "71.152.108.0/23", "71.152.110.0/24", "71.152.112.0/21", "71.152.122.0/23", "71.152.124.0/24", "71.152.126.0/23", "72.1.32.0/21", "72.13.121.0/24", "72.13.124.0/24", "72.18.76.0/23", "72.18.222.0/24", "72.21.192.0/19", "72.41.0.0/20", "72.46.77.0/24", "72.167.168.0/24", "74.80.247.0/24", "74.116.145.0/24", "74.116.147.0/24", "74.117.148.0/24", "74.118.105.0/24", "74.118.106.0/23", "74.200.120.0/24", "74.221.129.0/24", "74.221.130.0/24", "74.221.133.0/24", "74.221.135.0/24", "74.221.137.0/24", "74.221.139.0/24", "74.221.141.0/24", "75.2.0.0/17", "75.104.19.0/24", "76.76.17.0/24", "76.76.19.0/24", "76.76.21.0/24", "76.223.0.0/17", "76.223.128.0/22", "76.223.132.0/23", "76.223.160.0/22", "76.223.164.0/23", "76.223.166.0/24", "76.223.172.0/22", "76.223.176.0/21", "76.223.184.0/22", "76.223.188.0/23", "76.223.190.0/24", "77.73.208.0/23", "78.108.124.0/23", "79.125.0.0/17", "79.143.156.0/24", "80.210.95.0/24", "81.20.41.0/24", "81.90.143.0/24", 
                "82.145.126.0/24", "82.192.96.0/23", "82.192.100.0/23", "82.192.108.0/23", "83.97.100.0/22", "83.137.245.0/24", "83.147.240.0/22", "83.151.192.0/23", "83.151.194.0/24", "84.254.134.0/24", "85.92.101.0/24", 
                "85.113.84.0/24", "85.113.88.0/24", "85.158.142.0/24", "85.194.254.0/23", "85.236.136.0/21", "87.236.67.0/24", "87.238.80.0/21", "87.238.140.0/24", "88.202.208.0/23", "88.202.210.0/24", "88.212.156.0/22", "89.37.140.0/24", "89.116.141.0/24", "89.116.244.0/24", "89.117.129.0/24", "89.251.12.0/24", "91.102.186.0/24", "91.193.42.0/24", "91.194.25.0/24", "91.194.104.0/24", "91.198.107.0/24", "91.198.117.0/24", "91.207.12.0/23", "91.208.21.0/24", "91.209.81.0/24", "91.213.115.0/24", "91.213.126.0/24", "91.213.146.0/24", "91.218.37.0/24", "91.223.161.0/24", "91.227.75.0/24", "91.228.72.0/24", "91.228.74.0/24", "91.230.237.0/24", "91.231.35.0/24", "91.233.61.0/24", "91.233.120.0/24", "91.236.18.0/24", "91.236.66.0/24", "91.237.174.0/24", "91.240.18.0/23", "91.241.6.0/23", "93.93.224.0/22", "93.94.3.0/24", "93.191.148.0/23", "93.191.219.0/24", "94.124.112.0/24", "94.140.18.0/24", "94.142.252.0/24", "95.82.16.0/20", "95.130.184.0/23", "96.0.0.0/18", "96.0.64.0/21", "96.0.84.0/22", "96.0.88.0/22", "96.0.92.0/23", "96.0.96.0/22", "96.0.100.0/23", "96.0.104.0/22", "96.9.221.0/24", "98.97.248.0/22", "98.97.253.0/24", "98.97.254.0/23", "98.142.155.0/24", "99.77.0.0/18", "99.77.130.0/23", "99.77.132.0/22", "99.77.136.0/21", "99.77.144.0/23", "99.77.147.0/24", "99.77.148.0/23", "99.77.150.0/24", "99.77.152.0/21", "99.77.160.0/23", "99.77.183.0/24", "99.77.186.0/24", "99.77.188.0/23", "99.77.190.0/24", "99.77.233.0/24", "99.77.234.0/23", "99.77.238.0/23", "99.77.240.0/24", "99.77.242.0/24", "99.77.244.0/22", "99.77.248.0/22", "99.77.252.0/23", "99.78.128.0/19", "99.78.160.0/21", "99.78.168.0/22", "99.78.172.0/24", "99.78.176.0/21", "99.78.192.0/18", "99.79.0.0/16", "99.80.0.0/15", "99.82.128.0/19", "99.82.160.0/20", "99.82.184.0/21", 
                "99.83.72.0/21", "99.83.80.0/21", "99.83.96.0/22", "99.83.100.0/23", "99.83.102.0/24", "99.83.120.0/22", "99.83.128.0/17", "99.84.0.0/19", "99.84.32.0/20", "99.84.48.0/24", "99.84.50.0/23", "99.84.52.0/22", "99.84.56.0/21", "99.84.64.0/18", "99.84.128.0/24", "99.84.130.0/23", "99.84.132.0/22", "99.84.136.0/21", "99.84.144.0/20", "99.84.160.0/19", "99.84.192.0/18", "99.86.0.0/17", "99.86.128.0/21", "99.86.136.0/24", "99.86.144.0/21", "99.86.153.0/24", "99.86.154.0/23", "99.86.156.0/22", "99.86.160.0/20", "99.86.176.0/21", "99.86.185.0/24", "99.86.186.0/23", "99.86.188.0/22", "99.86.192.0/21", "99.86.201.0/24", "99.86.202.0/23", "99.86.204.0/22", "99.86.217.0/24", "99.86.218.0/23", "99.86.220.0/22", "99.86.224.0/20", "99.86.240.0/21", "99.86.249.0/24", "99.86.250.0/23", "99.86.252.0/22", "99.87.0.0/19", "99.87.32.0/22", "99.150.0.0/21", "99.150.16.0/20", "99.150.32.0/19", "99.150.64.0/18", "99.151.64.0/18", "99.151.128.0/19", "99.151.186.0/23", "100.20.0.0/14", "103.4.8.0/21", "103.8.172.0/22", "103.10.127.0/24", "103.16.56.0/24", "103.16.59.0/24", "103.16.101.0/24", "103.19.244.0/22", "103.23.68.0/23", "103.39.40.0/24", "103.43.38.0/23", "103.53.55.0/24", "103.58.192.0/24", "103.70.20.0/22", "103.70.49.0/24", "103.80.6.0/24", "103.85.213.0/24", "103.104.86.0/24", "103.107.56.0/24", "103.119.213.0/24", "103.123.219.0/24", "103.124.134.0/23", "103.127.75.0/24", "103.136.10.0/24", "103.143.45.0/24", "103.145.182.0/24", "103.145.192.0/24", "103.147.71.0/24", "103.149.112.0/24", "103.150.47.0/24", "103.150.161.0/24", "103.151.39.0/24", "103.151.192.0/23", "103.152.248.0/24", "103.161.77.0/24", "103.165.160.0/24", "103.166.180.0/24", "103.167.153.0/24", "103.168.156.0/23", "103.168.209.0/24", "103.175.120.0/23", "103.179.36.0/23", "103.180.30.0/24", "103.181.194.0/24", "103.181.240.0/24", "103.182.250.0/23", "103.187.14.0/24", "103.188.89.0/24", "103.190.166.0/24", "103.193.9.0/24", "103.195.60.0/22", "103.196.32.0/24", "103.211.172.0/24", "103.229.8.0/23", "103.229.10.0/24", "103.235.88.0/24", "103.238.120.0/24", "103.246.148.0/22", "103.246.251.0/24", "104.36.33.0/24", "104.153.112.0/23", "104.171.198.0/23", "104.192.136.0/23", "104.192.138.0/24", "104.192.140.0/23", "104.192.143.0/24", "104.193.186.0/24", "104.193.205.0/24", "104.193.207.0/24", "104.207.162.0/24", "104.207.170.0/23", "104.207.172.0/23", "104.207.174.0/24", "104.218.202.0/24", "104.232.45.0/24", "104.234.23.0/24", "104.238.244.0/23", "104.238.247.0/24", "104.249.160.0/23", "104.249.162.0/24", "104.253.192.0/24", "104.255.56.0/22", "104.255.60.0/24", "107.162.252.0/24", "108.128.0.0/13", "108.136.0.0/15", "108.138.0.0/16", "108.139.0.0/19", "108.139.32.0/20", "108.139.48.0/21", "108.139.56.0/24", "108.139.72.0/21", "108.139.80.0/22", "108.139.84.0/23", "108.139.86.0/24", "108.139.102.0/23", "108.139.104.0/21", "108.139.112.0/20", "108.139.128.0/20", "108.139.144.0/23", "108.139.146.0/24", "108.139.162.0/23", "108.139.164.0/22", "108.139.168.0/21", "108.139.176.0/20", "108.139.207.0/24", "108.139.208.0/20", "108.139.224.0/19", "108.156.0.0/17", "108.156.128.0/23", "108.156.130.0/24", "108.156.146.0/23", "108.156.148.0/22", "108.156.152.0/21", "108.156.160.0/19", "108.156.192.0/18", "108.157.0.0/21", "108.157.8.0/23", "108.157.85.0/24", "108.157.86.0/23", "108.157.88.0/21", "108.157.96.0/20", "108.157.112.0/23", "108.157.114.0/24", "108.157.130.0/23", "108.157.132.0/22", "108.157.136.0/21", "108.157.144.0/20", "108.157.160.0/21", "108.157.168.0/22", "108.157.172.0/23", "108.157.174.0/24", "108.157.205.0/24", "108.157.206.0/23", "108.157.208.0/20", "108.157.224.0/21", "108.157.232.0/23", "108.157.234.0/24", "108.158.39.0/24", "108.158.40.0/21", "108.158.48.0/20", "108.158.64.0/22", "108.158.68.0/24", "108.158.114.0/23", "108.158.116.0/22", "108.158.120.0/21", "108.158.128.0/20", "108.158.144.0/21", "108.158.152.0/22", "108.158.156.0/23", "108.158.158.0/24", "108.158.219.0/24", "108.158.220.0/22", "108.158.224.0/19", "108.159.0.0/18", "108.159.64.0/19", "108.159.96.0/23", "108.159.128.0/21", "108.159.136.0/22", "108.159.144.0/23", "108.159.155.0/24", "108.159.156.0/24", "108.159.160.0/23", "108.159.163.0/24", "108.159.164.0/24", "108.159.166.0/23", "108.159.168.0/21", "108.159.181.0/24", "108.159.182.0/23", "108.159.184.0/24", "108.159.188.0/22", "108.159.192.0/24", "108.159.197.0/24", "108.159.198.0/23", "108.159.200.0/21", "108.159.208.0/24", "108.159.213.0/24", "108.159.214.0/23", "108.159.216.0/21", "108.159.224.0/21", "108.159.247.0/24", "108.159.248.0/23", "108.159.250.0/24", "108.159.255.0/24", "108.175.52.0/23", "108.175.54.0/24", "109.68.71.0/24", "109.95.191.0/24", "109.224.233.0/24", "109.232.88.0/21", "116.214.100.0/23", "116.214.120.0/23", "122.248.192.0/18", "122.252.145.0/24", "122.252.146.0/23", "122.252.148.0/22", "129.33.138.0/23", "129.33.243.0/24", "129.41.76.0/23", "129.41.88.0/23", "129.41.167.0/24", "129.41.174.0/23", "129.41.222.0/24", "130.50.35.0/24", "130.137.20.0/24", "130.137.78.0/24", "130.137.81.0/24", "130.137.86.0/24", "130.137.99.0/24", "130.137.112.0/24", "130.137.124.0/24", "130.137.136.0/24", "130.137.150.0/24", "130.137.178.0/24", "130.137.215.0/24", "130.176.0.0/21", "130.176.9.0/24", "130.176.10.0/23", "130.176.13.0/24", "130.176.14.0/24", "130.176.16.0/23", "130.176.24.0/23", "130.176.27.0/24", "130.176.28.0/22", "130.176.32.0/21", "130.176.40.0/24", "130.176.43.0/24", "130.176.45.0/24", "130.176.48.0/24", "130.176.50.0/24", "130.176.53.0/24", "130.176.54.0/24", "130.176.56.0/24", "130.176.65.0/24", "130.176.66.0/23", "130.176.68.0/24", "130.176.71.0/24", "130.176.75.0/24", "130.176.76.0/22", "130.176.80.0/21", "130.176.88.0/22", "130.176.92.0/23", "130.176.96.0/22", "130.176.100.0/24", "130.176.102.0/23", "130.176.104.0/22", "130.176.108.0/23", "130.176.111.0/24", "130.176.112.0/23", "130.176.116.0/24", "130.176.118.0/23", "130.176.120.0/24", "130.176.125.0/24", 
                "130.176.126.0/23", "130.176.129.0/24", "130.176.130.0/23", "130.176.132.0/22", "130.176.136.0/23", "130.176.139.0/24", "130.176.140.0/22", "130.176.144.0/23", "130.176.146.0/24", "130.176.148.0/22", "130.176.152.0/24", "130.176.155.0/24", "130.176.156.0/22", "130.176.160.0/21", "130.176.168.0/24", "130.176.170.0/23", "130.176.172.0/24", "130.176.174.0/23", "130.176.179.0/24", "130.176.182.0/23", "130.176.184.0/21", "130.176.192.0/24", "130.176.194.0/23", "130.176.196.0/22", "130.176.200.0/21", "130.176.208.0/21", "130.176.217.0/24", "130.176.218.0/23", 
                "130.176.220.0/22", "130.176.224.0/24", "130.176.226.0/23", "130.176.231.0/24", "130.176.232.0/24", "130.176.254.0/23", "130.193.2.0/24", "131.232.37.0/24", "131.232.76.0/23", "131.232.78.0/24", "132.75.97.0/24", "134.224.0.0/17", "134.224.128.0/18", "134.224.192.0/19", "134.224.224.0/20", "134.224.242.0/23", "134.224.244.0/22", "134.224.248.0/22", "135.84.124.0/24", "136.18.18.0/23", "136.18.20.0/22", "136.175.24.0/23", "136.175.106.0/23", "136.175.113.0/24", "136.184.226.0/23", "136.184.229.0/24", "136.184.230.0/23", "136.184.232.0/23", "136.184.235.0/24", "136.226.219.0/24", "136.226.220.0/23", "137.83.193.0/24", "137.83.195.0/24", 
                "137.83.196.0/22", "137.83.202.0/23", "137.83.204.0/23", "137.83.208.0/22", "137.83.212.0/24", "137.83.214.0/24", "137.83.252.0/22", "138.43.114.0/24", "139.60.2.0/24", "139.60.113.0/24", "139.60.114.0/24", "139.64.232.0/24", "139.138.105.0/24", "139.180.31.0/24", "139.180.242.0/23", "139.180.246.0/23", "139.180.248.0/22", "140.19.64.0/24", "140.99.123.0/24", "140.228.26.0/24", "141.11.12.0/22", "141.163.128.0/20", "141.193.32.0/23", "141.193.208.0/23", "142.0.189.0/24", "142.0.190.0/24", "142.4.160.0/22", "142.4.177.0/24", "142.54.40.0/24", "142.202.20.0/24", "142.202.36.0/22", "142.202.40.0/24", "142.202.42.0/23", "142.202.46.0/24", "143.55.151.0/24", "143.204.0.0/19", "143.204.32.0/21", "143.204.40.0/24", "143.204.57.0/24", "143.204.58.0/23", "143.204.60.0/22", "143.204.64.0/20", "143.204.80.0/21", "143.204.89.0/24", "143.204.90.0/23", "143.204.92.0/22", "143.204.96.0/20", "143.204.112.0/21", "143.204.121.0/24", "143.204.122.0/23", "143.204.124.0/22", "143.204.128.0/18", "143.204.192.0/19", "143.204.224.0/20", "143.204.240.0/21", "143.204.249.0/24", "143.204.250.0/23", "143.204.252.0/22", "143.244.81.0/24", "143.244.82.0/23", "143.244.84.0/22", "144.2.170.0/24" ],
            "CLOUDFLARE_IPV4_LIST_1": ["173.245.48.0/20","103.21.244.0/22", "103.22.200.0/22", "103.31.4.0/22", "141.101.64.0/18", "108.162.192.0/18", "190.93.240.0/20", "188.114.96.0/20", "197.234.240.0/22", "198.41.128.0/17", "162.158.0.0/15", "104.16.0.0/13", "104.24.0.0/14", "172.64.0.0/13", "131.0.72.0/22"],
            "IMPERVA": ["45.60.0.0/16", "45.64.64.0/22", "45.223.0.0/16", "103.28.248.0/22", "107.154.0.0/16", "149.126.72.0/21", "185.11.124.0/22", "192.230.64.0/18", "198.143.32.0/19", "99.83.128.0/21"],
            "FASTLY": ["23.235.32.0/20", "43.249.72.0/22", "103.244.50.0/24", "103.245.222.0/23", "103.245.224.0/24", "104.156.80.0/20", "140.248.64.0/18", "140.248.128.0/17", "146.75.0.0/17", "151.101.0.0/16", "157.52.64.0/18", "167.82.0.0/17", "167.82.128.0/20", "167.82.160.0/20", "167.82.224.0/20", "172.111.64.0/18", "185.31.16.0/22", "199.27.72.0/21", "199.232.0.0/16"],
            "FACEBOOK": ["31.13.24.0/21", "31.13.64.0/19", "31.13.64.0/24", "31.13.69.0/24", "31.13.70.0/24", "31.13.71.0/24", "31.13.72.0/24", "31.13.73.0/24", "31.13.75.0/24", "31.13.76.0/24", "31.13.77.0/24", "31.13.78.0/24", "31.13.79.0/24", "31.13.80.0/24", "66.220.144.0/20", "66.220.144.0/21", "66.220.149.11/16", "66.220.152.0/21", "66.220.158.11/16", "66.220.159.0/24", "69.63.176.0/21", "69.63.176.0/24", "69.63.184.0/21", "69.171.224.0/19", "69.171.224.0/20", "69.171.224.37/16", "69.171.229.11/16", "69.171.239.0/24", "69.171.240.0/20", "69.171.242.11/16", "69.171.255.0/24", "74.119.76.0/22", "173.252.64.0/19", "173.252.70.0/24", "173.252.96.0/19", "204.15.20.0/22",
                    ],
        
    }

    def scan_server(host, port, user_agent, save_file):
        sock = socket.socket()
        sock.settimeout(5)
        success = False

        try:
            sock.connect((str(host), port))
            success = True
            payload = 'GET / HTTP/1.1\r\nHost: {}\r\nUser-Agent: {}\r\n\r\n'.format(host, user_agent)
            sock.send(payload.encode())
            response = sock.recv(1024).decode('utf-8', 'ignore')

            for data in response.split('\r\n'):
                data = data.split(':')


                if data[0] == 'Server':
                    result = f'Server: {host} port:{port} [{data[1].strip()}]'
                    print(f"{colorama.Fore.GREEN}{result}{colorama.Fore.RESET}")
                    with open(save_file, 'a+') as file:
                        file.write(result + '\n')

        except socket.timeout:
            print(f"{host} timed out ")
        except Exception as e:
            print(f"{host} caused an error: {str(e)}")
        finally:
            sock.close()
            time.sleep(1)

    def cidrs():
        cidrs_list = []
        while True:
            cidr = input("Enter a CIDR range (e.g. 192.168.1.0/24): ")
            cidrs_list.append(cidr)
            more = input("Enter another CIDR range? (y/n) ")
            if more.lower() == 'n':
                break
        return cidrs_list

    def cidrs_file():
        file_path = input("Enter the path to the text file containing IPs or CIDR ranges: ")
        try:
            with open(file_path, 'r') as file:
                cidrs_list = [line.strip() for line in file.readlines()]
            return cidrs_list
        except FileNotFoundError:
            print("File not found.")
            return []

    def b():
        R = colorama.Fore.RED
        Blu = colorama.Fore.BLUE
        for k, v in ipranges.items():
            print('{', k, ' : ', v, '}', end='\n')
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Select an option:")
        print("1. Enter CIDR range manually")
        print("2. Input CIDR ranges from a text file")
        print("3. CLOUDFRONT EDGE IP")
        print("4. CLOUDFRONT 1")
        print("5. CLOUDFRONT 2")
        print("6. CLOUDFRONT 3")
        print("7. CLOUDFRONT 4")
        print("8. CLOUDFLARE ipv4 list")
        print("9. IMPERVA")
        print("10. FASTLY")
        print("11. FACEBOOK")

        option = int(input("Enter your choice: "))
        cidrs_list = []

        if option == 1:
            cidrs_list = cidrs()
        elif option == 2:
            cidrs_list = cidrs_file()
        elif option == 3:
            cidrs_list = ipranges["CLOUDFRONT_GLOBAL_IP_LIST"]
        elif option == 4:
            cidrs_list = ipranges["CLOUDFRONT_REGIONAL_EDGE_IP_LIST_1"]
        elif option == 5:
            cidrs_list = ipranges["CLOUDFRONT_REGIONAL_EDGE_IP_LIST_2"]
        elif option == 6:
            cidrs_list = ipranges["CLOUDFRONT_REGIONAL_EDGE_IP_LIST_3"]
        elif option == 7:
            cidrs_list = ipranges["CLOUDFRONT_REGIONAL_EDGE_IP_LIST_4"]
        elif option == 8:
            cidrs_list = ipranges["CLOUDFLARE_IPV4_LIST_1"]
        elif option == 9:
            cidrs_list = ipranges["IMPERVA"]
        elif option == 10:
            cidrs_list = ipranges["FASTLY"]
        elif option == 11:
            cidrs_list = ipranges["FACEBOOK"]
        else:
            print("Invalid option.")
            return

        save_filename = input("Enter the output file name: ")
        workers = 255

        with open(save_filename, 'a+') as file:
            with ThreadPoolExecutor(max_workers=workers) as executor:
                for cidr in cidrs_list:
                    iprange = [ip for ip in ipcalc.Network(cidr)]
                    for index, ip in enumerate(iprange):
                        executor.submit(process_ip, R, Blu, ip, save_filename)

    def process_ip(R, Blu, ip, save_filename):
        try:
            print("{}[INFO] Probing... [{}]{}".format(R, ip, Blu))
            user_agent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.888']
            scan_server(ip, 80, user_agent, save_filename)
            scan_server(ip, 443, user_agent, save_filename)
        except KeyboardInterrupt:
            print(f"{R}[ERROR] CTRL+C Received, Quitting.")
            quit()
        except Exception as e:
            print(f"{R}[ERROR] Exception: {e}")

    if __name__ == '__main__':
        try:
            b()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()

def script4():
    print("\033[33m" + """ 
    ██╗  ██╗ ██████╗ ███████╗████████╗                      
    ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝                      
    ███████║██║   ██║███████╗   ██║                         
    ██╔══██║██║   ██║╚════██║   ██║                         
    ██║  ██║╚██████╔╝███████║   ██║                         
    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝                                                                                          
       ██████╗██╗  ██╗███████╗ ██████╗██╗ ██╗ ███████╗██████╗ 
      ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
      ██████╗ ██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
      ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ \033[0m""")
    class bcolors:
                OKPURPLE = '\033[95m'
                OKCYAN = '\033[96m'
                OKPINK = '\033[94m'
                OKlime = '\033[92m'
                ORANGE = '\033[91m\033[93m'
                FAIL = '\033[91m'
                ENDC = '\033[0m'
                UNDERLINE = '\033[4m'
                Magenta = fg('#FF00FF')
                OKBLUE = '\033[94m'
                blue2 ='#c0b7dd'
                brown = '#783f04'
                peach = '#ea9999'

    def check_status(url, filename=None):
            
            try:
                if not url.startswith('https://') and not url.startswith('https://'):
                    url = 'http://' + url

                    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',}

                r_http = requests.head(url, headers=headers, timeout=1)
                status_http = r_http.status_code
                server_http = r_http.headers.get('server', 'server information not found')
                connection_http = r_http.headers.get('connection', '')

                url_https = url.replace('http://', 'https://')
                r_https = requests.head(url_https, headers=headers, timeout=2)
                status_https = r_https.status_code
                server_https = r_https.headers.get('server', 'server information not found')
                connection_https = r_https.headers.get('connection', '').lower()

                # Print status for HTTP
                if status_http == 200:
                    if connection_http and 'keep-alive' in connection_http.lower():
                        print(f'{bcolors.OKlime} [OK] 200: port 80: {bcolors.OKCYAN} Keep-Alive: active{bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [OK] 200: port 80: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_http == 301:
                    if connection_http and 'keep-alive' in connection_http.lower():
                        print(f'{bcolors.OKlime} [Moved Permanently] 301: port 80: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Moved Permanently] 301: port 80: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_http == 302:
                    if connection_http and 'keep-alive' in connection_http.lower():
                        print(f'{bcolors.OKlime} [Temporary redirect] 302: port 80 {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Temporary redirect] 302: port 80 {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_http == 409:
                    if connection_http and 'keep-alive' in connection_http.lower():
                        print(f'{bcolors.OKlime} [Conflict] 409: port 80: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Conflict] 409: port 80: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_http == 403:
                    if connection_http and 'keep-alive' in connection_http.lower():
                        print(f'{bcolors.OKlime} [Forbidden] 403: port 80: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Forbidden] 403: port 80: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_http == 404:
                    if connection_http and 'keep-alive' in connection_http.lower():
                        print(f'{bcolors.OKlime} [Not Found] 404: port 80: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Not Found] 404: port 80: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_http == 407:
                    if connection_http and 'keep-alive' in connection_http.lower():
                        print(f'{bcolors.OKlime} [Internal Server Error] 500: port 80: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Internal Server Error] 500: port 80: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_http == 206:
                    if connection_http and 'keep-alive' in connection_http.lower():
                        print(f'{bcolors.OKlime} [Partial Content] 206: port 80: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Partial Content] 206: port 80: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_http == 400:
                    if connection_http and 'keep-alive' in connection_http.lower():
                        print(f'{bcolors.OKlime} [Bad Request] 400: port 80: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Bad Request] 400: port 80: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')

                # Print status for HTTPS
                if status_https == 200:
                    if connection_https and 'keep-alive' in connection_https.lower():
                        print(f'{bcolors.OKlime} [OK] 200: port 443: {bcolors.OKCYAN} Keep-Alive: active{bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [OK] 200: port 443: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_https == 301:
                    if connection_https and 'keep-alive' in connection_https.lower():
                        print(f'{bcolors.OKlime} [Moved Permanently] 301: port 443: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Moved Permanently] 301: port 443: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_https == 302:
                    if connection_https and 'keep-alive' in connection_https.lower():
                        print(f'{bcolors.OKlime} [Temporary redirect] 302: port 443: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Temporary redirect] 302: port 443: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_https == 409:
                    if connection_https and 'keep-alive' in connection_https.lower():
                        print(f'{bcolors.OKlime} [Conflict] 409: port 443: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Conflict] 409: port 443: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_https == 403:
                    if connection_https and 'keep-alive' in connection_https.lower():
                        print(f'{bcolors.OKlime} [Forbidden] 403: port 443: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Forbidden] 403: port 443: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_https == 404:
                    if connection_https and 'keep-alive' in connection_https.lower():
                        print(f'{bcolors.OKlime} [Not Found] 404: port 443: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Not Found] 404: port 443: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_https == 407:
                    if connection_https and 'keep-alive' in connection_https.lower():
                        print(f'{bcolors.OKlime} [Internal Server Error] 500: port 443: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Internal Server Error] 500: port 443: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_https == 206:
                    if connection_https and 'keep-alive' in connection_https.lower():
                        print(f'{bcolors.OKlime} [Partial Content] 206: port 443: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Partial Content] 206: port 443: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')
                elif status_https == 400:
                    if connection_https and 'keep-alive' in connection_https.lower():
                        print(f'{bcolors.OKlime} [Bad Request] 400: port 443: {bcolors.OKCYAN} Keep-Alive: active {bcolors.ENDC}')
                    else:
                        print(f'{bcolors.OKlime} [Bad Request] 400: port 443: {bcolors.FAIL} Keep-Alive: inactive{bcolors.ENDC}')

                # Add color coding based on server information
                if 'cloudflare' in server_http.lower() or 'cloudflare' in server_https.lower() and connection_https.lower() or connection_http.lower():
                    print(f'{bcolors.ORANGE} {url} {server_http if "cloudflare" in server_http.lower() else server_https}{bcolors.ENDC} {bcolors.UNDERLINE}check host {status_http} status found : {connection_http}\x1b[0m{bcolors.ENDC}')
                    print(f'{bcolors.ORANGE} {url_https} {server_https if "cloudflare" in server_https.lower() else server_http}{bcolors.ENDC} {bcolors.UNDERLINE}check host {status_https} status found : {connection_https}\x1b[0m{bcolors.ENDC}')
                elif 'cloudfront' in server_http.lower() or 'cloudfront' in server_https.lower():
                    print(f'{bcolors.blue2} {url} {server_http if "cloudfront" in server_http.lower() else server_https} {bcolors.UNDERLINE}check host {status_http} status found : {connection_http}\x1b[0m{bcolors.ENDC}')
                    print(f'{bcolors.blue2} {url_https} {server_https if "cloudfront" in server_https.lower() else server_http} {bcolors.UNDERLINE}check host {status_https} status : {connection_https} found\x1b[0m{bcolors.ENDC}')
                elif 'sffe' in server_http.lower() or 'sffe' in server_https.lower() and connection_https.lower() or connection_http.lower():
                    print(f'{bcolors.ORANGE} {url} {server_http if "sffe" in server_http.lower() else server_https}{bcolors.ENDC} {bcolors.UNDERLINE}check host {status_http} status found : {connection_http}\x1b[0m{bcolors.ENDC}')
                    print(f'{bcolors.ORANGE} {url_https} {server_https if "sffe" in server_https.lower() else server_http}{bcolors.ENDC} {bcolors.UNDERLINE}check host {status_https} status found : {connection_https}\x1b[0m{bcolors.ENDC}')
                elif 'cloudfront' in server_http.lower() or 'cloudfront' in server_https.lower():
                    print(f'{bcolors.blue2} {url} {server_http if "cloudfront" in server_http.lower() else server_https}{bcolors.UNDERLINE}check host {status_http} status found : {connection_http}\x1b[0m{bcolors.ENDC}')
                    print(f'{bcolors.blue2} {url_https} {server_https if "cloudfront" in server_https.lower() else server_http} {bcolors.UNDERLINE}check host {status_https} status : {connection_https} found\x1b[0m{bcolors.ENDC}')
                elif 'akamaighost' in server_http.lower() or 'akamaighost' in server_https.lower():
                    print(f'{bcolors.OKPURPLE} {url} {server_http if "akamaighost" in server_http.lower() else server_https} {bcolors.UNDERLINE}check {status_http} status found : {connection_http}\x1b[0m{bcolors.ENDC}')
                    print(f'{bcolors.OKPURPLE} {url_https} {server_https if "akamaighost" in server_https.lower() else server_http} {bcolors.UNDERLINE}check {status_https} status found : {connection_https}\x1b[0m{bcolors.ENDC}')
                elif 'Apple' in server_http.lower() or 'Apple' in server_https.lower() and connection_https.lower() or connection_http.lower():
                    print(f'{bcolors.OKPINK} {url} {server_http if "Apple" in server_http.lower() else server_https} {bcolors.UNDERLINE}check {status_http} status found : {connection_http}\x1b[0m{bcolors.ENDC}')
                    print(f'{bcolors.OKPINK} {url_https} {server_https if "Apple" in server_https.lower() else server_http} {bcolors.UNDERLINE}check {status_https} status found : {connection_https}\x1b[0m{bcolors.ENDC}')
                elif 'microsoft-IIS/10.0' in server_http.lower() or 'microsoft-IIS/10.0' in server_https.lower() and connection_https.lower() or connection_http.lower():
                    print(f'{bcolors.OKCYAN} {url} {server_http if "microsoft-IIS/10.0" in server_http.lower() else server_https} {bcolors.UNDERLINE}check {status_http} status found : {connection_http}\x1b[0m{bcolors.ENDC}')
                    print(f'{bcolors.OKCYAN} {url_https} {server_https if "microsoft-IIS/10.0" in server_https.lower() else server_http} {bcolors.UNDERLINE}check {status_https} status found : {connection_https}\x1b[0m{bcolors.ENDC}')
                elif 'fastly' in server_http.lower() or 'fastly' in server_https.lower() and connection_https.lower() or connection_http.lower():
                    print(f'{bcolors.brown} {url} {server_http if "fastly" in server_http.lower() else server_https} {bcolors.UNDERLINE}check {status_http} status found : {connection_http}\x1b[0m{bcolors.ENDC}')
                    print(f'{bcolors.brown} {url_https} {server_https if "fastly" in server_https.lower() else server_http} {bcolors.UNDERLINE}check {status_https} status found : {connection_https}\x1b[0m{bcolors.ENDC}')
                elif 'varnish' in server_http.lower() or 'varnish' in server_https.lower() and connection_https.lower() or connection_http.lower():
                    print(f'{bcolors.peach} {url} {server_http if "varnish" in server_http.lower() else server_https} {bcolors.UNDERLINE}check {status_http} status found : {connection_http}\x1b[0m{bcolors.ENDC}')
                    print(f'{bcolors.peach} {url_https} {server_https if "varnish" in server_https.lower() else server_http} {bcolors.UNDERLINE}check {status_https} status found : {connection_https}\x1b[0m{bcolors.ENDC}')

                if server_http == 'server information not found' and server_https == 'server information not found':
                    domains_not_found.append(url)

                if filename:
                    with open(filename, 'a') as f:
                        f.write(f'{url} : HTTP({status_http}), : {server_http}, :{connection_http}\n')
                        f.write(f'{url_https} : HTTPS({status_https}) : {server_https}, : {connection_https}\n')

            except requests.ConnectionError as e:
                print(f'{bcolors.FAIL}{url} failed to connect \x1b[0m{bcolors.ENDC}')
            except requests.Timeout as e:
                print(f'{url} timeout error')
            except requests.RequestException as e:
                print(f'{url} general error')

    while True:
        file_name = input("Enter the name of the file to scan: ")
        try:
            with open(file_name) as f:
                lines = f.readlines()
            break
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")

    while True:
        save_output = input("Save output to file? (y/n) ")
        if save_output.lower() == 'y':
            filename = input("Enter the name of the output file: ")
            break
        elif save_output.lower() == 'n':
            filename = None
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    while True:
        try:
            num_threads = int(input("Enter the number of threads (1-200): "))
            if num_threads < 1 or num_threads > 200:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 200.")

    threads = []
    domains_not_found = []  # List to store domains with missing server information

    for line in tqdm(lines):
        url = line.strip()
        t = threading.Thread(target=check_status, args=(url, filename))
        threads.append(t)
        t.start()
        # Limit the number of threads to the number specified by the user
        while threading.active_count() > num_threads:
            pass

    for t in threads:
        t.join()

    if filename:
        print(f'\nOutput saved in {filename}')

    # Save domains with missing server information to a separate file
    if domains_not_found:
        not_found_filename = input("Enter the name of the file to save domains with missing server information: ")

        # Check if the file name is provided
        if not not_found_filename:
            slowprint("File name not provided. Exiting...")
        else:
            try:
                with open(not_found_filename, 'w') as not_found_file:
                    for domain in domains_not_found:
                        not_found_file.write(domain + '\n')
                print(f'Domains with missing server information saved in {not_found_filename}')
            except FileNotFoundError:
                print(f"Error: The specified directory for '{not_found_filename}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
    else:
        print('No domains with missing server information found.')

    import time
    import os

    time.sleep(1)

    print("""
    ===================================
                Menu                
    ===================================
    1. Return to main menu
    2. View output file
    """)

    while True:
        choice = input("Enter your choice (1): ")
        if choice == '1':
            print("Returning to BUGHUNTERS PRO...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()
            return
        elif choice == '2':
            if filename and os.path.exists(filename):
                with open(filename, 'r') as f:
                    print(f.read())
                time.sleep(2)
                print("Returning to BUGHUNTERS PRO...")
            else:
                print("Output file not found or not saved.")
            break
        sys.exit
        
def script5():
    print ("""
    ███████╗██████╗ 
    ██╔════╝██╔══██╗
    █████╗  ██████╔╝
    ██╔══╝  ██╔═══╝ 
    ██║     ██║     
    ╚═╝     ╚═╝     
    """)
    print("""
        ===================================
        File Processing Script   
        ===================================
        """)
    import ipaddress
    import os
    import time
    from tqdm import tqdm

    def calculate_cidr_blocks(ip_ranges):
        cidr_blocks = []
        for start, end in ip_ranges:
            start_ip = ipaddress.ip_address(start)
            end_ip = ipaddress.ip_address(end)
            cidr = ipaddress.summarize_address_range(start_ip, end_ip)
            cidr_blocks.extend(cidr)
        return cidr_blocks

    def extract_ip_ranges(file_path):
        ip_ranges = []
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    start = parts[0]
                    end = parts[1]
                    ip_ranges.append((start, end))
        return ip_ranges

    def save_cidr_blocks(output_file, cidr_blocks):
        with open(output_file, 'w') as file:
            for block in cidr_blocks:
                file.write(str(block) + '\n')

    def remove_duplicates(filename, new_filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        lines = list(set(lines))
        try:
            with open(new_filename, 'w') as f:
                start_time = time.time()
                pbar = tqdm(total=len(lines))
                for line in lines:
                    f.write(line)
                    pbar.update(1)
                    # Calculate and display CPM
                    elapsed_time = time.time() - start_time
                    cpm = pbar.n / elapsed_time * 60 if elapsed_time > 0 else 0 
                    print(f"\rCPM: {cpm:.2f}", end='')
                pbar.close()
                print("\nFile saved successfully!")
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected, exiting without saving...")

    def split_file(filename):
        chunk_size = 1024 * 1024  # 1 MB chunk size
        with open(filename, 'r') as file:
            num_lines = sum(1 for _ in file)
            file.seek(0)  # Reset file pointer
            print(f"The file '{filename}' has {num_lines} lines.")
            while True:
                try:
                    parts = int(input("How many parts do you want to split the file into? "))
                    if parts <= 0:
                        raise ValueError("Number of parts must be a positive integer.")
                    break
                except ValueError as e:
                    print("Error:", e)
            lines_per_part = num_lines // parts
            remainder = num_lines % parts
            start = 0
            for i in range(parts):
                end = start + lines_per_part
                if remainder > 0:
                    end += 1
                    remainder -= 1
                part_filename = f"{os.path.splitext(filename)[0]}_{i+1}.txt"
                with open(part_filename, 'w') as part_file:
                    file.seek(start)  # Move file pointer to start position
                    written_lines = 0
                    while written_lines < end - start:
                        chunk = file.readlines(chunk_size)
                        if not chunk:
                            break
                        part_file.writelines(chunk)
                        written_lines += len(chunk)
                    print(f"Wrote {written_lines} lines to {part_filename}")
                start = end

    def extract_domains(input_file, output_file):
        try:
            # Open input file for reading
            with open(input_file, 'r') as f:
                data = f.read()

            # Open output file for writing
            with open(output_file, 'w') as f_out:
                # Split lines and extract domain part
                for line in data.split('\n'):
                    parts = line.split(',')
                    if len(parts) == 2:
                        domain = re.sub(r'^\d+', '', parts[1])  # Strip away numbers at the start
                        f_out.write(domain + '\n')

            print("Processing complete. Data saved to", output_file)

        except FileNotFoundError:
            print("File not found. Please make sure the input file exists in the current directory.")
        except Exception as e:
            print("An error occurred:", e)
                            
    def separate_domains_ips(input_file):
        domains = []
        ips = []
        with open(input_file, 'r') as file:
            for line in file:
                # Use regular expressions to identify IPs and domains in each line
                ip_matches = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
                domain_matches = re.findall(r'(?:(?:http|https)://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,63})', line)
                
                # Add IPs and domains to their respective lists
                ips.extend(ip_matches)
                domains.extend(domain_matches)
            
        return domains, ips

    def save_to_file(domains, ips, input_filename):
        # Remove the existing extension (if any)
        base_filename, _ = os.path.splitext(input_filename)
        
        # Generate output filenames for domains and IPs
        domain_output_file = base_filename + ".domains.txt"
        ip_output_file = base_filename + ".ips.txt"
        
        # Save domains to file
        with open(domain_output_file, 'w') as domain_file:
            for domain in domains:
                domain_file.write(domain + '\n')
        print(f"Domains saved to {domain_output_file}")

        # Save IPs to file
        with open(ip_output_file, 'w') as ip_file:
            for ip in ips:
                ip_file.write(ip + '\n')
        print(f"IPs saved to {ip_output_file}")


    def d():
        filename = input("Enter the name of the file to be processed: ")
        if not os.path.exists(filename):
            print("Error: File does not exist.")
            exit()
        with open(filename, 'r') as file:
            content = file.read()
            num_lines = content.count('\n')
            print(f"The file '{filename}' has {num_lines} lines.")
            
        print("What do you want to do with the file?")
        print("1. Remove duplicate lines")
        print("2. Split the file into equal parts")
        print("3. Extract ips from asn2 document")
        print("4. remove numbering on .csv files")
        print("5. Separate domains and IPs")

        option = input("Enter your choice: ")
        
        if option == '1':
            new_filename = input("Enter the new filename: ")
            remove_duplicates(filename, new_filename)
            
        elif option == '2':
            split_file(filename)
            
        elif option == '3':
            output_file = input("Enter the name of the output file: ")
            ip_ranges = extract_ip_ranges(filename)
            cidr_blocks = calculate_cidr_blocks(ip_ranges)
            output_path = os.path.join(os.path.dirname(__file__), output_file)
            save_cidr_blocks(output_path, cidr_blocks)
            print(f"CIDR Blocks saved to {output_path}")

        elif option == '5':
            domains, ips = separate_domains_ips(filename)
            save_to_file(domains, ips, filename)
            
            print("\nIPs:")
            for ip in ips:
                print(ip)
            
            save_option = input("Do you want to save the output to a text file? (yes/no): ").lower()
            if save_option == 'yes':
                output_file ='home.txt'
                save_to_file(domains, ips, filename)
            
        elif option == '4':
            output_file = input("Enter output file name: ")
            extract_domains(filename, output_file)           
        else:
            print("Invalid option. Exiting...")

    if __name__ == '__main__':
        try:
            d()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected, exiting...")

        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()
            
def ult():
    
    import threading
    import sys
    import os
    import ipaddress
    import socket
    import urllib.parse
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    class DirectScanner:
        method_list = ['HEAD', 'GET']
        host_list = []
        port_list = [80, 443]
        isp_redirects = [
            "http://safaricom.zerod.live/?c=77",
            
        ]
        output_data = []
        lock = threading.BoundedSemaphore(10)  # Threading lock with a limit of 10 threads

        def log_info(self, **kwargs):
            for x in ['status_code', 'server']:
                kwargs[x] = kwargs.get(x, '')

            location = kwargs.get('location')

            if location:
                if location.startswith(f"https://{kwargs['host']}"):
                    kwargs['status_code'] = f"{kwargs['status_code']:<4}"
                else:
                    kwargs['host'] += f" -> {location}"

            messages = []

            for x in ['\033[36mMethod:\033[0m {method}', '\033[35mStatus Code:\033[0m {status_code}', 'Server: {server}', 'Host: {host}', 'Port: {port}']:
                messages.append(f'{x}')

            self.output_data.append('  '.join(messages).format(**kwargs))
            print('  '.join(messages).format(**kwargs))

        def get_task_list(self):
            for method in self.method_list:
                for host in self.host_list:
                    for port in self.port_list:
                        yield {
                            'method': method.upper(),
                            'host': host,
                            'port': port,
                        }

        def get_url(self, host, port):
            protocol = 'https' if port in [443, 8443] else 'http'
            return f"{protocol}://{host}:{port}"

        def init(self):
            self.log_info(method='Method', status_code='Code', server='Server', host='Host', port='Port')

        def task(self, payload):
            method = payload['method']
            host = payload['host']
            port = payload['port']

            try:
                local_ip, local_port = self.get_local_ip_and_port(host, port)
                response = self.request(method, self.get_url(host, port), retries=1, timeout=5, allow_redirects=False)
            except Exception as e:
                print(f"No More: {host}")
                return

            if response is not None:
                status_code = response.status_code
                server = response.headers.get('server', '')
                location = response.headers.get('location', '')

                if status_code == 302 and location in self.isp_redirects:
                    return

                if status_code and status_code != 302:
                    data = {
                        'method': method,
                        'host': host,
                        'port': port,
                        'status_code': status_code,
                        'server': server,
                        'location': location,
                    }
                    self.log_info(local_ip=local_ip, local_port=local_port, **data)

        def get_local_ip_and_port(self, remote_host, remote_port):
            try:
                remote_ip = socket.gethostbyname(remote_host)
                port = remote_port

                temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                temp_socket.connect((remote_ip, port))
                local_ip, local_port = temp_socket.getsockname()
                temp_socket.close()
                return local_ip, local_port
            except socket.gaierror:
                print(f"Error: Failed to resolve hostname '{remote_host}'. Skipping.")
                return None, None
            except Exception as e:
                print(f"Error: {remote_host}")
                return None, None
        def request(self, method, url, retries, **kwargs):
                session = requests.Session()
                retry_strategy = Retry(
                    total=retries,
                    backoff_factor=1,
                    status_forcelist=[429, 500, 502, 503, 504],
                    method_whitelist=["HEAD", "GET", "OPTIONS"]
                )
                adapter = HTTPAdapter(max_retries=retry_strategy)
                session.mount("http://", adapter)
                session.mount("https://", adapter)
                return session.request(method, url, **kwargs)

    def get_user_input():
            while True:
                option = input("Enter '1' for a domain or IP, '2' for a file, '3' for CIDR block: ")
                if option == '1':
                    host = input("Enter the domain or IP to scan: ")
                    return [host]
                elif option == '2':
                    filename = input("Enter the filename to scan (in the same directory): ")
                    if not os.path.isfile(filename):
                        print("File not found. Please try again.")
                    else:
                        with open(filename) as f:
                            return f.read().splitlines()
                elif option == '3':
                    cdir = input("Enter the CIDR block to scan: ")
                    try:
                        network = ipaddress.ip_network(cdir)
                        return [str(ip) for ip in network.hosts()]
                    except ValueError:
                        print("Invalid CIDR block. Please try again.")
                else:
                    print("Invalid option. Please try again.")

    def f():
            slowprint("Welcome BugHunter!")
            slowprint("Check the status response of HOST, IP or CDIR")

            host_list = get_user_input()
            print("Host List:", host_list)
            if not host_list:
                print("No hosts provided. Exiting.")
                sys.exit()

            scanner = DirectScanner()
            scanner.host_list = host_list
            scanner.init()

            threads = []
            for task in scanner.get_task_list():
                thread = threading.Thread(target=scanner.task, args=(task,))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            save_output = input("Do you want to save the output to a text file? (y/n): ")
            if save_output.lower() == 'y':
                save_to_file(scanner.output_data)

    def save_to_file(output_data):
            filename = input("Enter your output.txt: ")
            with open(filename, "w") as file:
                for line in output_data:
                    file.write(remove_color_codes(line) + "\n")
            print(f"Output saved to {filename}.")

    def remove_color_codes(line):
            import re
            return re.sub(r'\033\[[0-9;]+m', '', line)

    if __name__ == "__main__":
        try:
            f()
        except Exception as e:
            print(f"An error occurred: ")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()

def script7():
    print("\033[95m" + """         
    ██╗██████╗                 
    ██║██╔══██╗                
    ██║██████╔╝                
    ██║██╔═══╝                 
    ██║██║                     
    ╚═╝╚═╝                      \033[0m""") 
    print("\033[93m" + """   
         ██████╗ ███████╗███╗   ██╗
        ██╔════╝ ██╔════╝████╗  ██║
        ██║  ███╗█████╗  ██╔██╗ ██║
        ██║   ██║██╔══╝  ██║╚██╗██║
        ╚██████╔╝███████╗██║ ╚████║
        ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                     \033[0m""")

    def validate_ip_range(ip_range):
        try:
            ipaddress.ip_network(ip_range)
        except ValueError:
            raise argparse.ArgumentTypeError("Invalid IP range")
        return ip_range

    def calculate_ipv4_addresses(ip_ranges, num_threads, pbar):
        addresses = []

        def calculate_ipv4_addresses_thread(ip_range):
            ip_network = ipaddress.ip_network(ip_range)
            for address in ip_network:
                addresses.append(address)
                pbar.update(1)

        threads = []
        for ip_range in ip_ranges:
            t = threading.Thread(target=calculate_ipv4_addresses_thread, args=(ip_range,))
            threads.append(t)
            t.start()

        # Wait for all threads to finish before returning the addresses
        for t in threads:
            t.join()

        return addresses

    def print_addresses(addresses, output_file):
        with open(output_file, "w") as f:
            for address in addresses:
                f.write(str(address) + "\n")

    def e():
        input_choice = input("Enter '1' to input IP ranges or '2' to specify a file containing IP ranges: ")
        
        if input_choice == '1':
            ip_ranges_input = input("Enter a single IP range in CIDR notation or list of IP ranges separated by comma: ")
            ip_ranges = [ip_range.strip() for ip_range in ip_ranges_input.split(",")]

            for ip_range in ip_ranges:
                validate_ip_range(ip_range)
        elif input_choice == '2':
            file_name = input("Enter the name of the file containing IP ranges (must be in the same directory as the script): ")
            try:
                with open(file_name) as f:
                    ip_ranges = [line.strip() for line in f]
            except FileNotFoundError:
                print("Error: File not found.")
                return
        else:
            print("Invalid input.")
            return

        output_file = input("Enter the name of the output file: ")
        num_threads = int(input("Enter the number of threads to use: "))

        total_addresses = sum([2 ** (32 - ipaddress.ip_network(ip_range).prefixlen) for ip_range in ip_ranges])

        with tqdm(total=total_addresses, desc="Calculating addresses") as pbar:
            addresses = calculate_ipv4_addresses(ip_ranges, num_threads, pbar)

        print_addresses(addresses, output_file)

    if __name__ == '__main__':
        try:
            e()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()
            
def script8():
    print("\033[33m" + """
     ████████╗██╗     ███████╗               
     ╚══██╔══╝██║     ██╔════╝               
        ██║   ██║     ███████╗               
        ██║   ██║     ╚════██║               
        ██║   ███████╗███████║               
        ╚═╝   ╚══════╝╚══════╝               
                                                
         ██████╗██╗  ██╗██╗  ██╗███████╗██████╗ 
        ██╔════╝██║  ██║██║ ██╔╝██╔════╝██╔══██╗
        ██║     ███████║█████╔╝ █████╗  ██████╔╝
        ██║     ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
        ╚██████╗██║  ██║██║  ██╗███████╗██║  ██║
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                       
    \033[0m""")
    import ssl
    import socket
    from concurrent.futures import ThreadPoolExecutor
    from colorama import Fore, Style
    from tqdm import tqdm

    IGNORED_SSL_ERRORS = {'WRONG_VERSION_NUMBER'}

    def print_color(message, color=Fore.WHITE, style=Style.RESET_ALL):
        print(f"{color}{message}{Style.RESET_ALL}")

    def save_to_file(result, file_name):
        try:
            with open(file_name, 'a') as file:
                file.write(result)
        except Exception as e:
            print_color(f"Error saving result to '{file_name}': {e}", Fore.RED)

    def check_tls_details(host, port, file_name, pbar):
        global progress_counter
        ip_address = None  # Initialize ip_address here

        try:
            ip_address = socket.gethostbyname(host)
            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

            with socket.create_connection((host, port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    result = f"TLS details for {host} ({ip_address}):{port}\n" \
                            f"TLS Version: {ssock.version()}\nCipher Suite: {ssock.cipher()}\n"
            print(result)
            save_to_file(result, file_name)
        except ssl.SSLError as e:
            error_message = str(e)
            error_code = getattr(e, 'reason', None)
            if error_code and error_code in IGNORED_SSL_ERRORS:
                result = f"Ignoring SSL error for {host} ({ip_address}):{port}: {error_message}\n"
            else:
                result = f"Error for {host} ({ip_address}):{port}: {error_message}\n"
            print_color(result, Fore.RED)
        except socket.timeout as e:
            result = f"Timeout error for {host} ({ip_address}):{port}: {str(e)}\n"
            print_color(result, Fore.RED)
        except Exception as e:
            result = f"Error for {host} ({ip_address}):{port}: {str(e)}\n"
            print_color(result, Fore.RED)

        progress_counter += 1  # Increment the global progress counter
        pbar.update(1)  # Increment the main progress bar

    def check_tls_for_domains(domains, ports=(443, 80)):
        global total_tasks
        file_name = input("Enter the name of the file to save the TLS details (e.g., output.txt): ")
        total_tasks = len(domains) * len(ports)

        with ThreadPoolExecutor() as executor, tqdm(total=total_tasks, desc="Overall Progress") as pbar:
            futures = []
            for domain in domains:
                for port in ports:
                    futures.append(executor.submit(check_tls_details, domain, port, file_name, pbar))
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    print_color(f"Error processing task: {str(e)}", Fore.RED)
        executor.shutdown(wait=True)

    def g():
        choice = input("Do you want to input a domain manually (M) or provide a text file (T)? ").upper()

        if choice == "M":
            domain = input("Enter the domain or IP address: ")
            check_tls_for_domains([domain])
        elif choice == "T":
            file_name = input("Enter the name of the text file with domains: ")
            try:
                with open(file_name, "r") as file:
                    domains = [line.strip() for line in file]

                check_tls_for_domains(domains)
            except FileNotFoundError:
                print_color(f"Error: File '{file_name}' not found.", Fore.RED)
        else:
            print_color("Invalid choice. Please choose 'M' for manual input or 'T' for a text file.", Fore.RED)

    if __name__ == '__main__':
        try:
            g()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()

def script9():
    print('''
     ██████╗ ██████╗  ██████╗
    ██╔═══██╗██╔══██╗██╔════╝
    ██║   ██║██████╔╝██║     
    ██║   ██║██╔═══╝ ██║     
    ╚██████╔╝██║     ╚██████╗
    ╚═════╝ ╚═╝      ╚═════╝                
        ''')
    
    def scan_ports(target, port):
        """Scan a single port for a given target."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                return f"Port {port} is open"
            elif result == 11:
                return f"Port {port} is closed"
            else:
                return f"Port {port} is filtered"
        except Exception as e:
            return f"An error occurred while scanning port {port}: {e}"

    def scan_ports_threaded(target, ports, num_threads):
        """Scan ports for a given target using multiple threads."""
        print(f"Scanning ports for {target}...")
        results = []
        threads = []
        for port in ports:
            thread = threading.Thread(target=scan_ports_thread_worker, args=(target, port, results))
            thread.start()
            threads.append(thread)
            if len(threads) >= num_threads:
                for thread in threads:
                    thread.join()
                threads.clear()
        
        for thread in threads:
            thread.join()

        return '\n'.join(results)

    def scan_ports_thread_worker(target, port, results):
        """Thread worker function to scan a single port and store the result."""
        result = scan_ports(target, port)
        results.append(result)

    def save_to_file(filename, data):
        """Save data to a file."""
        with open(filename, "w") as file:
            file.write(data)
        print(f"Results saved to {filename}")

    def h():
        """Main function to handle user inputs and initiate scanning."""
        try:
            input_type = input("Select input type (1: Domain/IP, 2: Domain List/IP List): ")
            results_to_save = []

            if input_type == "1":  # Single domain
                target = input("Enter the domain: ")
                num_threads = int(input("Enter the number of threads: "))
                results = scan_ports_threaded(target, ports, num_threads)
                print(results)
                results_to_save.append(results)

            elif input_type == "2":  # Domain list from file
                filename = input("Enter the filename containing the domain list: ")
                with open(filename, "r") as file:
                    targets = [line.strip() for line in file]

                num_threads = int(input("Enter the number of threads: "))
                for target in targets:
                    results = scan_ports_threaded(target, ports, num_threads)
                    print(results)
                    results_to_save.append(results)

            save_file = input("Do you want to save the results to a file? (Y/N): ")
            if save_file.lower() == "y":
                filename = input("Enter the filename to save the results: ")
                save_to_file(filename, '\n\n'.join(results_to_save))

        except Exception as e:
            print("An error occurred:", e)

    if __name__ == '__main__':
        ports = [80, 8080, 443, 21, 22, 53, 67, 68, 123, 161, 162, 500, 520, 514, 5353, 4500, 1900]  # Define ports to scan
        try:
            h()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()

def script10():
    print("""
          
    ███████╗██████╗ 
    ██╔════╝██╔══██╗
    █████╗  ██████╔╝
    ██╔══╝  ██╔═══╝ 
    ██║     ██║     
    ╚═╝     ╚═╝              
          """)
    def process_domain(domain):
        """Process a single domain."""
        domain = re.sub(r"^https?://", "", domain)
        if not domain.startswith("www."):
            domain = f"www.{domain}"
        try:
            ip_address = socket.gethostbyname(domain)
            try:
                server_info = socket.gethostbyaddr(ip_address)[0]
                return f"Server for {domain}: {server_info}"
            except socket.herror:
                return None
        except socket.gaierror:
            return "Failed to perform DNS lookup"

    def process_domain_threaded(domain):
        """Process a single domain within a thread."""
        result = process_domain(domain)
        if result:
            print(result)
            return result

    def aa1():
        """Main function to handle user inputs and initiate processing."""
        try:
            input_type = input("Enter input type (1 for single domain, 2 for domain list): ")

            if input_type == "1":
                domain = input("Enter your domain: ")
                result = process_domain(domain)
                if result:
                    print(result)
                    save_output = input("Do you want to save the output to a file? (y/n): ")
                    if save_output.lower() == "y":
                        output_file = input("Enter the output file name: ")
                        with open(output_file, "w") as file:
                            file.write(result)
                        print(f"Output saved to {output_file}")

            elif input_type == "2":
                domain_file = input("Enter the domain list file name: ")

                try:
                    with open(domain_file, "r") as file:
                        domains = file.readlines()

                    num_threads = int(input("Enter the number of threads: "))

                    output_results = []
                    threads = []

                    for domain in domains:
                        domain = domain.strip()
                        thread = threading.Thread(target=process_domain_threaded, args=(domain,))
                        thread.start()
                        threads.append(thread)
                        if len(threads) >= num_threads:
                            for thread in threads:
                                thread.join()
                            output_results.extend([t.result() for t in threads])
                            threads = []
                    for thread in threads:
                        thread.join()

                    save_output = input("Do you want to save the output to a file? (y/n): ")
                    if save_output.lower() == "y":
                        output_file = input("Enter the output file name: ")
                        with open(output_file, "a") as file:
                            for result in output_results:
                                if result:
                                    file.write(result + "\n")
                        print(f"Output saved to {output_file}")

                except FileNotFoundError:
                    print("Domain list file not found.")
            else:
                print("Invalid input type.")

        except Exception as e:
            print("An error occurred:", e)

    if __name__ == '__main__':
        try:
            aa1()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()
            
def script11():
    print("\033[94m" + """
    ██████╗ ███████╗██╗  ██╗███████╗
    ██╔══██╗██╔════╝╚██╗██╔╝██╔════╝
    ██║  ██║█████╗   ╚███╔╝ █████╗  
    ██║  ██║██╔══╝   ██╔██╗ ██╔══╝  
    ██████╔╝███████╗██╔╝ ██╗██║     
    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     
            \033[0m""")
    def search_crt_sh(domain):
        url = f"https://crt.sh/?q={domain}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            return response.content
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
    def extract_certificate_info(html_content):
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            certificate_data = []

            for row in tqdm(soup.select('table tr'), desc="Extracting data"):
                columns = row.select('td')
                if len(columns) >= 7:
                    raw_common_name = columns[5].get_text(strip=True)

                    # Use a regular expression to extract valid domains
                    matches = re.findall(r'\b(?:[a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}\b', raw_common_name)

                    for domain in matches:
                        # Check if the domain has a dot before the end and not ending with a dot
                        if '.' in domain and not domain.endswith('.'):
                            certificate_data.append({"common_name": domain.strip()})
            return certificate_data
        else:
            return []
    def remove_duplicates(certificate_info):
        unique_set = set()
        unique_certificate_info = []
        for info in certificate_info:
            unique_data = (info["common_name"])
            if unique_data not in unique_set:
                unique_set.add(unique_data)
                unique_certificate_info.append(info)
        return unique_certificate_info
    
    def save_domains_to_file(domains, filename):
        filename = input("enter save file name: ")
        with open(filename, "a") as file:
            for domain in domains:
                file.write(f"{domain}\n")
            print(f"Domains saved to {filename}")

    def z():
        print("1. Search for a single domain")
        print("2. Load domain list from a text file")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            domain = input("Enter a domain: ").lower()  # Convert to lowercase for case-insensitive check
            # Check if the input is a valid domain (you can improve this validation)
            if '.' in domain:
                html_content = search_crt_sh(domain)
                certificate_info = extract_certificate_info(html_content)

                if certificate_info:
                    print("Certificate Information:")
                    unique_certificate_info = remove_duplicates(certificate_info)
                    for info in unique_certificate_info:
                        if info['common_name'].lower() != domain:  # Exclude the user-entered domain
                            print(f"{info['common_name']}")
                            print()  # Add a new line between entries

                    save_domains_to_file([info['common_name'] for info in unique_certificate_info if info['common_name'].lower() != domain], "output.txt")
                else:
                    print("No certificate information found.")
            else:
                print("Invalid domain format.")
        elif choice == "2":
            filename = input("Enter the filename containing the domain list: ")
            with open(filename, "r") as file:
                domains = [line.strip() for line in file.readlines()]

            if domains:
                for domain in domains:
                    print(f"Searching for domain: {domain}")
                    html_content = search_crt_sh(domain)
                    certificate_info = extract_certificate_info(html_content)

                    if certificate_info:
                        print("Certificate Information:")
                        unique_certificate_info = remove_duplicates(certificate_info)
                        for info in unique_certificate_info:
                            if info['common_name'].lower() != domain:  # Exclude the user-entered domain
                                print(f"{info['common_name']}")
                                print()  # Add a new line between entries

                        save_domains_to_file([info['common_name'] for info in unique_certificate_info if info['common_name'].lower() != domain], "output.txt")
                    else:
                        print("No certificate information found for this domain.")
            else:
                print("No domains found in the file.")
        else:
            print("Invalid choice. Please choose 1 or 2.")
            
    if __name__ == '__main__':
        try:
            z()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()
            
def script12():
    
    import requests
    from bs4 import BeautifulSoup as bsoup
    from tqdm import tqdm

    GREEN, RED = '\033[1;32m', '\033[91m'

    def get_user_input():
        url = input('[?] Enter the URL to look up: ')
        pages = input('[?] Enter the number of pages to search (Default: 1): ')
        if not pages:
            pages = 1
        output_file = input('[?] Enter the output file name: ')
        return url, int(pages), output_file

    def google_search(query, page):
        base_url = 'https://www.google.com/search'
        headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
        params   = { 'q': query, 'start': page * 10 }
        resp = requests.get(base_url, params=params, headers=headers)
        soup = bsoup(resp.text, 'html.parser')
        links  = soup.findAll('cite')
        result = [link.text for link in links]
        return result

    def bing_search(query, page):
        base_url = 'https://www.bing.com/search'
        headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
        params   = { 'q': query, 'first': page * 10 + 1 }
        resp = requests.get(base_url, params=params, headers=headers)
        soup = bsoup(resp.text, 'html.parser')
        links  = soup.findAll('cite')
        result = [link.text for link in links]
        return result

    def ask_search(query, page):
        base_url = 'https://www.ask.com/search'
        headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
        params   = { 'q': query, 'first': page * 10 + 1 }
        resp = requests.get(base_url, params=params, headers=headers)
        soup = bsoup(resp.text, 'html.parser')
        links  = soup.findAll('cite')
        result = [link.text for link in links]
        return result

    def yandex_search(query, page):
        base_url = 'https://www.yahoo.com/search'
        headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
        params   = { 'q': query, 'first': page * 10 + 1 }
        resp = requests.get(base_url, params=params, headers=headers)
        soup = bsoup(resp.text, 'html.parser')
        links  = soup.findAll('cite')
        result = [link.text for link in links]
        return result

    def duckgo_search(query, page):
        base_url = 'https://duckduckgo.com/html'
        headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
        params   = { 'q': query, 's': page * 30 }  # Adjusting page parameter here
        resp = requests.post(base_url, data=params, headers=headers)
        soup = bsoup(resp.text, 'html.parser')
        links  = soup.findAll('cite')
        result = [link.text for link in links]
        return result

    def save_results(filename, results):
        unique_urls = set()  # Create a set to store unique URLs
        with open(filename, 'w') as file:
            for result_list in tqdm(results, desc="Saving Results", unit="page"):
                for result in result_list:
                    if result not in unique_urls:  # Check if the URL is unique
                        file.write(result + '\n')
                        unique_urls.add(result)  # Add the URL to the set of unique URLs

    def cc():
        print()
        url, pages, output_file = get_user_input()

        engines = [google_search, bing_search, yandex_search, duckgo_search, ask_search]

        results = []
        for engine in tqdm(engines, desc="Search Engines", unit="engine"):
            result = []
            for page_num in range(pages):
                result.extend(engine(url, page_num))
            results.append(result)

        print('-' * 70)
        print(f'Searching for: {url} in {pages} page(s) of all engines')
        print('-' * 70)
        print()

        counter = 0
        for result in results:
            for r in result:
                print('[+] ' + r)
                counter += 1

        print()
        print('-' * 70)
        print(f'Number of URLs: {counter}')
        print('-' * 70)

        if output_file:
            save_results(output_file, results)
            print(f'Results saved to {output_file}')

    if __name__ == "__main__":

        try:
            cc()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()

def script13():
    print('''
          
    ██████╗ ██████╗ ██╗
    ██╔══██╗╚════██╗██║
    ██║  ██║ █████╔╝██║
    ██║  ██║██╔═══╝ ██║
    ██████╔╝███████╗██║
    ╚═════╝ ╚══════╝╚═╝       
            ''')

    import subprocess
    import re
    import os
    import time
    from tqdm import tqdm

    def nslookup_single(target, output_filename=None):
        try:
            command = f"nslookup {target}"
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                result = stdout.decode()
                print(f"Results for {target}:\n{result}")
                if output_filename:
                    with open(output_filename, 'a') as output_file:  # Append mode to add results for multiple targets
                        output_file.write(f"Results for {target}:\n{result}\n\n")
                    print(f"Result saved to {output_filename}")
                return result
            else:
                return f"Error executing lookup for {target}:\n{stderr.decode()}"
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def extract_addresses(result):
        addresses = re.search(r'Addresses:(.*?)(?=\w+:|$)', result, re.DOTALL)
        if addresses:
            return addresses.group(1).strip()
        else:
            return None

    def nslookup_from_file(filename, output_filename=None):
        try:
            with open(filename, 'r') as file:
                lines = [line.strip() for line in file.readlines()]  # Remove leading and trailing whitespace
                for line in tqdm(lines, desc="Progress", unit="target"):
                    target = line.lstrip()  # Remove only leading spaces
                    nslookup_single(target, output_filename=output_filename)
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def y():
        print("Lookup Tool")
        save_results = input("Do you want to save the result to a file? (y/n): ")
        if save_results.lower() == 'y':
            output_filename = input("Enter the filename to save the result: ")
        else:
            output_filename = None

        choice = input("Enter '1' for a single IP/domain or '2' for a file with a list of IPs/domains: ")
        if choice == '1':
            target = input("Enter an IP address or domain name: ")
            nslookup_single(target, output_filename=output_filename)
        elif choice == '2':
            filename = input("Enter the name of the file containing a list of IPs/domains (in the same directory as the script): ")
            nslookup_from_file(filename, output_filename=output_filename)
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    if __name__ == '__main__':
        try:
            y()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0

def kingscript():
    import os
    import ssl
    import requests
    import socket
    import concurrent.futures
    from http.client import HTTPException
    from socket import gaierror
    from termcolor import colored
    from tqdm import tqdm

    # Suppress SSL certificate verification warnings
    ssl._create_default_https_context = ssl._create_unverified_context

    def scan_domain(domain, timeout=3):
        ip = None
        server = None
        color = 'white'

        try:
            ip_list = [ip for ip in socket.gethostbyname_ex(domain)[2] if '.' in ip]
            ip = ip_list[0] if ip_list else None

            # Attempt HTTP HEAD request to retrieve server information
            try:
                response = requests.head(f"http://{domain}", timeout=timeout)
                server = response.headers.get('Server', '')
                location = response.headers.get('Location', '')
            except (requests.RequestException, HTTPException):
                pass

            if server:
                if 'cloudflare' in server.lower():
                    color = 'yellow'
                elif 'cloudfront' in server.lower():
                    color = 'blue'
                elif 'apple' in server.lower():
                    color = 'magenta'

        except (socket.gaierror, requests.RequestException):
            pass

        return ip, domain, server, color

    def scan_direct(filename, timeout=3, output=None, max_workers=2):
        domain_list = set()

        # Read domain list from file
        with open(filename, 'r') as file:
            for line in file:
                domain = line.strip()
                domain_list.add(domain)

        successful_scans = []

        # Initialize tqdm progress bar
        progress_bar = tqdm(total=len(domain_list), desc="Scanning", unit="domains")

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit scanning tasks
            futures = [executor.submit(scan_domain, domain, timeout) for domain in domain_list]

            # Process results as they become available
            for future in concurrent.futures.as_completed(futures):
                ip, domain, server, color = future.result()
                if ip:
                    successful_scans.append((ip, domain, server, color))
                progress_bar.update(1)

        # Close tqdm progress bar
        progress_bar.close()

        # Print results to console
        for ip, domain, server, color in successful_scans:
            server_info = colored(server, color)
            print(f"{ip:<15}  {domain:<30} {server_info}")

        # Write results to output file if provided
        if output:
            with open(output, 'w') as outfile:
                for ip, domain, server, color in successful_scans:
                    outfile.write(f"{ip:<15}  {domain:<30} {server}\n")

        # Notify the user if output file was created
        if output:
            print(f"\nResults saved to {output}")


    def lo():
        print(f"*note 2 threads for best results")
        print(f"* 5 sec timeout should find everything\n")
        filename = input("Enter the filename containing the list of domains: ")
        timeout = int(input("Enter the connection timeout (in seconds): "))
        output = input("Enter the output filename (leave blank for no output file): ")
        
        max_workers = int(input("Enter the number of concurrent threads 2 threads for best results: "))

        scan_direct(filename, timeout, output, max_workers)

    if __name__ == '__main__':
        try:
            lo()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()

def script16():
    
    print('''
        ██╗    ██╗███████╗███████╗
        ██║    ██║██╔════╝██╔════╝
        ██║ █╗ ██║███████╗███████╗
        ██║███╗██║╚════██║╚════██║
        ╚███╔███╔╝███████║███████║
        ╚══╝╚══╝ ╚══════╝╚══════╝
          ''')                      

    init(autoreset=True)
    print_lock = threading.Lock()  # Use threading.Lock for thread safety

    def establish_websocket_connection(websocket_domain, ip_or_domain, port, output_file_name):
        try:
            # Check if the input is a CIDR block
            if '/' in ip_or_domain:
                ip_network = ipaddress.IPv4Network(ip_or_domain, strict=False)
                ip_addresses = [str(ip) for ip in ip_network.hosts()]
            else:
                ip_addresses = [ip_or_domain]

            successful_connections = 0

            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(attempt_connection, ip, port, output_file_name) for ip in ip_addresses]

                for future in concurrent.futures.as_completed(futures):
                    with print_lock:
                        if future.result():
                            successful_connections += 1

            with print_lock:
                if successful_connections > 0:
                    print(f"Successfully saved {successful_connections} connections to {output_file_name}.")
                else:
                    print(f"{Fore.RED}No successful WebSocket connections found for {ip_or_domain}.")

        except ValueError as e:
            with print_lock:
                print(f"{Fore.RED}Invalid CIDR block {ip_or_domain}: {e}")

    def attempt_connection(ip, port, output_file_name):
        try:
            s = socket.create_connection((ip, port), timeout=2)

            if port == 443:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", category=DeprecationWarning)
                    s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1_2)

            with print_lock:
                print(f"{Fore.GREEN}{ip} : WebSocket connection established")

            with open(output_file_name, 'a') as output_file:
                with print_lock:
                    output_file.write(ip + '\n')

            return True

        except (socket.gaierror, ConnectionRefusedError, ssl.SSLError, socket.timeout, UnicodeError) as e:
            with print_lock:
                if "tlsv1 alert internal error" in str(e) or "sslv3 alert handshake failure" in str(e):
                    print(f"{Fore.RED}WebSocket connection to {ip} failed.")
                else:
                    print(f"{Fore.RED}WebSocket connection to {ip} failed: {e}")
        return False
        
    def k():
        ip_or_domain_list = []

        choice = input("""Choose an option  
        1. Input file name
        2. Manual input
        3. Auto Range: """)

        if choice == '1':
            file_name = input("Enter the file name containing IPs/Domains: ")

            try:
                with open(file_name, 'r') as file:
                    ip_or_domain_list.extend(line.strip() for line in file)
            except FileNotFoundError:
                print("File not found.")
                return

        elif choice == '2':
            manual_input = input("Enter a Ip/Domain: ")
            ip_or_domain_list.extend(manual_input.split(','))

        elif choice == '3':
            # Prompt the user to choose a group
            print("Choose a group of IPs:")
            print("1 - CLOUDFRONT_GLOBAL_IP_LIST ")
            print("2 - CLOUDFRONT_REGIONAL_EDGE_IP_LIST_1")
            print("3 - CLOUDFRONT_REGIONAL_EDGE_IP_LIST_1_cont'd ")
            print("4 - CLOUDFRONT_REGIONAL_EDGE_IP_LIST_2 ")
            print("5 - CLOUDFRONT_REGIONAL_EDGE_IP_LIST_3")
            print("6 - CLOUDFRONT_REGIONAL_EDGE_IP_LIST_4")
            print("7 - CLOUDFLARE_IPV4_LIST_1")

            group_choice = input("Enter the group number: ")

            if group_choice == '1':
                ip_or_domain_list.extend(["13.32.0.0/15", "52.46.0.0/18", "52.84.0.0/15", "52.222.128.0/17",
                                        "54.182.0.0/16", "54.192.0.0/16", "54.230.0.0/16", "54.239.128.0/18",
                                        "54.239.192.0/19", "54.240.128.0/18", "204.246.164.0/22 204.246.168.0/22",
                                        "204.246.174.0/23","204.246.176.0/20","205.251.192.0/19","205.251.249.0/24",
                                        "205.251.250.0/2","205.251.252.0/23","205.251.254.0/24","216.137.32.0/19",])
            elif group_choice == '2':
                ip_or_domain_list.extend(["13.54.63.128/26", "13.59.250.0/26", "13.113.203.0/24", "13.124.199.0/24", 
                                        "13.228.69.0/24", "18.216.170.128/25", "34.195.252.0/24", "34.216.51.0/25", 
                                        "34.226.14.0/24", "34.232.163.208/29", "35.158.136.0/24", "35.162.63.192/26", 
                                        "35.167.191.128/26", "52.15.127.128/26", "52.47.139.0/24", "52.52.191.128/26", 
                                        "52.56.127.0/25", "52.57.254.0/24", "52.66.194.128/26", "52.78.247.128/26", 
                                        "52.199.127.192/26", "52.212.248.0/26", "52.220.191.0/26", "54.233.255.128/26", 
                                        "2.57.12.0/24", "2.255.190.0/23", "3.0.0.0/15", "3.2.0.0/24", "3.2.2.0/23", 
                                        "3.2.8.0/21", "3.2.48.0/23", "3.2.50.0/24", "3.3.6.0/23", "3.3.8.0/21", 
                                        "3.3.16.0/20", "3.5.32.0/22", "3.5.40.0/21", "3.5.48.0/21", "3.5.64.0/21", 
                                        "3.5.72.0/23", "3.5.76.0/22", "3.5.80.0/21", "3.5.128.0/19", "3.5.160.0/21", 
                                        "3.5.168.0/23", "3.5.208.0/22", "3.5.212.0/23", "3.5.216.0/22", "3.5.220.0/23", 
                                        "3.5.222.0/24", "3.5.224.0/23", "3.5.226.0/24", "3.5.228.0/22", "3.5.232.0/21", 
                                        "3.5.240.0/20", "3.6.0.0/15", "3.8.0.0/13", "3.16.0.0/13", "3.24.0.0/14", "3.28.0.0/15", 
                                        "3.33.35.0/24", "3.33.44.0/22", "3.33.128.0/17", "3.34.0.0/15", "3.36.0.0/14", "3.64.0.0/12", 
                                        "3.96.0.0/14", "3.101.0.0/16", "3.104.0.0/13", "3.112.0.0/14", "3.120.0.0/13", "3.128.0.0/12", 
                                        "3.144.0.0/13", "3.248.0.0/13", "5.22.145.0/24", "5.183.207.0/24", "13.32.1.0/24", "13.32.2.0/23", 
                                        "13.32.4.0/22", "13.32.8.0/21", "13.32.16.0/20", "13.32.40.0/22", "13.32.45.0/24", "13.32.46.0/23", 
                                        "13.32.48.0/21", "13.32.56.0/23", "13.32.59.0/24", "13.32.60.0/23", "13.32.62.0/24", "13.32.64.0/23", 
                                        "13.32.66.0/24", "13.32.68.0/22", "13.32.72.0/21", "13.32.80.0/21", "13.32.88.0/22", "13.32.92.0/23", 
                                        "13.32.98.0/23", "13.32.100.0/22", "13.32.104.0/23", "13.32.106.0/24", "13.32.108.0/22", "13.32.112.0/20",
                                        ])
            elif group_choice == '3':
                ip_or_domain_list.extend(["13.32.128.0/22", "13.32.132.0/24", "13.32.134.0/23", "13.32.136.0/23", 
                                        "13.32.140.0/24", "13.32.142.0/23", "13.32.146.0/24", "13.32.148.0/22", "13.32.152.0/22",
                                        "13.32.160.0/19", "13.32.192.0/20", "13.32.208.0/21", "13.32.224.0/23", "13.32.226.0/24", 
                                        "13.32.229.0/24", "13.32.230.0/23", "13.32.232.0/24", "13.32.240.0/23", "13.32.246.0/23",
                                        "13.32.249.0/24", "13.32.252.0/22", "13.33.0.0/19", "13.33.32.0/21", "13.33.40.0/23", "13.33.43.0/24", 
                                        "13.33.44.0/22", "13.33.48.0/20", "13.33.64.0/19", "13.33.96.0/22", "13.33.100.0/23", "13.33.104.0/21", "13.33.112.0/20", "13.33.128.0/21", "13.33.136.0/22", "13.33.140.0/23", "13.33.143.0/24",
                                        "13.33.144.0/21", "13.33.152.0/22", "13.33.160.0/21", "13.33.174.0/24", "13.33.184.0/23", "13.33.189.0/24", "13.33.197.0/24", "13.33.200.0/21", "13.33.208.0/21", "13.33.224.0/23", "13.33.229.0/24", "13.33.230.0/23", "13.33.232.0/21", "13.33.240.0/20", "13.35.0.0/21", "13.35.8.0/23", "13.35.11.0/24", "13.35.12.0/22", "13.35.16.0/21", "13.35.24.0/23", "13.35.27.0/24", "13.35.28.0/22", "13.35.32.0/21", "13.35.40.0/23", "13.35.43.0/24", "13.35.44.0/22", "13.35.48.0/21", "13.35.56.0/24", "13.35.63.0/24", "13.35.64.0/21", "13.35.73.0/24", "13.35.74.0/23", "13.35.76.0/22", "13.35.80.0/20", "13.35.96.0/19", "13.35.128.0/20", "13.35.144.0/21", "13.35.153.0/24", "13.35.154.0/23", "13.35.156.0/22", "13.35.160.0/21", "13.35.169.0/24", "13.35.170.0/23", "13.35.172.0/22", "13.35.176.0/21", "13.35.192.0/24", "13.35.200.0/21", "13.35.208.0/21", "13.35.224.0/20", "13.35.249.0/24", "13.35.250.0/23",
                                        "13.35.252.0/22", "13.36.0.0/14", "13.40.0.0/14", "13.48.0.0/13", "13.56.0.0/14", 
                                        "13.112.0.0/14", "13.124.0.0/14", "13.200.0.0/15", "13.208.0.0/13", "13.224.0.0/18", 
                                        "13.224.64.0/19", "13.224.96.0/21", "13.224.105.0/24", "13.224.106.0/23", "13.224.108.0/22", 
                                        "13.224.112.0/21", "13.224.121.0/24", "13.224.122.0/23", "13.224.124.0/22", "13.224.128.0/20", 
                                        "13.224.144.0/21", "13.224.153.0/24", "13.224.154.0/23", "13.224.156.0/22", "13.224.160.0/21", "13.224.185.0/24", "13.224.186.0/23", "13.224.188.0/22", "13.224.192.0/18", "13.225.0.0/21", "13.225.9.0/24", "13.225.10.0/23", "13.225.12.0/22", "13.225.16.0/21", "13.225.25.0/24", "13.225.26.0/23", "13.225.28.0/22", "13.225.32.0/19", "13.225.64.0/19", "13.225.96.0/21", "13.225.105.0/24", "13.225.106.0/23", "13.225.108.0/22", "13.225.112.0/21", "13.225.121.0/24", "13.225.122.0/23", "13.225.124.0/22", "13.225.128.0/21", "13.225.137.0/24", "13.225.138.0/23", "13.225.140.0/22", "13.225.144.0/20", "13.225.160.0/21", "13.225.169.0/24", "13.225.170.0/23", "13.225.172.0/22", "13.225.176.0/21", "13.225.185.0/24", "13.225.186.0/23", "13.225.188.0/22", "13.225.192.0/19", "13.225.224.0/20", "13.225.240.0/21", "13.225.249.0/24", "13.225.250.0/23", "13.225.252.0/22", "13.226.0.0/21", "13.226.9.0/24", "13.226.10.0/23", "13.226.12.0/22", "13.226.16.0/20", "13.226.32.0/20", "13.226.48.0/21", "13.226.56.0/24", "13.226.73.0/24", "13.226.77.0/24", "13.226.78.0/23", "13.226.84.0/24", "13.226.86.0/23", "13.226.88.0/21", "13.226.96.0/21", "13.226.112.0/22", "13.226.117.0/24", "13.226.118.0/23", "13.226.120.0/21", "13.226.128.0/17", "13.227.1.0/24", "13.227.2.0/23", "13.227.5.0/24", "13.227.6.0/23",
                                        "13.227.8.0/21", "13.227.16.0/22", "13.227.21.0/24", "13.227.22.0/23", "13.227.24.0/21", "13.227.32.0/20", "13.227.48.0/22", "13.227.53.0/24", "13.227.54.0/23", "13.227.56.0/21", "13.227.64.0/20", "13.227.80.0/22", "13.227.85.0/24", "13.227.86.0/23", "13.227.88.0/21", "13.227.96.0/19", "13.227.128.0/19", "13.227.160.0/22", "13.227.164.0/24", "13.227.168.0/21", "13.227.198.0/23", "13.227.208.0/22", "13.227.216.0/21", "13.227.228.0/24", "13.227.230.0/23", "13.227.240.0/20", "13.228.0.0/14", "13.232.0.0/13", "13.244.0.0/14", "13.248.0.0/19", "13.248.32.0/20", "13.248.48.0/21", "13.248.60.0/22", "13.248.64.0/21", "13.248.72.0/24", "13.248.96.0/19", "13.248.128.0/17", "13.249.0.0/17", "13.249.128.0/20", "13.249.144.0/24", "13.249.146.0/23", "13.249.148.0/22", "13.249.152.0/21", "13.249.160.0/24", "13.249.162.0/23", "13.249.164.0/22", "13.249.168.0/21", "13.249.176.0/20", 
                                        "13.249.192.0/19", "13.249.224.0/20", "13.249.241.0/24", "13.249.242.0/23", "13.249.245.0/24", "13.249.246.0/23", "13.249.248.0/21", "13.250.0.0/15", "15.152.0.0/16", "15.156.0.0/15", "15.158.0.0/21", "15.158.8.0/22", "15.158.13.0/24", "15.158.15.0/24", "15.158.16.0/23", "15.158.19.0/24", "15.158.21.0/24", "15.158.22.0/23", "15.158.24.0/23", "15.158.27.0/24", "15.158.28.0/22", "15.158.33.0/24", "15.158.34.0/23", "15.158.36.0/22", "15.158.40.0/21", "15.158.48.0/21", "15.158.56.0/23", "15.158.58.0/24", "15.158.60.0/22", "15.158.64.0/22", "15.158.68.0/23", "15.158.70.0/24", "15.158.72.0/21", "15.158.80.0/21", "15.158.88.0/23", 
                                        "15.158.91.0/24", "15.158.92.0/22", "15.158.96.0/22", "15.158.100.0/24", "15.158.102.0/23", "15.158.104.0/23", "15.158.107.0/24", "15.158.108.0/22", "15.158.112.0/20", "15.158.128.0/24", "15.158.131.0/24", "15.158.135.0/24", "15.158.138.0/23", "15.158.140.0/23", "15.158.142.0/24", "15.158.144.0/22", "15.158.148.0/23", "15.158.151.0/24", "15.158.152.0/24", "15.158.156.0/22", "15.158.160.0/23", "15.158.162.0/24"
                                            ])
            elif group_choice == '4':
                ip_or_domain_list.extend(["15.158.165.0/24", "15.158.166.0/23", "15.158.168.0/21", "15.158.176.0/22", "15.158.180.0/24", "15.158.182.0/24", "15.158.184.0/21", "15.160.0.0/15", "15.164.0.0/15", "15.168.0.0/16", "15.177.8.0/21", "15.177.16.0/20", "15.177.32.0/19", "15.177.66.0/23", "15.177.68.0/22", "15.177.72.0/21", "15.177.80.0/21", "15.177.88.0/22", "15.177.92.0/23", "15.177.94.0/24", "15.177.96.0/22", "15.181.0.0/17", "15.181.128.0/20", "15.181.144.0/22", "15.181.160.0/19", "15.181.192.0/19", 
                                        "15.181.224.0/20", "15.181.240.0/21", "15.181.248.0/22", "15.181.252.0/23", "15.181.254.0/24", "15.184.0.0/15", "15.188.0.0/16", "15.190.0.0/22", "15.190.16.0/20", "15.193.0.0/22", "15.193.4.0/23", "15.193.7.0/24", "15.193.8.0/23", "15.193.10.0/24", "15.197.4.0/22", "15.197.12.0/22", "15.197.16.0/22", "15.197.20.0/23", "15.197.24.0/22", "15.197.28.0/23", "15.197.32.0/21", "15.197.128.0/17", "15.206.0.0/15", "15.220.0.0/19", "15.220.32.0/21", "15.220.40.0/22", "15.220.48.0/20", "15.220.64.0/21", "15.220.80.0/20", "15.220.112.0/20", "15.220.128.0/18", "15.220.192.0/20", "15.220.216.0/21", "15.220.224.0/19", "15.221.7.0/24", "15.221.8.0/21", "15.221.16.0/20", "15.221.36.0/22", "15.221.40.0/21", "15.221.128.0/22", "15.222.0.0/15", "15.228.0.0/15", "15.236.0.0/15", "15.248.8.0/22", "15.248.16.0/22", "15.248.32.0/21", "15.248.40.0/22", "15.248.48.0/21", "15.253.0.0/16", "15.254.0.0/16", "16.12.0.0/23", "16.12.2.0/24", "16.12.4.0/23", "16.12.9.0/24", "16.12.10.0/23", "16.12.12.0/23", "16.12.14.0/24", "16.12.18.0/23", "16.12.20.0/24", "16.12.24.0/21", "16.12.32.0/21", "16.12.40.0/23", "16.16.0.0/16", "16.24.0.0/16", "16.50.0.0/15", "16.62.0.0/15", "16.162.0.0/15", "16.168.0.0/14", "18.34.32.0/19", "18.34.64.0/20", "18.34.240.0/20", "18.35.32.0/19", "18.35.64.0/20", "18.35.240.0/20", "18.60.0.0/15", "18.64.0.0/19", "18.64.32.0/21", "18.64.40.0/22", "18.64.44.0/24", 
                                        "18.64.75.0/24", "18.64.76.0/22", "18.64.80.0/20", "18.64.96.0/20", "18.64.112.0/21", "18.64.135.0/24", "18.64.136.0/21", "18.64.144.0/20", "18.64.160.0/19", "18.64.192.0/20", "18.64.208.0/23", "18.64.225.0/24", "18.64.226.0/23", "18.64.228.0/22", "18.64.232.0/21", "18.64.255.0/24", "18.65.0.0/17", "18.65.128.0/18", "18.65.192.0/19", "18.65.224.0/21", "18.65.232.0/22", "18.65.236.0/23", "18.65.238.0/24", "18.65.254.0/23", "18.66.0.0/16", "18.67.0.0/18", "18.67.64.0/19", "18.67.96.0/20", "18.67.112.0/22", "18.67.116.0/24", "18.67.147.0/24", "18.67.148.0/22", "18.67.152.0/21", "18.67.160.0/23", "18.67.237.0/24", "18.67.238.0/23", "18.67.240.0/20", "18.68.0.0/20", "18.68.16.0/23", "18.68.19.0/24", "18.68.20.0/24", "18.68.64.0/20", "18.68.80.0/24", "18.68.82.0/23", "18.68.130.0/23", "18.68.133.0/24", "18.68.134.0/23", "18.68.136.0/22", "18.88.0.0/18", "18.100.0.0/15", "18.102.0.0/16", "18.116.0.0/14", "18.130.0.0/16", "18.132.0.0/14", "18.136.0.0/16", "18.138.0.0/15", "18.140.0.0/14", "18.144.0.0/15", "18.153.0.0/16", "18.154.30.0/23", "18.154.32.0/20", "18.154.48.0/21", "18.154.56.0/22", "18.154.90.0/23", "18.154.92.0/22", "18.154.96.0/19", "18.154.128.0/20", "18.154.144.0/22", "18.154.148.0/23", "18.154.180.0/22", "18.154.184.0/21", "18.154.192.0/18", "18.155.0.0/21", "18.155.8.0/22", "18.155.12.0/23", "18.155.29.0/24", "18.155.30.0/23", "18.155.32.0/19", "18.155.64.0/21", "18.155.72.0/23", "18.155.89.0/24", "18.155.90.0/23", "18.155.92.0/22", 
                                        "18.155.96.0/19", "18.155.128.0/17", "18.156.0.0/14", "18.160.0.0/18", "18.160.64.0/19", "18.160.96.0/22", "18.160.100.0/23", "18.160.102.0/24", "18.160.133.0/24", "18.160.134.0/23", "18.160.136.0/21", "18.160.144.0/20", "18.160.160.0/19", "18.160.192.0/19", "18.160.224.0/20", "18.160.240.0/21", "18.160.248.0/22", "18.160.252.0/24", "18.161.12.0/22", "18.161.16.0/20", "18.161.32.0/19", "18.161.64.0/21", "18.161.87.0/24", "18.161.88.0/21", "18.161.96.0/19", "18.161.128.0/19", "18.161.160.0/20", "18.161.176.0/24", "18.161.192.0/19", "18.161.224.0/20", "18.161.240.0/21", "18.161.248.0/22", "18.162.0.0/15", "18.164.15.0/24", "18.164.16.0/20", "18.164.32.0/19", "18.164.64.0/18", "18.164.128.0/17", "18.165.0.0/17", "18.165.128.0/22", "18.165.132.0/23", "18.165.149.0/24", "18.165.150.0/23", "18.165.152.0/21", "18.165.160.0/22", "18.165.179.0/24", "18.165.180.0/22", "18.165.184.0/21", "18.165.192.0/20", "18.165.208.0/24", "18.165.225.0/24", "18.165.226.0/23", "18.165.228.0/22", "18.165.232.0/21", "18.165.255.0/24", "18.166.0.0/15", "18.168.0.0/14", "18.172.86.0/23", "18.172.88.0/21", "18.172.96.0/22", "18.172.100.0/24", "18.172.116.0/22", "18.172.120.0/21", "18.172.128.0/19", "18.172.160.0/20", "18.172.206.0/23", "18.172.208.0/20", "18.172.224.0/21", "18.172.232.0/22", "18.172.251.0/24", "18.172.252.0/22", "18.173.0.0/21", "18.173.8.0/23", "18.173.40.0/22", "18.173.44.0/24", "18.173.49.0/24", "18.173.50.0/24", "18.173.55.0/24", "18.173.56.0/23", "18.173.58.0/24", "18.173.62.0/23", "18.173.64.0/23", 
                                        "18.173.70.0/23", "18.173.72.0/23", "18.173.74.0/24", "18.173.76.0/22", "18.173.81.0/24", "18.173.82.0/23", "18.173.84.0/24", "18.173.91.0/24", "18.173.92.0/23", "18.173.95.0/24", "18.173.98.0/23", "18.173.105.0/24", "18.173.106.0/23", "18.175.0.0/16", "18.176.0.0/13", "18.184.0.0/15", "18.188.0.0/14", "18.192.0.0/13", "18.200.0.0/14", "18.216.0.0/13", "18.224.0.0/13", "18.236.0.0/15", "18.238.0.0/21", "18.238.8.0/22", "18.238.12.0/23", "18.238.14.0/24", "18.238.121.0/24", "18.238.122.0/23", "18.238.124.0/22", "18.238.128.0/21", "18.238.161.0/24", "18.238.162.0/23", "18.238.164.0/22", "18.238.168.0/21", "18.238.200.0/23", "18.238.203.0/24", "18.238.204.0/23", "18.238.207.0/24", "18.238.209.0/24", "18.238.211.0/24", "18.238.235.0/24", "18.239.230.0/24", "18.244.111.0/24", "18.244.112.0/21", "18.244.120.0/22", "18.244.124.0/23", "18.244.131.0/24", "18.244.132.0/22", "18.244.136.0/21", "18.244.144.0/23", "18.244.151.0/24", "18.244.152.0/21", "18.244.160.0/22", "18.244.164.0/23", "18.244.171.0/24", "18.244.172.0/22", "18.244.176.0/21", "18.244.184.0/23", "18.244.191.0/24", "18.244.192.0/21", "18.244.200.0/22", "18.244.204.0/23", "18.245.229.0/24", "18.245.251.0/24", "18.246.0.0/16", "18.252.0.0/15", "18.254.0.0/16", "23.92.173.0/24", "23.92.174.0/24", "23.130.160.0/24", "23.131.136.0/24", "23.142.96.0/24", "23.144.82.0/24", "23.156.240.0/24", "23.161.160.0/24", "23.183.112.0/23", "23.191.48.0/24", "23.239.241.0/24", "23.239.243.0/24", "23.249.168.0/24", "23.249.208.0/23", "23.249.215.0/24", 
                                        "23.249.218.0/23", "23.249.220.0/24", "23.249.222.0/23", "23.251.224.0/22", "23.251.232.0/21", "23.251.240.0/21", "23.251.248.0/22", "27.0.0.0/22", "31.171.211.0/24", "31.171.212.0/24", "31.223.192.0/20", "34.208.0.0/12", "34.240.0.0/12", "35.71.64.0/22", "35.71.72.0/22", "35.71.97.0/24", "35.71.100.0/24", "35.71.102.0/24", "35.71.105.0/24", "35.71.106.0/24", "35.71.111.0/24", "35.71.114.0/24", "35.71.118.0/23", "35.71.128.0/17", "35.72.0.0/13", "35.80.0.0/12", 
                                        "35.152.0.0/16", "35.154.0.0/15", "35.156.0.0/14", "35.160.0.0/13", "35.176.0.0/13", "37.221.72.0/22", "43.198.0.0/15", "43.200.0.0/13", "43.218.0.0/16", "43.247.34.0/24", "43.250.192.0/23", "44.224.0.0/11", "45.8.84.0/22", "45.10.57.0/24", "45.11.252.0/23", "45.13.100.0/22", "45.42.136.0/22", "45.42.252.0/22", "45.45.214.0/24", "45.62.90.0/23", "45.88.28.0/22", "45.91.255.0/24", "45.92.116.0/22", "45.93.188.0/24", "45.95.94.0/24", "45.95.209.0/24", "45.112.120.0/22", "45.114.220.0/22", "45.129.53.0/24", "45.129.54.0/23", "45.129.192.0/24", "45.136.241.0/24", "45.136.242.0/24", "45.138.17.0/24", "45.140.152.0/22", "45.143.132.0/24", "45.143.134.0/23", "45.146.156.0/24", "45.149.108.0/22", "45.152.134.0/23", "45.154.18.0/23", "45.155.99.0/24", "45.156.96.0/22", "45.159.120.0/22", "45.159.224.0/22", "45.223.12.0/24", "46.18.245.0/24", "46.19.168.0/23", "46.28.58.0/23", "46.28.63.0/24", "46.51.128.0/18", "46.51.192.0/20", "46.51.216.0/21", "46.51.224.0/19", "46.137.0.0/16", "46.227.40.0/22", "46.227.44.0/23", "46.227.47.0/24", "46.228.136.0/23", "46.255.76.0/24", "47.128.0.0/14", "50.18.0.0/16", "50.112.0.0/16", "50.115.212.0/23", "50.115.218.0/23", "50.115.222.0/23", "51.16.0.0/15", "51.149.8.0/24", "51.149.14.0/24", "51.149.250.0/23", "51.149.252.0/24", "52.8.0.0/13", "52.16.0.0/14", "52.24.0.0/13", "52.32.0.0/13", 
                                        "52.40.0.0/14", "52.46.0.0/21", "52.46.8.0/24", "52.46.25.0/24", "52.46.34.0/23", "52.46.36.0/24", "52.46.43.0/24", "52.46.44.0/24", "52.46.46.0/23", "52.46.48.0/23", "52.46.51.0/24", "52.46.53.0/24", "52.46.54.0/23", "52.46.56.0/23", "52.46.58.0/24", "52.46.61.0/24", "52.46.62.0/23", "52.46.64.0/20", "52.46.80.0/21", "52.46.88.0/22", "52.46.96.0/19", "52.46.128.0/19", "52.46.172.0/22", "52.46.180.0/22", "52.46.184.0/22", "52.46.192.0/19", "52.46.240.0/22", "52.46.249.0/24", "52.47.0.0/16", "52.48.0.0/14", "52.52.0.0/15", "52.56.0.0/14", "52.60.0.0/16", "52.62.0.0/15", "52.64.0.0/14", "52.68.0.0/15", "52.74.0.0/15", "52.76.0.0/14", "52.84.2.0/23", "52.84.4.0/22", "52.84.8.0/21", "52.84.16.0/20", "52.84.32.0/23", "52.84.35.0/24", "52.84.36.0/22", "52.84.40.0/21", "52.84.48.0/21", "52.84.56.0/23", "52.84.58.0/24", "52.84.60.0/22", "52.84.64.0/22", "52.84.68.0/23", "52.84.70.0/24", "52.84.73.0/24", "52.84.74.0/23", "52.84.76.0/22", "52.84.80.0/22", "52.84.84.0/24", "52.84.86.0/23", "52.84.88.0/21", "52.84.96.0/19", "52.84.128.0/22", "52.84.132.0/23", "52.84.134.0/24", "52.84.136.0/21", "52.84.145.0/24", "52.84.146.0/23", "52.84.148.0/22", "52.84.154.0/23", "52.84.156.0/22", "52.84.160.0/19", "52.84.192.0/21", "52.84.212.0/22", "52.84.216.0/23", "52.84.219.0/24", "52.84.220.0/22", "52.84.230.0/23", "52.84.232.0/22", "52.84.243.0/24", "52.84.244.0/22", "52.84.248.0/23", "52.84.251.0/24", "52.84.252.0/22", "52.85.0.0/20", "52.85.22.0/23", "52.85.24.0/21", "52.85.32.0/21", "52.85.40.0/22", "52.85.44.0/24", "52.85.46.0/23", "52.85.48.0/21", "52.85.56.0/22", "52.85.60.0/23", "52.85.63.0/24", "52.85.64.0/19", "52.85.96.0/22", "52.85.101.0/24", "52.85.102.0/23", "52.85.104.0/21", "52.85.112.0/20", "52.85.128.0/19", "52.85.160.0/21", "52.85.169.0/24", "52.85.170.0/23", "52.85.180.0/24", "52.85.183.0/24", "52.85.185.0/24", "52.85.186.0/23", "52.85.188.0/22", "52.85.192.0/19", "52.85.224.0/20", "52.85.240.0/22", "52.85.244.0/24", "52.85.247.0/24", "52.85.248.0/22", 
                                        "52.85.252.0/23", "52.85.254.0/24", "52.88.0.0/15", "52.92.0.0/22", "52.92.16.0/21", "52.92.32.0/21", "52.92.128.0/19", "52.92.160.0/21", "52.92.176.0/21", "52.92.192.0/21", "52.92.208.0/21", "52.92.224.0/21", "52.92.240.0/20", "52.93.110.0/24", "52.94.0.0/21", "52.94.8.0/24", "52.94.10.0/23", "52.94.12.0/22", "52.94.16.0/22", "52.94.20.0/24", "52.94.22.0/23", "52.94.24.0/23", "52.94.28.0/23", "52.94.30.0/24", "52.94.32.0/19", "52.94.64.0/22", "52.94.68.0/23", "52.94.72.0/21", "52.94.80.0/20", "52.94.96.0/20", "52.94.112.0/22", "52.94.120.0/21", "52.94.128.0/20", "52.94.144.0/23", "52.94.146.0/24", "52.94.148.0/22", "52.94.160.0/19", "52.94.204.0/22", "52.94.208.0/20", "52.94.224.0/20", "52.94.240.0/22", "52.94.252.0/22", "52.95.0.0/20", "52.95.16.0/21", "52.95.24.0/22", "52.95.28.0/24", "52.95.30.0/23", "52.95.34.0/23", "52.95.48.0/22", "52.95.56.0/22", "52.95.64.0/19", "52.95.96.0/22", "52.95.104.0/22", 
                                        "52.95.108.0/23", "52.95.111.0/24", "52.95.112.0/20", "52.95.128.0/20", "52.95.144.0/21", "52.95.152.0/22", "52.95.156.0/24", "52.95.160.0/19", "52.95.192.0/20", "52.95.212.0/22", "52.95.224.0/22", "52.95.228.0/23", "52.95.230.0/24", "52.95.235.0/24", "52.95.239.0/24", "52.95.240.0/22", "52.95.244.0/24", "52.95.246.0/23", "52.95.248.0/22", "52.95.252.0/23", "52.95.254.0/24", "52.119.41.0/24", "52.119.128.0/20", "52.119.144.0/21", "52.119.156.0/22", "52.119.160.0/19", "52.119.192.0/21", "52.119.205.0/24", "52.119.206.0/23", "52.119.210.0/23", "52.119.212.0/22", "52.119.216.0/21", "52.119.224.0/21", "52.119.232.0/22", "52.119.240.0/21", "52.119.248.0/23", "52.119.252.0/22", "52.124.130.0/24", "52.124.180.0/24", "52.124.199.0/24", "52.124.215.0/24", "52.124.219.0/24", "52.124.220.0/23", "52.124.225.0/24", "52.124.227.0/24", "52.124.228.0/22", "52.124.232.0/22", "52.124.237.0/24", "52.124.239.0/24", "52.124.240.0/21", "52.124.248.0/23", "52.124.251.0/24", "52.124.252.0/22", "52.128.43.0/24", "52.129.34.0/24", "52.129.64.0/24", "52.129.66.0/24", "52.129.100.0/22", "52.129.104.0/21", "52.144.61.0/24", "52.192.0.0/13", "52.208.0.0/13", "52.216.0.0/18", "52.216.64.0/21", "52.216.72.0/24", "52.216.76.0/22", "52.216.80.0/20", "52.216.96.0/19", "52.216.128.0/18", "52.216.192.0/22", "52.216.200.0/21", "52.216.208.0/20", "52.216.224.0/19", "52.217.0.0/16", "52.218.0.0/21", "52.218.16.0/20", "52.218.32.0/19", "52.218.64.0/22", "52.218.80.0/20", "52.218.96.0/19", "52.218.128.0/24", "52.218.132.0/22", "52.218.136.0/21", "52.218.144.0/24", "52.218.148.0/22", "52.218.152.0/21", "52.218.160.0/24", "52.218.168.0/21", "52.218.176.0/21", "52.218.184.0/22", "52.218.192.0/18", "52.219.0.0/20", "52.219.16.0/22", "52.219.24.0/22", "52.219.32.0/20", "52.219.56.0/21", "52.219.64.0/21", "52.219.72.0/22", "52.219.80.0/20", "52.219.96.0/19", "52.219.128.0/20", "52.219.144.0/22", "52.219.148.0/23", "52.219.152.0/21", "52.219.160.0/23", "52.219.164.0/22", "52.219.168.0/21", 
                                        "52.219.176.0/20", "52.219.192.0/21", "52.219.200.0/24", "52.219.202.0/23", "52.219.204.0/22", "52.219.208.0/22", "52.219.216.0/23", "52.219.218.0/24", "52.220.0.0/15", "52.222.128.0/18", "52.222.192.0/21", "52.222.200.0/22", "52.222.207.0/24", "52.222.211.0/24", "52.222.221.0/24", "52.222.222.0/23", "52.222.224.0/19", "52.223.0.0/17", "54.64.0.0/12", "54.92.0.0/17", "54.93.0.0/16", "54.94.0.0/15", "54.148.0.0/14", "54.153.0.0/16", "54.154.0.0/15", "54.168.0.0/14", "54.176.0.0/14", "54.180.0.0/15", "54.182.0.0/21", "54.182.134.0/23", "54.182.136.0/21", "54.182.144.0/20", "54.182.162.0/23", "54.182.166.0/23", "54.182.171.0/24", "54.182.172.0/22", "54.182.176.0/21", "54.182.184.0/23", "54.182.188.0/23", "54.182.190.0/24", "54.182.195.0/24", "54.182.196.0/22", "54.182.200.0/22", "54.182.205.0/24", "54.182.206.0/23", "54.182.209.0/24", "54.182.211.0/24", "54.182.215.0/24", "54.182.216.0/21", "54.182.224.0/22", "54.182.228.0/23", "54.182.235.0/24", "54.182.240.0/23", "54.182.246.0/23", "54.182.248.0/22", "54.182.252.0/23", "54.182.254.0/24", "54.183.0.0/16", "54.184.0.0/13", "54.192.0.0/21", "54.192.8.0/22", "54.192.13.0/24", "54.192.14.0/23", "54.192.16.0/21", "54.192.28.0/22", "54.192.32.0/21", "54.192.41.0/24", "54.192.42.0/23", "54.192.48.0/20", "54.192.64.0/18", "54.192.128.0/22", "54.192.136.0/22", "54.192.144.0/22", 
                                        "54.192.152.0/21", "54.192.160.0/20", "54.192.177.0/24", "54.192.178.0/23", "54.192.180.0/22", "54.192.184.0/23", "54.192.187.0/24", "54.192.188.0/23", "54.192.191.0/24", "54.192.192.0/21", "54.192.200.0/24", 
                                        "54.192.202.0/23", "54.192.204.0/22", "54.192.208.0/22", "54.192.216.0/21", "54.192.224.0/20", "54.192.248.0/21", "54.193.0.0/16", "54.194.0.0/15", "54.199.0.0/16", "54.200.0.0/14", "54.206.0.0/15", "54.212.0.0/14", "54.216.0.0/14", "54.220.0.0/16", "54.228.0.0/15", "54.230.0.0/22", "54.230.6.0/23", "54.230.8.0/21", "54.230.16.0/21", "54.230.28.0/22", "54.230.32.0/21", "54.230.40.0/22", "54.230.48.0/20", "54.230.64.0/22", "54.230.72.0/21", "54.230.80.0/20", "54.230.96.0/22", "54.230.100.0/24", "54.230.102.0/23", "54.230.104.0/21", "54.230.112.0/20", "54.230.129.0/24", "54.230.130.0/24", "54.230.136.0/22", "54.230.144.0/22", "54.230.152.0/23", "54.230.155.0/24", "54.230.156.0/22", "54.230.160.0/20", "54.230.176.0/21", "54.230.184.0/22", "54.230.188.0/23", "54.230.190.0/24", "54.230.192.0/20", "54.230.208.0/22", "54.230.216.0/21", "54.230.224.0/19", "54.231.0.0/24", "54.231.10.0/23", "54.231.16.0/22", "54.231.32.0/22", "54.231.36.0/24", "54.231.40.0/21", "54.231.48.0/20", "54.231.72.0/21", "54.231.80.0/21", "54.231.88.0/24", "54.231.96.0/19", "54.231.128.0/17", "54.232.0.0/15", "54.238.0.0/16", "54.239.2.0/23", "54.239.4.0/22", "54.239.8.0/21", "54.239.16.0/20", "54.239.32.0/21", "54.239.48.0/20", "54.239.64.0/21", "54.239.96.0/24", "54.239.98.0/23", "54.239.108.0/22", "54.239.113.0/24", "54.239.116.0/22", "54.239.120.0/21"],)
            elif group_choice == '5':  
                ip_or_domain_list.extend(["144.81.144.0/21", "144.81.152.0/24", "144.220.1.0/24", "144.220.2.0/23", "144.220.4.0/23", "144.220.11.0/24", "144.220.12.0/22", "144.220.16.0/21", "144.220.26.0/24", "144.220.28.0/23", "144.220.31.0/24", "144.220.37.0/24", "144.220.38.0/24", "144.220.40.0/24", "144.220.49.0/24", "144.220.50.0/23", "144.220.52.0/24", "144.220.55.0/24", "144.220.56.0/24", "144.220.59.0/24", "144.220.60.0/22", "144.220.64.0/22", "144.220.68.0/23", "144.220.72.0/22", "144.220.76.0/24", "144.220.78.0/23", "144.220.80.0/23", "144.220.82.0/24", "144.220.84.0/24", "144.220.86.0/23", "144.220.90.0/24", "144.220.92.0/23", "144.220.94.0/24", "144.220.99.0/24", "144.220.100.0/23", "144.220.103.0/24", "144.220.104.0/21", "144.220.113.0/24", "144.220.114.0/23", "144.220.116.0/23", "144.220.119.0/24", "144.220.120.0/23", "144.220.122.0/24", "144.220.125.0/24", "144.220.126.0/23", "144.220.128.0/21", "144.220.136.0/22", "144.220.140.0/23", "144.220.143.0/24", "146.66.3.0/24", "146.133.124.0/24", "146.133.127.0/24", "147.124.160.0/22", "147.124.164.0/23", "147.160.133.0/24", "147.189.18.0/23", "148.5.64.0/24", "148.5.74.0/24", "148.5.76.0/23", "148.5.80.0/24", "148.5.84.0/24", "148.5.86.0/23", "148.5.88.0/24", "148.5.93.0/24", "148.5.95.0/24", "148.163.131.0/24", "149.19.6.0/24", "149.20.11.0/24", "150.242.68.0/24", "151.148.32.0/22", "151.148.37.0/24", "151.148.38.0/23", "151.148.40.0/23", "152.129.248.0/23", "152.129.250.0/24", "155.46.191.0/24", "155.46.192.0/23", "155.46.195.0/24", "155.46.196.0/23", "155.46.212.0/24", "155.63.85.0/24", "155.63.86.0/24", "155.63.90.0/23", "155.63.208.0/23", "155.63.210.0/24", "155.63.213.0/24", "155.63.215.0/24", "155.63.216.0/23", "155.63.221.0/24", "155.63.222.0/23", "155.226.224.0/20", "155.226.254.0/24", "156.70.116.0/24", "157.53.255.0/24", "157.84.32.0/23", "157.84.40.0/23", "157.166.132.0/22", "157.166.212.0/24", "157.167.134.0/23", "157.167.136.0/21", "157.167.144.0/21", "157.167.152.0/23", "157.167.155.0/24", "157.167.156.0/24", "157.167.225.0/24", "157.167.226.0/23", "157.167.228.0/22", "157.167.232.0/23", "157.175.0.0/16", "157.241.0.0/16", "157.248.214.0/23", "157.248.216.0/22", "158.51.9.0/24", "158.51.65.0/24", "158.115.133.0/24", "158.115.141.0/24", "158.115.147.0/24", "158.115.151.0/24", "158.115.156.0/24", "159.60.0.0/20", 
                                        "159.60.192.0/19", "159.60.224.0/20", "159.60.240.0/21", "159.60.248.0/22", "159.112.232.0/24", "159.140.140.0/23", "159.140.144.0/24", "159.148.136.0/23", "160.202.21.0/24", "160.202.22.0/24", "161.38.196.0/22", "161.38.200.0/21", "161.69.8.0/21", "161.69.58.0/24", "161.69.75.0/24", "161.69.76.0/22", "161.69.94.0/23", "161.69.100.0/22", "161.69.105.0/24", "161.69.106.0/23", "161.69.109.0/24", "161.69.110.0/23", "161.69.124.0/24", "161.69.126.0/23", "161.129.19.0/24", "185.206.120.0/24", "161.188.128.0/20", "161.188.144.0/22", "161.188.148.0/23", "161.188.152.0/22", "161.188.158.0/23", "161.188.160.0/23", 
                                        "161.188.205.0/24", "161.199.67.0/24", "162.33.124.0/23", "162.33.126.0/24", "162.136.61.0/24", "162.212.32.0/24", "162.213.126.0/24", "162.213.205.0/24", "162.218.159.0/24", "162.219.9.0/24", "162.219.11.0/24", "162.219.12.0/24", "162.221.182.0/23", "162.247.163.0/24", "162.248.24.0/24", "162.249.117.0/24", "162.250.61.0/24", "162.250.63.0/24", "163.123.173.0/24", "163.123.174.0/24", "163.253.47.0/24", "164.55.233.0/24", "164.55.235.0/24", "164.55.236.0/23", "164.55.240.0/23", "164.55.243.0/24", "164.55.244.0/24", "164.55.255.0/24", "164.152.64.0/24", "164.153.130.0/23", "164.153.132.0/23", "164.153.134.0/24", "165.1.160.0/21", "165.1.168.0/23", "165.69.249.0/24", "165.84.210.0/24", "165.140.171.0/24", "165.225.100.0/23", "165.225.126.0/24", "167.88.51.0/24", "185.206.228.0/24", "168.87.180.0/22", "168.100.27.0/24", "168.100.65.0/24", "168.100.67.0/24", "168.100.68.0/22", "168.100.72.0/22", "168.100.76.0/23", "168.100.79.0/24", "168.100.80.0/21", "168.100.88.0/22", "168.100.93.0/24", "168.100.94.0/23", "168.100.97.0/24", "168.100.98.0/23", "168.100.100.0/22", "168.100.104.0/24", "168.100.107.0/24", "168.100.108.0/22", "168.100.113.0/24", "168.100.114.0/23", "168.100.116.0/22", "168.100.122.0/23", "168.100.164.0/24", "168.100.168.0/24", "168.149.242.0/23", "168.149.244.0/23", "168.149.247.0/24", "168.203.6.0/23", "168.238.100.0/24", 
                                        "169.150.104.0/24", "169.150.106.0/24", "169.150.108.0/22", "170.39.131.0/24", "170.39.141.0/24", "170.72.226.0/24", "170.72.228.0/22", "170.72.232.0/24", "170.72.234.0/23", "170.72.236.0/22", "170.72.240.0/22", "170.72.244.0/23", "170.72.252.0/22", "170.89.128.0/22", "170.89.132.0/23", "170.89.134.0/24", "170.89.136.0/22", "170.89.141.0/24", "170.89.144.0/24", "170.89.146.0/23", "170.89.149.0/24", "170.89.150.0/24", "170.89.152.0/23", "170.89.156.0/22", "170.89.160.0/24", "170.89.164.0/24", "170.89.173.0/24", "170.89.176.0/24", "170.89.178.0/24", "170.89.181.0/24", "170.89.182.0/23", "170.89.184.0/24", "170.89.189.0/24", "170.89.190.0/23", "170.114.16.0/20", "170.114.34.0/23", "170.114.37.0/24", "170.114.38.0/24", "170.114.40.0/23", "170.114.42.0/24", "170.114.44.0/24", "170.114.49.0/24", "170.114.53.0/24", "170.176.129.0/24", "170.176.135.0/24", "170.176.153.0/24", "170.176.154.0/24", "170.176.156.0/24", "170.176.158.0/24", "170.176.160.0/24", "170.176.200.0/24", "170.176.212.0/22", "170.176.216.0/23", "170.176.218.0/24", "170.176.220.0/22", "170.200.94.0/24", "172.86.224.0/24", "172.99.250.0/24", "173.199.36.0/23", "173.199.38.0/24", "173.199.56.0/23", "173.231.88.0/22", "173.240.165.0/24", "173.241.39.0/24", "173.241.44.0/23", "173.241.46.0/24", "173.241.82.0/24", "173.241.87.0/24", "173.241.94.0/24", "173.249.168.0/22", "174.34.225.0/24", "175.29.224.0/19", "175.41.128.0/17", "176.32.64.0/19", "176.32.96.0/20", "176.32.112.0/21", "176.32.120.0/22", "176.32.126.0/23", "176.34.0.0/16", "176.110.104.0/24", "176.116.14.0/24", "176.116.21.0/24", "176.124.224.0/24", "176.221.80.0/24", "176.221.82.0/23", "177.71.128.0/17", "177.72.240.0/21", "178.21.147.0/24", "178.21.148.0/24", "185.207.135.0/24", "178.213.75.0/24", 
                                        "178.236.0.0/20", "178.239.128.0/23", "178.239.130.0/24", "179.0.17.0/24", "182.54.135.0/24", "184.72.0.0/18", "184.94.214.0/24", "184.169.128.0/17", "185.7.73.0/24", "185.20.4.0/24", "185.31.204.0/22", "185.36.216.0/22", "185.37.37.0/24", "185.37.39.0/24", "185.38.134.0/24", "185.39.10.0/24", "185.43.192.0/22", "185.44.176.0/24", "185.48.120.0/22", 
                                        "185.49.132.0/23", "185.53.16.0/22", "185.54.72.0/22", "185.54.124.0/24", "185.54.126.0/24", "185.55.188.0/24", "185.55.190.0/23", "185.57.216.0/24", "185.57.218.0/24", "185.64.6.0/24", "185.64.73.0/24", "185.66.202.0/23", "185.68.58.0/23", "185.69.1.0/24", "185.75.61.0/24", "185.75.62.0/23", "185.79.75.0/24", "185.83.20.0/22", "185.88.184.0/23", "185.88.186.0/24", "185.95.174.0/24", "185.97.10.0/24", "185.98.156.0/24", "185.98.159.0/24", "185.107.197.0/24", "185.109.132.0/22", "185.118.109.0/24", "185.119.223.0/24", "185.120.172.0/22", "185.121.140.0/23", "185.121.143.0/24", "185.122.214.0/24", "185.127.28.0/24", "185.129.16.0/23", "185.133.70.0/24", "185.134.79.0/24", "185.135.128.0/24", "185.137.156.0/24", "185.143.16.0/24", "185.143.236.0/24", "185.144.16.0/24", "185.144.18.0/23", "185.144.236.0/24", "185.145.38.0/24", "185.146.155.0/24", "185.150.179.0/24", "185.151.47.0/24", 
                                        "185.166.140.0/22", "185.169.27.0/24", "185.170.188.0/23", "185.172.153.0/24", "185.172.155.0/24", "185.175.91.0/24", "185.186.212.0/24", "185.187.116.0/22", "185.195.0.0/22", "185.195.148.0/24", "185.210.156.0/24", "185.212.105.0/24", "185.212.113.0/24", "185.214.22.0/23", "185.215.115.0/24", "185.219.146.0/23", "185.221.84.0/24", "185.225.252.0/24", "185.225.254.0/23", "185.226.166.0/24", "185.232.99.0/24", "185.235.38.0/24", "185.236.142.0/24", "185.237.5.0/24", "185.237.6.0/23", "185.253.9.0/24", "185.255.32.0/22", "185.255.54.0/24", "188.72.93.0/24", "188.95.140.0/23", "188.95.142.0/24", "188.116.35.0/24", "188.172.137.0/24", "188.172.138.0/24", "188.209.136.0/22", "188.241.223.0/24", "188.253.16.0/20", "191.101.94.0/24", "191.101.242.0/24", "192.35.158.0/24", "192.42.69.0/24", "192.64.71.0/24", "192.71.84.0/24", "192.71.255.0/24", "192.80.240.0/24", "192.80.242.0/24", "192.80.244.0/24", "192.81.98.0/24", "192.84.23.0/24", "192.84.38.0/24", "192.84.231.0/24", "192.101.70.0/24", "192.111.5.0/24", "192.111.6.0/24", "192.118.71.0/24", "192.132.1.0/24", "192.151.28.0/23", "192.152.132.0/23", "192.153.76.0/24", "192.161.151.0/24", "192.161.152.0/24", "192.161.157.0/24", "192.175.1.0/24", "192.175.3.0/24", "192.175.4.0/24", "192.184.67.0/24", "192.184.69.0/24", "192.184.70.0/23", "192.190.135.0/24", "192.190.153.0/24", "192.197.207.0/24", "192.206.0.0/24", "192.206.146.0/23", "192.206.206.0/23", "192.210.30.0/23", "192.225.99.0/24", "192.230.237.0/24", "192.245.195.0/24", "193.0.181.0/24", "193.3.28.0/24", "193.3.160.0/24", "193.9.122.0/24", "193.16.22.0/24", "193.17.68.0/24", "193.24.42.0/23", "193.25.48.0/24", "193.25.51.0/24", "193.25.52.0/23", "193.25.54.0/24", "193.25.60.0/22", "193.30.161.0/24", "193.31.111.0/24", "193.33.137.0/24", "193.35.157.0/24", "193.37.39.0/24", "193.37.132.0/24", "193.39.114.0/24", "193.47.187.0/24", "193.57.172.0/24", "193.84.26.0/24", "193.100.64.0/24", "193.104.169.0/24", "193.105.212.0/24", "193.107.65.0/24", "193.110.146.0/24", "193.111.200.0/24", "193.131.114.0/23", "193.138.90.0/24", "193.150.164.0/24", "193.151.92.0/24", "193.151.94.0/24", "193.160.155.0/24", "193.176.54.0/24", "193.200.30.0/24", "193.200.156.0/24", "193.207.0.0/24", "193.219.118.0/24", "193.221.125.0/24", "193.227.82.0/24", "193.234.120.0/22", "193.239.162.0/23", "193.239.236.0/24", "193.243.129.0/24", "194.5.67.0/24", "194.5.147.0/24", "194.29.54.0/24", "194.29.58.0/24", 
                                        "194.30.175.0/24", "194.33.184.0/24", "194.42.96.0/23", "194.42.104.0/23", "194.53.200.0/24", "194.99.96.0/23", "194.104.235.0/24", "194.140.230.0/24", "194.165.43.0/24", "194.176.117.0/24", "194.195.101.0/24", "194.230.56.0/24", "194.247.26.0/23", "195.8.103.0/24", "195.42.240.0/24", "195.46.38.0/24", "195.60.86.0/24", "195.69.163.0/24", "195.74.60.0/24", "195.82.97.0/24", "195.85.12.0/24", "195.88.213.0/24", "195.88.246.0/24", "195.93.178.0/24", "195.191.165.0/24", "195.200.230.0/23", "195.234.155.0/24", "195.244.28.0/24", "195.245.230.0/23", "198.99.2.0/24", "198.137.150.0/24", "198.154.180.0/23", "198.160.151.0/24", "198.169.0.0/24", "198.176.120.0/23", "198.176.123.0/24", "198.176.124.0/23", "198.176.126.0/24", "198.183.226.0/24", "198.202.176.0/24", "198.204.13.0/24", "198.207.147.0/24", "198.212.50.0/24", "198.251.128.0/18", "198.251.192.0/19", "198.251.224.0/21", "199.43.186.0/24", "199.47.130.0/23", "199.59.243.0/24", "199.65.20.0/22", "199.65.24.0/23", "199.65.26.0/24", "199.65.242.0/24", "199.65.245.0/24", "199.65.246.0/24", "199.65.249.0/24", "199.65.250.0/24", "199.65.252.0/23", "199.68.157.0/24", "199.85.125.0/24", "199.87.145.0/24", "199.91.52.0/23", "199.115.200.0/24", "199.127.232.0/22", 
                                        "199.165.143.0/24", "199.187.168.0/22", "199.192.13.0/24", "199.196.235.0/24", "199.250.16.0/24", "199.255.32.0/24", "199.255.192.0/22", "199.255.240.0/24", "202.8.25.0/24", "202.44.120.0/23", "202.44.127.0/24", "202.45.131.0/24", "202.50.194.0/24", "202.52.43.0/24", "202.92.192.0/23", "202.93.249.0/24", "202.128.99.0/24", "202.160.113.0/24", "202.160.115.0/24", "202.160.117.0/24", "202.160.119.0/24", "202.173.24.0/24", "202.173.26.0/23", "202.173.31.0/24", "203.12.218.0/24", "203.20.242.0/23", "203.27.115.0/24", "203.27.226.0/23", "203.55.215.0/24", "203.57.88.0/24", "203.83.220.0/22", "203.175.1.0/24", "203.175.2.0/23", "203.210.75.0/24", "204.10.96.0/21", "204.11.174.0/23", "204.15.172.0/24", "204.15.215.0/24", "204.27.244.0/24", "204.48.63.0/24", "204.77.168.0/24", "204.90.106.0/24", "204.110.220.0/23", "204.110.223.0/24", "204.154.231.0/24", "204.236.128.0/18", "204.239.0.0/24", "204.246.160.0/22", "204.246.166.0/24", "204.246.169.0/24", "204.246.175.0/24", "204.246.177.0/24", "204.246.178.0/24", "204.246.180.0/23", "204.246.182.0/24", "204.246.187.0/24", "204.246.188.0/22", "205.147.81.0/24", "205.157.218.0/23", "205.166.195.0/24", "205.201.44.0/23", "205.220.188.0/24", "205.235.121.0/24", "205.251.192.0/21",
                                        "205.251.200.0/24", "205.251.203.0/24", "205.251.206.0/23", "205.251.212.0/23", "205.251.216.0/24", "205.251.218.0/23", "205.251.222.0/23", "205.251.224.0/21", "205.251.232.0/22", "205.251.240.0/22", "205.251.244.0/23", "205.251.247.0/24", "205.251.248.0/23", "205.251.251.0/24", "205.251.253.0/24", "206.108.41.0/24", "206.130.88.0/23", "206.166.248.0/23", "206.195.217.0/24", "206.195.218.0/24", "206.195.220.0/24", "206.198.37.0/24", "206.198.131.0/24", "206.225.200.0/23", "206.225.203.0/24", "206.225.217.0/24", "206.225.219.0/24", "207.2.117.0/24", "207.2.118.0/23", "207.34.11.0/24", "207.45.79.0/24", "207.90.252.0/23", "207.167.92.0/22", "207.167.126.0/23", "207.171.160.0/19", "207.189.185.0/24", "207.202.17.0/24", "207.202.18.0/24", "207.202.20.0/24", "207.207.176.0/22", "207.230.151.0/24", "207.230.156.0/24", "208.56.44.0/23", "208.56.47.0/24", "208.56.48.0/20", "208.71.22.0/24", "208.71.106.0/24", "208.71.210.0/24", "208.71.245.0/24", "208.73.7.0/24", "208.81.250.0/24", "208.82.220.0/22", "208.89.247.0/24", "208.90.238.0/24", "208.91.36.0/23", "208.95.53.0/24", "208.127.200.0/21", "209.51.32.0/21", "209.54.160.0/19", "209.94.75.0/24", "209.126.65.0/24", "209.127.220.0/24", "209.160.100.0/22", "209.163.96.0/24", "209.169.228.0/24", "209.169.242.0/24", "209.182.220.0/24", "209.222.82.0/24", "211.44.103.0/24", "212.4.240.0/22", "212.8.241.0/24", "212.19.235.0/24", "212.19.236.0/24", "212.104.208.0/24", "212.192.221.0/24", "213.5.226.0/24", "213.109.176.0/22", "213.170.156.0/24", 
                                        "213.170.158.0/24", "213.217.29.0/24", "216.9.204.0/24", "216.24.45.0/24", "216.73.153.0/24", "216.73.154.0/23", "216.74.122.0/24", "216.75.96.0/22", "216.75.104.0/21", "216.99.220.0/24", "216.115.17.0/24", "216.115.20.0/24", "216.115.23.0/24", "216.120.142.0/24", "216.120.187.0/24", "216.122.176.0/22", "216.137.32.0/24", "216.137.34.0/23", "216.137.36.0/22", "216.137.40.0/21", "216.137.48.0/21", "216.137.56.0/23", "216.137.58.0/24", "216.137.60.0/23", "216.137.63.0/24", "216.147.0.0/23", "216.147.3.0/24", "216.147.4.0/22", "216.147.9.0/24", "216.147.10.0/23", "216.147.12.0/23", "216.147.15.0/24", "216.147.16.0/23", "216.147.19.0/24", "216.147.20.0/23", "216.147.23.0/24", "216.147.24.0/22", "216.147.29.0/24", "216.147.30.0/23", "216.147.32.0/23", "216.157.133.0/24", "216.157.139.0/24", "216.169.145.0/24", "216.170.100.0/24", "216.182.236.0/23", "216.198.2.0/23", "216.198.17.0/24", 
                                        "216.198.18.0/24", "216.198.33.0/24", "216.198.34.0/23", "216.198.36.0/24", "216.198.49.0/24", "216.211.162.0/24", "216.219.113.0/24", "216.238.188.0/23", "216.238.190.0/24", "216.241.208.0/20", "217.8.118.0/24", "217.117.65.0/24", "217.117.71.0/24", "217.117.76.0/24", "217.119.96.0/24", "217.119.98.0/24", "217.119.104.0/23", "217.169.73.0/24", "218.33.0.0/18" ],)
            elif group_choice == '6':  
                ip_or_domain_list.extend(["54.239.130.0/23", "54.239.132.0/23", "54.239.135.0/24", "54.239.142.0/23", "54.239.152.0/23", "54.239.158.0/23", "54.239.162.0/23", "54.239.164.0/23", "54.239.168.0/23", "54.239.171.0/24", "54.239.172.0/24", "54.239.174.0/23", "54.239.180.0/23", "54.239.186.0/24", "54.239.192.0/24", "54.239.195.0/24", "54.239.200.0/24", "54.239.204.0/22", "54.239.208.0/21", "54.239.216.0/23", "54.239.219.0/24", "54.239.220.0/23", "54.239.223.0/24", "54.240.0.0/21", "54.240.16.0/24", "54.240.24.0/22", "54.240.50.0/23", "54.240.52.0/22", "54.240.56.0/21", "54.240.80.0/20", "54.240.96.0/20", "54.240.112.0/21", "54.240.129.0/24", "54.240.130.0/23", "54.240.160.0/23", "54.240.166.0/23", "54.240.168.0/21", "54.240.184.0/21", "54.240.192.0/21", "54.240.200.0/24", "54.240.202.0/24", "54.240.204.0/22", "54.240.208.0/20", "54.240.225.0/24", "54.240.226.0/23", "54.240.228.0/22", "54.240.232.0/22", "54.240.244.0/22", "54.240.248.0/21", "54.241.0.0/16", "54.244.0.0/14", "54.248.0.0/13", "57.180.0.0/14", "58.181.95.0/24", "62.133.34.0/24", "63.32.0.0/14", "63.140.32.0/22", "63.140.36.0/23", "63.140.48.0/22", "63.140.52.0/24", "63.140.55.0/24", "63.140.56.0/23", "63.140.61.0/24", "63.140.62.0/23", "63.246.112.0/24", "64.35.162.0/24", "64.45.129.0/24", "64.45.130.0/23", "64.52.111.0/24", "64.56.212.0/24", "64.65.61.0/24", "64.69.212.0/24", "64.69.223.0/24", "64.186.3.0/24", "64.187.128.0/20", "64.190.110.0/24", "64.190.237.0/24", "64.207.194.0/24", "64.207.196.0/24", "64.207.198.0/23", "64.207.204.0/23", "64.234.115.0/24", "64.238.2.0/24", "64.238.5.0/24", "64.238.6.0/24", "64.238.14.0/24", "64.252.65.0/24", "64.252.70.0/23", "64.252.72.0/21", "64.252.80.0/21", "64.252.88.0/23", "64.252.98.0/23", "64.252.100.0/22", "64.252.104.0/21", "64.252.112.0/23", "64.252.114.0/24", "64.252.118.0/23", "64.252.120.0/22", "64.252.124.0/24", "64.252.129.0/24", "64.252.130.0/23", "64.252.132.0/22", "64.252.136.0/21", "64.252.144.0/23", "64.252.147.0/24", "64.252.148.0/23", "64.252.151.0/24", "64.252.152.0/24", "64.252.154.0/23", "64.252.156.0/24", "64.252.159.0/24", "64.252.161.0/24", "64.252.162.0/23", "64.252.164.0/24", "64.252.166.0/23", "64.252.168.0/22", "64.252.172.0/23", "64.252.175.0/24", "64.252.176.0/22", "64.252.180.0/24", "64.252.182.0/23", "64.252.185.0/24", "64.252.186.0/23", "64.252.188.0/23", "64.252.190.0/24", "65.0.0.0/14", "65.8.0.0/23", "65.8.2.0/24", "65.8.4.0/22", "65.8.8.0/23", "65.8.11.0/24", "65.8.12.0/24", "65.8.14.0/23", "65.8.16.0/20", "65.8.32.0/19", "65.8.64.0/20", "65.8.80.0/21", "65.8.88.0/22", "65.8.92.0/23", "65.8.94.0/24", "65.8.96.0/20", "65.8.112.0/21", "65.8.120.0/22", "65.8.124.0/23", "65.8.129.0/24", "65.8.130.0/23", "65.8.132.0/22", "65.8.136.0/22", "65.8.140.0/23", "65.8.142.0/24", "65.8.146.0/23", "65.8.148.0/23", "65.8.150.0/24", "65.8.152.0/23", "65.8.154.0/24", "65.8.158.0/23", "65.8.160.0/19", "65.8.192.0/18", "65.9.4.0/24", "65.9.6.0/23", "65.9.9.0/24", "65.9.11.0/24", "65.9.14.0/23", "65.9.17.0/24", "65.9.19.0/24", "65.9.20.0/22", "65.9.24.0/21", "65.9.32.0/19", "65.9.64.0/19", "65.9.96.0/20", "65.9.112.0/23", "65.9.129.0/24", "65.9.130.0/23", "65.9.132.0/22", "65.9.136.0/21", "65.9.144.0/20", "65.9.160.0/19", "65.20.48.0/24", "65.37.240.0/24", "65.110.52.0/23", "65.110.54.0/24", "66.22.176.0/24", "66.22.190.0/24", "66.37.128.0/24", "66.51.208.0/24", "66.51.210.0/23", "66.51.212.0/22", "66.51.216.0/23", "66.54.74.0/23", "66.81.8.0/24", "66.81.227.0/24", "66.81.241.0/24", "66.117.20.0/24", "66.117.22.0/23", "66.117.24.0/23", "66.117.26.0/24", "66.117.30.0/23", "66.129.247.0/24", "66.129.248.0/24", "66.159.226.0/24", "66.159.230.0/24", "66.178.130.0/24", "66.178.132.0/23", "66.178.134.0/24", "66.178.136.0/23", "66.178.139.0/24", "66.182.132.0/23", "66.187.204.0/23", "66.206.173.0/24", "66.232.20.0/23", "66.235.151.0/24", "66.235.152.0/22", "67.20.60.0/24", "67.199.239.0/24", "67.219.241.0/24", "67.219.247.0/24", "67.219.250.0/24", "67.220.224.0/19", "67.221.38.0/24", "67.222.249.0/24", "67.222.254.0/24", "67.226.222.0/23", "68.64.5.0/24", "68.66.112.0/20", "68.70.127.0/24", "69.10.24.0/24", "69.58.24.0/24", "69.59.247.0/24", "69.59.248.0/24", "69.59.250.0/23", "69.64.150.0/24", "69.64.152.0/24", "69.72.44.0/22", "69.80.226.0/23", "69.94.8.0/23", "69.166.42.0/24", "69.169.224.0/20", "70.132.0.0/20", "70.132.16.0/22", "70.132.20.0/23", "70.132.23.0/24", "70.132.24.0/23", "70.132.27.0/24", "70.132.28.0/22", "70.132.32.0/21", "70.132.40.0/24", "70.132.42.0/23", "70.132.44.0/24", "70.132.46.0/24", "70.132.48.0/22", "70.132.52.0/23", "70.132.55.0/24", "70.132.58.0/23", "70.132.60.0/22", "70.224.192.0/18", "70.232.64.0/20", "70.232.80.0/21", "70.232.88.0/22", "70.232.96.0/20", "70.232.112.0/21", "70.232.120.0/22", "71.141.0.0/21", "71.152.0.0/22", "71.152.4.0/23", "71.152.7.0/24", "71.152.8.0/24", "71.152.10.0/23", "71.152.13.0/24", "71.152.14.0/23", "71.152.16.0/21", "71.152.24.0/22", 
                                        "71.152.28.0/24", "71.152.30.0/23", "71.152.33.0/24", "71.152.35.0/24", "71.152.36.0/22", "71.152.40.0/23", "71.152.43.0/24", "71.152.46.0/23", "71.152.48.0/22", "71.152.53.0/24", "71.152.55.0/24", "71.152.56.0/22", "71.152.61.0/24", "71.152.62.0/23", "71.152.64.0/21", "71.152.72.0/22", "71.152.76.0/23", "71.152.79.0/24", "71.152.80.0/21", "71.152.88.0/22", "71.152.92.0/24", "71.152.94.0/23", "71.152.96.0/22", "71.152.100.0/24", "71.152.102.0/23", "71.152.105.0/24", "71.152.106.0/23", "71.152.108.0/23", "71.152.110.0/24", "71.152.112.0/21", "71.152.122.0/23", "71.152.124.0/24", "71.152.126.0/23", "72.1.32.0/21", "72.13.121.0/24", "72.13.124.0/24", "72.18.76.0/23", "72.18.222.0/24", "72.21.192.0/19", "72.41.0.0/20", "72.46.77.0/24", "72.167.168.0/24", "74.80.247.0/24", "74.116.145.0/24", "74.116.147.0/24", "74.117.148.0/24", "74.118.105.0/24", "74.118.106.0/23", "74.200.120.0/24", "74.221.129.0/24", "74.221.130.0/24", "74.221.133.0/24", "74.221.135.0/24", "74.221.137.0/24", "74.221.139.0/24", "74.221.141.0/24", "75.2.0.0/17", "75.104.19.0/24", "76.76.17.0/24", "76.76.19.0/24", "76.76.21.0/24", "76.223.0.0/17", "76.223.128.0/22", "76.223.132.0/23", "76.223.160.0/22", "76.223.164.0/23", "76.223.166.0/24", "76.223.172.0/22", "76.223.176.0/21", "76.223.184.0/22", "76.223.188.0/23", "76.223.190.0/24", "77.73.208.0/23", "78.108.124.0/23", "79.125.0.0/17", "79.143.156.0/24", "80.210.95.0/24", "81.20.41.0/24", "81.90.143.0/24", "82.145.126.0/24", "82.192.96.0/23", "82.192.100.0/23", "82.192.108.0/23", "83.97.100.0/22", "83.137.245.0/24", "83.147.240.0/22", "83.151.192.0/23", "83.151.194.0/24", "84.254.134.0/24", "85.92.101.0/24", "85.113.84.0/24", "85.113.88.0/24", "85.158.142.0/24", "85.194.254.0/23", "85.236.136.0/21", "87.236.67.0/24", "87.238.80.0/21", "87.238.140.0/24", "88.202.208.0/23", "88.202.210.0/24", "88.212.156.0/22", "89.37.140.0/24", "89.116.141.0/24", "89.116.244.0/24", "89.117.129.0/24", "89.251.12.0/24", "91.102.186.0/24", "91.193.42.0/24", "91.194.25.0/24", "91.194.104.0/24", "91.198.107.0/24", "91.198.117.0/24", "91.207.12.0/23", "91.208.21.0/24", "91.209.81.0/24", "91.213.115.0/24", "91.213.126.0/24", "91.213.146.0/24", "91.218.37.0/24", "91.223.161.0/24", "91.227.75.0/24", "91.228.72.0/24", "91.228.74.0/24", "91.230.237.0/24", "91.231.35.0/24", "91.233.61.0/24", "91.233.120.0/24", "91.236.18.0/24", "91.236.66.0/24", "91.237.174.0/24", "91.240.18.0/23", "91.241.6.0/23", "93.93.224.0/22", "93.94.3.0/24", "93.191.148.0/23", "93.191.219.0/24", "94.124.112.0/24", "94.140.18.0/24", "94.142.252.0/24", "95.82.16.0/20", "95.130.184.0/23", "96.0.0.0/18", "96.0.64.0/21", "96.0.84.0/22", "96.0.88.0/22", "96.0.92.0/23", "96.0.96.0/22", "96.0.100.0/23", "96.0.104.0/22", "96.9.221.0/24", "98.97.248.0/22", "98.97.253.0/24", "98.97.254.0/23", "98.142.155.0/24", "99.77.0.0/18", "99.77.130.0/23", "99.77.132.0/22", "99.77.136.0/21", "99.77.144.0/23", "99.77.147.0/24", "99.77.148.0/23", "99.77.150.0/24", "99.77.152.0/21", "99.77.160.0/23", "99.77.183.0/24", "99.77.186.0/24", "99.77.188.0/23", "99.77.190.0/24", "99.77.233.0/24", "99.77.234.0/23", "99.77.238.0/23", "99.77.240.0/24", "99.77.242.0/24", "99.77.244.0/22", "99.77.248.0/22", "99.77.252.0/23", "99.78.128.0/19", "99.78.160.0/21", "99.78.168.0/22", "99.78.172.0/24", "99.78.176.0/21", "99.78.192.0/18", "99.79.0.0/16", "99.80.0.0/15", "99.82.128.0/19", "99.82.160.0/20", "99.82.184.0/21", "99.83.72.0/21", "99.83.80.0/21", "99.83.96.0/22", "99.83.100.0/23", "99.83.102.0/24", "99.83.120.0/22", "99.83.128.0/17", "99.84.0.0/19", "99.84.32.0/20", "99.84.48.0/24", "99.84.50.0/23", "99.84.52.0/22", "99.84.56.0/21", "99.84.64.0/18", "99.84.128.0/24", "99.84.130.0/23", "99.84.132.0/22", "99.84.136.0/21", "99.84.144.0/20", "99.84.160.0/19", "99.84.192.0/18", "99.86.0.0/17", "99.86.128.0/21", "99.86.136.0/24", "99.86.144.0/21", "99.86.153.0/24", "99.86.154.0/23", "99.86.156.0/22", "99.86.160.0/20", "99.86.176.0/21", "99.86.185.0/24", "99.86.186.0/23", "99.86.188.0/22", "99.86.192.0/21", "99.86.201.0/24", "99.86.202.0/23", "99.86.204.0/22", "99.86.217.0/24", "99.86.218.0/23", "99.86.220.0/22", "99.86.224.0/20", "99.86.240.0/21", "99.86.249.0/24", "99.86.250.0/23", "99.86.252.0/22", "99.87.0.0/19", "99.87.32.0/22", "99.150.0.0/21", "99.150.16.0/20", "99.150.32.0/19", "99.150.64.0/18", "99.151.64.0/18", "99.151.128.0/19", "99.151.186.0/23", "100.20.0.0/14", "103.4.8.0/21", "103.8.172.0/22", "103.10.127.0/24", "103.16.56.0/24", "103.16.59.0/24", "103.16.101.0/24", "103.19.244.0/22", "103.23.68.0/23", "103.39.40.0/24", "103.43.38.0/23", "103.53.55.0/24", "103.58.192.0/24", "103.70.20.0/22", "103.70.49.0/24", "103.80.6.0/24", "103.85.213.0/24", "103.104.86.0/24", "103.107.56.0/24", "103.119.213.0/24", "103.123.219.0/24", "103.124.134.0/23", "103.127.75.0/24", "103.136.10.0/24", "103.143.45.0/24", "103.145.182.0/24", "103.145.192.0/24", "103.147.71.0/24", 
                                        "103.149.112.0/24", "103.150.47.0/24", "103.150.161.0/24", "103.151.39.0/24", "103.151.192.0/23", "103.152.248.0/24", "103.161.77.0/24", "103.165.160.0/24", "103.166.180.0/24", "103.167.153.0/24", "103.168.156.0/23", "103.168.209.0/24", "103.175.120.0/23", "103.179.36.0/23", "103.180.30.0/24", "103.181.194.0/24", "103.181.240.0/24", "103.182.250.0/23", "103.187.14.0/24", "103.188.89.0/24", "103.190.166.0/24", "103.193.9.0/24", "103.195.60.0/22", "103.196.32.0/24", "103.211.172.0/24", "103.229.8.0/23", "103.229.10.0/24", "103.235.88.0/24", "103.238.120.0/24", "103.246.148.0/22", "103.246.251.0/24", "104.36.33.0/24", "104.153.112.0/23", "104.171.198.0/23", "104.192.136.0/23", "104.192.138.0/24", "104.192.140.0/23", "104.192.143.0/24", "104.193.186.0/24", "104.193.205.0/24", "104.193.207.0/24", "104.207.162.0/24", "104.207.170.0/23", "104.207.172.0/23", "104.207.174.0/24", "104.218.202.0/24", "104.232.45.0/24", "104.234.23.0/24", "104.238.244.0/23", "104.238.247.0/24", "104.249.160.0/23", "104.249.162.0/24", "104.253.192.0/24", "104.255.56.0/22", "104.255.60.0/24", "107.162.252.0/24", "108.128.0.0/13", "108.136.0.0/15", "108.138.0.0/16", "108.139.0.0/19", "108.139.32.0/20", "108.139.48.0/21", "108.139.56.0/24", "108.139.72.0/21", "108.139.80.0/22", "108.139.84.0/23", "108.139.86.0/24", "108.139.102.0/23", "108.139.104.0/21", "108.139.112.0/20", "108.139.128.0/20", "108.139.144.0/23", "108.139.146.0/24", "108.139.162.0/23", "108.139.164.0/22", "108.139.168.0/21", "108.139.176.0/20", "108.139.207.0/24", "108.139.208.0/20", "108.139.224.0/19", "108.156.0.0/17", "108.156.128.0/23", "108.156.130.0/24", "108.156.146.0/23", "108.156.148.0/22", "108.156.152.0/21", "108.156.160.0/19", "108.156.192.0/18", "108.157.0.0/21", "108.157.8.0/23", "108.157.85.0/24", "108.157.86.0/23", "108.157.88.0/21", "108.157.96.0/20", "108.157.112.0/23", "108.157.114.0/24", "108.157.130.0/23", "108.157.132.0/22", "108.157.136.0/21", "108.157.144.0/20", "108.157.160.0/21", "108.157.168.0/22", "108.157.172.0/23", "108.157.174.0/24", "108.157.205.0/24", "108.157.206.0/23", "108.157.208.0/20", "108.157.224.0/21", "108.157.232.0/23", "108.157.234.0/24", "108.158.39.0/24", "108.158.40.0/21", "108.158.48.0/20", "108.158.64.0/22", "108.158.68.0/24", "108.158.114.0/23", "108.158.116.0/22", "108.158.120.0/21", "108.158.128.0/20", "108.158.144.0/21", "108.158.152.0/22", "108.158.156.0/23", "108.158.158.0/24", "108.158.219.0/24", "108.158.220.0/22", "108.158.224.0/19", "108.159.0.0/18", "108.159.64.0/19", "108.159.96.0/23", "108.159.128.0/21", "108.159.136.0/22", "108.159.144.0/23", "108.159.155.0/24", "108.159.156.0/24", "108.159.160.0/23", "108.159.163.0/24", "108.159.164.0/24", "108.159.166.0/23", "108.159.168.0/21", "108.159.181.0/24", "108.159.182.0/23", "108.159.184.0/24", "108.159.188.0/22", "108.159.192.0/24", "108.159.197.0/24", "108.159.198.0/23", "108.159.200.0/21", "108.159.208.0/24", "108.159.213.0/24", "108.159.214.0/23", "108.159.216.0/21", "108.159.224.0/21", "108.159.247.0/24", "108.159.248.0/23", "108.159.250.0/24", "108.159.255.0/24", "108.175.52.0/23", "108.175.54.0/24", "109.68.71.0/24", "109.95.191.0/24", "109.224.233.0/24", "109.232.88.0/21", "116.214.100.0/23", "116.214.120.0/23", "122.248.192.0/18", "122.252.145.0/24", "122.252.146.0/23", "122.252.148.0/22", "129.33.138.0/23", "129.33.243.0/24", "129.41.76.0/23", "129.41.88.0/23", "129.41.167.0/24", "129.41.174.0/23", "129.41.222.0/24", "130.50.35.0/24", "130.137.20.0/24", "130.137.78.0/24", "130.137.81.0/24", "130.137.86.0/24", "130.137.99.0/24", "130.137.112.0/24", "130.137.124.0/24", "130.137.136.0/24", "130.137.150.0/24", "130.137.178.0/24", "130.137.215.0/24", "130.176.0.0/21", "130.176.9.0/24", "130.176.10.0/23", "130.176.13.0/24", "130.176.14.0/24", "130.176.16.0/23", "130.176.24.0/23", "130.176.27.0/24", "130.176.28.0/22", "130.176.32.0/21", "130.176.40.0/24", "130.176.43.0/24", "130.176.45.0/24", "130.176.48.0/24", "130.176.50.0/24", "130.176.53.0/24", "130.176.54.0/24", "130.176.56.0/24", "130.176.65.0/24", "130.176.66.0/23", "130.176.68.0/24", "130.176.71.0/24", "130.176.75.0/24", "130.176.76.0/22", "130.176.80.0/21", "130.176.88.0/22", "130.176.92.0/23", "130.176.96.0/22", "130.176.100.0/24", "130.176.102.0/23", "130.176.104.0/22", "130.176.108.0/23", "130.176.111.0/24", "130.176.112.0/23", "130.176.116.0/24", "130.176.118.0/23", "130.176.120.0/24", "130.176.125.0/24", "130.176.126.0/23", "130.176.129.0/24", "130.176.130.0/23", "130.176.132.0/22", "130.176.136.0/23", "130.176.139.0/24", "130.176.140.0/22", "130.176.144.0/23", "130.176.146.0/24", "130.176.148.0/22", "130.176.152.0/24", "130.176.155.0/24", "130.176.156.0/22", "130.176.160.0/21", "130.176.168.0/24", "130.176.170.0/23", "130.176.172.0/24", "130.176.174.0/23", "130.176.179.0/24", "130.176.182.0/23", "130.176.184.0/21", "130.176.192.0/24", "130.176.194.0/23", "130.176.196.0/22", 
                                        "130.176.200.0/21", "130.176.208.0/21", "130.176.217.0/24", "130.176.218.0/23", "130.176.220.0/22", "130.176.224.0/24", "130.176.226.0/23", "130.176.231.0/24", "130.176.232.0/24", "130.176.254.0/23", "130.193.2.0/24", "131.232.37.0/24", "131.232.76.0/23", "131.232.78.0/24", "132.75.97.0/24", "134.224.0.0/17", "134.224.128.0/18", "134.224.192.0/19", "134.224.224.0/20", "134.224.242.0/23", "134.224.244.0/22", "134.224.248.0/22", "135.84.124.0/24", "136.18.18.0/23", "136.18.20.0/22", "136.175.24.0/23", "136.175.106.0/23", "136.175.113.0/24", "136.184.226.0/23", "136.184.229.0/24", "136.184.230.0/23", "136.184.232.0/23", "136.184.235.0/24", "136.226.219.0/24", "136.226.220.0/23", "137.83.193.0/24", "137.83.195.0/24", "137.83.196.0/22", "137.83.202.0/23", "137.83.204.0/23", "137.83.208.0/22", "137.83.212.0/24", "137.83.214.0/24", "137.83.252.0/22", "138.43.114.0/24", "139.60.2.0/24", "139.60.113.0/24", "139.60.114.0/24", "139.64.232.0/24", "139.138.105.0/24", "139.180.31.0/24", "139.180.242.0/23", "139.180.246.0/23", "139.180.248.0/22", "140.19.64.0/24", "140.99.123.0/24", "140.228.26.0/24", "141.11.12.0/22", "141.163.128.0/20", "141.193.32.0/23", "141.193.208.0/23", "142.0.189.0/24", "142.0.190.0/24", "142.4.160.0/22", "142.4.177.0/24", "142.54.40.0/24", "142.202.20.0/24", "142.202.36.0/22", "142.202.40.0/24", "142.202.42.0/23", "142.202.46.0/24", "143.55.151.0/24", "143.204.0.0/19", "143.204.32.0/21", "143.204.40.0/24", "143.204.57.0/24", "143.204.58.0/23", "143.204.60.0/22", "143.204.64.0/20", "143.204.80.0/21", "143.204.89.0/24", "143.204.90.0/23", "143.204.92.0/22", "143.204.96.0/20", "143.204.112.0/21", "143.204.121.0/24", "143.204.122.0/23", "143.204.124.0/22", "143.204.128.0/18", "143.204.192.0/19", "143.204.224.0/20", "143.204.240.0/21", "143.204.249.0/24", "143.204.250.0/23", "143.204.252.0/22", "143.244.81.0/24", "143.244.82.0/23", "143.244.84.0/22", "144.2.170.0/24"],
    )
            elif group_choice == '7':  
                ip_or_domain_list.extend(["173.245.48.0/20","103.21.244.0/22", "103.22.200.0/22", "103.31.4.0/22", "141.101.64.0/18", "108.162.192.0/18", "190.93.240.0/20", "188.114.96.0/20", 
                                        "197.234.240.0/22", "198.41.128.0/17", "162.158.0.0/15", "104.16.0.0/13", "104.24.0.0/14", "172.64.0.0/13", "131.0.72.0/22"])  # Replace with actual IPs
            else:
                print("Invalid group choice.")
                return

        else:
            print("Invalid choice.")
            return

        if not ip_or_domain_list:
            print("No WebSocket domains or IPs provided.")
            return
        
        websocket_domain = "d1ekq586huygub.cloudfront.net"
        port = 443

        output_file_name = input("Enter the name of the output (or leave blank to skip saving): ")

        successful_connections = 0

        with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
            results = [
                executor.submit(establish_websocket_connection, websocket_domain, ip_or_domain.strip(), port, output_file_name)
                for ip_or_domain in ip_or_domain_list
            ]

            for future in concurrent.futures.as_completed(results):
                if future.result() is not None:
                    successful_connections += 1

        if output_file_name.strip():
            print
        else:
            print(f"{Fore.RED}No successful WebSocket connections found.")

    if __name__ == '__main__':
        try:
            k()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()
                  
def script17():
    print("""
          
    ██████╗ ██████╗ ██████╗ 
    ╚════██╗╚════██╗╚════██╗
    ▄███╔╝  ▄███╔╝  ▄███╔╝
    ▀▀══╝   ▀▀══╝   ▀▀══╝ 
    ██╗     ██╗     ██╗   
    ╚═╝     ╚═╝     ╚═╝   
                        
          """)

    class DnsDumpster:
        def __init__(self):
            self.headers = {
                "Referer": "https://dnsdumpster.com",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                "User-Agent": "Mzoilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
            }
            r = requests.get("https://dnsdumpster.com", headers=self.headers)
            doc = BeautifulSoup(r.text.strip(), "html.parser")
            try:
                tag = doc.find("input", {"name": "csrfmiddlewaretoken"})
                self.csrftoken = tag['value']
                self.headers = {
                    "Referer": "https://dnsdumpster.com",
                    "Cookie": f"csrftoken={self.csrftoken};"
                }
            except:
                pass

        def _clean_table(self, table, record_type=0):
            retval = {}
            if record_type == 1:
                for idx, tag in enumerate(table.find_all('td')):
                    retval[idx] = tag.string
            for idx, tag in enumerate(table.find_all('td', {'class': 'col-md-4'})):
                clean_name = tag.text.replace('\n', '')
                clean_ip = tag.a['href'].replace('https://api.hackertarget.com/reverseiplookup/?q=', '')
                retval[idx] = {'ip': clean_ip, 'host': clean_name}
            return retval

        def dump(self, target):
            retval = {}
            data = {"csrfmiddlewaretoken": self.csrftoken, "targetip": target}
            r = requests.post("https://dnsdumpster.com", headers=self.headers, data=data)
            doc = BeautifulSoup(r.text.strip(), "html.parser")
            tables = doc.find_all('table')
            try:
                retval['dns'] = self._clean_table(tables[0])
                retval['mx'] = self._clean_table(tables[1])
                retval['txt'] = self._clean_table(tables[2], 1)
                retval['host'] = self._clean_table(tables[3])
                return retval
            except:
                return False

        def hostsearch(self, target):
            try:
                r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={target}")
                return r.text
            except:
                return "An error occurred."

        def reversedns(self, target):
            try:
                r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
                return r.text
            except:
                return "An error occurred."

        def dnslookup(self, target):
            try:
                r = requests.get(f"https://api.hackertarget.com/dnslookup/?q={target}")
                return r.text
            except:
                return "An error occurred."

        def pagelinks(self, target):
            try:
                r = requests.get(f"https://api.hackertarget.com/pagelinks/?q={target}")
                return r.text
            except:
                return "An error occurred."

        def httpheaders(self, target):
            try:
                r = requests.get(f"https://api.hackertarget.com/httpheaders/?q={target}")
                return r.text
            except:
                return "An error occurred."


    def j():
        print("\n\n")
        target = input("Enter the target domain: ")

        # Create an instance of DnsDumpster
        dnsdump = DnsDumpster()

        # Perform various actions based on user prompts
        action = input('''Select action 
    1: Host Search
    2: Reverse DNS 
    3: DNS Lookup 
    4: DNS Dump 
    5: Page Links 
    6: HTTP Headers 
    7: All 
    ''')

        user_specified_file = input("Enter the filename to save the output (e.g., output.txt): ")

        output_data = None  # Variable to store output data

        if action == '1':
            output_data = dnsdump.hostsearch(target)
        elif action == '2':
            output_data = dnsdump.reversedns(target)
        elif action == '3':
            output_data = dnsdump.dnslookup(target)
        elif action == '4':
            output_data = json.dumps(dnsdump.dump(target), indent=1)
        elif action == '5':
            output_data = dnsdump.pagelinks(target)
        elif action == '6':
            output_data = dnsdump.httpheaders(target)
        elif action == '7':
            output_data = {
                'dns': dnsdump.dump(target),
                'hostsearch': dnsdump.hostsearch(target),
                'reversedns': dnsdump.reversedns(target),
                'dnslookup': dnsdump.dnslookup(target),
                'pagelinks': dnsdump.pagelinks(target),
                'httpheaders': dnsdump.httpheaders(target)
            }
            output_data = json.dumps(output_data, indent=1)

        # Print or save the output based on user choice
        if user_specified_file:
            # If the user provides a filename, save the output to that file
            with open(user_specified_file, "w") as file:
                # Replace '\n' with actual new lines before writing to the file
                if isinstance(output_data, str):
                    output_data = output_data.replace('\\n', '\n')
                file.write(output_data)
            print(f"Output saved to '{user_specified_file}' ")
        else:
            # If the user didn't provide a filename, print the output to the console
            print(output_data)


    if __name__ == '__main__':
        try:
            j()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script17()

def script18():
    import requests 
    import json
    print('''
    ██╗   ██╗██████╗ ██╗     
    ██║   ██║██╔══██╗██║     
    ██║   ██║██████╔╝██║     
    ██║   ██║██╔══██╗██║     
    ╚██████╔╝██║  ██║███████╗
    ╚═════╝ ╚═╝  ╚═╝╚══════╝                      
            ██╗ ██████╗           
            ██║██╔═══██╗          
            ██║██║   ██║          
            ██║██║   ██║          
    ██╗     ██║╚██████╔╝          
    ╚═╝     ╚═╝ ╚═════╝           
                            
    ''')
    import requests
    import tldextract

    def search_urlscan(domain):
        url = f"https://urlscan.io/api/v1/search/?q=domain:{domain}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def save_results(results, filename):
        unique_urls = set()
        with open(filename, 'w') as file:
            for domain_info in results['DomainInfo']:
                unique_urls.add(domain_info['url'])
            
            for apex_domain, urlscan_info in results['Urlscan'].items():
                if urlscan_info is not None and 'results' in urlscan_info:
                    for result in urlscan_info['results']:
                        task = result.get('task', {})
                        unique_urls.add(task.get('url'))
            
            for url in unique_urls:
                file.write(f"{url}\n")

    def extract_domain_info(url):
        extracted = tldextract.extract(url)
        apex_domain = f"{extracted.domain}.{extracted.suffix}"
        return {
            'domain': extracted.domain,
            'apex_domain': apex_domain,
            'url': url
        }

    def extract_urlscan_info(urlscan_result):
        extracted_info = []
        if 'results' in urlscan_result:
            for result in urlscan_result['results']:
                task = result.get('task', {})
                extracted_info.append({
                    'domain': task.get('domain'),
                    'apex_domain': task.get('apexDomain'),
                    'url': task.get('url')
                })
        return extracted_info

    def process_domains(domains):
        processed_domains = set()
        results = {'DomainInfo': [], 'Urlscan': {}}

        for user_input in domains:
            try:
                domain_info = extract_domain_info(user_input.strip())
                apex_domain = domain_info['apex_domain']
                
                if apex_domain in processed_domains:
                    print(f"Domain '{apex_domain}' already processed. Skipping.")
                    continue

                processed_domains.add(apex_domain)
                results['DomainInfo'].append(domain_info)
                urlscan_result = search_urlscan(user_input)
                results['Urlscan'][apex_domain] = urlscan_result

                # Display the required fields on the screen
                print("Domain Info:")
                print(f"Domain: {domain_info['domain']}")
                print(f"Apex Domain: {domain_info['apex_domain']}")
                print(f"URL: {domain_info['url']}\n")

            except Exception as e:
                print(f"An error occurred: {str(e)}")

        output_filename = input("Enter a filename to save the results (e.g., results.txt): ")
        save_results(results, output_filename)
        print("Results saved successfully!")

    def l():
        input_option = input("Enter '1' to input a domain or IP manually, '2' to read from a file: ").strip()

        if input_option == '1':
            domain_or_ip = input("Enter a domain or IP: ").strip()
            process_domains([domain_or_ip])
        elif input_option == '2':
            file_path = input("Enter the filename (e.g., domains.txt): ").strip()
            try:
                with open(file_path, 'r') as file:
                    domains = file.readlines()
                    process_domains(domains)
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
        else:
            print("Invalid option selected.")

    if __name__ == '__main__':
        try:
            l()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()
            
def script19():

    print('''            
     ██████╗██████╗ ███╗   ██╗                                  
    ██╔════╝██╔══██╗████╗  ██║                                  
    ██║     ██║  ██║██╔██╗ ██║                                  
    ██║     ██║  ██║██║╚██╗██║                                  
    ╚██████╗██████╔╝██║ ╚████║                                  
    ╚═════╝╚═════╝ ╚═╝  ╚═══╝                                                                
    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝''')
    def findcdnfromhost(host):
        cloudflare_headers = ["cloudflare"]
        for header in cloudflare_headers:
            if header.lower() in host.lower():
                return "Cloudflare"
        return host

    def fetch_tls_ssl_certificate(host):
        ip_address = resolve_host_ip(host)
        if ip_address:
            try:
                with socket.create_connection((ip_address, 443)) as sock:
                    context = ssl.create_default_context()
                    with context.wrap_socket(sock, server_hostname=host) as ssock:
                        return ssock.getpeercert()
            except (socket.error, ssl.SSLError) as e:
                print(f"Error fetching TLS/SSL certificate for {host}: {e}")
                return None
        return None

    def resolve_host_ip(host):
        try:
            ip_address = socket.gethostbyname(host)
            return ip_address
        except socket.gaierror as e:
            print(f"Error resolving IP address for {host}: {e}")
            return None

    def get_http_headers(url):
        try:
            response = requests.head(url)
            return response.headers
        except Exception as e:
            print(f"HTTP request failed: {e}")
            return None

    def get_dns_records(host):
        try:
            answers_a = dns.resolver.resolve(host, 'A')
            a_records = [str(answer) for answer in answers_a]
        except Exception as e:
            print(f"Failed to fetch A records: {e}")
            a_records = []

        try:
            nslookup_result = get_aaaa_records(host)
            aaaa_records = nslookup_result if nslookup_result else []
        except Exception as e:
            print(f"Failed to fetch AAAA records: {e}")
            aaaa_records = []

        try:
            answers_ptr = dns.resolver.resolve(host, 'PTR')
            ptr_records = [str(answer) for answer in answers_ptr]
        except Exception as e:
            ptr_records = []

        try:
            answers_txt = dns.resolver.resolve(host, 'TXT')
            txt_records = [str(txt_answer) for txt_answer in answers_txt]
        except Exception as e:
            print(f"Failed to fetch TXT records: {e}")
            txt_records = []

        try:
            answers_mx = dns.resolver.resolve(host, 'MX')
            mx_records = [f"{answer.preference} {answer.exchange}" for answer in answers_mx]
        except Exception as e:
            print(f"Failed to fetch MX records: {e}")
            mx_records = []

        try:
            soa_records = [str(answer) for answer in dns.resolver.resolve(host, 'SOA')]
        except Exception as e:
            print(f"Failed to fetch SOA records: {e}")
            soa_records = []

        return a_records, aaaa_records, ptr_records, txt_records, mx_records, soa_records

    def get_aaaa_records(host):
        result = subprocess.run(["nslookup", "-query=AAAA", host], capture_output=True, text=True)
        return result.stdout.splitlines()

    def save_to_file(filename, content):
        with open(filename, 'w') as file:
            file.write(content)
            save_to_file()

    def w():
        user_input = input("Enter '1' to provide a URL, '2' to provide a text file with URLs: ")

        if user_input == '1':
            url = input("Enter the URL: ")
        elif user_input == '2':
            file_name = input("Enter the name of the text file with URLs: ")
            with open(file_name, 'r') as file:
                urls = file.readlines()
            url = urls[0].strip() if urls else None
        else:
            print("Invalid input. Exiting.")
            exit()

        if not urlparse(url).scheme:
            url = "http://" + url

        hostname = urlparse(url).hostname
        a_records, aaaa_records, ptr_records, txt_records, mx_records, soa_records = get_dns_records(hostname)

        output_filename = input("Enter the output file name: ")

        with open(output_filename, 'w') as output_file:
            output_file.write("\nDNS Records:")
            if a_records:
                print(f"A record:\n{a_records}\n")
                output_file.write(f"\nA Records: {a_records}")
            else:
                output_file.write("\nNo A Records found.")

            if aaaa_records:
                print(f"AAAA records:\n{aaaa_records}\n")
                output_file.write("\n\nAAAA Records:")
                for line in aaaa_records:
                    output_file.write(f"\n{line}")
            else:
                output_file.write("\nNo AAAA Records found.")

            if ptr_records:
                print(f"PTR records:\n {ptr_records}\n")
                output_file.write(f"\n\nPTR Records: {ptr_records}")
            else:
                output_file.write("\nNo PTR Records found.")

            if txt_records:
                print(f"TXT records:\n{txt_records}\n")
                output_file.write("\n\nTXT Records:")
                for line in txt_records:
                    output_file.write(f"\n{line}")
            else:
                output_file.write("\nNo TXT Records found.")

            if mx_records:
                print(f"MX records:\n{mx_records}\n")
                output_file.write("\n\nMX Records:")
                for line in mx_records:
                    output_file.write(f"\n{line}")
            else:
                output_file.write("\nNo MX Records found.")

            if soa_records:
                print(f"SOA records:\n{soa_records}\n")
                output_file.write("\n\nSOA Records:")
                for line in soa_records:
                    output_file.write(f"\n{line}")
            else:
                output_file.write("\nNo SOA Records found.")

            headers = get_http_headers(url)

            tls_ssl_certificate = fetch_tls_ssl_certificate(hostname)

            if headers:
                print(f"Header:\n{headers}\n")
                output_file.write("\n\nHTTP Headers:")
                for key, value in headers.items():
                    output_file.write(f"\n{key}: {value}")

                if tls_ssl_certificate:
                    print(f"TLS/SSL:\n{tls_ssl_certificate}\n")
                    output_file.write("\n\nTLS/SSL Certificate Information:")
                    for key, value in tls_ssl_certificate.items():
                        output_file.write(f"\n{key}: {value}")
                else:
                    output_file.write("\nFailed to fetch TLS/SSL certificate.")
            else:
                output_file.write("\nFailed to fetch HTTP headers.")

            server_header = headers.get("Server", "")
            
            cdn_provider = findcdnfromhost(server_header)
            print(f"CDN PROVIDER:\n{cdn_provider}\n")
            output_file.write(f"\n\nCDN Provider: {cdn_provider}")

        print(f"Output saved to {output_filename}")
    if __name__ == '__main__':
        try:
            w()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu2()
 
def script20():
    import requests
    import os
    import threading
    import time
    from urllib3.exceptions import ConnectTimeoutError
    from concurrent.futures import ThreadPoolExecutor
    from tqdm import tqdm

    class ConnectionError(Exception):
        pass

    def load_proxies(file_path):
        with open(file_path, 'r') as file:
            proxies = [line.strip() for line in file.readlines()]
        return proxies

    def check_domain_with_proxy(proxy, target, results_set, console_lock, file_lock):
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        try:
            # Try HTTP request
            response = requests.get(f"http://{target}", proxies=proxy_dict, timeout=3)
            handle_response(response, proxy, target, results_set, console_lock, file_lock)

            # Try HTTPS request
            response = requests.get(f"https://{target}", proxies=proxy_dict, timeout=3)
            handle_response(response, proxy, target, results_set, console_lock, file_lock)
                
        except requests.RequestException as e:
            error_message = str(e)
            if isinstance(e, requests.exceptions.ProxyError):
                error_message = f"Proxy connection error!!!"
            raise ConnectionError(f"{error_message} (Proxy: {proxy}, URL: {target})")

    def handle_response(response, proxy, target, results_set, console_lock, file_lock):
        if response.status_code == 200:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[92m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        elif response.status_code == 503:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[93m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        elif response.status_code == 502:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[93m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        
        elif response.status_code == 403:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[93m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        elif response.status_code == 404:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[93m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        elif response.status_code == 301:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[93m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        elif response.status_code == 302:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[93m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        elif response.status_code == 101:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[93m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        elif response.status_code == 309:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[93m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        elif response.status_code == 400:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[93m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        elif response.status_code == 500:
            result = f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}\n"
            with console_lock:
                print(f"\033[91m{result}\033[0m")
            with file_lock:
                results_set.add(result)
        else:
            with console_lock:
                print(f"Proxy {proxy} - Target: {target}, Status Code: {response.status_code}")


    def save_results_to_file(results_set, file_path):
        with open(file_path, 'a') as results_file:
            results_file.writelines(results_set)

    def process_proxy(proxy, target, results_set, console_lock, file_lock, pbar):
        try:
            check_domain_with_proxy(proxy, target, results_set, console_lock, file_lock)
        except requests.RequestException as ce:
            error_message = str(ce)
            if isinstance(e, requests.exceptions.ProxyError):
                error_message = f"Proxy connection error!!!"
            raise ConnectionError(f"{error_message} (Proxy: {proxy}, URL: {target})")
        finally:
            pbar.update(1)

    def lol():
        script_dir = os.path.dirname(os.path.realpath(__file__))

        proxies_file = input("Enter the proxies file (in txt format) in the script's directory: ").strip()
        proxy_file_path = os.path.join(script_dir, proxies_file)

        if not os.path.isfile(proxy_file_path):
            print(f"Error: File not found - {proxy_file_path}")
        else:
            target_type = input("Enter 'domain' for domain or 'file' for a list of domains or IPs: ").strip().lower()
            if target_type == 'domain':
                target = input("Enter the domain to check: ")
                targets = [target]
            elif target_type == 'file':
                target_file = input("Enter the file name containing domains or IPs (in txt format): ").strip()
                target_file_path = os.path.join(script_dir, target_file)
                if not os.path.isfile(target_file_path):
                    print(f"Error: File not found - {target_file_path}")
                    return
                with open(target_file_path, 'r') as file:
                    targets = [line.strip() for line in file.readlines()]
            else:
                print("Invalid input.")
                return

            print(f"Checking targets: {targets}")

            proxies = load_proxies(proxy_file_path)

            save_file_path = input("Enter the file path to save 200 OK results: ").strip()

            console_lock = threading.Lock()
            file_lock = threading.Lock()
            results_set = set()

            with tqdm(total=len(proxies) * len(targets)) as pbar:
                with ThreadPoolExecutor() as executor:
                    try:
                        for proxy in proxies:
                            for target in targets:
                                executor.submit(process_proxy, proxy, target, results_set, console_lock, file_lock, pbar)
                        time.sleep(30)  # You might want to adjust this sleep duration
                        with file_lock:
                            save_results_to_file(results_set, save_file_path)
                            results_set.clear()
                    except ConnectionError as ce:
                        print(ce)

    if __name__ == '__main__':
        try:
            lol()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu2()

def script21():
    print('''   
    ███████╗██████╗ ███████╗███████╗          
    ██╔════╝██╔══██╗██╔════╝██╔════╝          
    █████╗  ██████╔╝█████╗  █████╗            
    ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝            
    ██║     ██║  ██║███████╗███████╗          
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝                                                     
    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
    ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ 
    ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  
    ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                        
    ''')

    def get_proxies_from_source(source_url):
        try:
            response = requests.get(source_url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching proxy from {source_url}: {e}")
            return None

    def extract_proxies(data):
        # Use regular expression to extract proxies from the response
        proxies = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', data)
        return proxies

    def scrape_proxies(sources):
        all_proxies = []

        for source in tqdm(sources, desc="Scraping Proxies", unit="source"):
            source_data = get_proxies_from_source(source)

            if source_data:
                proxies = extract_proxies(source_data)
                all_proxies.extend(proxies)

        return all_proxies

    def check_proxy(proxy):
        try:
            response = requests.get("https://www.google.com", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=1)
            response.raise_for_status()
            return proxy
        except requests.exceptions.RequestException:
            return None

    def check_proxies(proxies):
        working_proxies = []

        with ThreadPoolExecutor(150) as executor:
            results = list(tqdm(executor.map(check_proxy, proxies), total=len(proxies), desc="Checking Proxies", unit="proxy"))

        working_proxies = [proxy for proxy in results if proxy is not None]

        return working_proxies

    def save_to_file(proxies, filename):
        with open(filename, 'w') as file:
            for proxy in proxies:
                file.write(f"{proxy}\n")

    def o():
        http_sources = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
            "https://openproxylist.xyz/http.txt",
            "https://proxyspace.pro/http.txt",
            "https://proxyspace.pro/https.txt",
            "http://free-proxy-list.net",
            "http://us-proxy.org",
            "https://www.proxy-list.download/api/v1/?type=http",
            "https://www.proxy-list.download/api/v1/?type=https",
            "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
            # Add other HTTP sources from your configuration here
            # ...
        ]

        socks4_sources = [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
            "https://www.proxy-list.download/api/v1/get?type=socks4&anon=elite"
            "https://openproxylist.xyz/socks4.txt",
            "https://proxyspace.pro/socks4.txt",
            "https://www.proxy-list.download/api/v1/get/?type=socks4"
            
            # Add other SOCKS4 sources from your configuration here
            # ...
        ]

        socks5_sources = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
            "https://www.proxy-list.download/api/v1/?type=socks5",
            "https://www.proxy-list.download/api/v1/get?type=socks5&anon=elite"
            "https://openproxylist.xyz/socks5.txt",
            "https://proxyspace.pro/socks5.txt",
            # Add other SOCKS5 sources from your configuration here
            # ...
        ]

        print("Choose the proxy type to save:")
        print("1. HTTP")
        print("2. SOCKS4")
        print("3. SOCKS5")

        try:
            user_choice = int(input("Enter the number corresponding to your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        if user_choice == 1:
            proxies = scrape_proxies(http_sources)
            working_proxies = check_proxies(proxies)
            save_to_file(working_proxies, 'http.txt')
            print(f"HTTP Proxies saved to http.txt. Total proxies: {len(working_proxies)}")
        elif user_choice == 2:
            proxies = scrape_proxies(socks4_sources)
            working_proxies = check_proxies(proxies)
            save_to_file(working_proxies, 'socks4.txt')
            print(f"SOCKS4 Proxies saved to socks4.txt. Total proxies: {len(working_proxies)}")
        elif user_choice == 3:
            proxies = scrape_proxies(socks5_sources)
            working_proxies = check_proxies(proxies)
            save_to_file(working_proxies, 'socks5.txt')
            print(f"SOCKS5 Proxies saved to socks5.txt. Total proxies: {len(working_proxies)}")
        else:
            print("Invalid choice. Please enter a valid number.")

    if __name__ == '__main__':
        try:
            o()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu2()
           
def teamerror():
    import requests
    import time
    import base64
    import os
    import re
    from tqdm import tqdm
    import time
    import json
    from concurrent.futures import ThreadPoolExecutor
    from colorama import init, Fore
    from ping3 import ping, verbose_ping
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = [
        "██╗  ██╗ ██████╗ ██╗  ██╗    ███████╗██████╗ ██████╗  ██████╗ ██████╗ ",
        "██║  ██║██╔═████╗██║  ██║    ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗",
        "███████║██║██╔██║███████║    █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝",
        "╚════██║████╔╝██║╚════██║    ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗",
        "     ██║╚██████╔╝     ██║    ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║",
        "     ╚═╝ ╚═════╝      ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝",
    ]

    def print_banner_seamless_horizontal(banner):
        for row in banner:
            for char in row:
                print(char, end='', flush=True)
                time.sleep(0.001)
            print()
            time.sleep(0.05)

    print_banner_seamless_horizontal(banner)

    def script001():

        def fetch_and_save_data(urls, output_filename):
            all_contents = []

            for url in urls:
                response = requests.get(url)
                if response.status_code == 200:
                    content = response.text
                    all_contents.append(content)
                else:
                    print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")

            if all_contents:
                with open(output_filename, 'w', encoding="utf-8") as file:
                    file.writelines(all_contents)
                print(f"Data saved to {output_filename}")
            else:
                print("No data retrieved. Output file not created.")

        def decode_base64_file(input_file):
            try:
                with open(input_file, "r", encoding="utf-8") as file:
                    data = file.read()
                decoded_data = base64.urlsafe_b64decode(data).decode('utf-8')
                with open(input_file, "a", encoding="utf-8") as file:
                    file.write(decoded_data)
                print(f"Decoded data saved to {input_file}")

            except FileNotFoundError:
                print("Input file not found.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        

        def a1():
            link_groups = {
                "Vless Configurations": [
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/vless",
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless",
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/vless",
                ],
                "Vmess Configurations": [
                   #"https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/vmess",
                   #"https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Splitted-By-Protocol/vmess.txt",
                   "https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/vmess.txt",
                   "https://raw.githubusercontent.com/resasanian/Mirza/main/best",
                   "https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/Splitted-By-Protocol/vmess.txt",
                    
                    
                ],
                "Trojan Configurations": [
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/trojan",
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/trojan",
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/trojan",
                ],
                "Shadowsocks Configurations": [
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/shadowsocks",
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/shadowsocks",
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/shadowsocks",
                ],
                
                "Hysteria Configurations": [
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/hysteria",
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/hysteria",
                    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/hysteria",
                ],
            }

            print("Choose a group of links:")
            for i, group_name in enumerate(link_groups.keys(), start=1):
                print(f"{i}: {group_name}")

            group_choice = int(input("Enter the number of the group you want to select: "))

            if 0 <= group_choice <= len(link_groups):
                selected_group = list(link_groups.keys())[group_choice - 1]
                output_filename = input("Enter the name of the output file (e.g., output.txt): ")
                fetch_and_save_data(link_groups[selected_group], output_filename)
                decode_base64_file(output_filename)
            else:
                print("Invalid group choice. Exiting.")
                time.sleep(0.5)

        if __name__ == '__main__':
            try:
                a1()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                teamerror()
                    
    def script002():
        
                         
        def decode_vmess_file(input_file, output_file):
            try:
                with open(input_file, 'r') as file:
                    file_content = file.read()
                decoded_v2ray_data_list = []

                for encoded_data in file_content.splitlines():
                    decoded_v2ray_data = decode_v2ray(encoded_data)
                    if decoded_v2ray_data:
                        decoded_v2ray_data_list.append(decoded_v2ray_data)

                if decoded_v2ray_data_list:
                    with open(output_file, 'w') as output_file:
                        json.dump(decoded_v2ray_data_list, output_file, indent=2)
                    print(f"Decoded data saved to '{output_file}'")
                else:
                    print(f"No valid V2Ray data found in '{input_file}'.")

            except FileNotFoundError:
                print(f"File '{input_file}' not found. Please provide a valid input file name.")
            except Exception as e:
                print(f"An error occurred: {e}")

        def decode_v2ray(encoded_data):
            for protocol_prefix in ["vmess://", "vless://", "trojan://"]:
                if encoded_data.startswith(protocol_prefix):
                    encoded_data = encoded_data[len(protocol_prefix):]
            decoded_bytes = base64.urlsafe_b64decode(encoded_data.encode('utf-8'))
            decoded_str = decoded_bytes.decode('utf-8')
            if not decoded_str:
                return None
            try:
                v2ray_data = json.loads(decoded_str)
                return v2ray_data
            except json.JSONDecodeError:
                return None

        def a2():
            input_file = input("Enter the name of the input text file containing Vmess data (e.g., input.txt): ")
            output_file = input("Enter the name of the output text file (e.g., decoded_output.txt): ")

            decode_vmess_file(input_file, output_file)
        if __name__ == '__main__':
            try:
                a2()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                teamerror()
        
    def script003():
        
        def z1():
            print("Select an operation:")
            print("1. Replace host or IP address in vmess file")
            print("2. Update IP addresses in ss/vless/hyst file")
            print("3. SNI Replacement")
            print("4. Go back to teamerror")
        
        def replace_host_in_json(input_file, output_file, replace_host):
            try:
                with open(input_file, 'r') as file:
                    data = file.read()
                pattern = re.compile(r'"add":\s*"[^"]*"')
                data = pattern.sub(f'"add": "{replace_host}"', data)
                with open(output_file, 'w') as file:
                    file.write(data)
                print(f'Replaced all occurrences: "{replace_host}" in {input_file} and saved the result in {output_file}')

            except FileNotFoundError:
                print(f"File '{input_file}' not found. Please provide a valid input file name.")
            except Exception as e:
                print(f"An error occurred: {e}")
                
        
        def replace_host_in_json2(input_file, output_file, replace_host):
                    try:
                        with open(input_file, 'r') as file:
                            data = file.read()
                        pattern = re.compile(r'"sni":\s*"[^"]*"')
                        data = pattern.sub(f'"sni": "{replace_host}"', data)
                        with open(output_file, 'w') as file:
                            file.write(data)
                        print(f'Replaced all occurrences: "{replace_host}" in {input_file} and saved the result in {output_file}')

                    except FileNotFoundError:
                        print(f"File '{input_file}' not found. Please provide a valid input file name.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        
        def update_ip_addresses_in_file(file_name, new_ip):
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                modified_lines = []
                with tqdm(total=len(lines), position=0, leave=True) as pbar:
                    for line in lines:
                        ip_match = re.search(r'@(\d+\.\d+\.\d+\.\d+)', line)
                        if ip_match:
                            current_ip = ip_match.group(1)
                            modified_line = line.replace(f'@{current_ip}', f'@{new_ip}')
                            modified_lines.append(modified_line)
                        else:
                            modified_lines.append(line)
                        pbar.update(1)
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.writelines(modified_lines)
                print("IP addresses updated successfully in", file_name)

            except FileNotFoundError:
                print(f"File '{file_name}' not found in the current directory. Please provide a valid file name.")
            except Exception as e:
                print(f"An error occurred: {e}")
                return None

        if __name__ == '__main__':
                try:
                    while True:
                        z1()
                        operation = input("Enter your choice: ")

                        if operation == '1':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            input_file = input("Enter the name of the input text file: ")
                            output_file = input("Enter the name of the output text file: ")
                            replace_host = input("Enter the new host or IP address to replace with: ")
                            replace_host_in_json(input_file, output_file, replace_host)
                            
                        elif operation == '3':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            input_file = input("Enter the name of the input text file: ")
                            output_file = input("Enter the name of the output text file: ")
                            replace_host = input("Enter the new host or IP address to replace with: ")
                            replace_host_in_json2(input_file, output_file, replace_host)
                            
                        elif operation == '2':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            file_name = input("Enter the name of the text file in the current directory: ")
                            new_ip = input("Enter the new IP address: ")
                            update_ip_addresses_in_file(file_name, new_ip)
                            print("Job done!")
                            time.sleep(2)

                        elif operation == '4':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            teamerror()
                            # Exit the loop to return to teamerror()
                            break

                except Exception as e:
                    print(f"An error occurred: {e}")

                finally:
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    teamerror()  # Assuming you want to call teamerror() after the loop exits
            
    def script004():
        import base64
        import json

        def reencode_v2ray_data():
            input_file_name = input("Enter the name of the input file (e.g., v2ray_data.txt): ")
            protocol_prefix = input("Enter the protocol prefix (e.g., 'vmess://'): ")

            try:
                with open(input_file_name, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                print(f"File '{input_file_name}' not found.")
                return

            output_file_name = input("Enter the name of the output file (e.g., reencoded_v2ray_data.txt): ")

            reencoded_data_list = []
            for v2ray_data in data:
                reencoded_data = encode_v2ray(v2ray_data, protocol_prefix)
                if reencoded_data:
                    reencoded_data_list.append(reencoded_data)

            with open(output_file_name, 'w') as output_file:
                for reencoded_data in reencoded_data_list:
                    output_file.write(reencoded_data + '\n')
            print(f"Re-encoded data saved to '{output_file_name}'")

        def encode_v2ray(v2ray_data, protocol_prefix):
            try:
                json_str = json.dumps(v2ray_data, ensure_ascii=False)
                encoded_data = base64.urlsafe_b64encode(json_str.encode('utf-8')).decode('utf-8')
                return protocol_prefix + encoded_data
            except Exception as e:
                return None

        def a3():
            
            reencode_v2ray_data()
        if __name__ == '__main__':
                try:
                    a3()
                except Exception as e:
                    print(f"An error occurred: {e}")
                finally:
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    teamerror()
                    
    def script005():
        
        def test_vmess_url(vmess_url):
            try:
                decoded_vmess = base64.urlsafe_b64decode(vmess_url.split("://")[1]).decode("utf-8")
                vmess_data = json.loads(decoded_vmess)
                server_address = vmess_data.get("add", "")
                server_port = vmess_data.get("port", "")
                
                # Establish a TCP connection to the server
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(5)  # Set a timeout for the connection attempt
                    s.connect((server_address, server_port))
                
                return vmess_url, 1  # Return the URL and 1 for a successful connection
            
            except Exception as e:
                return None, 0  # Return None and 0 for any exceptions

        def a4():
            file_path = input("Enter the name of the text file containing vmess URLs: ")

            try:
                with open(file_path, 'r') as file:
                    vmess_urls = [line.strip() for line in file.readlines()]

                connected_count = 0
                connected_vmess_urls = []

                with ThreadPoolExecutor(max_workers=10) as executor:
                    results = list(tqdm(executor.map(test_vmess_url, vmess_urls), total=len(vmess_urls), desc="Testing VMess URLs"))
                
                for url, connection_status in results:
                    if connection_status == 1:
                        connected_count += 1
                        connected_vmess_urls.append(url)

                print(Fore.CYAN + f"Total connected VMess URLs: {connected_count}")
                save_file = input("Do you want to save connected VMess URLs to a file? (yes/no): ").lower()
                if save_file == 'yes':
                    output_file_path = input("Enter the name of the output text file: ")
                    with open(output_file_path, 'w') as output_file:
                        for vmess_url in connected_vmess_urls:
                            output_file.write(f"{vmess_url}\n")

                    print(Fore.CYAN + f"Working VMess URLs saved to '{output_file_path}'.")

            except FileNotFoundError:
                print(Fore.RED + f"File '{file_path}' not found in the current directory. Please provide a valid file name.")
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}" + ENDC)

        if __name__ == '__main__':
                try:
                    a4()
                except Exception as e:
                    print(Fore.RED + f"An error occurred: {e} " + ENDC)

                finally:
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    teamerror()
                
    time.sleep(1)
    print("1.""\033[32mGRAB CONFIGS\033[0m""         2.)""\033[32mDECODE vmess \033[0m")                       
    print("3.""\033[95mReplace all host/ip\033\033[0m""  4.)""\033[33mRe-encode Vmess\033[0m")
    print("5.""\033[32mTEST VMESS ONLY\033[0m")
    print("0.""\033[34mReturn to main\033[0m")

    choice = input("Return to BUGHUNTERS PRO (0): ")
    if choice == '0':
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu2()  # Return to the main menu
    elif choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        script001() 
    elif choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        script002()  # 
    elif choice == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        script003()  # 
    elif choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        script004()
    elif choice == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        script005()  # # # Assuming o() is defined elsewhere
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

def help():
    import time
    import sys

    def slowprint(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust this value to change the printing speed
        print()

    def sub_domain_finder():
        subdomainfinder1 = "\033[33m" + """
        SUBDOMAIN FINDER
        
        This is a web scraping tool that scans a 
        specific domain for subdomains and IPS
        The user is prompted to enter a domain 
        name for which they want to find subdomains or IPs
        e.g google.com, the script will then prompt 
        the user to save the results (y/n). 
        Then it will ask the user to input the name 
        of txt file they want to save their results as...
        The script will then ask the user if they 
        want to save the ips only to a txt file (y/n)
        it will then scan for subdomains and 
        save the found results to your txt files
        scan time 1hr - 5 mins\033[0m"""
        slowprint(subdomainfinder1)
        return_to_menu()

    def subdomain_enum():
        subdomain_enum_text = "\033[33m" + """     
        SUB DOMAIN ENUM

        This script sends a GET request to the Transparency Certificate
        of a website.
        The script then parses the JSON response to extract the subdomain
        names and prints them out.\033[0m"""
        slowprint(subdomain_enum_text)
        return_to_menu()
        
    def host_checker():
        host_checker_text = "\033[35m" + """
        HOST CHECKER
        
        This script scans all the domains and
        subdomains in a given list and
        writes them to a specified output file. \033[0m"""
        slowprint(host_checker_text)
        return_to_menu()
        
    def ip_gen():
        ip_gen_text = "\033[33m" + """ 
        IP GEN
        
        This script takes an IP range as input and calculates
        all the addresses in that range. It then prints the addresses
        to the console and writes them to a file specified by the user.\033[0m"""
        slowprint(ip_gen_text)
        return_to_menu()
        
    def revultra():
        rev_text = "\033[33m" + """ 
        REVULTRA
        
        This script takes an IP range, Single IP or Host as input
        does a rdns lookup and writes them to a file specified by the user.
        these domains can then be used in host checker on zero data for finding
        bugs\033[0m"""
        slowprint(rev_text)
        return_to_menu()
    
    def cdn_finder():
        cdn_finder_text = "\033[33m" + """ 
        CDN FINDER
        INSTALLATION NOTES!!!!!!!! MUST READ!!!!!!
        FOR TERMUX USERS COPY THE COMMANDS AS FOLLOWS
        pkg install dnsutils
        pip install dnspython
        cd
        cd ..
        cd usr/etc
        nano resolv.conf
        
        if the file is blank then add these 2 lines
        
        nameserver 8.8.8.8
        nameserver 8.8.4.4
        
        then hit ctrl + x then y and enter to save the edit
        if it's already there no need to edit
        
        now from that directory do cd .. and hit enter
        
        cd lib/python3.11/site-packages/dns
        
        ( ls ) to see the the files in the directory
        now use nano to edit the resolver.py file like so
        
        nano resolver.py
        
        we are looking for the line that points the resolver.py 
        to where the resolv.conf is at.
        
        Vist https://mega.nz/file/35QSCIDI#1pVPy8y-V5GHDghRKIxMOHJCkML31egZt7vBMAh8Pcg
        for an image on what you are looking for.
        replace your lines with the lines you see in the image
        
        This is what the updated line should read.
        
        /data/data/com.termux/files/usr/etc/resolv.conf
        
        now ctrl + x and y then hit enter that's it... cdn scanner now works fine....
        This script finds the CDN inuse on the host or ip
        and more...
        \033[0m"""
        slowprint(cdn_finder_text)
        return_to_menu()

    def crypto_installer():
        
        installation = "\033[33m" + """
        
        Cryptography installation
        
        pkg install rust 
        pkg install clang python openssl openssl-tool make
        pkg install binutils
        export AR=/usr/bin/aarch64-linux-android-ar
        pip install cryptography --no-binary cryptography
        \033[0m"""
        slowprint(installation)
        return_to_menu()
        
    def return_to_menu():
        choice = input("Do you want to return to the previous menu? (y/n): ")
        if choice.lower() == "y":
            help()
        elif choice.lower() == "n":
            print("back to main.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()
            return
        
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            return_to_menu()

    def helpmain():
        print("Choose an option:")
        print("1. SUBDOMAIN FINDER           7. Cryptography installation")
        print("2. Sub Domain Enum")
        print("3. Host Checker")
        print("4. Ip Gen")
        print("5. Revultra")
        print("6. CDN Finder")
        choice = input("Enter your choice: ")

        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            sub_domain_finder()
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            subdomain_enum()
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            host_checker()
        elif choice == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            ip_gen()
        elif choice == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            revultra()
        elif choice == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            cdn_finder()
        elif choice == "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            crypto_installer()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            script0()

    if __name__ == "__main__":
        helpmain()

def script22():
    import sys
    lime = fg('#00FF00')
    blue = fg('#0000A5')
    pink = fg('#FF69B4')
    yuh_fada = '\033[0m'

    def randomshit(bullshit):
        
        color_list = [blue, pink, lime]
        
        your_pussy = random.choice(color_list)
        
        for myballs in your_pussy:
            sys.stdout.write(myballs)
            sys.stdout.flush()
            time.sleep(3. / 100)

        print(bullshit, yuh_fada)

    
    randomshit("""
    ██████╗    ██████╗                                  
    ██╔══██╗   ██╔══██╗                                 
    ██║  ██║   ██████╔╝                                 
    ██║  ██║   ██╔══██╗                                 
    ██████╔╝██╗██║  ██║                                 
    ╚═════╝ ╚═╝╚═╝  ╚═╝                                 
                                                        
         █████╗  ██████╗ ██████╗███████╗███████╗███████╗
        ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
        ███████║██║     ██║     █████╗  ███████╗███████╗
        ██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║
        ██║  ██║╚██████╗╚██████╗███████╗███████║███████║
        ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝
                                                        
    """)
    
    import threading
    import sys
    import requests
    import socket
    import ssl
    import queue
    import re

    lock = threading.RLock()

    def get_value_from_list(data, index, default=""):
        try:
            return data[index]
        except IndexError:
            return default

    def log(value):
        with lock:
            print(value)

    def log_replace(value):
        with lock:
            sys.stdout.write(f"{value}\r")
            sys.stdout.flush()

    class BugScanner:
        def __init__(self):
            self.output = None
            self.scanned = {"direct": {}, "ssl": {}, "proxy": {}}
            self.deep = 5
            self.ignore_redirect_location = ""
            self.method = "HEAD"
            self.mode = "direct"
            self.port = 80
            self.proxy = None
            self.threads = 8

        brainfuck_config = {
            "ProxyRotator": {
                "Port": "3080",
            },
            "Inject": {
                "Enable": True,
                "Type": 2,
                "Port": "8989",
                "Rules": {},
                "Payload": "",
                "MeekType": 0,
                "ServerNameIndication": "sslgstatic.com",
                "Timeout": 5,
                "ShowLog": False,
            },
            "PsiphonCore": 4,
            "Psiphon": {
                "CoreName": "psiphon-tunnel-core",
                "Tunnel": 1,
                "Region": "",
                "Protocols": [
                    "FRONTED-MEEK-HTTP-OSSH",
                    "FRONTED-MEEK-OSSH",
                ],
                "TunnelWorkers": 6,
                "KuotaDataLimit": 4,
                "Authorizations": [""],
            },
        }

        def request(self, method, hostname, port, *args, **kwargs):
            try:
                url = ("https" if port == 443 else "http") + "://" + (hostname if port == 443 else f"{hostname}:{port}")
                log_replace(f"{method} {url}")
                return requests.request(method, url, *args, **kwargs)
            except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
                return None

        def resolve(self, hostname):
            try:
                cname, hostname_list, host_list = socket.gethostbyname_ex(hostname)
            except (socket.gaierror, socket.herror):
                return []

            for i in range(len(hostname_list)):
                yield get_value_from_list(host_list, i, host_list[-1]), hostname_list[i]

            yield host_list[-1], cname

        def get_direct_response(self, method, hostname, port):
            if f"{hostname}:{port}" in self.scanned["direct"]:
                return None

            response = self.request(method.upper(), hostname, port, timeout=5, allow_redirects=False)
            if response is not None:
                status_code = response.status_code
                server = response.headers.get("server", "")
            else:
                status_code = ""
                server = ""

            self.scanned["direct"][f"{hostname}:{port}"] = {
                "status_code": status_code,
                "server": server,
            }
            return self.scanned["direct"][f"{hostname}:{port}"]

    class SSLScanner(BugScanner):
        def __init__(self):
            super().__init__()
            self.host_list = []

        def get_task_list(self):
            for host in self.filter_list(self.host_list):
                yield {
                    'host': host,
                }

        def log_info(self, color, status, server_name_indication):
            log(f'{color}{status:<6}  {server_name_indication}')

        def log_info_result(self, **kwargs):
            status = kwargs.get('status', '')
            server_name_indication = kwargs.get('server_name_indication', '')

            if status:
                self.log_info('', 'True', server_name_indication)
            else:
                self.log_info('', 'False', server_name_indication)

        def init(self):
            log('Stat  Host')
            log('----  ----')

        def task(self, payload):
            server_name_indication = payload['host']
            log_replace(server_name_indication)

            response = {
                'server_name_indication': server_name_indication,
                'status': False
            }

            try:
                socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_client.settimeout(5)
                socket_client.connect((server_name_indication, 443))
                socket_client = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2).wrap_socket(
                    socket_client, server_hostname=server_name_indication, do_handshake_on_connect=True
                )
                response['status'] = True

                self.task_success(server_name_indication)

            except Exception:
                pass

            finally:
                socket_client.close()

            self.log_info_result(**response)
            if response['status']:
                self.scanned["ssl"][f"{server_name_indication}:443"] = response

        def get_proxy_response(self, method, hostname, port, proxy):
            if f"{hostname}:{port}" in self.scanned["proxy"]:
                return None

            response = self.request(method.upper(), hostname, port, proxies={"http": "http://" + proxy, "https": "http://" + proxy}, timeout=5, allow_redirects=False)
            if response is None:
                return None

            if response.headers.get("location") == self.ignore_redirect_location:
                log(f"{self.proxy} -> {self.method} {response.url} ({response.status_code})")
                return None

            self.scanned["proxy"][f"{hostname}:{port}"] = {
                "proxy": self.proxy,
                "method": self.method,
                "url": response.url,
                "status_code": response.status_code,
                "headers": response.headers,
            }
            return self.scanned["proxy"][f"{hostname}:{port}"]

        def print_result(self, host, hostname, port=None, status_code=None, server=None, sni=None, color=""):
            if ((server == "AkamaiGHost" and status_code != 400) or
                    (server == "Varnish" and status_code != 500) or
                    (server == "AkamaiNetStorage")):
                color = 'G2'  # Assuming G2 is some special char

            host = f"{host:<15}"
            hostname = f"  {hostname}"
            sni = f"  {sni:<4}" if sni is not None else ""
            server = f"  {server:<20}" if server is not None else ""
            status_code = f"  {status_code:<4}" if status_code is not None else ""

            log(f"{host}{status_code}{server}{sni}{hostname}")

        def print_result_proxy(self, response):
            if response is None:
                return

            data = []
            data.append(f"{response['proxy']} -> {response['method']} {response['url']} ({response['status_code']})\n")
            for key, val in response['headers'].items():
                data.append(f"|   {key}: {val}")
            data.append("|\n\n")

            log("\n".join(data))

        def is_valid_hostname(self, hostname):
            if len(hostname) > 255:
                return False
            if hostname[-1] == ".":
                hostname = hostname[:-1]
            allowed = re.compile(r"(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
            return all(allowed.match(x) for x in hostname.split("."))

        def get_sni_response(self, hostname, deep):
            if f"{hostname}:443" in self.scanned["ssl"]:
                return None

            try:
                socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_client.settimeout(5)
                socket_client.connect((hostname, 443))
                context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
                with context.wrap_socket(socket_client, server_hostname=hostname) as ssock:
                    ssock.do_handshake()
                    response = {
                        "server_name_indication": hostname,
                        "status": True,
                    }
                    self.scanned["ssl"][f"{hostname}:443"] = response
                    return response
            except (socket.timeout, ssl.SSLError, socket.error):
                return {
                    "server_name_indication": hostname,
                    "status": False,
                }
            finally:
                socket_client.close()

        def scan(self):
            while True:
                hostname = self.queue_hostname.get()
                if not self.is_valid_hostname(hostname):
                    log(f"Invalid hostname: {hostname}")
                    self.queue_hostname.task_done()
                    continue

                for host, resolved_hostname in self.resolve(hostname):
                    if self.mode == "direct":
                        response = self.get_direct_response(self.method, resolved_hostname, self.port)
                        if response is None:
                            continue
                        self.print_result(host, resolved_hostname, port=self.port, status_code=response["status_code"], server=response["server"])

                    elif self.mode == "ssl":
                        response = self.get_sni_response(resolved_hostname, self.deep)
                        self.print_result(host, response["server_name_indication"], sni="True" if response["status"] else "False")

                        if response["status"] and self.output is not None:
                            with open(self.output, 'a', encoding='utf-8') as f:
                                f.write(f"{host},{response['server_name_indication']},True\n")

                    elif self.mode == "proxy":
                        response = self.get_proxy_response(self.method, resolved_hostname, self.port, self.proxy)
                        self.print_result_proxy(response)

                self.queue_hostname.task_done()

        def start(self, hostnames):
            try:
                if self.mode == "direct":
                    self.print_result("host", "hostname", status_code="code", server="server")
                    self.print_result("----", "--------", status_code="----", server="------")
                elif self.mode == "ssl":
                    self.print_result("host", "hostname", sni="sni")
                    self.print_result("----", "--------", sni="---")

                self.queue_hostname = queue.Queue()
                for hostname in hostnames:
                    self.queue_hostname.put(hostname)

                for _ in range(min(self.threads, self.queue_hostname.qsize())):
                    thread = threading.Thread(target=self.scan)
                    thread.daemon = True
                    thread.start()

                self.queue_hostname.join()

                if self.output is not None:
                    with open(f"{self.output}", 'a', encoding='utf-8') as f:
                        for key, value in self.scanned.items():
                            f.write(f"{key}:\n")
                            for sub_key, sub_value in value.items():
                                if sub_value.get("server"):  # Check if server field is not empty
                                    f.write(f"  {sub_key}: {sub_value}\n")

                    log(f"Output saved to {self.output}")
            except KeyboardInterrupt:
                log("Keyboard interrupt received. Exiting...")

    def main():
        bugscanner = SSLScanner()
        bugscanner.deep = 5
        bugscanner.ignore_redirect_location = ""
        bugscanner.method = "HEAD"
        bugscanner.mode = input("Enter the mode (direct, ssl) (default: direct): ") or "direct"
        bugscanner.output = input("Enter output file name (optional): ")
        bugscanner.port = int(input("Enter the target port (default: 80): ") or 80)
        bugscanner.proxy = None
        bugscanner.threads = 8
        filename = input(f"Enter filename: ")

        with open(filename) as file:
            bugscanner.start(file.read().splitlines())

    if __name__ == "__main__":
        main()
        print("check output")
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu2()
     
def script23():
    import requests
    import gzip
    import io
    import os
    import time

    # Function to download and search the TSV data
    def search_ip2asn_data(company_name):
        # Download the TSV file
        url = 'https://iptoasn.com/data/ip2asn-combined.tsv.gz'
        response = requests.get(url)
        
        # Check if download was successful
        if response.status_code == 200:
            # Wrap the content in a BytesIO object
            content = io.BytesIO(response.content)
            
            # Decompress the gzip file
            with gzip.open(content, 'rb') as f:
                # Decode the content using 'latin-1' encoding
                decoded_content = f.read().decode('latin-1')
                
                # Check for occurrences of the company name
                if company_name.lower() in decoded_content.lower():
                    # Split the content by lines and search for the company name
                    lines = decoded_content.split('\n')
                    result_lines = [line for line in lines if company_name.lower() in line.lower()]
                    return result_lines
                else:
                    return ["Company not found in the IP2ASN data."]
        else:
            return ["Failed to download IP2ASN data."]

    # Function to save results to a file
    def save_to_file(file_path, lines):
        with open(file_path, 'w') as f:
            for line in lines:
                f.write(line + '\n')
        print(f"Results saved to {file_path}")

    # Main function
    def az():
        # Prompt the user for the company name
        company_name = input("Enter the company name to look up: ")
        
        # Search for the company name in the IP2ASN data
        result_lines = search_ip2asn_data(company_name)
        
        # Prompt the user to save the results to a file
        if result_lines:
            for line in result_lines:
                print(line)
            
            save_option = input("Do you want to save the results to a file? (yes/no): ")
            if save_option.lower() == 'yes':
                file_name = input("Enter the file name (without extension): ")
                file_path = os.path.join(os.path.dirname(__file__), f"{file_name}.txt")
                save_to_file(file_path, result_lines)
        else:
            print("No results found.")
    if __name__ == "__main__":
        az()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu2()   
        
def script24():
    import aiohttp
    import asyncio
    import socket
    import signal
    from urllib.parse import urlparse, urljoin
    from bs4 import BeautifulSoup

    visited_urls = set()
    found_urls = set()
    output_file = input("input filename: ")
    MAX_CONCURRENT_REQUESTS = 10

    async def fetch_url(session, url):
        if url in visited_urls:
            return
        visited_urls.add(url)

        try:
            async with session.get(url) as response:
                response_code = response.status
                server = response.headers.get('Server')
                ip_address = socket.gethostbyname(urlparse(url).netloc)
                print(f"url: {url} | Response Code: {response_code} | Server: {server} | IP: {ip_address}")

                if response_code == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    for link in soup.find_all('a', href=True):
                        href = link['href']
                        next_url = urljoin(url, href)
                        if next_url not in found_urls:
                            found_urls.add(next_url)
                            await fetch_url(session, next_url)

        except aiohttp.ClientError as e:
            print(f"Error: {e}")

    async def ax():
        url_or_file = input("Enter a URL to crawl: ").strip()

        if url_or_file.endswith('.txt'):
            try:
                with open(url_or_file, 'r') as f:
                    urls = f.readlines()
                    async with aiohttp.ClientSession() as session:
                        await asyncio.gather(*[fetch_url(session, url.strip()) for url in urls])
            except FileNotFoundError:
                print("Error: File not found.")
        else:
            parsed_url = urlparse(url_or_file)
            if not parsed_url.scheme:
                url_or_file = 'https://' + url_or_file
            async with aiohttp.ClientSession() as session:
                await fetch_url(session, url_or_file)

        if len(found_urls) >= 200:
            save_output()

    def save_output():
        with open(output_file, 'w') as f:
            for url in sorted(found_urls):
                f.write(url + '\n')
        print(f"Output saved to {output_file}")

    def handle_interrupt():
        print("\nKeyboardInterrupt detected. Saving results before exiting...")
        save_output()

    if __name__ == "__main__":
        try:
            asyncio.run(ax())
        except KeyboardInterrupt:
            handle_interrupt()
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu2()   

def script25():
    import datetime
    import json
    import os
    from requests import get
    from requests.exceptions import ConnectionError
    
    print("""
    ██╗    ██╗ █████╗ ██╗   ██╗██████╗  █████╗  ██████╗██╗  ██╗
    ██║    ██║██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
    ██║ █╗ ██║███████║ ╚████╔╝ ██████╔╝███████║██║     █████╔╝ 
    ██║███╗██║██╔══██║  ╚██╔╝  ██╔══██╗██╔══██║██║     ██╔═██╗ 
    ╚███╔███╔╝██║  ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗
    ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                            
    """)

    common_prefixes = [
        "{host}",
    ]

    def get_input_from_file_or_domain():
        while True:
            choice = input("Enter '1' for domain name or '2' for file name: ").lower()
            if choice == '1':
                domain = input("Enter the domain name: ")
                return domain
            elif choice == '2':
                filename = input("Enter the name of the file: ")
                if os.path.exists(filename):
                    with open(filename, 'r') as file:
                        return file.read()
                else:
                    print("File not found. Please enter a valid file name.")
            else:
                print("Invalid input. Please enter 'd' or 'f'.")

    def save_output_to_file(output):
        filename = input("Enter the name of the file to save the output (with .txt extension): ")
        if not filename.endswith('.txt'):
            filename += '.txt'
        try:
            with open(filename, 'w') as file:
                file.write(output)
            print(f"Output saved to {filename}")
        except Exception as e:
            print(f"Error occurred while saving the file: {e}")

    def time_machine():
        """Query archive.org."""
        mode = "prefix"  # Hard-coded mode to "prefix"
        host_or_data = get_input_from_file_or_domain()
        
        if os.path.isfile(host_or_data):  # If the input is a file
            data = host_or_data
        else:  # If the input is a domain name
            domains = host_or_data.split()
            urls = []
            total_domains = len(domains)
            found_domains = 0
            for domain in domains:
                found = False
                now = datetime.datetime.now()
                to = str(now.year) + str(now.day) + str(now.month)
                if now.month > 6:
                    fro = str(now.year) + str(now.day) + str(now.month - 6)
                else:
                    fro = str(now.year - 1) + str(now.day) + str(now.month + 6)
                
                for prefix in common_prefixes:
                    formatted_prefix = prefix.format(host=domain)
                    url = "http://web.archive.org/cdx/search?url=%s&matchType=%s&collapse=urlkey&fl=original&filter=mimetype:text/html&filter=statuscode:200&output=json&from=%s&to=%s" % (formatted_prefix, mode, fro, to)
                    try:
                        response = get(url)
                        if response.status_code == 200:
                            try:
                                parsed = response.json()[1:]
                                for item in parsed:
                                    urls.append(item[0])
                                found_domains += 1
                                found = True
                                break
                            except json.JSONDecodeError as e:
                                print(f"Failed to parse JSON response from {url}. Error: {e}")
                        else:
                            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
                    except ConnectionError as e:
                        print("Connection Error occurred for prefix:", formatted_prefix)
                        print("Error:", e)
                        continue  # Continue to the next prefix
                
                if not found:
                    print(f"No domains found for {domain}.")
            
            data = "\n".join(urls)
            print(f"Found {found_domains} out of {total_domains} domains.")
        
        return data, len(urls)


    if __name__ == "__main__":
        result, num_domains = time_machine()
        print(f"Found {num_domains} domains.")
        if num_domains > 0:
            print("Archived URLs:")
            print(result)
            save_output_to_file(result)

    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    menu2()   
    
def script26():
    import ssl
    from cryptography import x509
    from cryptography.hazmat.backends import default_backend
    import certifi
    import os
    from concurrent.futures import ThreadPoolExecutor
    from tqdm import tqdm

    def fetch_certificate(hostname):
        try:
            # Create SSL context using certifi CA certificates
            context = ssl.create_default_context(cafile=certifi.where())

            with ssl.create_connection((hostname, 443)) as sock:
                # Fetch SSL/TLS certificate
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    # Get SSL/TLS certificate
                    cert_der = ssock.getpeercert(binary_form=True)

            return cert_der
        except Exception as e:
            print(f"Error fetching certificate for {hostname}: {e}")
            return None

    def extract_subdomains(cert_der, domain):
        try:
            # Parse the certificate
            cert = x509.load_der_x509_certificate(cert_der, default_backend())

            # Extract subdomains from SAN extension
            subdomains = []
            for ext in cert.extensions:
                if isinstance(ext.value, x509.SubjectAlternativeName):
                    for name in ext.value:
                        if isinstance(name, x509.DNSName):
                            subdomain = name.value
                            if not subdomain.startswith("*."):  # Filter out subdomains starting with .*
                                if subdomain == domain:
                                    subdomains.append(f"{subdomain} (check)")
                                else:
                                    subdomains.append(subdomain)

            return subdomains
        except Exception as e:
            print(f"Error extracting subdomains: {e}")
            return []

    def fetch_subdomains(domain):
        cert_der = fetch_certificate(domain)
        if cert_der:
            return extract_subdomains(cert_der, domain)
        else:
            return []

    def fetch_subdomains_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                domains = [line.strip() for line in file.readlines()]
            subdomains = []
            with ThreadPoolExecutor(max_workers=10) as executor:
                for result in tqdm(executor.map(fetch_subdomains, domains), total=len(domains), desc="Fetching Subdomains"):
                    subdomains.extend(result)
            return subdomains
        except FileNotFoundError:
            print("File not found.")
            return []

    def save_subdomains_to_file(subdomains, output_file):
        try:
            with open(output_file, 'w') as file:
                for subdomain in subdomains:
                    file.write(subdomain + '\n')
            print(f"Subdomains saved to {output_file}")
        except Exception as e:
            print(f"Error saving subdomains to {output_file}: {e}")

    def ma():
        try:
            print("Choose an option:")
            print("1. Enter a single domain")
            print("2. Enter Dommain list from .txt file")
            choice = input("Enter your choice (1 or 2): ").strip()

            if choice == '1':
                domain = input("Enter the domain: ").strip()
                subdomains = fetch_subdomains(domain)
            elif choice == '2':
                file_name = input("Enter the filename of the text file: ").strip()
                subdomains = fetch_subdomains_from_file(file_name)
            else:
                print("Invalid choice.")
                return

            if subdomains:
                output_file = input("Enter the output filename: ").strip()
                save_subdomains_to_file(subdomains, output_file)
            else:
                print("No subdomains found.")
        except KeyboardInterrupt:
            print("\nCtrl+C detected. Saving results, if any...")
            if subdomains:
                output_file = input("Enter the output filename: ").strip()
                save_subdomains_to_file(subdomains, output_file)
                print("Results saved.")
            else:
                print("No subdomains found. Exiting...")
            return

    if __name__ == "__main__":
        ma()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu2()   

def menu2():
    OKCYAN = '\033[96m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    WARNING = '\033[93m'
    OKYELLOW = '\033[33m'
    OKPURPLE = '\033[35m'
    ORANGE = '\033[38;5;208m'
    Magenta = '\033[38;5;201m'
    Olive = '\033[38;5;142m'
    OKlime = '\033[38;5;10m'
    OKBLUE = '\033[38;5;21m'
    OKPINK = '\033[38;5;219m'

    banner_lines = [        
        Magenta + "██████╗ ██╗   ██╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ ███████╗ ®" + ENDC,
        Magenta + "██╔══██╗██║   ██║██╔════╝ ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝" + ENDC,
        Magenta + "██████╔╝██║   ██║██║  ███╗███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝███████╗" + ENDC,
        Magenta + "██╔══██╗██║   ██║██║   ██║██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗╚════██║" + ENDC,
        Magenta + "██████╔╝╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║███████║" + ENDC,
        Magenta + "╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝" + ENDC,
        ORANGE + "██████╗ ██████╗  ██████╗" + OKPINK + "this script is a tool used for creating and scanning" + ENDC,
        ORANGE + "██╔══██╗██╔══██╗██╔═══██╗" + OKPINK + "domains, ips or ranges for for testing" + ENDC,
        ORANGE + "██████╔╝██████╔╝██║   ██║" + OKPINK + "usage of this script is soley upto user discretion" + ENDC,
        ORANGE + "██╔═══╝ ██╔══██╗██║   ██║" + OKPINK + "and should understand that useage of this script" + ENDC,
        ORANGE + "██║     ██║  ██║╚██████╔╝" + OKPINK + "may be concidered an attack on a data network" + ENDC,
        ORANGE + "╚═╝     ╚═╝  ╚═╝ ╚═════╝" + OKPURPLE + "use on your own network or get permission first" + ENDC,
        ORANGE + "All rights reserved 2022-2024 ♛: ®" + ENDC,      
        OKYELLOW + "Programmed by King  t.me/ssskingsss ☏: " + OKYELLOW + "®" + ENDC,
    ]
    
    for line in banner_lines:
        print(line)
    print("""
    ===================================
              Menu                
    ===================================
    Hit enter to return to the main menu
    17. CDN Finder                   22. ASN2
    18. Free Proxies                 23. Web Crawler
    19. Vmess/Trojan/SS/HYS/Vless    24. WayBack
    20. Host proxy checker           25. Offline Subdomain enum
    21. D.R.ACCESS/HOSTCHECKER V2 
    """)
    
    choice = input("Enter your choice: ")
    if choice == '1':
        print("Returning to BUGHUNTERS PRO...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit
        script0()
        return# Return to the main menu
    elif choice == '17':
        os.system('cls' if os.name == 'nt' else 'clear')
        script19()  
    elif choice == '18':
        os.system('cls' if os.name == 'nt' else 'clear')
        script21()
    elif choice == '19':
        os.system('cls' if os.name == 'nt' else 'clear')
        teamerror()
    elif choice == '20':
        os.system('cls' if os.name == 'nt' else 'clear')
        script20()
    elif choice == '21':
        os.system('cls' if os.name == 'nt' else 'clear')
        script22()
    elif choice == '22':
        os.system('cls' if os.name == 'nt' else 'clear')
        script23()
    elif choice == '23':
        os.system('cls' if os.name == 'nt' else 'clear')
        script24()
    elif choice == '24':
        os.system('cls' if os.name == 'nt' else 'clear')
        script25()
    elif choice == '25':
        os.system('cls' if os.name == 'nt' else 'clear')
        script26()                                                                                           
    else:
        print("Returning to BUGHUNTERS PRO...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        script0()
        return  # Return to the main menu

def menu():
  print("Menu: use option 0 for the help menu")
  print("1.""\033[96mSUBDOMAIN ENUM\033[0m""             2.)""\033[32mSUBDOMAIN FINDER\033[0m")                       
  print("3.""\033[95mWEBSOCKET\033[93m SCANNER\033[0m""          4.)""\033[33mHOST CHECKER\033[0m")
  print("5.""\033[32mFile Processing Script\033[0m""     6.)""\033[95mREVULTRA\033[0m")
  print("7.""\033[95mIP\033[0m""\033[93m GEN \033[0m""                    8.)""\033[96mTLS\033[32m checker\033[0m")
  print("9.""\033[95mOpen Port Checker\033[0m""         10.)""\033[96mserver info n/a\033[32m checker\033[0m")
  print("11.""\033[94mDOMAIN EXTENTION FINDER\033[0m""  12.)""\033[96mDORK SCANNER\033[0m")
  print("13.""\033[33mDOMAIN 2 IPS\033[0m""             14.)""\033[91m???\033[0m")
  print("15.""\033[33murlscan.io\033[0m""               16.)""\033[38;5;208mMore Options\033[0m")
  print("99.""\033[91mQuit\033[0m")
  
menu_loop = True
time.sleep(0.5)
while menu_loop:
  menu()
  
  choice = input("Enter your choice: ")
  if choice == "1":
    os.system('cls' if os.name == 'nt' else 'clear')
    script1()
  if choice == "0":
    os.system('cls' if os.name == 'nt' else 'clear')
    help()
  if choice == "2":
    os.system('cls' if os.name == 'nt' else 'clear')
    script2()
  if choice == "3":
    os.system('cls' if os.name == 'nt' else 'clear')
    script3()
  if choice == "4":
    os.system('cls' if os.name == 'nt' else 'clear')
    script4()
  if choice == "5":
    os.system('cls' if os.name == 'nt' else 'clear')
    script5()
  if choice == "6":
    os.system('cls' if os.name == 'nt' else 'clear')
    script6()
  if choice == "7":
    os.system('cls' if os.name == 'nt' else 'clear')
    script7()
  if choice == "8":
    os.system('cls' if os.name == 'nt' else 'clear')
    script8()
  if choice == "9":
    os.system('cls' if os.name == 'nt' else 'clear')
    script9()
  if choice == "10":
    os.system('cls' if os.name == 'nt' else 'clear')
    script10()
  if choice == "11":
    os.system('cls' if os.name == 'nt' else 'clear')
    script11()
  if choice == "12":
    os.system('cls' if os.name == 'nt' else 'clear')
    script12()
  if choice == "13":
    os.system('cls' if os.name == 'nt' else 'clear')
    script13()
  if choice == "kingscript":
    os.system('cls' if os.name == 'nt' else 'clear')
    kingscript()
  if choice == "websocket":
    os.system('cls' if os.name == 'nt' else 'clear')
    script16()
  if choice == "14":
    os.system('cls' if os.name == 'nt' else 'clear')
    script17()
  if choice == "15":
    os.system('cls' if os.name == 'nt' else 'clear')
    script18()           
  if choice == "16":
    os.system('cls' if os.name == 'nt' else 'clear')
    menu2()
  if choice == "17":
    os.system('cls' if os.name == 'nt' else 'clear')
    script19()
  if choice == "18":
    os.system('cls' if os.name == 'nt' else 'clear')
    script21()
  if choice == 'ult':
    os.system('cls' if os.name == 'nt' else 'clear')
    ult()  
  if choice == "99":
    print("\033[96mThank you for using\nBUGHUNGERS PRO ®\033[0m")
    time.sleep(1)
    print("\033[96mHave Nice Day ;) \033[0m")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    menu_loop = False
    
if __name__ == "__main__":
    menu()