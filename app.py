import streamlit as st
import numpy as np

st.title("REVENUE PREDICTION")
x = st.number_input('Input temperature')
x_new = np.array([x])

if st.button('Predict'):
    import pickle
    filename = 'model.pickle'
    model = pickle.load(open('model.pickle', 'rb'))
    x_new = x_new.reshape(-1,1)
    y_new = model.predict(x_new)
    st.success(y_new)  