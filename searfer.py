import random
import string

import threading

import requests


class Searfer:
    def __init__(self, *, threads: int=1) -> None:
        self.threads = threads
        
    def main(self) -> list[str, requests.Response]:
        domain = self.domain(random.randint(2, 50))
            
        url = self.url(domain=domain, protocole='http', code='com')
        
        try:
            response = requests.get(url)
                    
            print(url, response)
            
            return [url, response]
        except requests.ConnectionError:
            pass
            
    def domain(self, lenght: int=2) -> None:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(lenght))
        
    def url(self, *, protocole: str, domain: str, code: str) -> str:
        return f'{protocole}://{domain}.{code}'
        
    def run(self) -> None:
        for _ in range(self.threads):
            threading.Thread(target=self.main())
            
