import time
from flask import Flask, request


from filter import hi


app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/recommendations')
def query_example():
    # if key doesn't exist, returns None
    type = request.args.get('type')

    # if key doesn't exist, returns a 400, bad request error
    concern = request.args['concern']

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              '''.format(type, concern)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)