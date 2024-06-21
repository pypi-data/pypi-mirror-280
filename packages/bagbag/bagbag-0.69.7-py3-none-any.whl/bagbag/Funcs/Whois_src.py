from .whois import whois 
from .whois.parser import WhoisError 


def Whois(domain:str, retryTimes:int=3, useCommand:bool=False) -> dict | None:
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