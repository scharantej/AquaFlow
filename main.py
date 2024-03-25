
# Import the necessary libraries.
from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import pandas as pd

# Create a Flask application.
app = Flask(__name__)

# Define the route for the home page.
@app.route('/')
def home():
    # Render the home page.
    return render_template('index.html')

# Define the route for the predict page.
@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data.
    consumption = request.form.get('consumption')
    space = request.form.get('space')

    # Convert the form data to numerical values.
    consumption = int(consumption)
    space = int(space)

    # Calculate the recommended tank size.
    tank_size = 1000 * consumption / 365

    # Calculate the number of modules needed.
    num_modules = tank_size / 1000

    # Determine if the system is suitable for the available space.
    if num_modules * 1000 > space:
        suitable = False
    else:
        suitable = True

    # Create a dictionary of the prediction results.
    results = {
        'tank_size': tank_size,
        'num_modules': num_modules,
        'suitable': suitable
    }

    # Render the predict page with the prediction results.
    return render_template('predict.html', results=results)

# Run the application.
if __name__ == '__main__':
    app.run(debug=True)
