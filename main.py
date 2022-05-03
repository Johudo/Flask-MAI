from flask import Flask, abort, redirect, render_template

app = Flask(__name__)

users = [
    {"name": "Alex", "id": 1, "surname": "Turner", "age": 36},
    {"name": "Thom", "id": 2, "surname": "Yorke", "age": 53},
]


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def users_page():
    return render_template("users.html", users=users)


@app.route("/user/<int:user_id>")
def user_page(user_id):
    user = None

    for user_item in users:
        if user_item["id"] == user_id:
            user = user_item

    if user == None:
        return abort(404)

    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
