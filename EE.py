import pandas as pd
import json
import jsonlines
import math

def default_dump_json(obj, json_file_path, encoding='utf-8', ensure_ascii=False, indent=2, **kwargs):
    with open(json_file_path, 'w', encoding=encoding) as fout:
        json.dump(obj, fout,
                  ensure_ascii=ensure_ascii,
                  indent=indent,
                  **kwargs)

def default_load_json(json_file_path, encoding='utf-8', **kwargs):
    with open(json_file_path, 'r', encoding=encoding) as fin:
        tmp_json = json.load(fin, **kwargs)
    return tmp_json



schema = pd.read_excel('./data/our_schema.xlsx')
event_type_list = schema['事件类型'].tolist()
event_subtype_list = schema['子事件类型'].tolist()
last_class = event_type_list[0]
out = []
for idx,c in enumerate(event_type_list):
    if(not pd.isna(c)):
        last_class = c
    example = {}
    example['event_type'] = last_class+'-'+event_subtype_list[idx]
    role_list = schema.iloc[idx]
    example['role_list'] = []
    for role in role_list[2:]:
        if(pd.isna(role)):
            break
        example['role_list'].append({'role':role})
    example['class'] = last_class
    out.append(example)
with open("./data/our_event_schema.json", 'w', encoding='utf-8') as f:
    for dic in out:
        json.dump(dic, f, ensure_ascii=False)
        f.write("\n")
    f.close()
print("A")

