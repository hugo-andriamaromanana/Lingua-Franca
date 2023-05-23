import pandas as pd
import os
import json
from functions.data_languages import languages_data_swapped

history_filepath = os.path.join('settings', 'history', 'history.csv')


def load_data(filepath):
    return pd.read_csv(filepath)

def load_json(filepath):
    with open(filepath) as f:
        return json.load(f)
    
def get_history_df():
    history_filepath = os.path.join('settings', 'history', 'history.csv')
    history_df = load_data(history_filepath)
    return history_df

def add_dic_as_row_in_csv(csv_path, datetime, language_from, language_to, text_from, text_to):
    dic = {
        'datetime': datetime,
        'language_from': languages_data_swapped[language_from],
        'language_to': languages_data_swapped[language_to],
        'text_from': text_from,
        'text_to': text_to
    }
    df = pd.DataFrame(dic, index=[-1])
    df.to_csv(csv_path, mode='a', header=False, index=False)
