import streamlit as st

st.title('Bienvenido a Sexuapp')
if st.session_state.get('step') is None:
    st.session_state['step'] = 0
# the number is my 'configuration'
if st.session_state.get('number') is None:
    st.session_state['number'] = 0
  
  
if st.button('start configuration'):
    st.session_state['step'] = 1
  
if st.session_state['step'] == 1:
    with st.form('my form'):
        st.session_state['number'] = st.number_input('choose a number', 1, 13)
        if st.form_submit_button("save configuration"):            
            st.session_state['step'] = 2
            st.experimental_rerun()  # form should not be shown after clicking 'save' 
  
  
if st.session_state['step'] == 2:
    st.write('Your configuration is:')
    st.write(f'number: {st.session_state["number"]}')



                   

