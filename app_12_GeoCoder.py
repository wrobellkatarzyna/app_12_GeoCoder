from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


def file_to_string(filepath):
    text = textract.process(filepath)
    print (text)
    return text

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method == 'POST':
        file = request.files["file"]
        data = file.read()
        #file.save(secure_filename("uploaded " + file.filename))
        #request.session['text'] = file_to_string(file.file.path)
        #data = pd.read_csv(file.name)
        #print(request.session['text'])

        return render_template("index.html", btn="download.html")

@app.route("/download")
def download():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()