DOS Attack Tool by Eyna
Disclaimer ⚠️

This tool is created for educational purposes only and should only be used in environments where you have permission to perform penetration testing. Any misuse of this tool is the responsibility of the user. You should never use it against unauthorized targets. Illegal activities are not encouraged or supported by the creator of this tool.
Features

This tool provides multiple DOS (Denial of Service) attack methods. Each attack type can be used to test the stability and security of networks or systems under authorized conditions.
Available Attacks

    UDP Flood: Flood a target with User Datagram Protocol (UDP) packets.
    ICMP Flood: Send a large number of ICMP (ping) requests to the target.
    SYN Flood: Exhaust the target's resources by sending SYN packets.
    ACK Flood: Send a flood of ACK (Acknowledgement) packets to overwhelm a target.
    XMAS Flood: Utilize TCP packets with unusual flag combinations to perform an attack.
    HTTP GET/POST Flood: Send GET/POST requests to a target URL to flood HTTP servers.
    Slowloris Attack: Open multiple slow HTTP connections to exhaust a server’s capacity.

Installation
Requirements

This tool requires the following libraries to be installed:

    Python 3.x
    Scapy (pip install scapy)
    Colorama (pip install colorama)
    Requests (pip install requests)

Setup

    Clone the Repository
    Clone this repository to your local machine:

    bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Install Dependencies
Install the necessary Python packages:

bash

    pip install -r requirements.txt

    Run as Administrator/Root
    Ensure you are running the script with the proper privileges (Administrator for Windows or Root for Linux).

Usage

    Run the Script

    Run the script by executing:

    bash

python dos_tool.py

Choose an Attack Type
From the main menu, select your attack type:

scss

    ---------------
    [1] DOS Attacks
    [2] NMAP (Coming soon...)
    --------------- 

    After selecting DOS Attacks, you can choose one of the available attack types.

    Example Usage: UDP Flood Attack
    After selecting the UDP Flood option, provide the following inputs:
        Target IP
        Target Port
        Duration of the attack (in seconds)

    Exit
    You can exit the program by choosing the exit option from the menu.

Attack Descriptions

    UDP Flood:
    A UDP flood attack sends a large number of UDP packets to random ports on a target system, causing the system to respond with ICMP "Destination Unreachable" messages.

    ICMP Flood:
    An ICMP flood attack sends multiple ICMP packets (pings) to a target, overwhelming the system's network resources.

    SYN Flood:
    A SYN flood attack sends multiple SYN packets (used to initiate TCP connections) to the target, consuming resources and potentially crashing the target.

    ACK Flood:
    An ACK flood sends a series of ACK packets to the target, often used to confuse or crash a system.

    XMAS Flood:
    The XMAS flood sends TCP packets with unusual flag combinations, often used to identify open ports and confuse the target.

    HTTP GET/POST Flood:
    This attack sends multiple HTTP GET and POST requests to a target server to overwhelm its resources.

    Slowloris:
    The Slowloris attack opens many HTTP connections to the server and keeps them open as long as possible, using a minimal number of resources.

NMAP (Coming Soon)

Future versions of this tool may include the integration of nmap functionality to perform network mapping and reconnaissance.
Contributing

Contributions to the project are welcome! You can fork the repository, make your changes, and submit a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Special thanks to the developers of the libraries used in this project, including:

    Scapy
    Colorama
    Requests

Disclaimer Again!

This tool should only be used in environments where you have explicit permission from the owner to test their systems. Misuse of this tool can result in serious legal consequences.

Let me know if you want any further changes!
