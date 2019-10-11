from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis',port=6379)

@app.route('/')
def shlaom():
    redis.incr('hits')
    return 'Shalom laBenadam ha - %s SheRoeh et haFlask HaBeseder Haze' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

