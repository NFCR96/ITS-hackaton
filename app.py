import streamlit as st

st.title('Bienvenido a Sexuapp')
import SessionState

button1 = st.empty()
text1 = st.empty()
button2 = st.empty()
text2 = st.empty()

ss = SessionState.get(button1 = False)

if button1.button('1') :
    ss.button1 = True

if ss.button1:
    text1.write('you clicked the first button')
    if button2.button('2'):
        text2.write('you clicked the second button')

	



                   

