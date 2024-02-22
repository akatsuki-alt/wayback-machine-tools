from typing import TypedDict, List

import requests

class Url(TypedDict):
    urlkey: str
    timestamp: str
    original: str
    mimetype: str
    statuscode: str
    digest: str
    length: str

def get_urls(domain: str) -> List[Url]:
    req = requests.get(f"http://web.archive.org/cdx/search/cdx?url={domain}&output=json&matchType=prefix")
    return req.json()[1:]
