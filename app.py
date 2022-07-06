from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from controllers import members
from werkzeug import exceptions
# from flask_pymongo import PyMongo



app = Flask(__name__)
CORS(app)



## Mongo stuff
# mongodb_client = PyMongo(app, uri="mongodb+srv://gio:gio@cluster0.er7j3.mongodb.net/?retryWrites=true&w=majority")
# db = mongodb_client.db


#######


@app.route('/')
def home():
    return jsonify({'message': "What's up from Scotland BABY"}), 200

@app.route('/members', methods=['GET', 'POST'])
def members_handler():
    if request.method == 'POST': 
        obj = { "name": request.form['first'], 'alter-ego': request.form['last']}
        resp, code = members.create(jsonify(obj))
        html_to_send = render_template('index.html', members = resp)
        return html_to_send, code
    
    elif request.method == 'GET':
        resp, code = members.index(request)
        html_to_send = render_template('index.html', members=resp)
        return html_to_send, code



#New route
@app.route('/members?first=<first>&last=<last>', methods=['POST'])
def members_post_handler(first, last):
    print(first, last)
    members.create(jsonify({ "name": first, "alter-ego": last}))
    return True





@app.route('/members/<int:member_id>', methods=['GET', 'PATCH', 'DELETE'])
def member_handler(member_id):
    fns ={
        'GET': members.show,
        'PATCH': members.update,
        'DELETE': members.destroy
    }
    resp, code = fns[request.method](request, uid=member_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
