from flask import Flask
from flask import render_template
from flask import request
import sys

app = Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)

@app.route("/plusone")
def plusone():
    count = int(request.args.get('count').replace('/',''))
    return '''
      <p>
        {count}
        <input type="hidden" name="count" value={count}/>
      </p>
      '''.format(count = count + 1)

@app.route("/minusone")
def minusone():
    count = int(request.args.get('count').replace('/',''))
    return '''
      <p>
        {count}
        <input type="hidden" name="count" value={count}/>
      </p>
      '''.format(count = count - 1)