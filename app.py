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
	
	
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
if st.session_state.get('multiselect') != True:
	 st.session_state['multiselect'] = options
		if st.session_state['multiselect'] == True:
			st.write("options is True")
			 if st.multiselect('Hombre', 'mujer'):

        st.write("Hello, it's working")

        st.session_state['multiselect'] = False

        st.multiselect('Hinchazon', 'dolor', 'llagas', 'berrugas')
	



                   

