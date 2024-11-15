from flask import Flask, render_template, request
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the model
with open('model_pickle2', 'rb') as file:
    model = pickle.load(file)

# Route for the home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# Route to handle form submission and make predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    age = int(request.form['age'])

    # Prepare data for prediction
    prediction = model.predict([[area, bedrooms, age]])

    # Render the HTML page with the prediction result
    return render_template("index.html", prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
