import streamlit as st
import pandas as pd
import numpy as np
st.write("""
         # Aplicación inicial de Streamlit
            Una exploración de Streamlit para aprender los diferentes componentes de la librería
         """)

st.write("""
         ##componente Slider
         ###Muestra un slider en la interfaz de usuario recibe un título y un rango de valores
         """)

st.slider("Que numero desea", 0, 100)

st.write("""
         ##componente Checkbox
         ### Muestra un checkbox en la interfaz de usuario recibe un título y un valor por defecto
        """)
st.checkbox("Mostrar/Ocultar")

st.write("""
         ##componente Radio
         ### Muestra un radio button en la interfaz de usuario recibe un título y una lista de opciones
        """)
st.radio("Cual raza prefiere?", ("Pug", "Huskee", "Labrador"))

st.write("""
         ##componente Selectbox
         ## Muestra un selectbox en la interfaz de usuario recibe un título y una lista de opciones
        """)
st.selectbox("Que fruta come más?", ("Pera", "Manzana", "Uva"))

st.write("""
         ##componente MultiSelect
         ### Muestra un multiselect en la interfaz de usuario recibe un título y una lista de opciones
        """)
st.multiselect("Cual es el color deseado?", ("Negro", "Blanco", "Azul"))
st.write("""
         ##componente Text Input
         ### Muestra un campo de texto en la interfaz de usuario recibe un título y un valor por defecto
        """)
st.text_input("Ingrese su nombre")

st.write("""
         ##componente Number Input
         ### Muestra un campo de entrada numérica en la interfaz de usuario recibe un título y un rango de valores
        """)
st.number_input("Ingrese su edad", 0, 100)

st.write("""
         ##componente Date Input
         ### Muestra un selector de fecha en la interfaz de usuario recibe un título
        """)
st.date_input("Seleccione una fecha")

st.write("""
         ##componente File Uploader
         ### Muestra un componente para subir archivos en la interfaz de usuario recibe un título
        """)
st.file_uploader("Suba un archivo")

import matplotlib.pyplot as plt

st.write("""
         ##componente Tabs
         ### Muestra un conjunto de pestañas en la interfaz de usuario
        """)
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Esta es la Tab 1")
    st.line_chart(np.random.randn(20, 2))

with tab2:
    st.write("Esta es la Tab 2")
    st.bar_chart(np.random.randn(20, 2))

st.write("""
         ##componente Table
         ### Muestra una tabla en la interfaz de usuario
        """)
df = pd.DataFrame({
    'Column A': np.random.randn(10),
    'Column B': np.random.randn(10),
    'Column C': np.random.randn(10)
})
st.table(df)

st.write("""
         ##componente DataFrame
         ### Muestra un DataFrame en la interfaz de usuario
        """)
st.dataframe(df)

st.write("""
         ##componente Gráfica con Slider
         ### Muestra una gráfica que se puede modificar con un slider
        """)
x = st.slider("Seleccione el valor de X", 1, 100, 50)
y = x * np.random.randn(100)
fig, ax = plt.subplots()
ax.hist(y, bins=30)
st.pyplot(fig)
