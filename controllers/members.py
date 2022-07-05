
from werkzeug.exceptions import BadRequest

members = [
    {'id': 1, 'name': 'Sam', 'alter-ego': 'ADogHas2Bark'},
    {'id': 2, 'name': 'Amir', 'alter-ego': 'IceMan'},
]

def idFunc(e):
    return e['id']

def index(req):
    members.sort(key=idFunc)
    return [m for m in members], 200

def create(req):
    new_member = req.get_json()
    print(type(sorted([m['id'] for m in members])[-1]))
    new_member['id'] = (sorted([m['id'] for m in members])[-1] + 1)
    # print(new_member['id'])
    members.append(new_member)
    return new_member, 201
