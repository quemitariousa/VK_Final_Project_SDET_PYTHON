import threading
from flask import Flask, jsonify, request

app = Flask(__name__)

DATA = {'quemitariousa6':4100}
MOCK_HOST = '0.0.0.0'
MOCK_PORT = '4500'

@app.route('/vk_id/<username>', methods=['GET'])
def get_user(username):
    if username in DATA:
        return {'vk_id': DATA[username]}, 200
    else:
        return jsonify({}), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': MOCK_HOST,
        'port': MOCK_PORT
    })

    server.start()
    return server


def shutdown_stub():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_stub()
    return jsonify(f'Ok, exiting'), 200

if __name__ == '__main__':
    app.run(MOCK_HOST, MOCK_PORT)