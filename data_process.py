import json


out = []
example = {}
with open('./data/final_event_schema.json') as f:
    lines = f.readlines()
    for data in lines:
        pdata = json.loads(data)
        example[pdata['event_type']] = []
        for role in pdata['role_list']:
            example[pdata['event_type']].append(role['role'])
print(example)

