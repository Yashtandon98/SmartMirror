from flask import Flask, render_template
from Modules.Weather.weather import query_api
from pprint import pprint as pp

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def webprint():
    data = []
    error = None
    select = 'Chennai'
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
        if len(data) != 2:
            error = 'Bad Response from Weather API'
            return render_template('home.html', data=data, error=error)
