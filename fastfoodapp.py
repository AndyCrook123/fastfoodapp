from flask import Flask, render_template

app = Flask(__name__)
  
@app.route("/")
def root():
    return render_template('homepage.html')

@app.route("/favourites.html")
def favourites():
    return render_template('favourites.html')

@app.route("/burgers.html")
def burgers():
    return render_template('burgers.html')

@app.route("/italian.html")
def italian():
    return render_template('italian.html')

@app.route("/indian.html")
def indian():
    return render_template('indian.html')

@app.route("/chinese.html")
def chinese():
    return render_template('chinese.html')

@app.route("/contactus.html")
def contactus():
    return render_template('contactus.html')

@app.route("/login.html")
def login():
    return render_template('login.html')

@app.route("/signup.html")
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
