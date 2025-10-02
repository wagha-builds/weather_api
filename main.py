from flask import Flask, render_template
import pandas as pd

app = Flask(__name__) # Creating a website object.


# When the user visits the url + "{app route url}" input, it will call the function below it.
@app.route("/") # This line is a decorator.
def home():
    return render_template("home.html")


# <> is a special syntax of flask used to describe the URL pattern.
@app.route("/api/v1/<station>/<date>") # This line is a decorator.
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


# Ensures that the Flask app is run only when this .py file runs directly.
if __name__ == "__main__":
    app.run(debug=True, port=5001)