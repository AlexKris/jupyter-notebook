import os

import pandas as pd

path = '/Users/admin/Documents/k_data/'

new_path = '/Users/admin/Documents/k_data_new/'

file_list = os.listdir(path)

for file_name in file_list:
    print(path + file_name)
    df = pd.read_csv(path + file_name)
    drop_row_index = df[df['date']<='2022-10-14 23:59:59'].index
    df = df.drop(drop_row_index)
    df.to_csv(new_path + file_name, index=False, index_label=False)