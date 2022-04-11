import streamlit as st

st.title('Bienvenido a Sexuapp')

import pandas as pd

df = pd.DataFrame({
    'first column': [hombre, mujer],
    'second column':  [hinchazon, enrojeciemnto, picazon]
    })

option = st.selectbox(
    'selecciona tu sexo?',
     df['first column'])


	



                   

