from flask import Flask, render_template, request
from api import *
from data import languages_data, languages_data_swapped
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def dropdown_from():
    
    if request.method == 'POST':
        selected_language = str(request.get_data('language'))
        src = languages_data_swapped[selected_language[:selected_language.find(
            '&')].replace('language1=', '')[2:]]
        dest = languages_data_swapped[selected_language[selected_language.find(
            '&'):].replace('language2=', '')[1:-1]]
        print(src, dest)

    languages = [languages_data[i] for i in languages_data.keys()]
    return render_template('index.html', languages=languages)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
