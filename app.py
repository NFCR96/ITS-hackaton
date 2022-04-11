import streamlit as st

st.title('Bienvenido a Sexuapp')
option = st.selectbox(
     'cual es tu sexo biologico?',
     ('hombre', 'mujer'))
option = st.selectbox(
     'sintomas?',
     ('hinchazon', 'picazon'))
# Input fields
a = st.number_input("First value", 1, 1000)
b = st.number_input("Second value", 1, 1000)

# Perform an operation, and save its result
if st.button("Compute value"):
    result = a * b
    st.experimental_set_query_params(my_saved_result=result)  # Save value

# Retrieve app state
app_state = st.experimental_get_query_params()  

# Display saved result if it exist
if "my_saved_result" in app_state:
    saved_result = app_state["my_saved_result"][0]
    st.write("Here is your result", saved_result)
else:
    st.write("No result to display, compute a value first.")

                   

