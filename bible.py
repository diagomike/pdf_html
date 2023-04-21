import requests
from JsonUtils import *
url = "https://app.rhapsodyofrealities.org/api/devotional/"

querystring = '2022-03-12'

payload = ""

headers = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-GPC": "1",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "__tawkuuid=e::rhapsodyofrealities.org::xDAS4OMtkDhI3RrEjIk1W/Yc/mkBgFh/AMus4uhLcUPBBwS4fEBWl4zV8gNoa8eU::2; sourceurl=/zone/official; sourceid=official; _ca_MNL=1; __stripe_mid=ff673f7e-2ee4-4cb7-b3a2-2c7d706813c787e552; __stripe_sid=8406d2d2-345d-4c07-afad-e8e619d1300301d763"
}


response = requests.request("GET", url+querystring, data=payload, headers=headers)

print(response.status_code)
saveJson('test',response.json())