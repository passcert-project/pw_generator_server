#!/usr/bin/env python
import subprocess
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_random_password():
    pw_options = request.get_json()
    print(f'GOT THESE OPTIONS => {pw_options}')
    pw_options = pw_options.get('pw_settings')
    x = pw_options.split()

    result = subprocess.run(["./passwordGeneratorApp.out", "-a", f"{x[0]}", f"{x[1]}", f"{x[2]}", f"{x[3]}", f"{x[4]}",
                            f"{x[5]}", f"{x[6]}", f"{x[7]}", f"{x[8]}"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    result = result.split()
    print(f'\n\n RESULT => {result}\n\n')
    print(f'\n\nGenerated Password => {result[2]}\n\n')

    return jsonify({"generated_password": result[2]})


@app.route('/')
def hello_world():
    return "<h1>Welcome to Passcert's Password Generator.</h1><br/><h3>Please make a POST request to /generate to receive a new password.</h3>"


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
