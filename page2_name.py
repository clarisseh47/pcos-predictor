import streamlit as st
import pickle

def display_page():
    model_file_path = 'model.pkl'
    with open(model_file_path, 'rb') as f:
        model = pickle.load(f)
    st.title("PCOS Predictor")
    st.header("Check your Risk for PCOS")
    st.write(
        "Try out our model."
    )
    bmi = st.radio("Select your BMI", [0.0, 1.0, 2.0, 3.0])
    mr = st.radio("Select your MR", [0.0, 1.0])
    hir = st.radio("Select your hir", [0.0, 1.0])
    acne = st.radio("Select your acne", [0.0, 1.0, 2.0, 3.0])
    fhx = st.radio("Select your FHx", [0.0, 1.0])
    ins = st.radio("Select your ins", [0.0, 1.0])
    stress = st.radio("Select your stress", [0.0, 1.0, 2.0])
    ur = st.radio("Select your ur", [0.0, 1.0])
    ses = st.radio("Select your SES", [0.0, 1.0, 2.0])
    conc = st.radio("Select your conc", [0.0, 1.0])
    ethn = st.radio("Select your ethn", [0.0, 1.0, 2.0, 3.0, 4.0])
    age = st.number_input("Enter your age", min_value=18, max_value=50)
    ls = st.number_input("Enter your LS", min_value=1, max_value=10)

    if st.button('make pred'):
        input_data = [[bmi, mr, hir, acne, fhx, ins, stress, ur, ses, conc, ethn, age, ls]]
        prediction = model.predict(input_data)
        st.write(f'preidction: {prediction[0]}')