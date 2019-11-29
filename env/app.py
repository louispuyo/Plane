from flask import Flask, jsonify
from flask_cors import CORS

#config

DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)

#enable CORS 

CORS(app, resources = {r'/*': {'origins':'*'}}) # je sais pas trop

#sanity checkout route

@app.route('/ping', methods=['GET'])

def ping_pong():
    return jsonify('pong')
if __name__ == "__main__":
    app.run()




