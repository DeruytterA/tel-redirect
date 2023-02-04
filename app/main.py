from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def telurl():
    telnr = request.args.get('tel')
    return redirect(f'tel:{telnr}')
