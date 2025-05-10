const form = document.getElementById('predictForm');
console.log(form);
form.addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form refresh
    const Gender = document.querySelector('input[name="gender"]:checked').value;
    const Married = document.querySelector('input[name="married"]:checked').value;
    const Dependents = document.querySelector('input[name="dependents"]:checked').value;
    const Education = document.querySelector('input[name="education"]:checked').value;
    const Self_Employed = document.querySelector('input[name="selfEmp"]:checked').value;
    const ApplicantIncome = document.getElementById('incomeInp').value;
    const CoapplicantIncome = document.getElementById('coIncomeInp').value;
    const LoanAmount = document.getElementById('amountInp').value;
    const Loan_Amount_Term = document.getElementById('termInp').value;
    const Credit_History = document.querySelector('input[name="creditHist"]:checked').value;
    const Property_Area = document.getElementById('propArea').value;
    const formData = {
        Gender : parseFloat(Gender), 
        Married: parseFloat(Married),
        Dependents: parseFloat(Dependents),
        Education: parseFloat(Education),
        Self_Employed : parseFloat(Self_Employed),
        ApplicantIncome : parseFloat(ApplicantIncome),
        CoapplicantIncome : parseFloat(CoapplicantIncome),
        LoanAmount : parseFloat(LoanAmount),
        Loan_Amount_Term : parseFloat(Loan_Amount_Term),
        Credit_History : parseFloat(Credit_History),
        Property_Area : parseFloat(Property_Area)
    };

    fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data.Loan_Status)
            resultPara = document.getElementById('result');
            resultPara.textContent = `Prediction: ${data.Loan_Status}`
            if(resultPara.textContent == "Prediction: Not Approved")
                resultPara.style.color = "red";
            else
                resultPara.style.color = "green";
        })
        .catch(err => {
            console.error("Error:", err);
            result = document.getElementById('result');
            result.textContent = "Server error or CORS issue."
            result.style.color = "red";
        });
});