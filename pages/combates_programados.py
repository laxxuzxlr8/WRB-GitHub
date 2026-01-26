import streamlit as st
import pandas as pd
from time import sleep
from core import cargar_combates, guardar_combates

if "combates_programados" not in st.session_state:                  # ~ Combates programados ~ #
    combat = cargar_combates()
    st.session_state.combates_programados = combat    

if "seleccion" not in st.session_state:                             # ~ Combate Seleccionado ~ #
    st.session_state.seleccion = None

if "lista_patrocinadores" not in st.session_state:                  # ~ Listado de Patrocinadores ~ #
    st.session_state.lista_patrocinadores = None

# --- #: Seccion Listado de Combates :# --- #

st.header("Listado de Combates", text_alignment="center", anchor= False)

st.write("\n")

if len(st.session_state.combates_programados) > 0:

    col1,col2 = st.columns(
        [0.5,1.5]
    )
    
    with col1:
        
        st.session_state.lista_patrocinadores = pd.Series([combate for combate in st.session_state.combates_programados.keys()])
        
        st.session_state.seleccion = st.dataframe(                                          # ~ Listado de Patrocinadores ~ #
            pd.Series([combate for combate in st.session_state.combates_programados.keys()], name="Seleccione un Combate:"),
            on_select="rerun",
            selection_mode="single-cell",
            hide_index=True,
            width='content',
            use_container_width=True,
            height="auto"
            )["selection"]["cells"]

    with col2:

        if st.session_state.seleccion != []: 
            
            evento = st.session_state.combates_programados[st.session_state.lista_patrocinadores.iloc[st.session_state.seleccion[0][0]]]
            
            st.dataframe(                                   # ~ Listado con fecha, arena, modo, control ~ #
                [evento],
                column_order=["Fecha", "Arena", "Modo", "Control"],
                )
            
            col1,col2 = st.columns(
                [0.5, 1.5]
            )
            
            with col1:
                                                                # ~ Listado de Equipos(Robots) ~ #
                st.dataframe(                                   
                    pd.Series(evento["Equipo_A"].keys(), name="Equipo A" if evento["Modo"] == "Equipo vs Equipo" else "Combatiente A"),
                    hide_index=True
                    )
                
                st.dataframe(
                    pd.Series(evento["Equipo_B"].keys(), name="Equipo B" if evento["Modo"] == "Equipo vs Equipo" else "Combatiente B"),
                    hide_index=True
                    )
                
            with col2:
                                                                # ~ Listado de Equipos(Armas) ~ #
                st.dataframe(
                    pd.Series(evento["Equipo_A"].values(), name="Armas Equipadas Equipo A" if evento["Modo"] == "Equipo vs Equipo" else "Armas Equipadas Combatiente A"),
                    hide_index=True
                    )
                
                st.dataframe(
                    pd.Series(evento["Equipo_B"].values(), name="Armas Equipadas Equipo B" if evento["Modo"] == "Equipo vs Equipo" else "Armas Equipadas Combatiente B"),
                    hide_index=True
                   )

    st.divider()

# --- #: Seccion Eliminar Combate :# --- #

    st.subheader(
        body = "Sección Eliminar Combate",
        text_alignment = "center",
        anchor = False
        )
    
    st.write("\n")
    
    col1,col2,col3 = st.columns(
        [0.5, 1, 0.5],
        gap = "small",
        vertical_alignment = "center"
        )
    
    with col2:
        
        with st.form(
            key="form_eliminar",
            clear_on_submit=True
            ):
            
            combate_eliminado = st.selectbox(                                   # ~ Panel Seleccionar combate a eliminar ~ #
            label = "**Seleccione el :violet[combate] a :red[eliminar]:**",
            options = [combate for combate in st.session_state.combates_programados.keys()],
            help = "**Elimina un *combate* permanentemente del *sistema*, seleccionando el nombre del *Patrocinador***",
            index = None,
            placeholder = "¡Acción Irreversible!"
            )
            
            with st.container(
                horizontal_alignment="center"
                ):
                
                Eliminar = st.form_submit_button("**:red[Eliminar]**")          # ~ Boton eliminar ~ #
    
        if Eliminar:
            
            if combate_eliminado:
                st.session_state.combates_programados.pop(combate_eliminado)
                guardar_combates(st.session_state.get("combates_programados"))
                st.success("El **Combate** ha sido *eliminado* exitosamente.")
                sleep(1.3)
                st.rerun()
            
            else:
                st.warning("Seleccione un **Combate** primero.")
                sleep(1.3)
                st.rerun()

else:
    
    col1,col2,col3 = st.columns(
        [0.3,1.4,0.3]
    )
    
    with col2:
        st.info("No hay *Combates Programados*, diríjase a **Organizar** un *Combate*. ")
        
        st.write("\n")
        with st.container(
            horizontal_alignment="center"
        ):
            
            st.page_link(
                label="**:green[Organice uno aquí]**",
                page="pages/organizar_combate.py",
                help="Link para **Organizar** un *combate*.")