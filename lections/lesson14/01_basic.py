from flask import Flask
#Отвечает за всю обработку и вызов http кода
app = Flask(__name__)

# / - корневой путь
@app.route("/", methods=["GET"])
def hello():
    return {
            'json_key': 'str',
            'nested': {
                'test': 123,
                'test2': 'zxczxc',
                }
            }

@app.route("/privet")
def privet():
    return "privet"

@app.route("/", methods=["POST"])
def post():
    return {'some_key': '1234'}
