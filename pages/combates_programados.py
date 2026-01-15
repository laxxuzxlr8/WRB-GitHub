import streamlit as st
import pandas as pd


import sys
sys.path.append(r"C:\Users\Adrian\Documents\GitHub\Proyecto - Copy")
from core import cargar_combates


combates = cargar_combates()
combates = pd.DataFrame.from_dict(
    data=combates,
    orient="index",
    )
# combates = pd.DataFrame(combates).drop(columns="patrocinador")

st.dataframe(
    data=combates,
    width="stretch",
    height="auto",
    hide_index=True,
    column_order=["fecha", "patrocinador", "modo", "equipo_a", "equipo_b", "arena", "control"])