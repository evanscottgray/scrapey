# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from flask import Flask
from flask import request
import utils
import json

app = Flask(__name__)


@app.route("/")
def trip():
    source = request.args.get('source', '')
    destination = request.args.get('destination', '')
    return json.dumps(utils.trip_stats(source, destination))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
