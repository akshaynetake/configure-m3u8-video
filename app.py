from flask import render_template, Flask, request

app = Flask(__name__)


@app.route('/stream')
def page():
    return render_template('stream.html')


@app.route("/iframe", methods=["GET"])
def iframe():
    if request.method == "GET":
        return render_template("iframe-src.html")


if __name__ == '__main__':
    app.run(debug = True)
