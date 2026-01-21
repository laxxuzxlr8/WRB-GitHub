import streamlit as st

with st.container(
    border = True
    ):

    st.header(
        body = "¡Salón de la Fama de la WRB!",
        text_alignment = "center",
        anchor = False
        )
    
    st.write("\n")

st.write("\n")

st.subheader(
    body = "*Ranking Top 10 Mejores Robots Última Temporada*",
    text_alignment = "center",
    anchor = False
)

st.write("\n")
st.write("\n")

col1, col2 = st.columns(
    2, 
    gap = 'large'
    )

with col1:
    st.image("images/robots/Atom.jpg")
    st.subheader("*:blue[Atom]*")
    st.write("**Resistencia y capacidad de aprendizaje.**")
    
    st.write("\n")
    
    st.image("images/robots/Twin.jpg")
    st.subheader("*:red[Twin Cities]*")
    st.write("**Dos cabezas, gran capacidad de ataque simultáneo.**")
    
    st.write("\n")
    
    st.image("images/robots/Metro.jpg")
    st.subheader("*:rainbow[Metro]*")
    st.write("**Resistencia física, robot de entrenamiento.**")
    
    st.write("\n")
    
    st.image("images/robots/Midas.jpg")
    st.subheader("*:yellow[Midas]*")
    st.write("**Gran fuerza bruta, estilo callejero.**")
    
    st.write("\n")
    
    st.image("images/robots/Shooter.png")
    st.subheader("*:gray[Six Shooter]*")
    st.write("**Rapidez y ataques múltiples.**")
    
with col2:
   
    st.image("images/robots/Zeus.jpg")
    st.subheader("*:green[Zeus]*")
    st.write("**Máxima fuerza y velocidad, invicto en el campeonato.**")
    
    st.write("\n")
    
    st.image("images/robots/Noisy.jpg")
    st.subheader("*:violet[Noisy Boy]*")
    st.write("**Potencia ofensiva y estilo llamativo.**")
    
    st.write("\n")
    
    st.image("images/robots/Ambush.jpg")
    st.subheader("*Ambush*")
    st.write("**Robot de segunda mano, poca resistencia.**")
    
    st.write("\n")
    
    st.image("images/robots/Axelrod.jpg")
    st.subheader("*:orange[Axelrod]*")
    st.write("**Robot de exhibición, estilo técnico.**")
    
    st.write("\n")
    
    st.image("images/robots/Blacktop.jpg")
    st.subheader("*:red[Blacktop]*")
    st.write("**Estilo rudo, robot de peleas clandestinas.**")
    
st.divider()

st.subheader(
    body ="Coming soon...",
    text_alignment="center",
    anchor = False
    )