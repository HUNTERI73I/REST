from flask import Flask, abort, request
import json
import os


app = Flask(__name__)


POSSIBLE_ATTRIBUTES = {
    'id': (type(1),), 
    'artists': (type([1,1]),), 
    'genre': (type('1'),), 
    'year': (type(1)), 
    'album': (type('1'),),
    'name': (type('1'),)
}


with open(os.path.dirname(__file__) + '/tracks.json', 'r') as file:
    data = json.load(file)
    TRACKS = {int(key): value for key, value in data.items()}



def dump_data(data):
    with open(os.path.dirname(__file__) + '/tracks.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def validate_car(good):
    for key, value in good.items():
        if key not in POSSIBLE_ATTRIBUTES and not isinstance(value, POSSIBLE_ATTRIBUTES.get(key)):
            return False
    return len(POSSIBLE_ATTRIBUTES) == len(good)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/tracks', methods=['GET'])
def show_all():
    return TRACKS


@app.route('/tracks/<id>', methods=['GET'])
def show_one(id):
    return TRACKS.get(int(id)) if int(id) in TRACKS else abort(404)


@app.route('/tracks', methods=['POST'])
def store():
    recieved_data = request.get_json()

    if not validate_car(recieved_data):
        return 406

    if TRACKS.get(recieved_data['id']):
        return 409

    TRACKS[recieved_data['id']] = recieved_data

    dump_data(TRACKS)

    return TRACKS


def validate_modification(data):
    for key, value in data.items():
        if key not in POSSIBLE_ATTRIBUTES or not isinstance(value, POSSIBLE_ATTRIBUTES.get(key)):
            return False
    return True


@app.route('/tracks/<id>', methods=['PATCH'])
def modify_track(id):
    recieved_data = request.get_json()

    if not validate_modification(recieved_data):
        return 406

    print(TRACKS)

    print(id, type(id), '!!!')

    TRACKS[int(id)] = TRACKS[int(recieved_data['id'])] | recieved_data

    print(TRACKS)

    dump_data(TRACKS)

    return TRACKS[int(id)]


@app.route('/tracks/<id>', methods=['DELETE'])
def delete_track(id):
    try:
        TRACKS.pop(int(id))
        dump_data(TRACKS)
    except KeyError:
        return abort(404)


def run():
    app.run(debug=True)

        
if __name__ == '__main__':
    run()
