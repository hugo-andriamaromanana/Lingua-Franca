from flask import Flask, render_template, request
from api import *
from data import languages_data, languages_data_swapped
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')



@app.route('/', methods=['GET', 'POST'])

def dropdown_from():

    output_text = ''

    if request.method == 'POST':
        
        selected_language = str(request.get_data('language'))[
            :str(request.get_data('language')).find('input_text')]

        src = languages_data_swapped[selected_language[:selected_language.find(
            '&')].replace('language1=', '')[2:]].replace('+', ' ').replace('%27', "'").replace('%2C', ',')
        dest = languages_data_swapped[selected_language[selected_language.find(
            '&'):].replace('language2=', '')[1:-1]].replace('+', ' ').replace('%27', "'").replace('%2C', ',')
        print(src, dest)

        input_text = str(request.get_data('language'))[str(request.get_data(
            'language')).find('input_text') + 10:][1:-1].replace('+', ' ')
        print(input_text)

        output_text = translate(input_text, dest, src)
        print(output_text)

        if output_text == input_text:
            output_text = 'Sorry, I cannot translate this text. Please try again.'

        if src == dest:
            output_text = input_text

        if output_text == '':
            output_text = 'Empty fill. Please try again.'

    languages = [languages_data[i] for i in languages_data.keys()]
    return render_template('index.html', languages=languages,output_text=output_text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
