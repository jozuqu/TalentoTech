import streamlit as st
import pandas as pd

st.title("""
         # Profundización en el componente de tabla usando streamlit
         """)

# Preparamos un Dataset
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [23, 34, 45, 29],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}
df = pd.DataFrame(data)

# Mostramos la tabla usando st.table
st.subheader("Ejemplo de st.table")
st.table(df)

# Mostramos la tabla usando st.dataframe
st.subheader("Ejemplo de st.dataframe")
st.dataframe(df)

#Podemos agregar un estilo a la tabla
st.subheader("Ejemplo de st.table con estilo")
st.table(df.style.highlight_max(axis=0))

#(data: Data = None, width: int | None = None, height: int | None = None, *, use_container_width: bool = False, hide_index: bool | None = None, column_order: Iterable[str] | None = None, column_config: ColumnConfigMappingInput | None = None, key: Key | None = None, on_select: Literal['ignore'] = "ignore", selection_mode: SelectionMode | Iterable[SelectionMode] = "multi-row") -> DeltaGenerator

# vamos a usar cada parámetro de la función st.dataframe
st.subheader("Ejemplo de st.dataframe con estilo")
st.dataframe(df.style.highlight_max(axis=0), width=300, height=300, use_container_width=True, hide_index=True, column_order=['Edad', 'Ciudad', 'Nombre'])
