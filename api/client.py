import requests
from urllib.parse import urljoin

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/') + '/'
        self.session = requests.Session()

    def get(self, path: str, **kwargs):
        url = urljoin(self.base_url, path.lstrip('/'))
        return self.session.get(url, **kwargs)

    def post(self, path: str, **kwargs):
        url = urljoin(self.base_url, path.lstrip('/'))
        return self.session.post(url, **kwargs)
