# Used shell from MBTA-Web-App-Project for this project

from flask import Flask, request, render_template
import nasa

app = Flask(__name__)

@app.route("/")
def index():
    """
    home page with a greeting and a form for the user to enter a date to fetch the astronomy picture of the day.
    """
    return render_template("index.html", username="Astronomy Enthusiast")

@app.route("/get_apod", methods=["POST"])
def get_apod():
    """
    return and display the astronomy picture of the day for the given date from the form.
    """
    date = request.form.get("date")
    if date:
        apod_data = nasa.get_apod(date)
        if apod_data:
            return render_template("apod.html", apod=apod_data, date=date)
        else:
            return render_template("error.html", message="No data found for this date.")
    else:
        return render_template("error.html", message="Invalid date provided.")

if __name__ == "__main__":
    app.run(debug=True)
    