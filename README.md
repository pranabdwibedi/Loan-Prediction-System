# Loan Approval Prediction

## Overview

This project is a Loan Approval Prediction system that uses a machine learning model to predict whether a loan application will be approved or not. The frontend is built using Tkinter, and the backend consists of a FastAPI service that processes the input data and returns predictions.

## Features

- User-friendly GUI built with Tkinter.
- Allows users to input relevant details such as gender, marital status, dependents, education, self-employment status, income, loan amount, loan term, credit history, and property area.
- Sends data to a FastAPI backend for prediction.
- Displays the loan approval status based on the model's output.

## Technologies Used

### Frontend:

- Python
- Tkinter
- ttk (Themed Tkinter Widgets)

### Backend:

- FastAPI
- Requests (for API calls)
- Machine Learning Model (pre-trained for loan approval prediction)

## Installation & Setup

### Prerequisites:

- Python 3.7+
- Required Python libraries:
  ```bash
  pip install tkinter fastapi uvicorn requests
  ```

### Steps to Run the Application:

1. Clone the repository:
   ```bash
   git clone https://github.com/pranabdwibedi/Loan-Approval-Prediction.git
   cd Loan-Approval-Prediction
   ```
2. Start the FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```
3. Run the Tkinter GUI:
   ```bash
   python app.py
   ```

## API Endpoint

The backend exposes a prediction endpoint:

- `POST /predict`: Takes user inputs in JSON format and returns a loan approval status.

Example JSON Request:

```json
{
  "Gender": 1,
  "Married": 1,
  "Dependents": 0,
  "Education": 1,
  "Self_Employed": 0,
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 2000,
  "LoanAmount": 150,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area": 2
}
```

Example Response:

```json
{
  "Loan Status": "Approved"
}
```

## Future Enhancements

- Deploy the backend on a cloud platform.
- Improve GUI design.
- Add authentication for users.
- Enhance model accuracy with additional training data.

## Contributing

Feel free to fork this repository and submit pull requests to improve the project.

## License

This project is open-source and available under the MIT License.


