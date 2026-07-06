from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Enter the R² score printed by train_model.py
accuracy = 0.9187   # Replace with your actual R² score

@app.route("/")
def home():
    return render_template("index.html", accuracy=accuracy)

@app.route("/predict", methods=["POST"])
def predict():

    income = float(request.form["income"])
    age = float(request.form["age"])
    rooms = float(request.form["rooms"])
    bedrooms = float(request.form["bedrooms"])
    population = float(request.form["population"])

    features = np.array([[income, age, rooms, bedrooms, population]])

    prediction = model.predict(features)

    return render_template(
        "index.html",
        prediction_text=f"Estimated House Price: ${prediction[0]:,.2f}",
        accuracy=accuracy
    )

if __name__ == "__main__":
    app.run(debug=True)