import datetime
import os
from flask import Flask, render_template, redirect
APP = Flask(__name__)

@APP.route("/")
@APP.route('/index')
def helindexlo():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : "Yo",
        'time' : timeString
    }
    return render_template('/main.html', **templateData)

@APP.route("/test/<value>")
def test(value):
    return "Value from querystring is: " + value


@APP.route("/notepad")
def notepad():
    os.system('start notepad.exe')
    return redirect("/", code=302)

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=80, debug=True)
