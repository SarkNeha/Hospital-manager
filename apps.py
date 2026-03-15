from flask import Flask, render_template, request, redirect
from models import Patient
from hospital_data import add_patient, get_patients, get_recent

app = Flask(__name__)

@app.route("/")
def home():
    patients = get_patients()
    recent = get_recent()
    return render_template("index.html", patients=patients, recent=recent)


@app.route("/add", methods=["GET", "POST"])
def add_patient_page():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        diagnosis = request.form["diagnosis"]
        contact = request.form.get("contact", "N/A")

        new_patient = Patient(name, age, diagnosis, contact)
        add_patient(new_patient)

        return redirect("/")

    return render_template("add_patient.html")


if __name__ == "__main__":
    app.run(debug=True)