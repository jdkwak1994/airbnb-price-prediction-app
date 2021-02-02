from flask import Flask, render_template, redirect, request, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)
app.static_folder = "templates/static"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        testdf = []
        boroughtype = int(request.form["boroughradio"])
        roomtype = int(request.form["roomtyperadio"])
        review_input = request.form["reviewmonth"]
        avail_input = request.form["availability"]
        for x in range(5):
            if boroughtype == 1:
                testdf.append(1)
            else:
                testdf.append(0)
            boroughtype = boroughtype - 1
        for x in range(3):
            if roomtype == 1:
                testdf.append(1)
            else:
                testdf.append(0)
            roomtype = roomtype - 1
        testdf.append(float(review_input))
        testdf.append(int(avail_input))
        print(testdf)
        return render_template("index.html", InputData=testdf)
    else:
        return render_template("index.html")


@app.route("/infographic")
def infographic():
    return render_template("infographic.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)