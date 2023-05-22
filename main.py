from flask import Flask, render_template, request
from api import *
from data import languages_data
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def dropdown_from():
    if request.method == 'POST':
        language = request.form.get('language')
        return render_template('index.html', language=language, languages=languages_data)
    

    languages = [languages_data[i] for i in languages_data.keys()]
    return render_template('index.html', languages=languages)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)