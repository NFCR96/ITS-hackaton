import streamlit as st

st.title('Bienvenido a Sexuapp')
if 'num' not in st.session_state:
    st.session_state.num = 0

choices1 = ['Cisgénero', 'Crossdresser', 'Drag king', 'Drag queen', 'Disforia de género', 'Fluidez de género', 'género no binario', 'Genderqueer ', 'Intersexual', 'Transgénero', 'Hombre transgénero', 'Mujer transgénero ', 'Gay', 'Inconformidad de género', 'Lesbiana', 'Intersexual', 'Poliamoroso', 'Femenino', 'Masculino', 'Chico', 'Chica', 'Tomboy', 'Hombre joven', 'Mujer joven', 'Hombre transexual', 'Mujer transexual',
 'Bigénero', 'Intersexual', 'Sin género', 'No estoy seguro', 'Prefiero no decir', 'Otro']
choices2 = ['Hombre', 'Mujer']
choices3 = ['No', 'Si']
choices4 = ['No', 'Si']
choices5 = ['Llagas', 'Hinchazon', 'Verrugas', 'Inflamacion, enrojecimiento o irritacion (Dentro o fuera de los genitales)']
choices6 = ['Si cuento con ardor', 'No cuento con ardor']
choices7 = ['Pene', 'Testiculos', 'No presento este sintoma']
choices8 = ['Al Orinar', 'Durante el acto sexual', 'Despues de eyacular', 'No presentado ardor']
choices9 = ['Si', 'No']
choices10 = ['Indoloras', 'dolorosas', 'No presento este sintoma']
choices11 = ['Desaparecieron solas,' 'Desaparecieron con algun Tratamiento', 'No presente Llagas']
choices12 = ['Si', 'No', 'No presente Llagas']
choices13 = ['Secrecion (Pene)', 'Secrecion Vagina']
choices14 = ['Sexo Pene-Vagina', 'Sexo Vagina-Vagina', 'Sexo Anal', 'Sexo Oral']
choices15 = ['3 semanas', '2 semanas', '1 mes']


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
qs6 = [('Haz presentado ardor en el pene?', choices6),
    ('Haz presentado ardor en el pene?', choices6),
    ('Haz presentado ardor en el pene?', choices6)]
qs7 = [('La hinchazon fue en?', choices7),
    ('La hinchazon fue en?', choices7),
    ('La hinchazon fue en?', choices7)]
qs8 = [('En caso de haber presentado ardor en el pene, el ardor fue...?', choices8),
    ('En caso de haber presentado ardor en el pene, el ardor fue...?', choices8),
    ('En caso de haber presentado ardor en el pene, el ardor fue...?', choices8)]
qs9 = [('¿Presentas Llagas?', choices9),
    ('¿Presentas Llagas?', choices9),
    ('¿Presentas Llagas?', choices9)]
qs10 = [('En caso de presentar llagas, estas son...?', choices10),
    ('En caso de presentar llagas, estas son...?', choices10),
    ('En caso de presentar llagas, estas son...?', choices10)]
qs11 = [('En caso de Haber presentado Llagas, estas...?', choices11),
    ('En caso de Haber presentado Llagas, estas...?', choices11),
    ('En caso de Haber presentado Llagas, estas...?', choices11)]
qs12 = [('En caso de haber presentado Llagas, y estas hubiesen desaparecido solas, en un periodo de un año (aproximadamente) despues de desaparecer (solas) presentaste sintomas como, Fiebre?, Dolor de Garganta, o Ganglios linfaticos inflados intermientemente durante este perido (Despues de la desaparicion)?', choices12),
    ('En caso de haber presentado Llagas, y estas hubiesen desaparecido solas, en un periodo de un año (aproximadamente) despues de desaparecer (solas) presentaste sintomas como, Fiebre?, Dolor de Garganta, o Ganglios linfaticos inflados intermientemente durante este perido (Despues de la desaparicion)?', choices12),
    ('En caso de haber presentado Llagas, y estas hubiesen desaparecido solas, en un periodo de un año (aproximadamente) despues de desaparecer (solas) presentaste sintomas como, Fiebre?, Dolor de Garganta, o Ganglios linfaticos inflados intermientemente durante este perido (Despues de la desaparicion)?', choices12)]
qs13 = [('Haz presentado algun tipo de secrecion inusual en los genitales?', choices13),
    ('Haz presentado algun tipo de secrecion inusual en los genitales?', choices13),
    ('Haz presentado algun tipo de secrecion inusual en los genitales?', choices13)]
qs14 = [('Como fue la practica sexual de la que sospechas pudiste haberte contagiado?', choices14),
    ('Como fue la practica sexual de la que sospechaspudiste haberte contagiado?', choices14),
    ('Como fue la practica sexual de la que sospechaspudiste haberte contagiado?', choices14)]
qs15 = [('Cual consideras fue el lapso entre la relacion sexual sospechosa y la precencia de estos sintomas?', choices15),
    ('Cual consideras fue el lapso entre la relacion sexual sospechosa y la precencia de estos sintomas?', choices15),
    ('Cual consideras fue el lapso entre la relacion sexual sospechosa y la precencia de estos sintomas?', choices7)]


def main():
    for _, _, _, _, _, _, _, _, _, _, _, _, _, _, _ in zip(qs1, qs2, qs3, qs4, qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13, qs14, qs15): 
        placeholder = st.empty()
        num = st.session_state.num
        with placeholder.form(key=str(num)):
            st.radio(qs1[num][0], key=num+1, options=qs1[num][1])
            st.radio(qs2[num][0], key=num+1, options=qs2[num][1])  
            st.radio(qs3[num][0], key=num+1, options=qs3[num][1])
            st.radio(qs4[num][0], key=num+1, options=qs4[num][1])
            st.radio(qs5[num][0], key=num+1, options=qs5[num][1])
            st.radio(qs6[num][0], key=num+1, options=qs6[num][1])
            st.radio(qs7[num][0], key=num+1, options=qs7[num][1])
            st.radio(qs8[num][0], key=num+1, options=qs8[num][1])
            st.radio(qs9[num][0], key=num+1, options=qs9[num][1])  
            st.radio(qs10[num][0], key=num+1, options=qs10[num][1])
            st.radio(qs11[num][0], key=num+1, options=qs11[num][1])
            st.radio(qs12[num][0], key=num+1, options=qs12[num][1])
            st.radio(qs13[num][0], key=num+1, options=qs13[num][1])
            st.radio(qs14[num][0], key=num+1, options=qs14[num][1])
            st.radio(qs15[num][0], key=num+1, options=qs15[num][1])
                      
            if st.form_submit_button():
                st.session_state.num += 1
                if st.session_state.num >= 3:
                    st.session_state.num = 0 
                placeholder.empty()
            else:
                st.stop()


main()


  
    

                   

