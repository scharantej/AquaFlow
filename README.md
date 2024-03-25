## Flask Application Design

### HTML Files

**index.html**

- Entry point for the application.
- Displays a form for users to enter their water consumption data.
- Submits the data to the "/predict" route upon form submission.

### Routes

** / **

- Serves the `index.html` file.

** /predict **

- Accepts the water consumption data from the form submission.
- Processes the data to generate a prediction based on the MVP's core features and solution.
- Returns the prediction to the user in a readable format.

### Execution Flow

1. User opens the application's URL, which serves the `index.html` file.
2. User enters their water consumption data and submits the form.
3. The "/predict" route is triggered, receiving the form data.
4. The "/predict" route processes the data, generates a prediction, and returns it to the user.
5. The user can view the prediction and make an informed decision about the HydraNest Rainwater Harvesting System.

### MVP Features Implementation

**Modular Storage Tanks**

- The prediction considers the user's water consumption and available space to recommend an appropriate tank size.

**Advanced Filtration System**

- The prediction explains the multi-stage filtration system and its impact on water quality.

**Smart Monitoring Dashboard**

- The prediction highlights the benefits of the smart dashboard for tracking water levels and system health.

**Easy Installation Kit**

- The prediction provides information about the DIY-friendly installation and instructional resources available.

**First-Flush Diverter**

- The prediction emphasizes the importance of the first-flush diverter in ensuring clean rainwater collection.