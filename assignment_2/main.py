import requests
import os 
import json 
import urllib.request
import re 

def parseJson():
    url = "https://gitlab.com/im-batman/simple-data-assestment/-/raw/main/superman.json"
    
    response = urllib.request.urlopen(url)
    js = response.read()
    writefileobj = open('events.json','wb')
    writefileobj.write(js)
    writefileobj.close()
    
# using regex to split the json object
    with open('events.json') as f:
        r = re.split('(\{.*?\})(?= *\{)', f.read())
    
    eventlist = []
    for ele in r:
        each = ele.splitlines()
        eventlist.extend(each)
    print('final rowcount:', len(eventlist))
    sortedeventlist = sorted(eventlist,key=lambda x: x[0])

            
    return sortedeventlist
   
def writefile(res):
    unique = { repr(each): each for each in res }.values()
    
    try:
        with open('final_result_event.json', 'w', encoding='utf-8') as f:
            for d in unique:
                f.write(d + '\n')
        print('final_result_event.json has been created')
    except IOError as e:
        print(e)
        
def main():
    res = parseJson()
    writefile(res)
    
if __name__ == "__main__":
    main()
