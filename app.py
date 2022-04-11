import streamlit as st

st.title('Bienvenido a Sexuapp')
a = st.selectbox(
     'cual es tu sexo biologico?',
     ('hombre', 'mujer'))
b = st.selectbox(
     'sintomas?',
     ('hinchazon', 'picazon'))
# Input fields
if st.button("submit"):
     result = a+b
     


  
    

                   

