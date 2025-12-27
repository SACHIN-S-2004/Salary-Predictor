<div align="center">

# 💼 Salary Predictor  
### *Machine Learning–Powered Salary Estimation System*

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Flask](https://img.shields.io/badge/Flask-Web_App-green?style=for-the-badge&logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-UI-purple?style=for-the-badge&logo=bootstrap)

🎯 **Predict employee salary based on experience, education, and job role using Machine Learning**

</div>

---

## 📌 Project Overview

The **Salary Predictor** is an end-to-end **Machine Learning + Web Application** that estimates an individual’s salary using key professional attributes such as age, education level, job title, and years of experience.

This project demonstrates how real-world HR and compensation data can be transformed into a **practical ML solution**, covering the entire pipeline:
- Data preprocessing
- Model training & comparison
- Model selection
- Deployment as a web application

It is designed to reflect **real hiring and compensation scenarios** used by companies.

---

## ✨ Key Features

✔️ Clean and intuitive web interface  
✔️ Handles both numerical and categorical inputs  
✔️ Robust preprocessing using encoding techniques  
✔️ Multiple ML models trained and evaluated  
✔️ Best-performing model deployed for real-time prediction  
✔️ Scalable and production-ready architecture  

---

## 🖼️ Demo Screenshots

<div align="center">

### 📊 Prediction Results

![alt text](sampleScreenshots/Screenshot%20(1701).png)

![alt text](sampleScreenshots/Screenshot%20(1702).png)

*Real-time classification results*

</div>

---
## 🧠 Machine Learning Workflow

### 🔹 Input Features
The model predicts salary using the following inputs:

- **Age**
- **Gender**
- **Education Level**
- **Job Title**
- **Years of Experience**

These features strongly influence salary trends in real-world datasets.

---

### 🔹 Data Preprocessing
- Categorical features encoded using **One-Hot Encoding**
- Numerical features cleaned and validated
- Dataset split into training and testing sets
- Same preprocessing pipeline reused in deployment

---

## 🧪 Models Trained & Evaluated

The following models were trained and compared inside the Jupyter Notebook:

| Model | Description |
|-----|-------------|
| 🌲 Random Forest Regressor | Ensemble model using bagging |
| 🚀 Gradient Boosting Regressor | Sequential boosting model |

---

## 🏆 Model Selection – Why Random Forest?

After evaluating both models on accuracy and generalization:

✅ **Random Forest performed better for this dataset**  
- Lower overfitting  
- Stable predictions across different inputs  
- Better handling of categorical features after encoding  

📌 **Final Decision:**  
➡️ **Random Forest Regressor** was selected for the web application.

---

## 🌐 Web Application Overview

🖥️ **Frontend**
- User-friendly form with validated inputs
- Dropdowns and radio buttons for categorical fields
- Responsive UI using Bootstrap

⚙️ **Backend**
- Flask processes user input
- Preprocessing pipeline applied
- Random Forest model predicts salary in real-time

📊 **Output**
- Predicted salary displayed instantly
- Clean and readable result presentation

---

## 🛠️ Tech Stack

| Layer | Technology |
|----|----|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Model Training | Jupyter Notebook |
| Backend | Flask |
| Frontend | HTML, Bootstrap |
| Deployment | Local (extendable to cloud) |

---
## 📂 Project Structure

