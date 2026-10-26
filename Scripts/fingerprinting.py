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
        # -------part1: scann type server--------
        response = requests.get(url ,headers=headers ,timeout= 10)
        response_headers = response.headers
        server = response_headers.get("Server","Hidden")
        os_guess = "Unknown / Hidden"
        if "microsoft-iis" in server.lower():
            if '8.5' in server:
                os_guess = "Windows Server 2012 R2"
            elif '8.0' in server:
                os_guess = "Windows Server 2012"
            elif '10.0' in server :
                os_guess = "Windows Server 2016/2019/2022/2025"
            elif '7.5' in server :
                os_guess = "Windows Server 2008 R2"
            elif '7.0' in server:
                os_guess = "Windows Server 2008"
            elif '6.0' in server :
                os_guess = "Windows Server 2003"
            elif '5.0' in server:
                os_guess = "Windows Server 2000"
            else:
                os_guess = "Windows Server"
        elif "ubuntu" in server.lower():
            os_guess = "Ubuntu Server Linux"
        elif "debian" in server.lower():
            os_guess = "Debian Server Linux"
        elif "centos" in server.lower():
            os_guess = "CentOS Server Linux"
        
        if server != "Hidden":
            print(
                f"\t[green][+][/][purple]Server:[/] {server} | [purple]OS:[/]"
                f" {os_guess}"
                )
        else:
            print(f"\t[red][-][/][purple]Server & OS: Hidden / Protected")
        #---------part2: scann techologies of server-----------
        powerd_value = response_headers.get("X-Powered-by")
        aspnet_value = response_headers.get("X-Aspnet-version")
        cookie_value = response_headers.get("Set-cookie")
        tech = []
        if powerd_value:
            tech.append(powerd_value)
        if aspnet_value:
            tech.append(f'version:{aspnet_value}')
        if cookie_value:
            if "ASP.NET_SessionId" in cookie_value:
                tech.append(f"ASP.NET Session")
            elif "PHPSESSID" in cookie_value:
                tech.append(f"PHP Backend")
            elif "JSESSIONID" in cookie_value:
                tech.append(f"Java/Tomcat Backend")
            else:
                cookie_name = cookie_value.split("=")[0].strip()
                tech.append(f"Custom cookies:({cookie_name})")
        if tech:
            print(f"\t[green][+][/][purple]Technologies:[/]{', '.join(tech)}")

        #--------part3: scann waf-------
        
        if "cf-ray" in response_headers or "cloudflare" in server.lower():
            waf = "Cloudflare"
            print(f"\t[green][+][/][purple]WAF Detected:[/] {waf}")
        elif "x-amz-cf-id" in response_headers or "cloudfront" in response_headers.get("Via","").lower():
            waf = "Amazon CloudFront"
            print(f"\t[green][+][/][purple]WAF Detected:[/] {waf}")
        elif "x-sucuri-id" in response_headers:
            waf = "Sucuri CloudProxy"
            print(f"\t[green][+][/][purple]WAF Detected:[/] {waf}")
        else:
            waf = "\t[red][-]No WAF Detected"
            print(waf)
        #---------part4:scann headers security---------
        security_headers = [
            'X-Frame-Options',
            'Strict-Transport-Security',
            'Content-Security-Policy',
            'X-Content-Type-Options'
        ]
        for sec_hd in security_headers:
            if sec_hd in response_headers:
                print(f"\t[green][+][/]{sec_hd} : [green]Enabled[/]")
            else:
                print(f"\t[red][-][/]{sec_hd} : [red]Missing[/]")
    except requests.exceptions.Timeout:
        print("[red]Timeout: Target took too long to respond.")
    except requests.exceptions.ConnectionError:
        print("[red]Connection failed: Target unreachable.")
    except Exception as error:
        print(f"[red]Error during fingerprinting:[/] {error}")