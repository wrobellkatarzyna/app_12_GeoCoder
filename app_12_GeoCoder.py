from io import StringIO

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method == 'POST':
        file = request.files["file"]
        data = StringIO(file.read().decode("utf-8"))
        global df
        df = pd.read_csv(data, sep=',', engine='python')

        if "Address" and "address" not in df.columns:
            return render_template("index.html",text="Your file does not contain Address column.")

        df["Longitude"] = "lon"
        df["latitude"] = "lat"

        return render_template("index.html", btn="download.html", tables=[df.to_html(classes='data', header="true", index=False)])


@app.route("/download")
def download():
    df.to_csv(
        r'C:\Users\Katrina\PycharmProjects\HomeTraining\app_12_GeoCoder\Your csv file.csv',index = False)
    #file.save(secure_filename("uploaded " + file.filename))
    return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
