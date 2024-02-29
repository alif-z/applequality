
import streamlit as st
import pandas as pd
import pickle

st.write("""
# Apple Quality App

### **1. Description**

This app contains information about prediction of the apples quality rating using various attributes.
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

st.subheader('2. User Input parameters') #headler - title #subheader - sub title
st.write(df) #display

loaded_model = pickle.load(open("applequality.h5", "rb"))   #iris_model -

prediction = loaded_model.predict(df)

st.subheader('3. Prediction of Apple Quality')
st.write(prediction)

st.write("""

**Key Features**
1. Size: Size of the fruit
2. Weight: Weight of the fruit
3. Sweetness: Degree of sweetness of the fruit
4. Crunchiness: Texture indicating the crunchiness of the fruit
5. Juiciness: Level of juiciness of the fruit
6. Ripeness: Stage of ripeness of the fruit
7. Acidity: Acidity level of the fruit
8. Quality: Overall quality of the fruit (1 = Good, 0 = Bad)
""")

# add image

option = prediction

if option=='1':
    st.image('good apple.jpg', caption='Good Apple', width=100, use_column_width=100)
else:
    st.image('bad apple.jpg', caption='Bad Apple', width=100, use_column_width=100)
