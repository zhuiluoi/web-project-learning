from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        print(request.form)
        username = request.form.get("username")
        sex = request.form.get("sex")
        hobby = request.form.getlist("hobby")
        city = request.form.get("city")
        skill = request.form.getlist("skill")
        note = request.form.get("note")
        print(username, sex, hobby, city, skill, note)
        return "注册成功"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        print(request.form)
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "123":
            return "登录成功"
        else:
            return "登录失败"


"""@app.route("/do/register/post", methods=["POST"])
def do_register_post():
    print(request.form)
    username = request.form.get("username")
    sex = request.form.get("sex")
    hobby = request.form.getlist("hobby")
    city = request.form.get("city")
    skill = request.form.getlist("skill")
    note = request.form.get("note")
    print(username, sex, hobby, city, skill, note)
    return "注册成功"
"""


@app.route("/do/register/get", methods=["GET"])
def do_register_get():
    print(request.args)
    return "注册成功"


if __name__ == '__main__':
    app.run()
