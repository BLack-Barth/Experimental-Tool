import argparse
import Scripts
from pyfiglet import print_figlet

print('-'*30)
print_figlet("recon")
print('-'*30)
parser = argparse.ArgumentParser(description="Network Reconnaissance")
parser.add_argument('-u','--url',required=True,help="Target URL")
parser.add_argument('-ip',action='store_true',help="Acquire target IP")
parser.add_argument('-fp',action='store_true',help="Exploring Server Identity")
parser.add_argument('-sc',action='store_true',help="Monitoring Readiness and Site Response")
parser.add_argument('-te',action='store_true',help="Uncovering Website Technologies and Frameworks")
arg = parser.parse_args()

if arg :
    from Scripts.helps import helps
    helps()
if arg.ip:
    from Scripts.get_ip import host_ip
    host_ip(arg.url)
if arg.fp:
    from Scripts.fingerprinting import fingerprinting
    fingerprinting(arg.url)
if arg.sc:
    from Scripts.status_code import status_code
    status_code(arg.url)
if arg.te:
    from Scripts.technology_enumeration import technology_enumeration
    technology_enumeration(arg.url)

