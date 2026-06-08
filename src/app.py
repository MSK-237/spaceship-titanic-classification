import streamlit as st
import pandas as pd
import joblib

model = joblib.load("spaceship_rf_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.set_page_config(page_title="Spaceship Titanic Classification", layout="centered")

st.title("Spaceship Titanic Classification")
st.write(
    "Bu uygulama, yolcu bilgilerine göre kişinin başka bir boyuta taşınıp taşınmadığını tahmin eder."
)

st.sidebar.header("Yolcu Bilgileri")

home_planet = st.sidebar.selectbox("HomePlanet", ["Earth", "Europa", "Mars"])
cryo_sleep = st.sidebar.selectbox("CryoSleep", [False, True])
destination = st.sidebar.selectbox(
    "Destination",
    ["TRAPPIST-1e", "55 Cancri e", "PSO J318.5-22"]
)
age = st.sidebar.slider("Age", 0, 80, 28)
vip = st.sidebar.selectbox("VIP", [False, True])

room_service = st.sidebar.number_input("RoomService", min_value=0.0, value=0.0)
food_court = st.sidebar.number_input("FoodCourt", min_value=0.0, value=0.0)
shopping_mall = st.sidebar.number_input("ShoppingMall", min_value=0.0, value=0.0)
spa = st.sidebar.number_input("Spa", min_value=0.0, value=0.0)
vr_deck = st.sidebar.number_input("VRDeck", min_value=0.0, value=0.0)

group_size = st.sidebar.slider("GroupSize", 1, 8, 1)
deck = st.sidebar.selectbox("Deck", ["A", "B", "C", "D", "E", "F", "G", "T"])
cabin_num = st.sidebar.number_input("CabinNum", min_value=0.0, value=500.0)
side = st.sidebar.selectbox("Side", ["P", "S"])

total_spend = room_service + food_court + shopping_mall + spa + vr_deck

input_data = pd.DataFrame({
    "HomePlanet": [home_planet],
    "CryoSleep": [cryo_sleep],
    "Destination": [destination],
    "Age": [age],
    "VIP": [vip],
    "RoomService": [room_service],
    "FoodCourt": [food_court],
    "ShoppingMall": [shopping_mall],
    "Spa": [spa],
    "VRDeck": [vr_deck],
    "GroupSize": [group_size],
    "Deck": [deck],
    "CabinNum": [cabin_num],
    "Side": [side],
    "TotalSpend": [total_spend]
})

input_encoded = pd.get_dummies(input_data, drop_first=True)

input_encoded = input_encoded.reindex(
    columns=model_columns,
    fill_value=0
)

if st.button("Tahmin Et"):
    prediction = model.predict(input_encoded)[0]

    if prediction == True:
        st.success("Tahmin: Yolcu başka bir boyuta taşınmış olabilir.")
    else:
        st.warning("Tahmin: Yolcu başka bir boyuta taşınmamış olabilir.")

st.subheader("Girilen Veriler")
st.dataframe(input_data)