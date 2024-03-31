import pandas as pd
import json


if __name__ == '__main__':
    
    df_1 = pd.read_json('./openappsec/legitimate_1.json')
    df_2 = pd.read_json('./openappsec/legitimate_2.json')
    df_3 = pd.read_json('./openappsec/legitimate_3.json')
    df_4 = pd.read_json('./openappsec/legitimate_4.json')
    df_5 = pd.read_json('./openappsec/legitimate_5.json')
    df_6 = pd.read_json('./openappsec/legitimate_6.json')

    df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6], axis=0, ignore_index=True)
    df.reset_index(drop=True, inplace=True)

    df = df.iloc[:, 0].to_list()

    with open('legitimate_dataset.json', 'w') as file:
        json.dump(df, file, indent=4)