import requests
import numpy as np

#code=<get code from kshitij>
Code = 'ACC'
#UnitTime=<get time unit from kshitij>
UnitTime = 1

response = requests.get('https://www.quandl.com/api/v3/datasets/NSE/'+Code+'.json?api_key=iRtWecmWy_bvJZuP-zu_')
data = response.json()

if UnitTime == 1 :
    i = 0
    a = []
    l = len(data["dataset"]["data"]) 
    while i < l-1 :
        y_temp = data["dataset"]["data"][i][5]
        x_temp = data["dataset"]["data"][i][0]
	a = np.append(a, [x_temp, y_temp])
	i = i + 1
    #post a

elif UnitTime == 2 :
    i = 0
    a = []
    l = len(data["dataset"]["data"])
    while i < l-1 :
        y_temp = data["dataset"]["data"][i][5]
        x_temp = data["dataset"]["data"][i][0]
	a = np.append(a, [x_temp, y_temp])
	i = i + 5
    #post a

elif UnitTime == 3 :
    i = 0
    a = []
    l = len(data["dataset"]["data"])
    while i < l-1 :
        x_temp = data["dataset"]["data"][i][0]
        if x_temp[8] == 0 and x_temp[9] == 1 :
            y_temp = data["dataset"]["data"][i][5]
            a = np.append(a, [x_temp, y_temp])
	i = i + 1
    #post a

else :
    #post error code
