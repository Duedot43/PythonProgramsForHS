import requests
import json
def getval(file):
    res = requests.get("http://xkcd.com/" + file + "/info.0.json")
    if res.status_code == 200:
        p2 = str(res.text)
        return p2
jsont = json.load(getval(1))
print(jsont)
