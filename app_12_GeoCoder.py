from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import pandas as pd
from io import StringIO
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    global filename
    if request.method == 'POST':
        file = request.files["file"]

        data = StringIO(file.read().decode("utf-8"))
        df = pd.read_csv(data, sep=',', engine='python')

        if "Address" and "address" not in df.columns:
            return render_template("index.html",
                                   text="Your file does not contain Address column.")

        df["Longitude"] = "lon"
        df["latitude"] = "lat"

        filename = "Your csv file " + datetime.datetime.now().strftime(
            '%Y%m%d-%H%M%S') + ".csv"
        import os
        filename =os.path.join("uploads",filename)
        df.to_csv(filename, index=False)

        return render_template("index.html", btn="download.html", tables=[
            df.to_html(classes='data', header="true", index=False)])


@app.route("/download")
def download():
    return send_file(filename,attachment_filename='yourfile.csv', as_attachment=True)
    #return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
