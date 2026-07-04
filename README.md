# 🚢 Titanic Survival Prediction System

A machine learning and deep learning-based Titanic Survival Prediction System developed using **Python**. The application predicts whether a passenger is likely to survive the Titanic disaster based on passenger information such as age, gender, fare, and passenger class.

---

## 📖 Project Overview

The Titanic Survival Prediction System analyzes passenger details and predicts survival probability using a trained predictive model. The application accepts user input through a simple command-line interface and provides both the survival probability and the final prediction.

This project demonstrates the application of predictive analytics in solving a binary classification problem using the Titanic dataset.

---

## ✨ Features

- 🚢 Predict passenger survival on the Titanic
- 👤 Age-based prediction
- 🚻 Gender-based analysis
- 💰 Fare-based evaluation
- 🎟️ Passenger class analysis
- 📊 Displays survival probability
- ⚡ Fast prediction results
- 💻 Simple command-line interface

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Scikit-learn

---

## 📂 Project Structure

```
Titanic-Survival-Prediction/
│── train.py
│── app.py
│── requirements.txt
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/hemasree200807/Titanic-Survival-Prediction.git
```

### Navigate to the project folder

```bash
cd Titanic-Survival-Prediction
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python train.py
```

### Run the Prediction Application

```bash
python app.py
```

---

## ▶️ How It Works

1. Train the prediction model using `train.py`.
2. Run `app.py`.
3. Enter the passenger details:
   - Age
   - Gender
   - Fare
   - Passenger Class
4. The trained model analyzes the passenger information.
5. The application displays:
   - Survival Probability
   - Final Prediction (Survived: Yes / No)

---

## 📊 Input Parameters

| Parameter | Description |
|-----------|-------------|
| Age | Passenger's age |
| Gender | Male or Female |
| Fare | Ticket fare paid by the passenger |
| Passenger Class | Travel class (1, 2, or 3) |

---

## 📌 Sample Input

```
Enter Age: 30
Gender (male/female): female
Fare: 2
Class (1/2/3): 1
```

## 📌 Sample Output

```
Probability: 0.87133366
Survived : Yes
```

---

## 📈 Future Enhancements

- Graphical User Interface (GUI)
- Streamlit web dashboard
- Batch prediction using CSV files
- Model performance visualization
- Passenger data analytics
- Interactive prediction dashboard

---

## 👩‍💻 Developed By

**Hemasree**

GitHub: https://github.com/hemasree200807

---

## 📄 License

This project is developed for educational and learning purposes.
