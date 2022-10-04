from flask import Flask, jsonify, request

app = Flask(__name__)


contacts = [{
    'Contact': 3000300030,
    'Name': "Tony",
    'done': False,
    'id': 1
},
    {
    'Contact': 9854215515,
    'Name': "Steve",
    'done': False,
    'id': 2
}]


@app.route("/")
def HelloWorld():
    return "Hello World"


@app.route("/add-data", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 400
        )
    task = {
        "id": contacts[-1]['id'] + 1,
        "Name": request.json['title'],
        "Contact": request.json.get('description', ""),
        "done": False
    }
    contacts.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    }
    )


@app.route("/get-data")
def getTask():
    return jsonify({
        "data": contacts,
    })


if (__name__ == "__main__"):
    app.run(debug=True)
