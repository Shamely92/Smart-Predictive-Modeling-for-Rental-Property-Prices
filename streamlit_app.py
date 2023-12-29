import streamlit as st
import pandas as pd
import joblib

# Load the trained Random Forest model
model = joblib.load(r'C:\Users\THEBEST\Desktop\Jupyter_workbook\test 8\random_forest_model.pkl')

st.title('RENT PREDICTION')

# User Input for Features
st.sidebar.header('User Input Features')

# Example default values (you can change these)
default_lease_type = 0  # Example encoded value
default_lift = 0  # Example encoded value
default_negotiable = 0  # Example encoded value
default_parking = 0  # Example encoded value
default_property_size = 1000  # Example value
default_property_age = 10  # Example value
default_bathroom = 1  # Example value
default_facing = 0  # Example encoded value
default_cup_board = 0  # Example value
default_floor = 0  # Example value
default_total_floor = 0  # Example value
default_water_supply = 0  # Example encoded value
default_building_type = 0  # Example encoded value
default_balconies = 0  # Example value
default_year = 2022  # Example value
default_month = 1  # Example value
default_day = 1  # Example value
default_time_in_mints = 0  # Example value
default_internet = 0  # Example encoded value

# Get user inputs
lease_type = st.sidebar.selectbox('Lease Type', [0, 1, 2, 3], index=0, format_func=lambda x: 'Select' if x == 0 else x)
lift = st.sidebar.selectbox('Lift', [0, 1], index=0, format_func=lambda x: 'Select' if x == 0 else x)
negotiable = st.sidebar.selectbox('Negotiable', [0, 1], index=0, format_func=lambda x: 'Select' if x == 0 else x)
parking = st.sidebar.selectbox('Parking', [0, 1, 2, 3], index=0, format_func=lambda x: 'Select' if x == 0 else x)
property_size = st.sidebar.slider('Property Size', 1, 5000, default_property_size)
property_age = st.sidebar.slider('Property Age', 1, 50, default_property_age)
bathroom = st.sidebar.slider('Bathroom', 1, 5, default_bathroom)
facing = st.sidebar.selectbox('Facing', [0, 1, 2, 3, 4, 5, 6, 7], index=0, format_func=lambda x: 'Select' if x == 0 else x)
cup_board = st.sidebar.slider('Cup Board', 1, 5, default_cup_board)
floor = st.sidebar.slider('Floor', 1, 20, default_floor)
total_floor = st.sidebar.slider('Total Floor', 1, 50, default_total_floor)
water_supply = st.sidebar.selectbox('Water Supply', [0, 1, 2], index=0, format_func=lambda x: 'Select' if x == 0 else x)
building_type = st.sidebar.selectbox('Building Type', [0, 1, 2, 3], index=0, format_func=lambda x: 'Select' if x == 0 else x)
balconies = st.sidebar.slider('Balconies', 0, 5, default_balconies)
year = st.sidebar.slider('Year', 2010, 2025, default_year)
month = st.sidebar.slider('Month', 1, 12, default_month)
day = st.sidebar.slider('Day', 1, 31, default_day)
time_in_mints = st.sidebar.slider('Time in Mints', 0, 1439, default_time_in_mints)
internet = st.sidebar.selectbox('Internet', [0, 1], index=0, format_func=lambda x: 'Select' if x == 0 else x)

# Prepare the user input as a DataFrame for prediction
user_input = pd.DataFrame({
    'lease_type': [lease_type],
    'lift': [lift],
    'negotiable': [negotiable],
    'parking': [parking],
    'property_size': [property_size],
    'property_age': [property_age],
    'bathroom': [bathroom],
    'facing': [facing],
    'cup_board': [cup_board],
    'floor': [floor],
    'total_floor': [total_floor],
    'water_supply': [water_supply],
    'building_type': [building_type],
    'balconies': [balconies],
    'year': [year],
    'month': [month],
    'day': [day],
    'time in mints': [time_in_mints],
    'INTERNET': [internet],
})

# Make a prediction using the loaded model
prediction = model.predict(user_input)

# Display the prediction
st.subheader('Rent Prediction')
st.write(f'The predicted rent is: {prediction[0]:,.2f} INR')