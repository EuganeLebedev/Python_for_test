import os
from flask import Flask, redirect, abort, request, make_response, session, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/", methods=["GET"])
def hello():
    print(request.path)
    print(request.method)
    request.headers

    return {
        "json_key": "str",
        "nested": {
            "test": 123,
            "test2": "zxxzc",
        }
    }

@app.route("/privet")
def privet():
    resp = make_response("privet", 200)
    resp.headers['X-Something'] = 'My HEADER'

    return resp

@app.route("/test")
def test():
    return ("RESPONSE", 201)

# /dynamic/vasya
@app.route("/dynamic/<username>")
def dynamic(username):
    if username == "123":
        abort(404)
    return f"Hello, {username}"

@app.route("/redirect/<username>")
def redirect_handler(username):
    return redirect(f"/dynamic/{username}")

@app.route("/", methods=["POST"])
def post():
    return {"some_key": 123123}

@app.errorhandler(404)
def handle_404(error):
    return "NOT FOUND"

@app.route("/pwd")
def pwd():
    return os.getcwd()

@app.route("/session/<username>")
def session_handler(username):
    session['username'] = username
    return "OK!!!"

@app.route("/session_get")
def session_reader():
    username = session['username']
    return f"Username: {username}"

@app.route("/register/<username>")
def new_user(username):
    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    session['user_id'] = user.id

    return "success"

@app.route("/me")
def me():
    if "user_id" not in session:
        abort(401)

    user_id = int(session["user_id"])
    user = db.session.query(User).filter_by(id=user_id).first()
    return f"Hello, {user.username}"

@app.route("/index")
def index():
    if "user_id" not in session:
        abort(401)

    user_id = int(session["user_id"])
    user = db.session.query(User).filter_by(id=user_id).first()
    return render_template("index.html", name=user.username)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)





