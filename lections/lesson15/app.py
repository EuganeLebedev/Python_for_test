from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    lastname = request.args.get("lastname")
    return render_template("index.html", name=name, lastname=lastname)

@app.route("/register", methods=["POST"])
def post():
    name=request.form.get("name")
    lastname=request.form.get("lastname")
    return render_template("register.html", name=name, lastname=lastname)

if __name__ == "__main__":
    app.run(debug=True)


