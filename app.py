from flask import Flask, render_template, request

from functions.translator import translate
from functions.data_languages import languages_data, languages_data_swapped
from functions.data_history import get_history_df, add_dic_as_row_in_csv, history_filepath
from datetime import datetime

app = Flask(__name__, template_folder='templateFiles',
            static_folder='staticFiles')


@app.route('/', methods=['GET', 'POST'])
def dropdown_form():
    input_text = ""

    if request.method == 'POST':
        selected_language1 = request.form['language1']
        selected_language2 = request.form['language2']
        input_text = request.form['input_text']

        output_text = translate(
            input_text, languages_data_swapped[selected_language1], languages_data_swapped[selected_language2])

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_dic_as_row_in_csv(history_filepath, current_datetime,
                              selected_language1, selected_language2, input_text, output_text)

        return output_text

    languages = [languages_data[i] for i in languages_data.keys()]

    return render_template('index.html', languages=languages, selected_language1="", selected_language2="")


@app.route('/history', methods=['GET'])
def history():
    history_df = get_history_df()
    return render_template('history.html', history_df=history_df)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
