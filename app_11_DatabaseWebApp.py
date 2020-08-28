from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

# console from app_11_DatabaseWebApp import db

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/height_collector'
app.config[
    'SQLALCHEMY_DATABASE_URI'] ='postgres://iiapsjjhfphcpo:ead04cf3dce57f3ebc24bdcc53a624628938fe4b0e6d66b2d346c1eeaee4180b@ec2-3-213-102-175.compute-1.amazonaws.com:5432/d85r535dcfqifa?sslmode=require'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method == 'POST':
        file = request.files["file"]
        content = file.read()
        file.save(secure_filename("uploaded " + file.filename))
        with open("uploaded " + file.filename, "w") as f:
            f.write("This was added later")
        print(content)
        print(type(file))
        return render_template("index.html", btn="download.html")

@app.route("/download")
def download():
    return send_file("uploaded " + file.filename, attachment_filename="YourFile.csv", as_attachment=True)


if __name__ == '__main__':
    app.debug = True
    app.run()
