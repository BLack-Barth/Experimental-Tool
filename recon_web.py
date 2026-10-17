import argparse
import Scripts
from pyfiglet import print_figlet

print('-'*30)
print_figlet("recon")
print('-'*30)
parser = argparse.ArgumentParser(description="Network Reconnaissance")
parser.add_argument("command",
                    choices=['helps','ip','-fp','sc','-te','-u'],
                    help="")
arg = parser.parse_args()

if arg.command == 'helps':
    from Scripts.helps import helps
    helps()
if arg.command == 'ip':
    from Scripts.get_ip import host_ip
    host_ip()
if arg.command == '-fp':
    from Scripts import fingerprinting
    fingerprinting()
if arg.command == 'sc':
    from Scripts.status_code import status_code
    status_code()
if arg.command == '-te':
    from Scripts import technology_enumeration
    technology_enumeration()
if arg.command == '-u':
    from Scripts import url_input
    url_input()

