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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# @app.route("/calc/", methods=["GET", "POST"])
# def calculate():
#     if request.method == "POST":
#         a = float(request.form["a"])
#         b = float(request.form["b"])
#         c = float(request.form["c"])
#         roots = quadratic(a, b, c)

#         if roots:
#             return render_template(
#                 "calculator_result.html",
#                 a=a,
#                 b=b,
#                 c=c,
#                 root_1=roots[0],
#                 root_2=roots[1],
#             )
#         else:
#             return render_template("calculator_form.html", error=True)
#     return render_template("calculator_form.html", error=None)


@app.get('/calc/')
def calc_get():
    return render_template("calculator_form.html", error=None)


@app.post('/calc/')
def calc_post():
    a = float(request.form["a"])
    b = float(request.form["b"])
    c = float(request.form["c"])
    roots = quadratic(a, b, c)

    if roots:
        return render_template(
            "calculator_result.html",
            a=a,
            b=b,
            c=c,
            root_1=roots[0],
            root_2=roots[1],
        )
    else:
        return render_template("calculator_form.html", error=True)


@app.route("/grade/")
def show_grades():
    grades = [
        {'name': 'John', 'grade': 80},
        {'name': 'Paul', 'grade': 90},
        {'name': 'George', 'grade': 85},
        {'name': 'Ringo', 'grade': 95},
    ]
    return render_template("grades.html", grades=grades)


if __name__ == "__main__":
    app.run(debug=True)
