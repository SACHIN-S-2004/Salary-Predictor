from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("salaryPredict_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":
        try:
            input_data = {
                "Age": int(request.form["age"]),
                "Gender": request.form["gender"],
                "Education Level": request.form["educationLevel"],
                "Job Title": request.form["job_title"],
                "Years of Experience": int(request.form["exp"])
            }

            input_df = pd.DataFrame([input_data])

            predicted_price = model.predict(input_df)[0]

            prediction = round(predicted_price, 2)

        except Exception as e:
            print("Prediction error:", e)
            prediction = "Error"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
