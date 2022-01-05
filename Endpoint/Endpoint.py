import requests
import json

class Endpoint:
    def __init__(self, ip) -> None:
        self.ip = ip
        self.worker_url = f'http://{self.ip}:9001/worker'
        self.req_url = f'http://{self.ip}:9001/req'
        self.headers = {'Content-Type': 'application/json'}

    def __SendReq(self, body: str):
        res = requests.post(url=self.worker_url, data=body, headers=self.headers)
        
    
    def CreateContainer(self):
        body = {'action': 'create'}