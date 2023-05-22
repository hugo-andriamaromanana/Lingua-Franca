from flask import Flask, render_template, request
from api import *
from data import languages_data, languages_data_swapped
app = Flask(__name__, template_folder='templateFiles',
            static_folder='staticFiles')


@app.route('/', methods=['GET', 'POST'])
def dropdown_form():
    if request.method == 'POST':
        selected_language1 = request.form['language1']
        selected_language2 = request.form['language2']
        input_text = request.form['input_text']
        print(selected_language1, selected_language2, input_text)
        return translate(input_text, languages_data_swapped[selected_language2], languages_data_swapped[selected_language1])

    languages = [languages_data[i] for i in languages_data.keys()]
    return render_template('index.html', languages=languages, selected_language1="", selected_language2="")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
