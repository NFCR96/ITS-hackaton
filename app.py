import streamlit as st

st.title('Bienvenido a Sexuapp')
# Using the "with" syntax
with st.form(key='ITS'):
	button = st.button('sexo al nacer?')
	submit_button = st.form_submit_button(label='Submit')



                   

