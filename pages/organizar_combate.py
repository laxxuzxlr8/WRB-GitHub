import streamlit as st
import datetime as datetime
from time import sleep
import re
import pandas as pd
from core import cargar_inventario, cargar_combates, guardar_combates

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
    
def validar_robot(robot):            # ~ Robot Valido ~ #

    if robot == "a":
        a = ["Equipo_A", robot_a, arma_izq_a, arma_der_a]
        
        if len(st.session_state.combate[a[0]]) == 1 and st.session_state.combate["Modo"] == "Robot vs Robot":
            return False, "El equipo está lleno. El modo seleccionado es Robot vs Robot.", False
        
        elif len(st.session_state.combate[a[0]]) == 3 and st.session_state.combate["Modo"] == "Equipo vs Equipo":
            return False, "El equipo está lleno. La capacidad máxima es de 3 robots por equipo.", False
        
        else:
            if a[1] == None or a[2] == None or a[3] == None:
                return False, "Debe llenar todos los campos para que el combate sea justo.", False
            if a[2] == a[3]:
                return False, "No puede haber armas repetidas, escoja una combinación diferente.", False
            combinacion_a = set([a[2], a[3]])
            for comb in st.session_state.inventario["combinaciones_no"].values():
                if combinacion_a == set(comb["combinacion"]):
                    return False, f'Esta combinación de armas no es válida, razón: {comb["razon"]}', True
    
    if robot == "b":
        b = ["Equipo_B", robot_b, arma_izq_b, arma_der_b]
        
        if len(st.session_state.combate[b[0]]) == 1 and st.session_state.combate["Modo"] == "Robot vs Robot":
            return False, "El equipo está lleno. El modo seleccionado es Robot vs Robot.", False
        
        elif len(st.session_state.combate[b[0]]) == 3 and st.session_state.combate["Modo"] == "Equipo vs Equipo":
            return False, "El equipo está lleno. La capacidad máxima es de 3 robots por equipo.", False
        
        else:
            if b[1] == None or b[2] == None or b[3] == None:
                return False, "Debe llenar todos los campos para que el combate sea justo.", False
            if b[2] == b[3]:
                return False, "No puede haber armas repetidas, escoja una combinación diferente.", False
            combinacion_b = set([b[2], b[3]])
            for comb in st.session_state.inventario["combinaciones_no"].values():
                if combinacion_b == set(comb["combinacion"]):
                    return False, f'Esta combinación de armas no es válida, razón: {comb["razon"]}', True
    
    return True, '', False

def validar_patrocinador():                     # ~ Patrocinador Valido ~ #
    
    for patro in st.session_state.combates_programados:
        if Patrocinador == patro:
            return False, "Ya existe un Patrocinador con este nombre, escriba otro."
    
    if not re.match(r'^[A-Za-z\\\\s-]+$', Patrocinador):
        return False, "Patrocinador solo debe contener letras y guiones."
    
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
        "robots" : [],
        "armas" : [],
        "arena" : []
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

# ------------------------------- #: Panel Principal :# ------------------------------- #

st.header("Organizar combate:", 
             text_alignment="center",
             anchor=False
             )

# --- #: Sección Fecha y Lugar :# --- #

st.subheader(
    body="📆 Fecha y lugar 🏟️", 
    text_alignment="center", 
    anchor=False
    )

año = datetime.datetime.today().year
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    max_value = datetime.datetime.today().date() + datetime.timedelta(days=367)
else:
    max_value = datetime.datetime.today().date() + datetime.timedelta(days=366)

Fecha = st.date_input(    
    label="**Elija una :violet[Fecha] para el combate:**", 
    min_value=datetime.datetime.today().date() + datetime.timedelta(days=1),
    max_value=max_value,
    format="DD/MM/YYYY",
    help="*Fecha* en la cual se desarrollará el combate.",
    value= None
    )

# --- #: Algoritmo de validación de Fecha y eliminacion de recursos :# --- #

if Fecha == None:
    st.session_state.fecha_anterior = None
    st.session_state.combate["Fecha"] = None
    
    st.session_state.combate["Arena"] = None
    
    st.session_state.combate["Equipo_A"] = {}
    st.session_state.combate["Equipo_B"] = {}
    
    st.session_state.len_anterior = {
        "Equipo_A" : 0,
        "Equipo_B" : 0,
    }
    st.session_state.disponibles["arena"] = []
    st.session_state.disponibles["armas"] = []
    st.session_state.disponibles["robots"] = []
    
    st.session_state.usados = {
        "robots" : [],
        "armas" : []
    }

if Fecha != st.session_state.fecha_anterior:
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

    st.session_state.combate["Arena"] = None
    
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
        st.success("Día válido, no hay eventos programados!")   
        st.session_state.combate["Fecha"] = str(Fecha)
        st.session_state.disponibles["arena"] = [arena for arena in st.session_state.inventario["arena"]]
        st.session_state.disponibles["robots"] = [robot for robot in st.session_state.inventario["robots"].keys()]
        st.session_state.disponibles["armas"] = [arma for arma in st.session_state.inventario["armas_equipables"].keys()]

        
    elif len(arena_no) >= len(st.session_state.inventario["arena"]):
        st.error("Todas las arenas están ocupadas para ese día, escoja otro.")
        st.session_state.combate["Fecha"] = None
        st.session_state.disponibles["arena"] = []
        st.session_state.disponibles["armas"] = []
        st.session_state.disponibles["robots"] = []

    else:
        st.info("Se mostrarán solo las arenas, robots y armas disponibles para esa fecha.")
        st.session_state.disponibles["arena"] = [arena for arena in st.session_state.inventario["arena"] if arena not in arena_no]
        st.session_state.disponibles["robots"] = [robot for robot in st.session_state.inventario["robots"].keys() if robot not in robot_no]
        st.session_state.disponibles["armas"] = [arma for arma in st.session_state.inventario["armas_equipables"].keys() if arma not in armas_no]   
        st.session_state.combate["Fecha"] = str(Fecha)    
    
    st.session_state.fecha_anterior = Fecha   

elif st.session_state.combate["Fecha"] == None:                         # ~ Recomendacion Proxima fecha disponible ~ # 
    día_disponible = datetime.datetime.today().date() + datetime.timedelta(days=1)
    contador = 0
    check = False
    if len(st.session_state.combates_programados.keys()) != 0:
        while True:
            
            for combate in st.session_state.combates_programados.values():
                
                if combate["Fecha"] == str(día_disponible):
                    if contador < 2:
                        contador +=1       
                
                if contador == 2:
                    día_disponible = día_disponible + datetime.timedelta(days=1)
                    check = False
                    contador = 0
                    break
                
                check = True    
            
            if check:
                break
        
    st.info(f"Recomendación de Próxima fecha disponible: {str(día_disponible)}")
        
# --- #: Sección Arena :# --- #

Arena = st.selectbox(
    label="**Seleccione la :violet[Arena] del combate:**",
    options=st.session_state.disponibles["arena"],
    help="Arena donde se desarrollará el combate: en un *terreno limpio* o en un *espacio con obstáculos*.",
    index=None,
    key="selectbox_arena" 
    )

if Arena:
    st.session_state.combate["Arena"] = Arena
else:
    st.session_state.combate["Arena"] = None

if st.session_state.combate["Arena"] == "Ring principal":               # ~ Imagenes Arenas ~ #
    st.image("images/Gestionar Combate/Ring.png")

elif st.session_state.combate["Arena"] == "Area con obstáculos":
    st.image("images/Gestionar Combate/Obstaculos.jpg")

else:
    st.info("Las arenas se utilizan durante 24 horas para organizar un Combate.")

st.write("\n")

st.divider()

# --- #: Sección Modo de juego :# --- #

st.subheader(
        "⚔️ Modo de juego ⚔️", 
        text_alignment="center", 
        anchor=False
        )

st.write("\n")

col1,col2 = st.columns(
    [0.7, 1.3],
    gap = "small",
    vertical_alignment='center')

with col1:

    with st.container(
        key="Modo", 
        horizontal_alignment="center"
        ):
        
        st.session_state.combate["Modo"] = st.radio(
            label="**Escoja un :violet[Modo de juego]:**",
            options=["Robot vs Robot", "Equipo vs Equipo"],
            help = "Establece la *distribución de equipos* para el combate: *1vs1* o *3vs3*"
            )

    if st.session_state.combate["Modo"] != st.session_state.modo_anterior:         # ~ Control con cambio de modo ~ #     
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

with col2:                                  # ~ Imagenes Modo ~ #
    if st.session_state.combate["Modo"] == "Robot vs Robot":
        st.image("images/Gestionar Combate/1vs1.png")   
    elif st.session_state.combate["Modo"] == "Equipo vs Equipo":
        st.image("images/Gestionar Combate/3vs3.png") 

st.divider()

# --- #: Sección Equipos :# --- #

st.subheader(
    body="👾 Gestionar equipos 👾",
    text_alignment="center",
    anchor=False
    )
 
# recursos_disponibles()

col1, col2 = st.columns(
    2, 
    gap = "large", 
    vertical_alignment="center"
    )

with col1:                      # ~ Asignacion Equipo A ~ #
        
    if st.session_state.combate["Modo"] == "Robot vs Robot":  
        st.subheader(
            body=":red[Combatiente A]", 
            text_alignment="center",
            anchor=False
            )
    else:
        st.subheader(
            body=":red[Equipo A]", 
            text_alignment="center",
            anchor=False
            )        
    
    with st.form(
        key="form_robot_a",
        clear_on_submit=True,
        enter_to_submit=True
        ):
                
        robot_a = st.selectbox(
            "**Escoja un :violet[robot]:**",
            options=[robot for robot in st.session_state.disponibles["robots"] if robot not in st.session_state.usados['robots']],
            index=None,
            )
                
        arma_izq_a = st.selectbox(
            "**Escoja un :violet[arma] para el brazo izquierdo:**",
            options=[arma for arma in st.session_state.disponibles["armas"] if arma not in st.session_state.usados["armas"]],
            index=None,
            )
                
        arma_der_a = st.selectbox(
            "**Escoja un :violet[arma] para el brazo derecho:**",
            options=[arma for arma in st.session_state.disponibles["armas"] if arma not in st.session_state.usados["armas"]],
            index=None,
            )
        
        with st.container(
            horizontal_alignment="center"
        ):        
        
            bt_a = st.form_submit_button(
                label="**:green[Agregar] Robot**",
                help="Agrega un *robot* al **Equipo A**. El robot debe estar *equipado* completamente para ser *válido*."
                )
    
    st.dataframe(
        pd.Series([robot for robot in st.session_state.combate["Equipo_A"].keys()], name = "Equipo A" if st.session_state.combate["Modo"] == "Equipo vs Equipo" else "Combatiente A"),
        hide_index=True
        )
         
    if bt_a:
        if st.session_state.combate["Fecha"] != None:
            valido_A, mensaje_A, tiempo_A = validar_robot("a")      
            if not valido_A:
                st.warning(mensaje_A)
                if tiempo_A:
                    sleep(2.5)
                else:
                    sleep(1.5)
                st.rerun()
            else:
                st.session_state.combate["Equipo_A"][robot_a] = [arma_izq_a, arma_der_a]
                st.session_state.usados["robots"] += [robot_a]
                st.session_state.usados["armas"] += [arma_izq_a]
                st.session_state.usados["armas"] += [arma_der_a]
                st.rerun()
        else:
            st.warning("Escoja una Fecha Válida primero.")
            sleep(1.3)
            st.rerun()
            
    if len(st.session_state.combate["Equipo_A"]) > st.session_state.len_anterior["Equipo_A"]:
        st.success("Robot añadido!")
        st.session_state.len_anterior["Equipo_A"] += 1
        sleep(1.3)
        st.rerun()

with col2:                      # ~ Asignacion Equipo B ~ #
        
    if st.session_state.combate["Modo"] == "Robot vs Robot":    
        st.subheader(
            body=":blue[Combatiente B]", 
            text_alignment="center",
            anchor=False
            )
        
    else:
        st.subheader(
            body=":blue[Equipo B]", 
            text_alignment="center",
            anchor=False
            )
            
    with st.form(
        key="form_robot_b",
        clear_on_submit=True,
        enter_to_submit=True
        ):
                
        robot_b = st.selectbox(
            "**Escoja un :violet[robot]:**",
            options=[robot for robot in st.session_state.disponibles["robots"] if robot not in st.session_state.usados['robots']],
            index=None,
            )
                
        arma_izq_b = st.selectbox(
            "**Escoja un :violet[arma] para el brazo izquierdo:**",
            options=[arma for arma in st.session_state.disponibles["armas"] if arma not in st.session_state.usados["armas"]],
            index=None,
            )
                
        arma_der_b = st.selectbox(
            "**Escoja un :violet[arma] para el brazo derecho:**",
            options=[arma for arma in st.session_state.disponibles["armas"] if arma not in st.session_state.usados["armas"]],
            index=None,
            )
        
        with st.container(
            horizontal_alignment="center"
        ):
                
            bt_b = st.form_submit_button(
                label="**:green[Agregar] Robot**",
                help="Agrega un *robot* al **Equipo B**. El robot debe estar *equipado* completamente para ser *válido*."
                )
     
    st.dataframe(
        pd.Series([robot for robot in st.session_state.combate["Equipo_B"].keys()], name = "Equipo B" if st.session_state.combate["Modo"] == "Equipo vs Equipo" else "Combatiente B"),
        hide_index=True
        )
                
    if bt_b:
        if st.session_state.combate["Fecha"] != None:
            valido_B, mensaje_B, tiempo_B = validar_robot("b")      
            if not valido_B:
                st.warning(mensaje_B)
                if tiempo_B:
                    sleep(2.5)
                else:
                    sleep(1.5)
                st.rerun()
            else:
                st.session_state.combate["Equipo_B"][robot_b] = [arma_izq_b, arma_der_b]
                st.session_state.usados["robots"] += [robot_b]
                st.session_state.usados["armas"] += [arma_izq_b]
                st.session_state.usados["armas"] += [arma_der_b]
                st.rerun()
        else:
            st.warning("Escoja una Fecha Válida primero.")
            sleep(1.3)
            st.rerun()
    
    if len(st.session_state.combate["Equipo_B"]) > st.session_state.len_anterior["Equipo_B"]:
        st.success("Robot añadido!")
        st.session_state.len_anterior["Equipo_B"] += 1
        sleep(1.3)
        st.rerun()   
            
st.divider()

# --- #: Sección Control :# --- #

st.subheader(
    body="🎮 Tipo de control 🎮",
    text_alignment="center",
    anchor=False
)

st.write("\n")

col1,col2 = st.columns(
    [0.7, 1.3],
    gap = "small",
    vertical_alignment='center')

with col1:                      
    
    with st.container(
        key="final", 
        horizontal_alignment="center",
        ):
        
        st.session_state.combate["Control"] = st.radio(
            label="**Escoja un tipo de :violet[Control]:**",
            options=["Control Manual", "AI Boxing"],
            index=0,
            horizontal=False,
            help="Escoger entre controlar a los robots *manualmente* o con *IA Boxing*."
            )

with col2:
    
    if st.session_state.combate["Control"] == "Control Manual":             # ~ Imagenes Control ~ #
        st.image("images/Gestionar Combate/Manual.png")   
    elif st.session_state.combate["Control"] == "AI Boxing":
        st.image("images/Gestionar Combate/AI.png") 
    
st.divider()    
       
# --- #: Sección Patrocinador :# --- #
    
st.subheader(
    body="👤 Patrocinador 👤",
    text_alignment="center",
    anchor=False
    )

st.write("\n")

col1,col2,col3 = st.columns(
    [0.3, 1.4, 0.3],
    gap = "small",
    vertical_alignment="center"
    )

with col2:
    if st.session_state.combate["Fecha"] != None:
        Patrocinador = st.text_input(
            label="**Escriba el nombre de un :violet[Patrocinador] para el combate:**",
            value=st.session_state.combate["Patrocinador"],
            max_chars=20,
            help="*Encargado* o *Responsable* del **combate**.",
            placeholder="Escriba un nombre."
            )
    else:
        Patrocinador = st.text_input(
            label="**Escriba el nombre de un :violet[Patrocinador] para el combate:**",
            help="*Encargado* o *Responsable* del **combate**.",
            disabled=True,
            placeholder="Seleccione una fecha primero."
            )    
        
    if Patrocinador:                    # ~ Validacion Patrocinador ~ #
        valid, error = validar_patrocinador()
        if not valid:
            st.error(error)
            st.session_state.combate["Patrocinador"] = None
        
        else:
            st.session_state.combate["Patrocinador"] = Patrocinador
            st.success("Patrocinador Válido.")   
            
st.divider()

st.write("\n")

# --- #: Confirmar/Cancelar evento :# --- #

col1, col2, col3 = st.columns(
    [0.3, 1.4, 0.3], 
    gap="small",
    vertical_alignment="bottom"
)

with col2:                      
    
    with st.container(
        border=True,
        key= "Menu_Botones",
        vertical_alignment="center"
    ):
        
        st.subheader(
            body = "Finalizar evento:",
            text_alignment="center",
            anchor=False
            )
        
        col1, col2 = st.columns(
            2,
            gap="small",
            vertical_alignment="center",
        )
        
        with col1:                  # ~ Boton para confirmar ~ #
            with st.container(
                key="button_confirm",
                horizontal_alignment="center"
                ):    
                
                bt_confirmar = st.button(
                    label = "**:green[Confirmar] evento**",
                    help = "**Confirma** el *combate* que estaba planificando. No se *agregará* hasta que todos los *campos* sean **válidos**."
                    )

        with col2:                  # ~ Boton para cancelar ~ #
            with st.container(                          
                key="button_cancel",
                horizontal_alignment="center"
                ):    
                
                bt_cancelar = st.button(
                    label = "**:red[Cancelar] evento**",
                    help = "**Cancela** el *combate* que estaba *planificando*."
                    )

        st.write("\n")

st.write("\n")

if bt_confirmar:                                
    
    val, campos = validar_combate()
    
    if not val:
        for error in campos:
            st.warning(f"Falta por llenar: {error}")
        sleep(2)
        st.rerun()
    
    else:
        st.success("El combate ha sido programado, que gane el mejor!")
        st.session_state.combates_programados[st.session_state.combate["Patrocinador"]] = st.session_state.combate
        guardar_combates(st.session_state.get("combates_programados"))
        resetear_web()
        sleep(2)
        st.rerun()
          
if bt_cancelar:
    
    st.info("El combate que estaba organizando a sido cancelado. Gracias por su atención!")
    resetear_web()
    sleep(2)
    st.rerun()      
