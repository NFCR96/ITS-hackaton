import streamlit as st

st.title('Bienvenido a Sexuapp')

st.write('Selecciona tu sexo')
page_names=['hombre', 'mujer']
page=st.ratio('selecciona un sexo',page_names)
if page='hombre':
	st.button('good?')

	



                   

