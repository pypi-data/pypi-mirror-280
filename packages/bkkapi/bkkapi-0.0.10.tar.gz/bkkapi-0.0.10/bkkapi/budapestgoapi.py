import requests

class BKKClient:
    def __init__(self,key: str, version = 4, appVersion = "0.0.1"):
        self.key = key
        self.version = version
        self.appVersion = appVersion
    
    def __str__(self):
        return f"BKK API Client with the following key: {self.key}"
    def get_bubi(self, includeReferences: str = "true" or "false"):
        self.includeReferences = includeReferences
        r = requests.get(f"https://futar.bkk.hu/api/query/v1/ws/otp/api/where/bicycle-rental.json?key={self.key}&version={self.version}&appVersion={self.appVersion}&includeReferences={self.includeReferences}")
        return Bubi(r.json())
    
    def alert_search(self, query: str, start:int, stop: int, minResult: int,   includeReferences: str = "true" or "false"):
        self.includeReferences = includeReferences
        self.query = query
        self.start = start
        self.stop = stop
        self.minResult = minResult
        r = requests.get(f"https://futar.bkk.hu/api/query/v1/ws/otp/api/where/alert-search?query={self.query}&start={self.start}&end={self.stop}&minResult={self.minResult}&appVersion={self.appVersion}&version={self.version}&includeReferences={self.includeReferences}&key={self.key}")
        return AlertResult(r.json())
class Bubi:
    def __init__(self, request: dict) -> None:
        self.request = request
        self.time = self.request["currentTime"]
        self.status = self.request["status"]
        self.code = self.request["code"]
        self.text = self.request["text"]
        self.data = self.request["data"]
    def __str__(self):
        return f"Bubi object received at {self.time}"
        
class AlertResult:
    def __init__(self, request: dict) -> None:
        self.request = request
        self.time = self.request["currentTime"]
        self.status = self.request["status"]
        self.code = self.request["code"]
        self.text = self.request["text"]
        self.data = self.request["data"]
    def __str__(self):
        return f"Alert search result object received at {self.time}"