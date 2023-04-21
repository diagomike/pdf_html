import json
import codecs
def loadJson(filename:str)->dict:
    with open(filename+'.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        return data

def saveJson(filename:str,data:dict):
    with open(filename+".json", "w", encoding='utf8') as outfile:
        json.dump(data, outfile)
    print("Saved "+filename+".json")

def updateJson(filename:str,data:dict):
    temp = loadJson(filename)
    temp.update(data)
    saveJson(filename,temp)

def loadHtml(filename:str)->str:
    f=codecs.open(filename+".html", 'r')
    return f.read()
