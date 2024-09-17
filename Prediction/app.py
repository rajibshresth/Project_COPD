# Import the Libraries
import pandas as pd
import pickle
import streamlit as st

# Load the trained model
with open('Best_Random_Forest_Model.pkl', 'rb') as f:
    model = pickle.load(f)


# Streamlit App
def main():
    st.title("COPD Prediction Dashboard")

    # User Input
    st.sidebar.header("User Input")

    age = st.sidebar.slider('Age', 30, 80, 50)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    bmi = st.sidebar.slider("BMI", 10, 40, 25)
    smoking_status = st.sidebar.selectbox("Smoking Status", ["Current", "Former", "Never"])
    biomass_fuel_exposure = st.sidebar.selectbox("Biomass Fuel Exposure", ["Yes", "No"])
    occupational_exposure = st.sidebar.selectbox("Occupational Exposure", ["Yes", "No"])
    family_history = st.sidebar.selectbox("Family History", ["Yes", "No"])
    air_pollution_level = st.sidebar.slider("Air Pollution Level", 0, 300, 50)
    respiratory_infection = st.sidebar.selectbox("Respiratory Infections in Childhood", ["Yes", "No"])
    location = st.sidebar.selectbox("Location", ['Lalitpur' 'Pokhara' 'Kathmandu' 'Butwal' 'Nepalgunj' 'Hetauda' 'Chitwan'
 'Bhaktapur' 'Dharan' 'Biratnagar'])
    
    # Process the Input Data
    input_data ={
        "Age": [age],
        "Biomass_Fuel_Exposure": [biomass_fuel_exposure],
        "Occupational_Exposure": [occupational_exposure],
        "Family_History_COPD": [family_history],
        "BMI": [bmi],
        "Air_Pollution_Level": [air_pollution_level],
        "Respiratory_Infections_Childhood": [respiratory_infection],
        "Smoking_Status_encoded": [smoking_status],
        "Gender_": [gender],
        # "Location": [location],
    }

    # Convert the data to a dataframe
    input_df = pd.DataFrame(input_data)

    # Encode the Data
    input_df["Gender_"] = input_df["Gender_"].map({
    "Male": 1,
    "Female":0
    });
    input_df["Smoking_Status_encoded"] = input_df["Smoking_Status_encoded"].map({
    "Current": 1,
    "Former":0.5,
    "Never":0
    });
    input_df["Biomass_Fuel_Exposure"] = input_df["Biomass_Fuel_Exposure"].map({
    "Yes": 1,
    "No":0
    });
    input_df["Occupational_Exposure"] = input_df["Occupational_Exposure"].map({
    "Yes": 1,
    "No":0
    });
    input_df["Family_History_COPD"] = input_df["Family_History_COPD"].map({
    "Yes": 1,
    "No":0
    });
    input_df["Respiratory_Infections_Childhood"] = input_df["Respiratory_Infections_Childhood"].map({
    "Yes": 1,
    "No":0
    });
    # input_df = pd.get_dummies(input_df, columns=["Location"], drop_first=True)

    # Add Missing Columns
    # missing_columns = set(X_train.columns)

    # Prediction
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.write("Predictions: COPD Detected")
    else:
        st.write("Predictions: No COPD Detected")

if __name__ == "__main__":
    main()