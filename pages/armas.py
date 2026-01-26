import streamlit as st

with st.container(
    border = True
    ):
    
    st.header(
    body = "¡Armas y Accesorios de la WRB!",
    text_alignment = "center",
    anchor = False
    )

    st.write("\n")
    
st.write("\n")

st.subheader(
    body = "Armas *:red[Ofensivas]*:",
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
    st.image("images/armas/Puño.png")
    st.subheader("*Puños :red[Reforzados]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Martillo.png")
    st.subheader("*Martillo :red[Hidráulico]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Giratorio.png")
    st.subheader("Arma de :red[Impacto Giratorio]")
        
with col2:
    
    st.image("images/armas/Sierra.jpg")
    st.subheader("*Sierra :red[Circular]*")
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Laser.jpg")
    st.subheader("*Cañón :red[Láser]*")
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Lanzallamas.jpg")
    st.subheader("*Lanza:red[llamas]*")
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Misiles.jpg")
    st.subheader("*Misiles de :red[corto alcance]*")
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Electro.jpg")
    st.subheader("*Electro:red[shock]*")
    
st.divider()

st.subheader(
    body = "Armas :blue[Defensivas]:",
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
    
    st.image("images/armas/Magnetico.jpg")
    st.subheader("*Campo Magnetico :blue[Protector]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Titanio.jpg")
    st.subheader("*Placas de :blue[Titanio]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Evasion.png")
    st.subheader("*Sistema de :blue[Evasión Automática]*")
    
with col2:
    
    st.image("images/armas/Blindaje.jpg")
    st.subheader("*Blindaje :blue[Reforzado]*")
    
    st.write("\n")
    st.write("\n")

    st.image("images/armas/Escudo.jpg")
    st.subheader("*Escudo de :blue[Energía]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Absorcion.jpg")
    st.subheader("*Absorción de :blue[Impactos]*")
    
st.divider()

st.subheader(
    body = "Accesorios de :green[Soporte]:",
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
    
    st.image("images/armas/Camaras.jpg")
    st.subheader("*Sistema de :green[Cámaras HD]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Optico.jpg")
    st.subheader("*Sensores :green[Ópticos Avanzados]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Energia.jpg")
    st.subheader("*Detector de :green[Energía Enemiga]*")
    
with col2:
    
    st.image("images/armas/Radar.jpg")
    st.subheader("*Radar de :green[Proximidad]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Drones.jpg")
    st.subheader("*Drones de :green[Reconocimiento]*")
    
st.divider()

st.subheader(
    body = "Accesorios :violet[Especiales]:",
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
    
    st.image("images/armas/UV.jpg")
    st.subheader("*Iluminación :violet[UV]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Niebla.jpg")
    st.subheader("*Generador de :violet[Niebla]*")
    
with col2:
    
    st.image("images/armas/Infrarrojo.jpg")
    st.subheader("*Iluminación :violet[Infrarroja]*")
    
    st.write("\n")
    st.write("\n")
    
    st.image("images/armas/Holografico.jpg")
    st.subheader("*Sistema de :violet[Hologramas Distractores]*")
    
st.divider()

st.subheader(
    body ="Coming soon...",
    text_alignment="center",
    anchor = False
    )