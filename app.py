from flask import Flask, render_template, request

from calculator import quadratic


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)


@app.route("/calc/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        c = float(request.form["c"])
        result = quadratic(a, b, c)

        if result is not None:
            if isinstance(result, float):
                print(f'The solution is {result}.')
                return render_template(
                    "calculator_result.html",
                    a=a,
                    b=b,
                    c=c,
                    root_1=result,
                    root_2=result,
                )
            else:
                return render_template(
                    "calculator_result.html",
                    a=a,
                    b=b,
                    c=c,
                    root_1=result[0],
                    root_2=result[1],
                )
        return render_template("calculator_form.html", error=True)
    return render_template("calculator_form.html", error=None)


@app.route("/grade")
def test():
    grades = [
        {'name': 'John', 'grade': 80},
        {'name': 'Paul', 'grade': 90},
        {'name': 'George', 'grade': 85},
        {'name': 'Ringo', 'grade': 95},
    ]
    return render_template("grades.html", grades=grades)
