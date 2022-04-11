import streamlit as st

st.title('Bienvenido a Sexuapp')
button1 = st.button('Sexo')

if st.session_state.get('button') != True:

    st.session_state['button'] = button1

if st.session_state['button'] == True:

    st.write("button1 is True")

    if st.button('Hombre'):

        st.write("Hello, it's working")

        st.session_state['button'] = False

        st.checkbox('Hinchazon', 'dolor', 'llagas', 'berrugas')
	if st.session_state.get('hinchazon') != True:

    st.session_state['hinchazon'] = checkbox

if st.session_state['checkbox'] == True:

	



                   

