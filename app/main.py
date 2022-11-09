from flask import Flask, request, render_template
import math
import pandas as pd
import os

app = Flask(__name__)


picfolder = os.path.join('static', 'pics')
app.config["UPLOAD_FOLDER"] = picfolder


@app.route("/")
def cv():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'cv.jpg')
    return render_template("cv.html", user_image=pic1)


@app.route("/sqrt", methods=["GET", "POST"])
def index3():
    if request.method == "GET":
        return render_template("sqrt.html")
    elif request.method == "POST":
        user = request.form.get("angka")
        angka = math.sqrt(int(user))
        return "hasilnya %s" % angka


@app.route('/csv', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('csv.html')
    elif request.method == 'POST':
        csv_file = request.files.get('file')
        csv = pd.read_csv(csv_file)
        return csv.to_json()


@app.route("/form", methods=["GET", "POST"])
def index2():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        namadepan = request.form.get("namadepan")
        namabelakang = request.form.get("namabelakang")
        gender = request.form.get("gender")
        return "Nama :" + namadepan + " " + namabelakang + ", " + "Jenis Kelamin : " + gender


if __name__ == '__main__':
    app.run(debug=True)
