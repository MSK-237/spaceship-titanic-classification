# 🚀 Spaceship Titanic Classification

## Project Overview

This project aims to predict whether passengers were transported to an alternate dimension using the Kaggle Spaceship Titanic dataset.

The workflow includes:

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Classification Modeling
- Kaggle Submission
- Streamlit Deployment
- Hugging Face Deployment

---

## Dataset

Source:

Kaggle Spaceship Titanic Competition

The dataset contains passenger information such as:

- HomePlanet
- CryoSleep
- Destination
- Age
- VIP Status
- RoomService
- FoodCourt
- ShoppingMall
- Spa
- VRDeck

Target Variable:

- Transported

---

## Feature Engineering

Additional features were created to improve model performance:

- GroupSize
- Deck
- CabinNum
- Side
- TotalSpend

---

## Models Evaluated

### Logistic Regression

Accuracy: 0.789

### Gradient Boosting

Accuracy: 0.800

### Random Forest

Accuracy: 0.804

Kaggle Public Score: **0.79237**

Random Forest achieved the best overall performance and was selected as the final model.

---

## Results

The Random Forest model successfully classified transported passengers with approximately 80% accuracy on the validation dataset.

Feature engineering contributed positively to model performance by extracting useful information from cabin structure and passenger spending behavior.

The final Kaggle submission achieved a public leaderboard score of **0.79237**.

---

## Streamlit Application

The application allows users to enter passenger information and predict transportation status using the trained Random Forest model.

### Live Demo

Hugging Face Space:

PASTE_YOUR_HUGGINGFACE_LINK_HERE

---

## Kaggle Notebook

PASTE_YOUR_KAGGLE_NOTEBOOK_LINK_HERE

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Streamlit
- Hugging Face

---

## Project Structure

```text
spaceship-titanic-classification/
│
├── src/
│   ├── app.py
│   ├── spaceship_rf_model.pkl
│   └── model_columns.pkl
│
├── requirements.txt
├── README.md
└── notebook.ipynb
```

---

## Acknowledgement

This project was developed for educational and portfolio purposes using the Kaggle Spaceship Titanic dataset.