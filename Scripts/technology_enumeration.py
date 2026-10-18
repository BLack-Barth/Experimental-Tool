def technology_enumeration(url):
    import requests
    from rich import print
    print('-'*50)
    print(' '*18+"[bold blue]Technology Enumeration")
    print('-'*50)
    try:
        headers = {
    "User-Agent": (
        "BugBounty-Hunter-BLackBart "
        "Mozilla/5.0 (X11; Linux x86_64) " 
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}
        response = requests.get(url ,headers=headers , timeout= 10)
        for key,value in response.headers.items():
            print(f'[yellow]{key}[/] : {value}')

        response.raise_for_status()
        
    except requests.exceptions.ConnectionError:
        print("[red]Connection failed. Check the URL or your internet connection.[/]")

    except requests.exceptions.ConnectTimeout:
        print("[red]Connection timed out, The server may be slow or unreachable.[/]")

    except requests.exceptions.HTTPError as http_error:
        print(f'[red]HTTP Error:[/] {http_error}')

    except requests.exceptions.RequestException as request_error:
        print(f'[red]Request Faild:[/] {request_error}')

    except requests.exceptions.TooManyRedirects:
        print("[red]Redirect Error:[/] The URL caused too many redirects (redirect loop).")
     
    except Exception as error:
        print(f'[red]Unexpected Error:[/] {error}')
