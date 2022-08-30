import pandas as pd
import json
import csv
import ast

def organizing():
    df = pd.read_csv('query_result_2022-08-24T08_59_31.12Z.csv')
    stdf = df['info_1'].apply(json.loads)
    stlst = list(stdf)
    stjson = json.dumps(stlst)
    df = df.join(pd.read_json(stjson))
    del(df['info_1'])
    print(df.head())
    df.to_csv('test.csv')

organizing()

def dict_to_csv():
    filename = open('test.csv', 'r')
    file = csv.DictReader(filename)

    entityids = []
    data = []
    data1=[]
    for col in file:
        entityids.append(col['entity_details_id'])
        data.append(col['0'])
    # print(type(data[0]))
    for da in data:
        res=ast.literal_eval(da)
        data1.append(res)
    # print(data1)
    out = pd.DataFrame.from_dict(data1)
    out['entity_details_id']=entityids

    print(out)
    out.to_csv('family.csv')

dict_to_csv()






