import streamlit as st

st.title('Bienvenido a Sexuapp')
if "button_clicked" not in st.session_state:    
    st.session_state.button_clicked = False

if (    
st.button("Open next part")     
or st.session_state.button_clicked   
 ):    
    if st.button("Pop out balloons"):    
        st.balloons()

	



                   

