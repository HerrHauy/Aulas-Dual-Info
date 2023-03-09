import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write('Segue a lista dos alunos sentados na frente da sala:')

df = pd.DataFrame({
	'Nomes' : ['Natan', 'Herlan', 'Gabriela'],
	'Sobrenomes' : ['Schons', 'Rocha', 'Santos']
	})

df

x = st.slider('x')

st.text_input('Digite seu nome', key='name')

st.write(st.session_state.name,'afirma que ', x, 'ao quadrado é igual a ', x**2)


fig, ax = plt.subplots()
ax.scatter([x], [1])
st.pyplot(fig)



if st.checkbox('Mostrar mensagem secreta'):
	st.write('Mensagem secreta')


option = st.selectbox('Escolha um número de 0 a 10:',[0,1,2,3,4,5,6,7,8,9,10])

'Você escolheu: ', option

add_selectbox = st.sidebar.selectbox('Escolha um animal: ',('Capivara','Jacu', 'Tigre') )

add_slider = st.sidebar.slider('Escolha um intervalo: ', 0.0, 100.0, (25.0,75.0))


st.sidebar.write('O intervalo tem tamanho ', add_slider[1]-add_slider[0] )
