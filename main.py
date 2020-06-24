from app1 import translate
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return render_template('index.html')


@app.route("/action", methods=["POST", 'GET'])
def ans():
    if(request.method == 'POST'):
        query = request.form.get('query')
        ans = translate(query)
        return render_template('action.html', par=ans, length=len(ans))


app.run()
