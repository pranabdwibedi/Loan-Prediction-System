import tkinter as tk
from tkinter import messagebox, ttk
import requests

# Mapping categorical values to numerical values
value_map = {
    "Gender": {"Male": 1, "Female": 0},
    "Married": {"Yes": 1, "No": 0},
    "Dependents": {"0": 0, "1": 1, "2": 2, "3+": 4},
    "Education": {"Graduate": 1, "Not Graduate": 0},
    "Self_Employed": {"Yes": 1, "No": 0},
    "Property_Area": {"Rural": 0, "Semiurban": 2, "Urban": 1},
    "Credit_History": {"Yes": 1, "No": 0}
}

# Function to check if all fields are filled
def check_fields(*args):
    if all([var.get() for var in variables.values()]) and all(entry.get() for entry in num_entries):
        predict_button.config(state=tk.NORMAL)
    else:
        predict_button.config(state=tk.DISABLED)

# Function to make API request
def predict():
    data = {
        "Gender": value_map["Gender"][gender_var.get()],
        "Married": value_map["Married"][married_var.get()],
        "Dependents": value_map["Dependents"][dependents_var.get()],
        "Education": value_map["Education"][education_var.get()],
        "Self_Employed": value_map["Self_Employed"][self_employed_var.get()],
        "ApplicantIncome": float(entry_applicant_income.get()),
        "CoapplicantIncome": float(entry_coapplicant_income.get()),
        "LoanAmount": float(entry_loan_amount.get()),
        "Loan_Amount_Term": float(entry_loan_term.get()),
        "Credit_History": value_map["Credit_History"][credit_history_var.get()],
        "Property_Area": value_map["Property_Area"][property_area_var.get()]
    }
    
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        result = response.json()
        messagebox.showinfo("Prediction Result", f"Loan Status: {result['Loan_Status']}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to API: {e}")

# Create main window
root = tk.Tk()
root.title("Loan Approval Prediction")
root.geometry("600x650")
root.configure(bg="#e6f7ff")

frame = tk.Frame(root, bg="#e6f7ff", padx=20, pady=20, relief=tk.RIDGE, borderwidth=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Dropdown values
gender_options = ['Male', 'Female']
married_options = ['Yes', 'No']
dependents_options = ['0', '1', '2', '3+']
education_options = ['Graduate', 'Not Graduate']
self_employed_options = ['Yes', 'No']
property_area_options = ['Rural', 'Semiurban', 'Urban']
credit_history_options = ['Yes', 'No']

# Define labels and dropdowns
fields = [
    ("Gender", gender_options, "gender_var"),
    ("Married", married_options, "married_var"),
    ("Dependents", dependents_options, "dependents_var"),
    ("Education", education_options, "education_var"),
    ("Self Employed", self_employed_options, "self_employed_var"),
    ("Property Area", property_area_options, "property_area_var"),
    ("Credit History", credit_history_options, "credit_history_var"),
]

variables = {}
for i, (label, options, var_name) in enumerate(fields):
    tk.Label(frame, text=label, bg="#e6f7ff", font=("Arial", 14, "bold")).grid(row=i, column=0, padx=10, pady=10, sticky="w")
    var = tk.StringVar()
    dropdown = ttk.Combobox(frame, textvariable=var, values=options, state="readonly", font=("Arial", 14), width=25)
    dropdown.grid(row=i, column=1, padx=10, pady=10)
    var.trace_add("write", check_fields)
    variables[var_name] = var

# Assign variables
gender_var = variables["gender_var"]
married_var = variables["married_var"]
dependents_var = variables["dependents_var"]
education_var = variables["education_var"]
self_employed_var = variables["self_employed_var"]
property_area_var = variables["property_area_var"]
credit_history_var = variables["credit_history_var"]

# Entry fields for numerical values
num_entries = []

def create_entry(label_text, row):
    tk.Label(frame, text=label_text, bg="#e6f7ff", font=("Arial", 14, "bold")).grid(row=row, column=0, padx=10, pady=10, sticky="w")
    entry = tk.Entry(frame, font=("Arial", 14), width=27, relief=tk.SUNKEN, bd=3)
    entry.grid(row=row, column=1, padx=10, pady=10)
    num_entries.append(entry)
    entry.bind("<KeyRelease>", lambda event: check_fields())
    return entry

entry_applicant_income = create_entry("Applicant Income", 7)
entry_coapplicant_income = create_entry("Coapplicant Income", 8)
entry_loan_amount = create_entry("Loan Amount", 9)
entry_loan_term = create_entry("Loan Amount Term", 10)

# Predict Button
predict_button = tk.Button(frame, text="Predict", command=predict, bg="#007BFF", fg="white", font=("Arial", 16, "bold"), state=tk.DISABLED, width=25, height=2, relief=tk.RAISED, bd=5)
predict_button.grid(row=11, columnspan=2, pady=20)

# Run Tkinter main loop
root.mainloop()
