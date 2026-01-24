import streamlit as st
import pandas as pd
from core import cargar_combates

combates = cargar_combates()
combates = pd.DataFrame.from_dict(
    data=combates,
    orient="index",
    )

st.dataframe(
    data=combates,
    width="stretch",
    height="auto",
    hide_index=True,
    column_order=["Fecha", "Patrocinador", "Modo", "Equipo_A", "Equipo_B", "Arena", "Control"])

st.divider()

st.subheader(
    body = "Sección Cancelar Combate",
    text_alignment = "center",
    anchor = False
    )
col1,col2,col3 = st.columns(
    [0.5, 1, 0.5],
    gap = "small",
    vertical_alignment = "center"
    )
with col2:
    st.selectbox(
        label = "Seleccione el :violet[combate] a :red[cancelar]:",
        options = [combate for combate in combates.keys()],
        help = "**Elimina un *combate* permanentemente del *sistema*, seleccionando el nombre del *Patrocinador***",
        index = None,
        placeholder = "¡Acción Irreversible!"
        )
    Cancelar = st.button("Cancelar")