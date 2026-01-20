import streamlit as st
import json
import datetime as datetime
from time import sleep
import re
import pandas as pd
from core import cargar_inventario, cargar_combates, guardar_combates

# --- #: Algoritmo de combates :# --- #

RUTA_COMBATES = "data/combates.json"

def guardar_combates():           # ~ Guardar Combates ~ #
    data = {
        "combates": st.session_state.get("combates_programados")
    }
    with open(RUTA_COMBATES, "w") as f:
        json.dump(data, f, indent=4)

# --- #: Funciones auxiliares :# --- #

def validar_combate():               # ~ Campos vacios ~ #
    llaves_estado = []
    
    for key, value in st.session_state.combate.items():
        if key in ["Equipo_A", "Equipo_B"]:
            if st.session_state.combate["Modo"] == "Robot vs Robot":
                if len(st.session_state.combate[key]) < 1:
                    llaves_estado.append(key)
            else:
                if len(st.session_state.combate[key]) < 3:
                    llaves_estado.append(key)
        elif not value:
            llaves_estado.append(key)
    
    if len(llaves_estado) == 0:
        return True, "" 
    else:
        return False, llaves_estado    

def resetear_web():                 # ~ Resetea los datos de la web ~ #
    st.session_state.combate.update({
        "Fecha": None,
        "Arena": None,
        "Modo": None,
        "Equipo_A": {},
        "Equipo_B": {},
        "Control": None,
        "Patrocinador": ""
        })
    
    st.session_state.inventario.update(cargar_inventario())
    
    st.session_state.combates_programados.update(cargar_combates())
    
    st.session_state.disponibles = {
        "robots" : [],
        "armas" : [],
        "arena" : []
    }
    
    st.session_state.usados = {
        "robots" : [],
        "armas" : []
    }
    
    st.session_state.fecha_anterior = None
    
    st.session_state.len_anterior = {
        "Equipo_A" : 0,
        "Equipo_B" : 0
    }
    
    st.session_state.modo_anterior = None
    
def recursos_disponibles():                   # ~ Asigna los recursos disponibles ~ #
    if st.session_state.usados["robots"] != []:
        st.session_state.disponibles["robots"] = [robot for robot in st.session_state.disponibles["robots"] if robot not in st.session_state.usados["robots"]]
        st.session_state.disponibles["armas"] = [arma for arma in st.session_state.disponibles["armas"] if arma not in st.session_state.usados["armas"]]  
        
def validar_robot(robot):            # ~ Robot Valido ~ #

    if robot == "a":
        a = ["Equipo_A", robot_a, arma_izq_a, arma_der_a]
        
        if len(st.session_state.combate[a[0]]) == 1 and st.session_state.combate["Modo"] == "Robot vs Robot":
            return False, "El equipo está lleno."
        
        elif len(st.session_state.combate[a[0]]) == 3 and st.session_state.combate["Modo"] == "Equipo vs Equipo":
            return False, "El equipo está lleno."
        
        else:
            if a[1] == None or a[2] == None or a[3] == None:
                return False, "Debe llenar todos los campos para que el combate sea justo."
            if a[2] == a[3]:
                return False, "No puede haber armas repetidas."
    
    if robot == "b":
        b = ["Equipo_B", robot_b, arma_izq_b, arma_der_b]
        
        if len(st.session_state.combate[b[0]]) == 1 and st.session_state.combate["Modo"] == "Robot vs Robot":
            return False, "El equipo está lleno."
        
        elif len(st.session_state.combate[b[0]]) == 3 and st.session_state.combate["Modo"] == "Equipo vs Equipo":
            return False, "El equipo está lleno."
        
        else:
            if b[1] == None or b[2] == None or b[3] == None:
                return False, "Debe llenar todos los campos para que el combate sea justo."
            if b[2] == b[3]:
                return False, "No puede haber armas repetidas."
    
    return True, ''

def validar_patrocinador():                     # ~ Patrocinador Valido ~ #
    
    for patro in st.session_state.combates_programados:
        if Patrocinador == patro:
            return False, "Ya existe un Patrocinador con este nombre, escriba otro."
    
    if not re.match(r'^[A-Za-z\\\\s-]+$', Patrocinador):
        return False, "Patrocinador solo debe contener letras, espacios y guiones."
    
    if len(Patrocinador) < 2:
        return False, "Patrocinador debe tener al menos 2 caracteres"
    
    return True, ""

# --- #: Creacióon del session_state :# --- #

if "combate" not in st.session_state:           # ~ Creacion del combate ~ #
    st.session_state.combate = {
        "Fecha": None,
        "Arena": None,
        "Modo": None,
        "Equipo_A": {},
        "Equipo_B": {},
        "Control": None,
        "Patrocinador": None
        }

if "inventario" not in st.session_state:           # ~ Inventario ~ #
    st.session_state.inventario = cargar_inventario()
    
if "combates_programados" not in st.session_state:                  # ~ Combates programados ~ #
    combat = cargar_combates()
    st.session_state.combates_programados = combat

if "disponibles" not in st.session_state:              # ~ Recursos disponibles ~ # 
    st.session_state.disponibles = {
        "robots" : None,
        "armas" : None,
        "arena" : None
    }

if "usados" not in st.session_state:                # ~ Recursos usados ~ #
    st.session_state.usados = {
        "robots" : [],
        "armas" : []
    }

if "fecha_anterior" not in st.session_state:            # ~ Control reset con cambio de fecha ~ #
    st.session_state.fecha_anterior = None
    
if "len_anterior" not in st.session_state:              # ~ Control robot añadido ~ #
    st.session_state.len_anterior = {
        "Equipo_A" : 0,
        "Equipo_B" : 0,
    }
    
if "modo_anterior" not in st.session_state:               # ~ Control modo ~ #
    st.session_state.modo_anterior = None

# --- #: Panel Principal :# --- #

st.header("Organizar combate:", 
             text_alignment="center",
             anchor=False
             )

# --- #: Sección Fecha y Lugar :# --- #

st.subheader(
    body="Fechar y lugar:", 
    text_alignment="center", 
    anchor=False
    )

Fecha = st.date_input(    
    label="**Elija una :violet[Fecha] para el combate:**", 
    min_value="today", 
    value=st.session_state.combate["Fecha"],
    format="DD/MM/YYYY",
    help="*Fecha* en la cual se desarrollará el combate."
    )

# --- #: Algoritmo de validación de Fecha y eliminacion de recursos :# --- #

if Fecha != st.session_state.fecha_anterior:
 
    arena_no = []
    robot_no = []
    armas_no = []
    
    for evento in st.session_state.combates_programados.values():           # ~ Selecciona recursos de fechas iguales ~ #
        if evento["Fecha"] == str(Fecha):
            arena_no.append(evento["Arena"])
            for rob_a, armas_a in evento["Equipo_A"].items():
                robot_no.append(rob_a)
                armas_no.append(armas_a[0])
                armas_no.append(armas_a[1])
            for rob_b, armas_b in evento["Equipo_B"].items():
                robot_no.append(rob_b)
                armas_no.append(armas_b[0])
                armas_no.append(armas_b[1])
                
    if len(arena_no) == 0:                                      # ~ Define los recursos disponibles ~ #
        st.success("Día valido, no hay eventos programados!")   
        st.session_state.combate["Fecha"] = str(Fecha)
        st.session_state.disponibles["arena"] = [arena for arena in st.session_state.inventario["arena"]]
        st.session_state.disponibles["robots"] = [robot for robot in st.session_state.inventario["robots"].keys()]
        st.session_state.disponibles["armas"] = [arma for arma in st.session_state.inventario["armas_equipables"].keys()]
    
    elif len(arena_no) >= len(st.session_state.inventario["arena"]):
        st.error("Todas las arenas estan ocupadas para ese día, escoja otro.")
        st.session_state.combate["Fecha"] = None
        st.session_state.disponibles["arena"] = []
        
    else:
        st.info("Se mostrarán solo las arenas, robots y armas disponibles para esa fecha.")
        st.session_state.disponibles["arena"] = [arena for arena in st.session_state.inventario["arena"] if arena not in arena_no]
        st.session_state.disponibles["robots"] = [robot for robot in st.session_state.inventario["robots"].keys() if robot not in robot_no]
        st.session_state.disponibles["armas"] = [arma for arma in st.session_state.inventario["armas_equipables"].keys() if arma not in armas_no]   
        st.session_state.combate["Fecha"] = str(Fecha)    
    
    st.session_state.fecha_anterior = str(Fecha)   

# --- #: Sección Arena :# --- #

Arena = st.selectbox(
    label="**Seleccione la :violet[Arena] del combate:**",
    options=st.session_state.disponibles["arena"],
    help="Arena donde se desarrollará el combate: en un *terreno limpio* o en un *espacio con obstáculos*.",
    index=None, 
    )

if Arena:
    st.session_state.combate["Arena"] = Arena

st.write("\n")
st.divider()

# --- #: Sección Modo de juego :# --- #

with st.container(
    key="Modo", 
    horizontal_alignment="center"
    ):
    
    st.subheader(
        "Modo de juego:", 
        text_alignment="center", 
        anchor=False
        )
    
    st.session_state.combate["Modo"] = st.radio(
        label="Escoja un Modo de juego:",
        label_visibility="hidden",
        options=["Robot vs Robot", "Equipo vs Equipo"]
        )

if st.session_state.combate["Modo"] != st.session_state.modo_anterior:         # ~ Control con cambia de modo ~ #     
    st.session_state.combate["Equipo_A"] = {}
    st.session_state.combate["Equipo_B"] = {}
    st.session_state.len_anterior = {
        "Equipo_A" : 0,
        "Equipo_B" : 0,
    }
    st.session_state.usados = {
        "robots" : [],
        "armas" : []
    }
    st.session_state.modo_anterior = st.session_state.combate["Modo"]
    st.rerun()

st.divider()

# --- #: Sección Equipos :# --- #

st.subheader(
    body="Gestionar equipos:",
    text_alignment="center",
    anchor=False
    )
 
recursos_disponibles()

col1, col2 = st.columns(
    2, 
    gap = "large", 
    vertical_alignment="center"
    )

with col1:                      # ~ Asignacion Equipo A ~ #
        
    if st.session_state.combate["Modo"] == "Robot vs Robot":  
        st.subheader(
            body="Combatiente A", 
            text_alignment="center",
            anchor=False
            )
    else:
        st.subheader(
            body="Equipo A", 
            text_alignment="center",
            anchor=False
            )        
    
    with st.form(
        key="form_robot_a",
        clear_on_submit=True,
        enter_to_submit=True
        ):
                
        robot_a = st.selectbox(
            "Escoja un robot:",
            options=st.session_state.disponibles["robots"],
            index=None,
            on_change= recursos_disponibles()
            )
                
        arma_izq_a = st.selectbox(
            "Escoja un arma para el brazo izquierdo:",
            options=st.session_state.disponibles["armas"],
            index=None,
            on_change= recursos_disponibles()
            )
                
        arma_der_a = st.selectbox(
            "Escoja un arma para el brazo derecho:",
            options=st.session_state.disponibles["armas"],
            index=None,
            on_change= recursos_disponibles()
            )
                
        bt_a = st.form_submit_button("Agregar Robot")
         
    if bt_a:
        if st.session_state.combate["Fecha"] != None:
            valido_A, mensaje_A = validar_robot("a")      
            if not valido_A:
                st.warning(mensaje_A)
            else:
                st.session_state.combate["Equipo_A"][robot_a] = [arma_izq_a, arma_der_a]
                st.session_state.usados["robots"] += [robot_a]
                st.session_state.usados["armas"] += [arma_izq_a]
                st.session_state.usados["armas"] += [arma_der_a]
                st.rerun()
        else:
            st.warning("Escoja una Fecha primero.")

    if len(st.session_state.combate["Equipo_A"]) > st.session_state.len_anterior["Equipo_A"]:
        st.success("Robot añadido!")
        st.session_state.len_anterior["Equipo_A"] += 1

with col2:                      # ~ Asignacion Equipo B ~ #
        
    if st.session_state.combate["Modo"] == "Robot vs Robot":    
        st.subheader(
            body="Combatiente B", 
            text_alignment="center",
            anchor=False
            )
        
    else:
        st.subheader(
            body="Equipo B", 
            text_alignment="center",
            anchor=False
            )
            
    with st.form(
        key="form_robot_b",
        clear_on_submit=True,
        enter_to_submit=True
        ):
                
        robot_b = st.selectbox(
            "Escoja un robot:",
            options=st.session_state.disponibles["robots"],
            index=None,
            on_change= recursos_disponibles()
            )
                
        arma_izq_b = st.selectbox(
            "Escoja un arma para el brazo izquierdo:",
            options=st.session_state.disponibles["armas"],
            index=None,
            on_change= recursos_disponibles()
            )
                
        arma_der_b = st.selectbox(
            "Escoja un arma para el brazo derecho:",
            options=st.session_state.disponibles["armas"],
            index=None,
            on_change= recursos_disponibles()
            )
                
        bt_b = st.form_submit_button("Agregar Robot")
                
    if bt_b:
        if st.session_state.combate["Fecha"] != None:
            valido_B, mensaje_B = validar_robot("b")      
            if not valido_B:
                st.warning(mensaje_B)
            else:
                st.session_state.combate["Equipo_B"][robot_b] = [arma_izq_b, arma_der_b]
                st.session_state.usados["robots"] += [robot_b]
                st.session_state.usados["armas"] += [arma_izq_b]
                st.session_state.usados["armas"] += [arma_der_b]
                st.rerun()
        else:
            st.warning("Escoja una Fecha primero.")
    if len(st.session_state.combate["Equipo_B"]) > st.session_state.len_anterior["Equipo_B"]:
        st.success("Robot añadido!")
        st.session_state.len_anterior["Equipo_B"] += 1
            
st.divider()

# --- #: Sección otros detalles :# --- #

st.subheader(
    body="Detalles finales:",
    text_alignment="center",
    anchor=False
)

st.write("\n")

col1,col2 = st.columns(
    [0.6, 1.4],
    gap = "small",
    vertical_alignment='top')

with col1:                      # ~ Seccion control ~ #
    
    with st.container(
        key="final", 
        horizontal_alignment="center",
        ):
        
        st.session_state.combate["Control"] = st.radio(
            label="**Escoja un tipo de :violet[Control]:**",
            options=["Control Manual", "AI Boxing"],
            index=0,
            horizontal=True,
            help="Escoger entre controlar a los robots *manualmente* o con *IA Boxing*."
            )

with col2:                      # ~ Seccion Patrocinador ~ #
    
    Patrocinador = st.text_input(
        label="**Escriba el nombre de un :violet[Patrocinador] para el combate:**",
        value=st.session_state.combate["Patrocinador"],
        max_chars=20,
        help="*Encargador* o *responsable* del combate.",
        )
    
    if Patrocinador:                    # ~ Validacion Patrocinador ~ #
        valid, error = validar_patrocinador()
        if not valid:
            st.error(error)
            st.session_state.combate["Patrocinador"] = None
        else:
            st.session_state.combate["Patrocinador"] = Patrocinador
         
st.divider()

# --- #: Confirmar/Cancelar evento :# --- #

st.write("\n")

col1, col2 = st.columns(
    2, 
    gap="small",
    vertical_alignment="bottom"
)

with col1:                      # ~ Boton para confirmar ~ #
    
    with st.container(
        key="button_confirm",
        horizontal_alignment="center"
    ):    
        bt_confirmar = st.button("Confirmar evento")

if bt_confirmar:                                
    val, campos = validar_combate()
    if not val:
        for error in campos:
            st.warning(f"Falta por llenar: {error}")
    
    else:
        st.success("El combate ha sido programado, que gane el mejor!")
        st.session_state.combates_programados[st.session_state.combate["Patrocinador"]] = st.session_state.combate
        guardar_combates()
        resetear_web()
        sleep(2)
        st.rerun()

with col2:                          # ~ Boton para cancelar ~ #
    
    with st.container(
        key="button_cancel",
        horizontal_alignment="center"
    ):    
        bt_cancelar = st.button("Cancelar evento")
           
if bt_cancelar:
    st.info("El combate que estaba organizando a sido cancelado. Gracias por su atención!")
    resetear_web()
    sleep(2)
    st.rerun()

