from flask import Flask, render_template
from .Modules.Weather.weather import query_api
from pprint import pprint as pp
from .Modules.News.news import getnews


app = Flask(__name__)

@app.route('/news', methods = ['GET', 'POST'])
def newsprint():
    ndata = []
    error = None
    nresp = getnews()
    if nresp:
        ndata.append(nresp)
        return render_template('news.html', ndata = ndata, error = error)

@app.route('/weather', methods = ['GET', 'POST'])
def weatherprint():
    from .Modules.Speak.speaker import wedata
    data = []
    error = None
    resp = wedata
    pp(resp)
    if resp:
        data.append(resp)
        return render_template('weather.html', data = data, error = error)

@app.route('/wiki', methods = ['GET', 'POST'])
def wikiprint():
    from .Modules.Speak.speaker import wikidata
    wdata = wikidata
    error = None
    pp(wdata)
    return render_template('wiki.html', wdata = wdata, error = error)

@app.route('/sports', methods = ['GET', 'POST'])
def sportsprint():
    ndata = sdata
    error = None
    return render_template('sports.html', ndata = ndata, error = error)

@app.route('/', methods = ['GET', 'POST'])
def webprint():
    data = []
    ndata = []
    error = None
    select = 'Chennai'
    resp = query_api(select)
    nresp = getnews()
    pp(resp)
    if resp or nresp:
        data.append(resp)
        ndata.append(nresp)
        if len(data) != 2:
            error = 'Bad Response from Weather API'
            return render_template('home.html', data=data, ndata=ndata, error=error)
