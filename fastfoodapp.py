from flask import Flask, render_template, request, redirect
from models import login, db, UserModel
from flask_login import login_required, current_user, login_user, logout_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login.init_app(app)
login.login_view = 'login'

@app.before_first_request
def create_table():
    db.create_all()
  
@app.route("/")
def root():
    return render_template('homepage.html')

@app.route("/favourites.html")
@login_required
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

@app.route("/login.html", methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/favourites.html')
     
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/favourites.html')
     
    return render_template('login.html')

@app.route("/signup.html", methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect('/favourites.html')
     
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
 
        if UserModel.query.filter_by(email=email):
            return ('Email already Present')
             
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login.html')
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
