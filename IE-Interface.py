import requests
import json


data = {"sentence":"实地探访胡鑫宇家乡：学校围墙装有铁丝网，叔叔说他内向话不多","type":"","access":"","task":"EE","lang":"chinese"}
data = json.dumps(data)
data = json.dumps(data)
# test = json.loads(data)
# test = json.loads(test)
header = {
    'Accept': 'application/json',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': '10.102.64.221:5000',
    'Origin': 'http://10.102.64.221:5000'
}
try:
    response = requests.post("http://10.102.64.221:5000/api/v1/updateStaff", data=data, headers=header)
except Exception as e:
    print('---chatbot---')
    print(e)

a = response
result = json.loads(a.content)


print(response)
