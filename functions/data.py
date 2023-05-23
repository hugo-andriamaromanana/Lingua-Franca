import json
import os

def load_data(filepath):
    with open(filepath) as f:
        return json.load(f)

languages_filepath=os.path.join('settings', 'languages','languages.json')

languages_data = load_data(languages_filepath)

languages_data_swapped = {v: k for k, v in languages_data.items()}