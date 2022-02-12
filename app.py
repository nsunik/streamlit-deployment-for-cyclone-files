import streamlit as st
import pickle
import numpy as np
st.set_page_config(layout="wide", page_title="Cyclone", page_icon="Wind")

model = pickle.load(open("Cyclone_Classification.sav", 'rb'))

st.title("Cyclone Classification")
c1, c2 = st.columns(2)
with c1:
    Year = st.number_input("Enter the Year :")
    Wind = st.number_input("Enter the Wind Speed (km/h) :")
    pressure = st.number_input("Enter the Wind Speed Pressure :")
    btn = st.button("Submit")
with c2:
    if btn:
        model.predict([[Year, Wind, pressure]])
        result = model.predict([[Year, Wind, pressure]])
        st.write(int(result))
        if int(result) == 0:
            st.header("This ia a SEVERE TROPICAL STORM Type of Cyclone")
        elif int(result) == 1:
            st.header("This ia a TROPICAL DEPRESSION Type of Cyclone")
        elif int(result) == 2:
            st.header("This ia a TROPICAL STORM Type of Cyclone")
        else:
            st.header("This ia a Typhoon STORM Type of Cyclone")
    else:
        pass

