import streamlit as st

st.title("REVENUE PREDICTION")
x = st.number_input('Input temperature')

import pickle
filename = 'model.pickle'
model = pickle.load(open(filename, "rb"))

if st.button('Predict'):
    x_new = x.reshape(-1, 1)
    y_new = model.predict(x_new)
    st.success(y_new)
