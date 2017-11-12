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
    b = []
    l = len(data["dataset"]["data"]) 
    while i < l-1 :
        y_temp1 = data["dataset"]["data"][i][5]
        y_temp2 = data["dataset"]["data"][i][5] - data["dataset"]["data"][i][1]
        x_temp = data["dataset"]["data"][i][0]
	a = np.append(a, [x_temp, y_temp1])
	b = np.append(a, [x_temp, y_temp2])
	i = i + 1
    #post a b

elif UnitTime == 2 :
    i = 0
    a = []
    b = []
    l = len(data["dataset"]["data"])
    while i < l-5 :
        y_temp1 = data["dataset"]["data"][i][5]
        y_temp2 = data["dataset"]["data"][i][5] - data["dataset"]["data"][i+4][1]
        x_temp = data["dataset"]["data"][i][0]
	a = np.append(a, [x_temp, y_temp1])
        b = np.append(a, [x_temp, y_temp2])
	i = i + 5
    #post a b

elif UnitTime == 3 :
    i = 0
    a = []
    b = []
    l = len(data["dataset"]["data"])
    while i < l-31 :
        x_temp = data["dataset"]["data"][i][0]
        if x_temp[8] == 0 and x_temp[9] == 1 :
            y_temp1 = data["dataset"]["data"][i][5]
            y_temp2 = data["dataset"]["data"][i][5] - data["dataset"]["data"][i+30][1]
            a = np.append(a, [x_temp, y_temp1])
            b = np.append(a, [x_temp, y_temp2])
	i = i + 1
    #post a b

else :
    #post error code
