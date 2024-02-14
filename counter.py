from flask import Flask
from flask import render_template
from flask import request
import sys

app = Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)

@app.route("/plusOne")
def plus_one():
    count = int(request.args.get('count').replace('/',''))
    return '''
      <p id="number">
        {count}
        <input type="hidden" name="count" value={count}/>
      </p>
      '''.format(count = count + 1)

@app.route("/minusOne")
def minus_one():
    count = int(request.args.get('count').replace('/',''))
    return '''
      <p id="number">
        {count}
        <input type="hidden" name="count" value={count}/>
      </p>
      '''.format(count = count - 1)