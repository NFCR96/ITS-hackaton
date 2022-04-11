
import streamlit as st
st.title('Bienvenido a Sexuapp')

option = st.selectbox(
     'Cual es tu sexo biologico',
     ('hombre', 'mujer',))
st.form_submit_button("hombre")
     

