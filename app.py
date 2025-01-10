from flask import Flask, render_template, request
app = Flask(__name__)
from database_time import time_dt
from data_users import adding, finding
@app.route("/")
def index_page():
    return render_template('holl.html', result_from_dt=["", ""])



@app.route("/enter")
def enter():
    name = request.args.get('name')
    pusswoerd = request.args.get('password')
    result = finding(name, pusswoerd, "for_enter")
    if ["", ""] == result:
        return render_template('site.html')
    else:
        return render_template("holl.html", result_from_dt=result)

@app.route("/tu_reg")
def tu_reg():
    return render_template("register.html", result_from_dt=["", ""])


@app.route("/reg")
def register():
    name = request.args.get('name')
    pusswoerd = request.args.get('password')
    result = finding(name, pusswoerd, "for_register")
    if result == ["", ""]:
        adding(name, pusswoerd)
        return render_template('holl.html', result_from_dt=result)
    else:
        print(result)
        return render_template("register.html", result_from_dt=result)


@app.route("/add")
def add_page():
    time = request.args.get('time')
    time_dt()
    return f'name: <br> time: {time}'

app.run(debug=True)