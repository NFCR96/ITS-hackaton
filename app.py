import streamlit as st

st.title('Bienvenido a Sexuapp')
cb1 = st.checkbox('a')

empty = st.empty()
empty.checkbox('b')

if cb1:
    empty.checkbox('b', True)
Or

import streamlit as st

button = st.button('a')

empty = st.empty()
empty.checkbox('c')

if button:
    empty.checkbox('c', True)

	



                   

