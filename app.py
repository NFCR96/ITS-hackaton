import streamlit as st

st.title('Bienvenido a Sexuapp')
if 'num' not in st.session_state:
    st.session_state.num = 0


choices1 = ['no answer', 'Hombre', 'Mujer']
choices2 = ['no answer', 'No', 'si']
choices3 = ['No', 'Si']
choices4 = ['Llagas', 'Hinchazon', 'Verrugas', 'Inflamacion o enrojecimiento']
choices5 = ['Indoloras', 'dolorosas', 'No presento']
choices6 = ['3 semanas', '2 semanas', '1 mes']


qs1 = [('Sexo biologico?', choices1),
    ('sexo biologico', choices1),
    ('sexo biologico', choices1)]
qs2 = [('haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como  el condon?', choices2),
    ('What country has the highest population?', choices2),
    ('What country has the highest oil deposits?', choices2)]
qs3 = [('Haz practicado sexo sin condon? ?', choices3),
    ('What country has the highest population?', choices3),
    ('What country has the highest oil deposits?', choices3)]
qs4 = [('Haz presentado alguno de estos sintomas?', choices4),
    ('What country has the highest population?', choices4),
    ('What country has the highest oil deposits?', choices4)]
qs5 = [('En caso de presentar llagas, estas son...?', choices5),
    ('What country has the highest population?', choices5),
    ('What country has the highest oil deposits?', choices5)]
qs5 = [('Cual consideras fue el lapso entre la relacion sexual sospechosa y la precencia de estos sintomas?', choices6),
    ('What country has the highest population?', choices6),
    ('What country has the highest oil deposits?', choices6)]


def main():
    for _, _ in zip(qs1, qs2, qs3, qs4, qs5, qs6): 
        placeholder = st.empty()
        num = st.session_state.num
        with placeholder.form(key=str(num)):
            st.radio(qs1[num][0], key=num+1, options=qs1[num][1])
            st.radio(qs2[num][0], key=num+1, options=qs2[num][1])  
            st.radio(qs3[num][0], key=num+1, options=qs3[num][1])
            st.radio(qs4[num][0], key=num+1, options=qs4[num][1])
            st.radio(qs5[num][0], key=num+1, options=qs5[num][1])
            st.radio(qs6[num][0], key=num+1, options=qs6[num][1])
                      
            if st.form_submit_button():
                st.session_state.num += 1
                if st.session_state.num >= 3:
                    st.session_state.num = 0 
                placeholder.empty()
            else:
                st.stop()


main()


  
    

                   

