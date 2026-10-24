def fingerprinting(url):
    from rich import print
    import requests
    print('-'*50)
    print(' '*18+"[bold blue]FingerPrinting")
    print('-'*50)
    try:
        headers = {
            "User-Agent": (
                "BugBountyHunter-hackerOne "
                "Mozilla/5.0 (X11; Linux x86_64) " 
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url ,headers=headers ,timeout= 10)
        response_headers = response.headers
        server = response_headers.get("Server","Unknown")
        os_guess = "Unknown / Hidden"
        if "microsoft-iis" in server.lower():
            if '8.5' in server:
                os_guess = "Windows Server 2012 R2"
            elif '10.0' in server :
                os_guess = "Windows Server 2016/2019/2022/2025"
            elif '7.5' in server :
                os_guess = "Windows Server 2008 R2"
            else:
                os_guess = "Windows Server"
        elif "ubuntu" in server.lower():
            os_guess = "Ubuntu Server Linux"
        elif "debian" in server.lower():
            os_guess = "Debian Server Linux"
        elif "centos" in server.lower():
            os_guess = "CentOS Server Linux"
        print(f'[purple]Server:[/] {server} |[purple] OS:[/] {os_guess}')
        powerd = response_headers.get("X-Powered-by","Unknown")
        aspnet = response_headers.get("X-Aspnet-version","Unknown")
        cookie = response_headers.get("Set-cookie","Unknown")
        print(powerd)
        print(aspnet)
        print(cookie)
        print(response_headers)
    except:
        pass