def fingerprinting(url):
    from rich import print
    import requests
    print('-'*50)
    print(' '*18+"[bold blue]FingerPrinting")
    print('-'*50)
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) " 
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url ,headers=headers ,timeout= 10)
        resp_headers = response.headers
        print('ok', resp_headers)
        for x,y in response.headers.items() :
            print(f'[yellow]{x} :[/] {y}')

    except:
        pass