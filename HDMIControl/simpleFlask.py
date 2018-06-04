from flask import Flask, render_template, redirect
APP = Flask(__name__)

@APP.route("/")
def index():
    #return "Let me show you da wae.  The way is ebola."
    return render_template('/index.html')

@APP.route("/Port1")
def Port1():
    return redirect("/", code=302)

@APP.route("/Port2")
def Port2():
    return redirect("/", code=302)
    
@APP.route("/Port3")
def Port3():
    return redirect("/", code=302)
    
@APP.route("/Port4")
def Port4():
    return redirect("/", code=302)
    
@APP.route("/Port5")
def Port5():
    return redirect("/", code=302)


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=80, debug=True)
