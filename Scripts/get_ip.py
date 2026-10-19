from rich import print
import socket
from urllib.parse import urlsplit
def host_ip(url):
    print('-'*50)
    print(' '*18+"[bold blue]IP Address")
    print('-'*50)
    try: 
        parsed_url = urlsplit(url if '://' in url else f"//{url}")# > example.com:8000
        domain = parsed_url.hostname # > exmaple.com
        if not domain :
            print("[red]Invalid URL: hostname is missing.[/]")
            return
        ip_domain = socket.gethostbyname(domain)
        print(f"[purple]Target Domain :[/] {domain}")
        print(f'[purple]Domain IP :[/] {ip_domain}')

    except ValueError as error :
        print(f'[red]Invalid URL format:[/] {error}')
    except OSError as error :
        print(f'[red]System network error:[/] {error}')
    except socket.gaierror:
        print(f'[red]Could not resolve the domain:{domain}[/]')
        print('[green]Some help:\n' \
        '\t   Enter the domain without(https://..)\n' \
        '\t   Check the domain name clearly ')