import pandas as pd
import json


if __name__ == '__main__':
    
    openappsec_df = pd.read_json('./openappsec/sqli_parsed.json')
    httpparams_df = pd.read_json('./httpparams/sqli_parsed.json')
    kaggle_df     = pd.read_json('./sqli_kaggle/sqli_parsed.json')
    sqlmap_df     = pd.read_json('./sqlmap/sqli_parsed.json')

    df = pd.concat([openappsec_df, httpparams_df, kaggle_df, sqlmap_df], axis=0, ignore_index=True)
    df.reset_index(drop=True, inplace=True)

    df = df.drop_duplicates()
    df.reset_index(drop=True, inplace=True)

    df = df.iloc[:, 0].to_list()

    with open('sqli_dataset.json', 'w') as file:
        json.dump(df, file, indent=4)
            

    

