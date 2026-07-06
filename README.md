# 🏠 House Price Prediction

A Machine Learning web application built with **Flask** that predicts house prices based on various housing features. The model is trained using **Linear Regression** from Scikit-learn and deployed through a simple web interface.

---

## 📌 Features

- Predict house prices instantly
- User-friendly web interface
- Machine Learning model using Linear Regression
- Flask backend
- HTML & CSS frontend
- Trained model stored as a `.pkl` file

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML5
- CSS3

---

## 📂 Project Structure

```
House_prediction/
│── app.py
│── train_model.py
│── housing.csv
│── house_model.pkl
│── requirements.txt
│── Procfile
│── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/deen-cyber/House_prediction.git
```

Move into the project folder:

```bash
cd House_prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

If the model file is not available, train it using:

```bash
python train_model.py
```

This generates the trained model file (`house_model.pkl`).

---

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

*(Use the port shown in your terminal if it differs, for example `5001`.)*

---

## 📊 Input Features

The application predicts house prices using:

- Average Area Income
- Average House Age
- Average Number of Rooms
- Average Number of Bedrooms
- Area Population

---

## 📸 Screenshots

Add screenshots here.

Example:

```
<img width="1181" height="770" alt="Screenshot 2026-07-06 at 2 10 15 PM" src="https://github.com/user-attachments/assets/afe490e5-23b7-4c29-a1f6-1809ec05e94e" /><img width="1170" height="781" alt="Screenshot 2026-07-06 at 2 10 46 PM" src="https://github.com/user-attachments/assets/ac7b2f4e-cd6e-4701-9a6a-0fe394b50357" />
<img width="1512" height="982" alt="Screenshot 2026-07-06 at 2 09 39 PM" src="https://github.com/user-attachments/assets/bd57083f-5588-4f3a-874b-d95f4ebf4bf8" />


```

---

## 🌐 Live Demo

Render Deployment:

```
https://house-prediction-eg1g.onrender.com
```

---

## 👨‍💻 Author

**Deendayal Kumar**

GitHub: https://github.com/deen-cyber

---

## 📄 License

This project is created for educational and learning purposes.
