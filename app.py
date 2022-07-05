from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import members
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': "What's up from Scotland BABY"}), 200

@app.route('/members', methods=['GET', 'POST'])
def member_handler():
    fns = {
        'GET': members.index,
        'POST': members.create
    }
    resp, code = fns[request.method](request)
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
