def status_code(url):
    import requests
    from rich import print
    print('-'*50)
    print(' '*18+"[bold blue]Status Code")
    print('-'*50)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if response.status_code == 200:
            print(f"[yellow]URL:[/] {url}[green] is OK[/] | status code : {response.status_code}")
        else :
                print(f"[purple]URL:[/] {url}[red] is NOT OK [/]| status code : {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("[red]Connection failed. Check the URL or your internet connection.[/]")

    except requests.exceptions.Timeout:
        print("[red]Request timed out. The server may be slow or unreachable.[/]")

    except requests.exceptions.HTTPError as error:
        print(f"[red]HTTP error:[/] {error}")

    except requests.exceptions.RequestException as error:
        print(f"[red]Request failed:[/] {error}")

    except Exception as error:
        print(f"[red]Unexpected error:[/] {error}")

