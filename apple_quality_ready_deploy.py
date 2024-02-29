
import streamlit as st
import pandas as pd
import pickle

st.write("""
# Apple Quality App

This app wants to know the **Quality** of each apple!
""")

st.sidebar.header('User Input Parameters') #inside sidebar, function we select is

def user_input_features():
    Size = st.sidebar.slider('Size', 0.0, 0.489598, 1.0)
    Weight = st.sidebar.slider('Weight', 0.0, 0.476418, 1.0)
    Sweetness = st.sidebar.slider('Sweetness', 0.0, 0.481538, 1.0)
    Crunchiness = st.sidebar.slider('Crunchiness', 0.0, 0.515785, 1.0)
    Juiciness = st.sidebar.slider('Juiciness', 0.0, 0.487466, 1.0)
    Ripeness = st.sidebar.slider('Ripeness', 0.0, 0.486020, 1.0)
    Acidity = st.sidebar.slider('Acidity', 0.0, 0.487895, 1.0)


    data = {'Size': Size,
            'Weight': Weight,
            'Sweetness': Sweetness,
            'Crunchiness': Crunchiness,
            'Juiciness': Juiciness,
            'Ripeness': Ripeness,
            'Acidity': Acidity}

    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters') #headler - title #subheader - sub title
st.write(df) #display

loaded_model = pickle.load(open("applequality.h5", "rb"))   #iris_model -

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write("""
Prediction if the apple is good or bad

             Note :
             1 = Good
             0 = Bad""")



