import requests
import json
import time

url = "http://api.dizhensubao.getui.com/api.htm"

aday = 86400 # a day miliseconds

startTime = int(round((time.time()-aday)*1000)) # timestamp 24h before

data = {"action":"requestMonitorDataAction","startTime":startTime,"dataSource":"CEIC"}

data_json = json.dumps(data)

res = requests.post(url,  data_json)

earchjson = json.loads(res.text)


data = earchjson["values"]

def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

for i in range(len(data)):
    print(data[i]['loc_name']+"\t于"
    +str(timeStamp(data[i]['time']))+
    "\t发生里式"+str(data[i]['mag'])+"级地震\t"+
    "(经度："+str(data[i]['longitude'])+"，纬度："+str(data[i]['latitude'])+", 震源深度："+str(data[i]['depth']/1000)+"千米)")


input("\n\n按下任意键退出")


