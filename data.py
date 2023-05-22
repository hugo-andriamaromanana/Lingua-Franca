import json
import os

def load_data(filepath):
    with open(filepath) as f:
        return json.load(f)

languages_filepath=os.path.join('settings', 'languages.json')

languages_data = load_data(languages_filepath)

