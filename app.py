import streamlit as st
import numpy as np
import pickle

st.title("REVENUE PREDICTION")
x = st.number_input('Input temperature')
x_new = np.array([x])

if st.button('Predict'):
    st.caption('Predict Revenue')
    model = pickle.load(open('model.pickle', 'rb'))
    x_new = x_new.reshape(-1,1)
    y_new = model.predict(x_new)
    st.success(y_new)  
