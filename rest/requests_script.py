import requests


def generate_dict(id, artists, genre, year, album, name):
    return {
    'id': id, 
    'artists': artists, 
    'genre': genre, 
    'year': year, 
    'album': album,
    'name': name
}


requests.post('http://127.0.0.1:5000/tracks', json=generate_dict(
    1, ['pioneer_rockers'], genre='rock', year=2007, album='the', name='eagles on motorcycles'
    ))
requests.post('http://127.0.0.1:5000/tracks', json=generate_dict(
    2, ['hands from shoulders'], genre='punk', year=2016, album='Best fo the best', name='the punk ballad'
))
requests.patch('http://127.0.0.1:5000/tracks', json={
    'id': 2,
    'album': 'Best of the best'
})
requests.delete('http://127.0.0.1:5000/tracks/1')
