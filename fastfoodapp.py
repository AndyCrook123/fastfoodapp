from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/favourites/")
def favourites():
    return render_template('favourites.html')

@app.route("/burgers/")
def burgers():
    return render_template('burgers.html')

@app.route("/italian/")
def italian():
    return render_template('italian.html')

@app.route("/indian/")
def indian():
    return render_template('indian.html')

@app.route("/chinese/")
def chinese():
    return render_template('chinese.html')

@app.route("/contactus/")
def contactus():
    return render_template('contactus.html')

@app.route("/login/")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
