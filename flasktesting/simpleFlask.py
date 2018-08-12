from flask import Flask
APP = Flask(__name__)

@APP.route("/")
def index():
    return "This kinda worked."

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=80, debug=True)
