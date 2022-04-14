import streamlit as st

st.title('Bienvenido a Sexuapp')
if 'num' not in st.session_state:
    st.session_state.num = 0

choices1 = ['Cisgénero', 'Crossdresser', 'Drag king', 'Drag queen', 'Disforia de género', 'Fluidez de género', 'género no binario', 'Genderqueer ', 'Intersexual', 'Transgénero', 'Hombre transgénero', 'Mujer transgénero ', 'Gay', 'Inconformidad de género', 'Lesbiana', 'Intersexual', 'Poliamoroso', 'Femenino', 'Masculino', 'Chico', 'Chica', 'Tomboy', 'Hombre joven', 'Mujer joven', 'Hombre transexual', 'Mujer transexual',
 'Bigénero', 'Intersexual', 'Sin género', 'No estoy seguro', 'Prefiero no decir', 'Otro']
choices2 = ['no answer', 'Hombre', 'Mujer']
choices3 = ['no answer', 'No', 'si']
choices4 = ['No', 'Si']
choices5 = ['Llagas', 'Hinchazon', 'Verrugas', 'Inflamacion o enrojecimiento']
choices6 = ['Indoloras', 'dolorosas', 'No presento']
choices7 = ['3 semanas', '2 semanas', '1 mes']


qs1 = [('Cual es tu genero?', choices1),
    ('sexo biologico', choices1),
    ('sexo biologico', choices1)]
qs2 = [('Cual fue tu sexo asignado al nacer?', choices2),
    ('sexo biologico', choices2),
    ('sexo biologico', choices2)]
qs3 = [('Haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como  el condon?', choices3),
    ('Haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como  el condon?', choices3),
    ('Haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como  el condon?', choices3)]
qs4 = [('Haz practicado sexo sin condon?', choices4),
    ('Haz practicado sexo sin condon?', choices4),
    ('Haz practicado sexo sin condon?', choices4)]
qs5 = [('Haz presentado alguno de estos sintomas?', choices5),
    ('Haz presentado alguno de estos sintomas?', choices5),
    ('Haz presentado alguno de estos sintomas?', choices5)]
qs6 = [('En caso de presentar llagas, estas son...?', choices6),
    ('En caso de presentar llagas, estas son...?', choices6),
    ('En caso de presentar llagas, estas son...?', choices6)]
qs7 = [('Cual consideras fue el lapso entre la relacion sexual sospechosa y la precencia de estos sintomas?', choices7),
    ('Cual consideras fue el lapso entre la relacion sexual sospechosa y la precencia de estos sintomas?', choices7),
    ('Cual consideras fue el lapso entre la relacion sexual sospechosa y la precencia de estos sintomas?', choices7)]


def main():
    for _, _, _, _, _, _, _ in zip(qs1, qs2, qs3, qs4, qs5, qs6, qs7): 
        placeholder = st.empty()
        num = st.session_state.num
        with placeholder.form(key=str(num)):
            st.radio(qs1[num][0], key=num+1, options=qs1[num][1])
            st.radio(qs2[num][0], key=num+1, options=qs2[num][1])  
            st.radio(qs3[num][0], key=num+1, options=qs3[num][1])
            st.radio(qs4[num][0], key=num+1, options=qs4[num][1])
            st.radio(qs5[num][0], key=num+1, options=qs5[num][1])
            st.radio(qs6[num][0], key=num+1, options=qs6[num][1])
            st.radio(qs7[num][0], key=num+1, options=qs6[num][1])
                      
            if st.form_submit_button():
                st.session_state.num += 1
                if st.session_state.num >= 3:
                    st.session_state.num = 0 
                placeholder.empty()
            else:
                st.stop()


main()


  
    

                   

