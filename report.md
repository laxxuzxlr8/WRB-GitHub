# ¡World Robot Boxing!

## Reporte del Proyecto

**Este documento se creó con el objetivo de dar a conocer al lector la lógica o funcionalidad del código detrás del Proyecto.**

## Tabla de Contenidos
- [Aspectos Generales](#aspectos-generales)
- [Session State](#session-state)
- [Sección: Info](#sección-info)
    - [Acerca de WRB](#acerca-de-wrb)
- [Sección: Combates](#sección-combates)
    - [Organizar Combate](#organizar-combate)
    - [Combates Programados](#combates-programados)
- [Sección: Catálogo](#sección-catálogo)
    - [Robots](#robots)
    - [Armas](#armas)

## Aspectos Generales

Primero que todo, esta web tiene conceptos fundamentales que se repiten a lo largo del código de varias de sus páginas:

- main.py es el **nexo** de todo el proyecto, relaciona todas las páginas en un Sidebar desplegable para mayor comodidad de navegación.

- Toda la base de datos del proyecto se almacena en la carpeta /data, todos los combates programados así como el inventario permanente utilizado en cada una las funciones de la WEB.

- Todo contenido multimedia del proyecto se encuentra organizado por nombres en la carpeta /images.

- Cada módulo posee un apartado de help (ayuda) que brinda una pequeña explicación de su funcionalidad.

- El flujo principal del proyecto se basa en:
    - Iniciar variables que deben perdurar en el session_state (viene con Streamlit).
    - Trabajar sobre el session_state, para ver cambios en tiempo real.
    - Guardar eventos confirmados en la base de datos del proyecto.

## Session State

El proyecto tiene diversas variables inicializadas en el session_state de Streamlit de las que se apoya. Algunas de estas son:

- combate: contiene toda la información del combate que se está creando.

- inventario: contiene el inventario de recursos.

- disponibles: contiene los recursos disponibles para la fecha seleccionada.

- usados: contiene los recursos que se van a utilizar en el evento que se está creando (es una especie de almacenamiento en tiempo real).

- fecha_anterior: guarda la fecha que se puso anteriormente en caso de cambio de fecha

- modo_anterior: guarda el modo anterior en caso de cambio.

Además existen otras variables en el session_state encargadas de controlar inputs y resets de campos de entrada como fecha, control y patrocinador, relacionadas con el vaciado de los de estos cuando se resetea la WEB.

## Sección Info

### Acerca de WRB

La primera sección de la WEB es de información sobre el Proyecto: ¿qué es la WRB?, ¿qué es lo que brinda?, ¿cuáles son sus puntos clave?; además de un enlace directo a la Película de la que se basa la idea central abordada. Sin complejidad, puro texto y formato de Streamlit.

No obstante esta página cumple una función muy importante, controla el flujo de eventos finalizados y los elimina de la base de datos para evitar una sobrecarga a largo plazo.

```bash
    if st.session_state.control_fechas and len(st.session_state.combates_programados) != 0 :
    
    listado_eliminar = []               # Listado eventos a eliminar #

    for patro, data in st.session_state.combates_programados.items():
        nums = data["Fecha"].replace("-", " ").split()
        dia = datetime.date(int(nums[0]), int(nums[1]), int(nums[2]))
        if datetime.date.today() > dia:
            listado_eliminar.append(patro)
    
    for i in listado_eliminar:
        st.session_state.combates_programados.pop(i)
    
    guardar_combates(st.session_state.combates_programados)
    st.session_state.control_fechas = False 
```

Al ser la primera página en ejecutarse, tiene prioridad sobre el código, inicia una variable de control en el session_state en True, la cual da paso a que inicie un bucle que recorre todos los eventos programados, en el caso de que exista al menos uno y compara su fecha con la del día actual para ver si ya se cumplió. En caso afirmativo, añade este a una lista filtro de combates a eliminar y los borra de la base de datos. Una vez finalizado este proceso, la variable de control de fechas del session_state pasa a ser False y no se vuelve a ejecutar hasta que se vuelva a abrir la WEB.

## Sección Combates

### Organizar Combate

La siguiente página (Organiza Combate) está relacionada con todo el proceso de gestionar, organizar y configurar la forma en la que quieres que se efectúe el combate que quieras crear. Es la página más importante y compleja del proyecto, pues contiene la mayor parte de lógica y funcionalidades que brinda este proyecto.

Funciones principales utilizadas:

- resetear_web(): encargada de eliminar todos los cambios realizados en el session_state relacionados con la gestion de un combate, los resetea a su estado original.

- validar_combate(): revisa que todos los requisitos para coder confirmar un combate se cumplan, es decir, tengan un valor correcto asignado.

- validar_robot(equipo, robot_sel, arma_izq, arma_der): encargada de verificar que todo robot añadido cumpla con los requisitos necesarios para su participación en un combate: el equipo no debe estar lleno, debe tener dos armas equipadas, una por cada brazo, sin repeticiones y sin conflictos entre ellas.

- validar_patrocinador(patrocinador): chequea que el nombre del patrocinador tenga solo los caracteres posibles: solo letras, espacios y guiones

- recomendar_fecha(): encargada de dar a conocer cuál es la próxima fecha disponible para poder organizar un evento. Comienza verificando cada día analizando si existen arenas disponibles, en caso afirmativo, da la información del día disponible.

Esta página tiene un flujo fundamental que siempre está presente: todo se basa en la fecha selecionada, si no hay fecha correcta, toda configuración se bloquea, si seleciona una fecha con otros combates planificados ese mismo día, solo se mostraran los recursos disponibles para esa misma fecha, si cambia de día, todos los cambios efectuados se resetearán, pues puede que el recurso seleccionado en la nueva fecha no esté disponible.

Una vez seleccionada una fecha válida, la WEB se encarga de repartir todos los recursos que pueden ser empleados ese día, evitando el conflictos de disponibilidad, uno de los puntos clave del Proyecto, esto soluciona muchos problemas a futuro.

Luego de esto, se desbloquearán todas las opciones disponibles para configurar su propio combate, está dividido por bloques:

- Arena: elijes una pista para el encuentro y se muestra su foto con una breve descripción.

```bash
Arena = st.selectbox(
    label = "**Seleccione la :violet[Arena] del combate:**",
    options = st.session_state.disponibles["arena"],
    help = "Arena donde se desarrollará el combate.",
    index = None,
    key = "selectbox_arena" 
    )
```

- Modo de juego: regla fundamental del combate, define la cantidad de miembros de los equipos, 1 o 3, con una representación visual a su derecha. Si el modo de juego cambia, los equipos se restablecen completamente.

```bash
opciones_modo = ["Robot vs Robot", "Equipo vs Equipo"]
        
st.session_state.combate["Modo"] = st.radio(
    label = "**Escoja un :violet[Modo de juego]:**",
    options = opciones_modo,
    index = opciones_modo.index(st.session_state.combate["Modo"]) if st.session_state.combate["Modo"] in opciones_modo else 0,
    help = "Establece la distribución de equipos para el combate: [1 vs 1] o [3 vs 3]"
    )
```

- Gestionar equipos: módulo relacionado con la configuración de cada equipo que participará en el combate. Cada bloque relacionado a un equipo, posee un formulario que depende de la función validar_robot() enunciada anteriormente. 

```bash
robot_a = st.selectbox(
    label = "**Escoja un :violet[robot]:**",
    options = [robot for robot in st.session_state.disponibles["robots"] if robot not in st.session_state.usados['robots']],
    index = None,
    help = panel_robot
    )

arma_izq_a = st.selectbox(
    label = "**Escoja un :violet[arma] para el brazo izquierdo:**",
    options = [arma for arma in st.session_state.disponibles["armas"] if arma not in st.session_state.usados["armas"]],
    index = None,
    help = panel_armas
    )
                
arma_der_a = st.selectbox(
    label = "**Escoja un :violet[arma] para el brazo derecho:**",
    options = [arma for arma in st.session_state.disponibles["armas"] if arma not in st.session_state.usados["armas"]],
    index = None,
    help = panel_incomp
    )

```
Se apoya en el modo de juego establecido para que los equipos sean parejos. Cada robot consume células de energía, una cantidad específica y definida para cada robot. Una vez agregado un robot al equipo podrás verlo abajo, representado en una "tabla" de pandas estructurada por series; estas son: combatiente(robot), C/E(células que consume) y borrar(al seleccionar la casilla asociada a un robot lo elimina del equipo, dando mayor libertad de configuración).

```bash
with col3:
    st.dataframe(
        pd.Series(
            data = [robot for robot in st.session_state.combate["Equipo_A"].keys()], 
            name = "Equipo A" if st.session_state.combate["Modo"] == "Equipo vs Equipo" else "Combatiente A"),
        hide_index = True
        )
    
with col4:
    st.dataframe(
        pd.Series(
            data = [f"⚡️{st.session_state.inventario["robots"][robot]}" for robot in st.session_state.combate["Equipo_A"].keys()], 
            name = "C/E"),
        hide_index = True
        )
    
with col5:
    st.session_state.robot_seleccionado["A"] = st.dataframe(
        pd.Series(
            data =[1 + robot for robot in range(len(st.session_state.combate["Equipo_A"].keys()))], 
            name = "Borrar A"),
        hide_index = True,
        on_select = "rerun",
        selection_mode = "single-cell",
        )
```

Al final de esta sección podrás ver un panel que muestra la cantidad de células disponibles y el total de células que requiere la configuración de equipos que seleccionaste; en caso de ser superior, a la hora de confirmar el combate te dará error y tendrás que crear equipos nuevos que se adapten a la cantidad de células disponibles para ese día.

```bash
with st.container(
    border = True
    ):
        
    if not st.session_state.combate["Fecha"]:
            
        st.markdown(
            body = ":yellow[Células de Energía]", 
            text_alignment = "center",
            help = "Menú de distribución de Células de Energía. Escoja una fecha para más información sobre el Sistema de Energía."                
            )
    else:
            
        st.markdown(
            body = f":violet[Células] disponibles: ⚡️:yellow[{st.session_state.disponibles["celulas"]}]  /  :violet[Células] requeridas: ⚡️:yellow[{energia}]", 
            text_alignment = "center",
            help = "Menú de distribución de Células de Energía. La cantidad requerida no puede pasar la cantidad disponible; en caso de que sí, redistribuya los Equipos borrando algunos robots añadidos mediante las barras laterales de 'Borrar', pulsando en la casilla con el número del robot."                
            )
```

- Tipo de control: seleccionas la forma en la que se controlan los robots en ese combate mediante un radio, muestra también una representación visual del estilo de control.

```bash
st.session_state.combate["Control"] = st.radio(
    label = "**Escoja un tipo de :violet[Control]:**",
    options = opciones_control,
    key = "input_control",
    horizontal = False,
    help = "Escoger entre controlar a los robots Manualmente o con IA Boxing."
    )
```

- Patrocinador: rellenas una caja de texto con el nombre del patrocinador en cuestión que organizó el evento(una especie de mecanismo para diferenciar combates).

```bash
Patrocinador = st.text_input(
            label = "**Escriba el nombre de un :violet[Patrocinador] para el combate:**",
            key = "input_patrocinador",
            max_chars = 20,
            help = "Encargado o Responsable de la planificación del combate.",
            placeholder = "Escriba un nombre."
            )
```

Los nombres no pueden ser repetidos y además sigue las reglas de validación de validar_patrocinador() mencionada anteriormente.

```bash
if Patrocinador:                    # ~ Validacion Patrocinador ~ #
        
    valid, error = validar_patrocinador(Patrocinador)
    if not valid:
        st.error(error)
        st.session_state.combate["Patrocinador"] = ""
        
    else:
        st.session_state.combate["Patrocinador"] = Patrocinador
        st.success("Patrocinador Válido.")
```

- Finalizar evento: módulo final de la página, posee dos botones: confirmar, encargado de ejecutar la función validar_combate(), verificar que todos los requisitos se cumplan, que ningún recurso choque y confirmar el combate, los guarda en la base de datos y ejecuta resetear_web() para crear otros combates; cancelar elimina toda configuración actual del evento que se esté creando y llama a resetear_web() para comenzar desde cero.

### Combates Programados

Combates programados es una página dedicada solamente a mostrar/listar los combates organizados hasta la fecha que no han sido disputados, así como cancelar en cualquier momento un evento establecido anteriormente.

Mediante un sistema de tablas/series con pandas distribuye la información de cada combate de manera sencilla, elegante. Las celdas con los nombres de los patrocinadores son interactivas y al pulsarlas muestran la información relacionada con el mismo.

```bash
st.session_state.seleccion = st.dataframe(                  # ~ Listado de Patrocinadores ~ #
    pd.Series(
        data = [combate for combate in st.session_state.combates_programados.keys()], 
        name = "Seleccione un Combate:"),
        on_select = "rerun",
        selection_mode = "single-cell",
        hide_index = True,
        width = 'content',
        use_container_width = True,
        height = "auto"
        )["selection"]["cells"]
```

Desde fecha, arena, modo, hasta cada uno de los recursos que consumen aparecen una vez seleccionado uno de los patrocinadores. Una forma rápida y compacta de dar detalles. En la sección de abajo se encuentra un Selectbox con una función característica: cancelar combates. Solo selecciona el nombre, pulsa eliminar y será borrado de la base de datos de la WEB.

```bash
if Eliminar:
            
    if combate_eliminado:
        st.session_state.combates_programados.pop(combate_eliminado)
        guardar_combates(st.session_state.get("combates_programados"))
        st.session_state.seleccion = []
        st.session_state.lista_patrocinadores = None
        st.success("El Combate ha sido eliminado exitosamente.")
        sleep(1.3)
        st.rerun()
            
    else:
        st.warning("Seleccione un Combate primero.")
        sleep(1.3)
        st.rerun()
```

## Sección Catálogo

### Robots

La página de robots esta orientada exclusivamente a mostrar de manera visual todos los robots disponibles en la WRB, solo fotos y código de Streamlit distribuido de manera vertical, con una breve descripción de estos.

```bash
st.image("images/robots/Albino.jpg")
    with st.container(border = True):
        st.subheader("*Albino*")
        st.write("**Diseño único, modelo de IA autónomo.**")
   
    st.write("\n")
   
    st.image("images/robots/Atom.jpg")
    with st.container(border = True):
        st.subheader("*:blue[Atom]*")
        st.write("**Gran espíritu y capacidad de aprendizaje.**")
    
    st.write("\n")
...
```

### Armas

De misma manera la página de armas está dedicada a mostrar de manera visual el armamento del que pueden disponer los robots en el campo de batalla, con la diferencia de que están organizadas por categoría mediante tabs interactivas (ofernsivo, defensivo, soporte, especial).

```bash
tab1, tab2, tab3, tab4 = st.tabs(                                   # ~ Menu de seleccion de tipo de armamento ~ #
    tabs = [":red[**Ofensivo**]", ":blue[**Defensivo**]", ":green[**Soporte**]", ":yellow[**Especial**]"]
    )

with tab1:                                                          # ~ Ofensivo ~ #
    
    st.subheader(
        body = ":red[Ofensivo]", 
        text_alignment = "center", 
        anchor = None
        )
    
    st.write("\n")
...
```
---
**Espero que les guste el Proyecto. Made with 💜 by [laxxuzxlr8](https://github.com/laxxuzxlr8)**