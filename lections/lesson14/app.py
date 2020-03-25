from flask import Flask, redirect, abort, request, make_response, session, render_template
import os
from flask_sqlalchemy import SQLAlchemy
#Отвечает за всю обработку и вызов http кода
app = Flask(__name__)
app.config['SQLALCHEMY+DATABASE_URI'] = 'sqllite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# / - корневой путь
@app.route("/", methods=["GET"])
def hello():
    print(request.path)
    print(request.method)
    return {
            'json_key': 'str',
            'nested': {
                'test': 123,
                'test2': 'zxczxc',
                }
            }

@app.route("/privet")
def privet():
    resp = make_response("privet", 200)
    resp.headers['X-Something'] = 'My HEADER'
    return resp

@app.route('/test')
def test():
    return ('RESPONSE', 201)

@app.route("/dynamic/<username>")
def dynamic(username):
    print(username)
    print(type(username))
    if username == '123':
        abort(404)
    return f"Hello {username}"
#Запрос без имя пользователя вернет 404
#http://127.0.0.1:5000/dynamic/john

#Перенаправления
@app.route("/redirect/<username>")
def redirect_handler(username):
    return redirect(f"/dynamic/{username}")

@app.route("/", methods=["POST"])
def post():
    return {'some_key': '1234'}


@app.errorhandler(404)
def hendler_404(error):
    return "NOT FOUND"

@app.route("/pwd")
def pwd():
    return os.getcwd()

@app.route("/session/<username>")
def session_handler(username):
    session['username'] = username
    return 'OK!!!'
@app.route("/session_get/")
def session_reader():
    username = session['username']
    return f"Username: {username}"
#Секретный ключ для шифрования куков.
app.secret_key=b'GFJKL(&T&K&%^$DGGJ^'

@app.route("/register/<username>")
def new_user(username):
    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    session['user_id'] = user.id

    return 'success'
@app.route("/me")
def me():
    if "user_id" not in session:
        abort(401)

    user_id = int(session['user_id'])
    user = db.session.query(User).filter_by(id=user_id).first()
    return f'Hello {user.username}'

@app.route("/index")
def index():
    if "user_id" not in session:
        abort(401)
        user_id = int(session["user_id"])
        user = db.session.query(User).filter_by(id=user_id).first()
        return render_template("index.html", name=user.name)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
