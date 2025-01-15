# import datetime

# print(datetime.datetime.now())


import json

jsondata = '{"brand":"ford","name":"ram"}'

a=json.loads(jsondata)
print(a['brand'])