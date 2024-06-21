from .whois import whois 

def DomainWhois(domain:str, retryTimes:int=3, useCommand:bool=False) -> dict | None:
        for _ in range(retryTimes):
            try:
                if useCommand:
                    return dict(whois(domain, command=True, executable='whois'))
                else:
                    return dict(whois(domain))
            except:
                pass 
        
        return None

    # whois(domain, command=True, executable='whois') # 使用系统的命令行客户端

def IPWhois(ip:str) -> dict | None:
    from ipwhois import IPWhois
    obj = IPWhois(ip)
    result = obj.lookup_rdap(
        depth=10, 
        inc_raw=True,
        nir_field_list=None, 
        asn_methods=None,
    )
    return result