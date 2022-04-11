import streamlit as st

st.title('Bienvenido a Sexuapp')
def show_names(name):
	if name == "Roy":
		list1 = ['Riya','Ananya','Tanya','Sanya','Nikita']
	elif name == "Sen":
		list1 = ['Tarun','Arun','Bob','Karan','John']
	
	return list1
import SessionState
import naming as n

def inp_det(type):
    if type == 'source':
        st.write('Enter name (Roy/Sen)')
        name = st.text_input('Source name')
    elif type == 'destination':
        st.write('Enter name (Roy/Sen)')
        name = st.text_input('Destination name')
    return name
    
def main():
    name = inp_det('source')
    session_state = SessionState.get(name="", button_sent=False)
    button_sent = st.button("SUBMIT")
    if button_sent or session_state.button_sent: # <-- first time is button interaction, next time use state to go to multiselect
        session_state.button_sent = True
        listnames = n.show_names(name)
        selectednames=st.multiselect('Select your names',listnames)
        st.write(selectednames)

if __name__ == "__main__":
    main()

                   

