import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parametros")
st.write("Elaborado por :Franco Olivera")

modulos = st.sidebar.selectbox("Selecione el módulo",["Listas", "Arreglos", "Funciones", "POO"])

if modulos == "Listas":
  st.write("Te encuentras en el módulo de listas")

elif modulos == "Arreglos":
  st.write("Te encuentras en el módulo de arreglos")

elif modulos == "Funciones":
  st.write("Te encuentras en el módulo de Funciones")
  
else:
  st.write("Te encuentras en el módulo de POO")
