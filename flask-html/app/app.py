from flask import Flask, render_template
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis',port=6379)

@app.route('/')
def shlaom():
    redis.incr('hits')
    return render_template('index.html', visitor=redis.get('hits'))

@app.route('/visitor')
def mevakrim():
    redis.incr('hits')    
    return redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

