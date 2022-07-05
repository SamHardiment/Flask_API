
from werkzeug.exceptions import BadRequest

members = [
    {'id': 1, 'name': 'Sam', 'alter-ego': 'ADogHas2Bark'},
    {'id': 3, 'name': 'Gio', 'alter-ego': 'johnny'},
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

def show(req, uid):
    return find_by_uid(uid), 200

def find_by_uid(uid):
    try:
        return next(member for member in members if member['id'] == uid)
    except:
        raise BadRequest(f"We don't have that member with id {uid}!")




def update(req, uid):
    to_update = find_by_uid(uid)
    request = req.get_json()
    print(request)
    for key, val in request.items():
        to_update[key] = val
    return to_update, 202


def destroy(req, uid):
    to_remove = find_by_uid(uid)
    members.remove(to_remove)
    return to_remove, 204










