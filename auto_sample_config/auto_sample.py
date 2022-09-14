import pandas as pd
import json
import os

if __name__ == '__main__':
    df = pd.read_csv('./sample_list.csv', header=None)
    sample_json = json.load(open(r'../scenario/3d_dambreak.json'))
    config_json = json.load(open(r'../config/config.json'))
    for i in range(len(df)):
        if i < 67:
            continue
        _data = df.iloc[i]
        _json = sample_json
        _json['fluid']['objs'][0]['start_pos'][0] = _data.iloc[0]
        _json['fluid']['objs'][0]['start_pos'][1] = _data.iloc[1]
        _json['fluid']['objs'][0]['start_pos'][2] = _data.iloc[2]
        _json['fluid']['objs'][0]['end_pos'][0] = _data.iloc[3]
        _json['fluid']['objs'][0]['end_pos'][1] = _data.iloc[4]
        _json['fluid']['objs'][0]['end_pos'][2] = _data.iloc[5]
        json.dump(_json, open(r'scene_temp.json', 'w'))

        _json = config_json
        _json['auto_start'] = True
        _json['auto_stop'] = True
        _json['save_csv_folder'] = os.path.join(r'E:\dufeilong\datasets', str(i))
        json.dump(_json, open(r'config_temp.json', 'w'))

        os.system(r'python ..\main.py -c config_temp.json -s scene_temp.json')

