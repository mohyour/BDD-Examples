from flask import Flask, request


app = Flask(__name__)
data = {}


@app.route("/user", methods=["POST", "GET"])
def add_user():
    if request.method == "POST":
        request_data = request.get_json()
        id = request_data.get("id")
        user = request_data.get("name")
        data[id] = user
        return {"id": id, "user": data[id]}, 200


@app.route("/users")
def get_all_users():
    all_users = []
    for key, value in data.items():
        all_users.append({"id": key, "name": value})
    return all_users, 200


@app.route("/user/<id>", methods=["PUT", "GET", "DELETE"])
def update_user(id):
    if request.method == "PUT":
        request_data = request.get_json()
        payload = request_data.get("name")
        user_id = id
        if user_id in data:
            data[user_id] = payload
            return {"id": user_id, "name": data[user_id]}, 200
        else:
            return {"error": "Not found"}, 404
    elif request.method == "GET":
        user_id = id
        if user_id in data:
            username = data.get(user_id)
            return {"id": user_id, "name": username}, 200
        return {"error": "Not found"}, 404
    elif request.method == "DELETE":
        user_id = int(id)
        if user_id in data:
            username = data.get(user_id)
            return {"message": "User deleted"}, 200
        return {"error": "Not found"}, 404


if __name__ == "__main__":
    app.run()
