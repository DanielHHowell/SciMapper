from flask import Flask, render_template, flash, request
from wtforms import Form, StringField, validators
import Main
import time


app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

class InputForm(Form):
    search = StringField('search:', [validators.required()])

@app.route("/", methods=['GET', 'POST'])
def index():

    form = InputForm(request.form)
    if request.method == 'POST':
        search = request.form['search']

        if form.validate():
            Main.main_scraper(search)
            time.sleep(.3)
            return render_template('/map.html')

        else:
            flash('Error')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='80')
