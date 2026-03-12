import streamlit as st

st.write("\n")

with st.container(
    border = True
    ):

    st.header(
        body = "¡Combatientes Robots de la WRB!",
        text_alignment = "center",
        anchor = False
        )
    
    st.write("\n")

st.divider()

st.write("\n")

col1, col2 = st.columns(                                        # ~ Catalogo de robots ~ #
    spec = 2, 
    gap = 'large'
    )

with col1:
    
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
    
    st.image("images/robots/Bash.jpg")
    with st.container(border = True):
        st.subheader("*:yellow[Bash]*")
        st.write("**Estilo agresivo, superviviente nativo.**")
    
    st.write("\n")
    
    st.image("images/robots/Blue Bot.jpg")
    with st.container(border = True):    
        st.subheader("*:blue[Blue Bot]*")
        st.write("**Robot genérico de peleas menores.**")
    
    st.write("\n")
    
    st.image("images/robots/Fatboy.jpg")
    with st.container(border = True):
        st.subheader("*:yellow[Fatboy]*")
        st.write("**Gran tamaño y fuerza, poca agilidad.**")
    
    st.write("\n")
    
    st.image("images/robots/Gridlock.jpg")
    with st.container(border = True):
        st.subheader("*:gray[Gridlock]*")
        st.write("**Fuerza mecánica, habilidad demoletora.**")
    
    st.write("\n")
    
    st.image("images/robots/Metro.jpg")
    with st.container(border = True):
        st.subheader("*:rainbow[Metro]*")
        st.write("**Catarra revivida, robot de entrenamiento.**")
    
    st.write("\n")
    
    st.image("images/robots/Nitro.jpg")
    with st.container(border = True):
        st.subheader("*:blue[Nitro]*")
        st.write("**Velocidad explosiva, difícil de seguir.**")
    
    st.write("\n")
    
    st.image("images/robots/Shogun.jpg")
    with st.container(border = True):
        st.subheader("*:red[Shogun]*")
        st.write("**Inspiración samurái, robot de exposición.**")
    
    st.write("\n")
    
    st.image("images/robots/Tackle.jpg")
    with st.container(border = True):
        st.subheader("*:green[Tackle]*")
        st.write("**Ataques de impacto elétrico y llamativo.**")
    
    st.write("\n")
    
    st.image("images/robots/Twin Cities.jpg")
    with st.container(border = True):
        st.subheader("*:red[Twin Cities]*")
        st.write("**Dos cabezas, gran capacidad de ataque simultáneo.**")
    
    st.write("\n")
    
    st.image("images/robots/Visualizer.jpg")
    with st.container(border = True):
        st.subheader("*:rainbow[Visualizer]*")
        st.write("**Sistema de análisis, predice movimientos.**")
    
with col2:
    
    st.image("images/robots/Ambush.jpg")
    with st.container(border = True):
        st.subheader("*:gray[Ambush]*")
        st.write("**Robot de segunda mano, poca resistencia.**")
    
    st.write("\n")
    
    st.image("images/robots/Axelrod.jpg")
    with st.container(border = True):
        st.subheader("*:orange[Axelrod]*")
        st.write("**Robot de exhibición, estilo técnico.**")
    
    st.write("\n")

    st.image("images/robots/Blacktop.jpg")
    with st.container(border = True):
        st.subheader("*:red[Blacktop]*")
        st.write("**Estilo rudo, robot de peleas clandestinas.**")

    st.write("\n")

    st.image("images/robots/Bricks.jpg")
    with st.container(border = True):
        st.subheader("*:orange[Bricks]*")
        st.write("**Gran resistencia física, por módulos.**")

    st.write("\n")

    st.image("images/robots/Gambit.jpg")
    with st.container(border = True):
        st.subheader("*:green[Gambit]*")
        st.write("**Movimientos impredecibles y naturales.**")
    
    st.write("\n")
    
    st.image("images/robots/HollowJack.jpg")
    with st.container(border = True):
        st.subheader("*:orange[HollowJack]*")
        st.write("**Estilo intimidante, inspiración fantástica.**")

    st.write("\n")
    
    st.image("images/robots/Midas.jpg")
    with st.container(border = True):
        st.subheader("*:yellow[Midas]*")
        st.write("**Gran fuerza bruta, estilo callejero.**")

    st.write("\n")
    
    st.image("images/robots/Noisy Boy.jpg")
    with st.container(border = True):
        st.subheader("*:violet[Noisy Boy]*")
        st.write("**Potencia ofensiva y estilo llamativo.**")

    st.write("\n")
    
    st.image("images/robots/Six Shooter.jpg")
    with st.container(border = True):
        st.subheader("*:gray[Six Shooter]*")
        st.write("**Estilo del Medio Oriente, sheriff local.**")

    st.write("\n")
    
    st.image("images/robots/Tri-Tip.jpg")
    with st.container(border = True):
        st.subheader("*:orange[Tri-Tip]*")
        st.write("**Diseño triangular, tamaño colosal.**")

    st.write("\n")
    
    st.image("images/robots/Vanda.jpg")
    with st.container(border = True):
        st.subheader("*:violet[Vanda]*")
        st.write("**Robot de modelo femenino y radiante.**")
    
    st.write("\n")
    
    st.image("images/robots/Wheeled Bot.jpg")
    with st.container(border = True):
        st.subheader("*:blue[Wheeled Bot]*")
        st.write("**Movilidad rápida, conoce el terreno.**")
    
    st.write("\n")
    
    st.image("images/robots/Zeus.jpg")
    with st.container(border = True):
        st.subheader("*:green[Zeus]*")
        st.write("**Máxima fuerza y velocidad, invicto en el campeonato**")
    
st.divider()

st.subheader(
    body = "Coming soon...",
    text_alignment = "center",
    anchor = False
    )