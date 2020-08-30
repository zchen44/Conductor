from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

hashes = json.load(open('./.credentials.json'))
profiles = {
    "dev": generate_password_hash(hashes['dev']),
    "prod": generate_password_hash(hashes['prod'])
}

@app.route("/")
def homepage():
    return "Conductor Middleman Server"

@auth.verify_password
def verify_password(profile, password):
    if profile in profiles and check_password_hash(profiles.get(profile), password):
        return profile

@app.route('/credentials/discord', methods=['GET'])
@auth.login_required
def discord_bot_token():
    creds = json.load(open('./.master_cred.json'))
    data = {'token': creds[auth.username()]['discord_token']}
    return jsonify(data), 200

@app.route('/credentials/weather', methods=['GET'])
@auth.login_required
def weather_token():
    creds = json.load(open('./.master_cred.json'))
    data = {'token': creds[auth.username()]['weather']}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run()