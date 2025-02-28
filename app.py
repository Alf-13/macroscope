import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from bls_survey_list import bls_survey_list

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

@app.route('/')
def home():
    return jsonify(bls_survey_list())

if __name__ == '__main__':
    app.run(debug=True)
