from JsonUtils import *
import requests
import time

url = "https://app.rhapsodyofrealities.org/api/devotional/"
    # Need to be stopped in detailed loop of len ju,p
querystring = {"date":"2022-03-12"}

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

def check_done(runnable:str,alldata:str)->bool:
    data = list(loadJson(alldata).keys())
    runit = loadJson(runnable)
    print('checked')
    if(list(filter(lambda left:left not in data,runit)) == []):
        print('returned true')
        return True
    else:
        return False
# response = []

if __name__ == '__main__':
    runner = loadJson('run/runnables')
    s = requests.Session()
    while(not check_done('run/runnables','run/alldata')):
        dones =loadJson('run/alldata')
        print('not done check!')
        tasks = [el for el in runner if el not in dones.keys()]
        for i in tasks:
            time.sleep(1)
            response = s.request("GET", url+i, data=payload, headers=headers)
            if(response.status_code == 200):
                print('sent-'+i.split('=')[-1].split('\n')[0])
                if(response.text == "{\n    \"result\": []\n}{\n    \"result\": []\n}"):
                    updateJson('run/alldata', {i:"ThatWierdInputThingy"})
                    print("Skipper of Error")
                else:
                    try:
                        updateJson('run/alldata', {i:response.json()['result'][0]})
                    except KeyError:
                        updateJson('run/alldata', {i:'Non Existant page by KeyError no results'})

            elif(200 < response.status_code < 500):
                updateJson('run/alldata', {i:'Non Existant page by status code'+str(response.status_code)})
                print('doesnt exists-'+i.split('=')[-1].split('\n')[0])
            else:
                print(response.json())
                break
            
        

# skipped dates exist