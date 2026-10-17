from rich import print
import socket
def host_ip():
    print('-'*50)
    print(' '*18+"[bold blue]IP Address"+' '*20)
    print('-'*50)
    try: 
        hostname = socket.gethostname()
        url_ip = input('Enter the domain: ')
        ip = socket.gethostbyname(hostname)
        ip_url = socket.gethostbyname(url_ip)
        print(f'[yellow]Your IP :[/] {ip} |[purple] Domain IP :[/] {ip_url}')

    except socket.gaierror:
        print('[red]The domain does not exist!')
        print('[green]Some help:\n' \
        '\t   Enter the domain without(https://..)\n' \
        '\t   Check the domain name clearly ')