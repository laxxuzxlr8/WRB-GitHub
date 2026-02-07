import json
import os
import streamlit as st

# --- #: Rutas de Base de Datos :# --- #

RUTA_INVENTARIO = "data/inventario.json"
RUTA_COMBATES = "data/combates.json"

# --- #: Función Guardar Combates :# --- #

def guardar_combates(combates):           
    
    data = {
        "combates": combates
    }
    with open(RUTA_COMBATES, "w") as f:
        json.dump(data, f, indent=4)

# --- #: Función Cargar data :# --- #

def cargar_combates():             # Cargar Combates #
    
    if not os.path.exists(RUTA_COMBATES):
        return
    try:
        with open(RUTA_COMBATES, "r") as f:
            COMBATES = json.load(f)   
            COMBATES = COMBATES.get("combates")
            return COMBATES
    except Exception as e:
        print(f'Error al cargar datos: {e}')
        
def cargar_inventario():          # Cargar Inventario #
    
    if not os.path.exists(RUTA_INVENTARIO):
        return
    try:
        with open(RUTA_INVENTARIO, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f'Error al cargar datos: {e}')
        
# --- #: Justificar Texto con sangría :# --- #

def mostrar_texto(texto: str, sangria: str = "40px"):
    html = f""" 
    <p style="text-align: justify; text-indent: {sangria};"> 
    {texto} 
    </p> 
    """ 
    st.markdown(html, unsafe_allow_html=True)