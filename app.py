
import streamlit as st
st.title('Bienvenido a Sexuapp')

option = st.selectbox(
     'Cual es tu sexo biologico',
     ('hombre', 'mujer',))
if hombre:
     nested_btn = st.button("button nested in selectbox")
     
     if nested_btn: 
          st.write(":cake:*25)
                   

