import streamlit as st

st.title('Bienvenido a Sexuapp')
page_names = ['mujer', 'hombre']
page = st.ratio('Sexo', page_names)
st.write("**a conitnuacion selecciona lo siguiente:**",page)

if page = 'mujer':
     st.subheader('welcome to sexuapp!')
     st.write("nice to see you! :wave:")
     check = st.checkbox("click here")
     st.write('state of the checkbox:', check)
if check:
     nested_btn = st.button("button nested in checkbox")
     
     if nested_btn:
          st.write(":cake:"*20)
              



     


  
    

                   

