#!/usr/bin/env python
import subprocess
import json
from flask import Flask, request, jsonify

api = Flask(__name__)


@api.route('/generate', methods=['POST'])
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


if __name__ == '__main__':
    api.run()
