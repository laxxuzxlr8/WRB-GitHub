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
    
tab1, tab2, tab3, tab4 = st.tabs([":red[**Ofensivo**]", ":blue[**Defensivo**]", ":green[**Soporte**]", ":yellow[**Especial**]"])

with tab1:
    
    st.subheader(":red[Ofensivo]", text_alignment = "center", anchor = None)
    
    st.write("\n")
    
    col1,col2,col3 = st.columns(3, gap="medium", vertical_alignment="top")
    
    with col1:
        
        st.image("images/Armas/Ofensivas/Aplastador neumático.jpg", caption="**Aplastador neumático**")
        st.image("images/Armas/Ofensivas/Cañón láser.jpg", caption="**Cañón láser**")
        st.image("images/Armas/Ofensivas/Cuchillas retráctiles de tungsteno.jpg", caption="**Cuchillas retráctiles de tungsteno**")
        st.image("images/Armas/Ofensivas/Lanza-arpón motorizado.jpg", caption="**Lanza-arpón motorizado**")
        st.image("images/Armas/Ofensivas/Lanzallamas.jpg", caption="**Lanzallamas**")
        st.image("images/Armas/Ofensivas/Maza electromagnética.jpg", caption="**Maza electromagnética**")
        st.image("images/Armas/Ofensivas/Puño reforzado.jpg", caption="**Puño reforzado**")
    
    with col2:
        
        st.image("images/Armas/Ofensivas/Cañón de microondas.jpg", caption="**Cañón de microondas**")
        st.image("images/Armas/Ofensivas/Cañón sónico.jpg", caption="**Cañón sónico**")
        st.image("images/Armas/Ofensivas/Electroshock.jpg", caption="**Electroshock**")
        st.image("images/Armas/Ofensivas/Lanza-chispas de arco eléctrico.jpg", caption="**Lanza-chispas de arco eléctrico**")
        st.image("images/Armas/Ofensivas/Martillo hidráulico.jpg", caption="**Martillo hidráulico**")
        st.image("images/Armas/Ofensivas/Misiles de corto alcance.jpg", caption="**Misiles de corto alcance**")
        st.image("images/Armas/Ofensivas/Sierra de cadena doble.jpg", caption="**Sierra de cadena doble**")
    
    with col3:
        
        st.image("images/Armas/Ofensivas/Cañón de plasma de baja potencia.jpg", caption="**Cañón de plasma de baja potencia**")
        st.image("images/Armas/Ofensivas/Cuchilla guillotina vertical.jpg", caption="**Cuchilla guillotina vertical**")
        st.image("images/Armas/Ofensivas/Garra prensil aplastante.jpg", caption="**Garra prensil aplastante**")
        st.image("images/Armas/Ofensivas/Lanzador de proyectiles metálicos.jpg", caption="**Lanzador de proyectiles metálicos**")
        st.image("images/Armas/Ofensivas/Martillo rotatorio de impacto.jpg", caption="**Martillo rotatorio de impacto**")
        st.image("images/Armas/Ofensivas/Motosierra.jpg", caption="**Motosierra**")
        st.image("images/Armas/Ofensivas/Taladro percutor industrial.jpg", caption="**Taladro percutor industrial**")

with tab2:
    
    st.subheader(":blue[Defensivo]", text_alignment = "center", anchor = None)
    
    st.write("\n")
    
    col1,col2,col3 = st.columns(3, gap="medium", vertical_alignment="top")
    
    with col1:
        
        st.image("images/Armas/Defensivas/Absorción de impactos.jpg", caption="**Absorción de impactos**")
        st.image("images/Armas/Defensivas/Blindaje reforzado.jpg", caption="**Blindaje reforzado**")
        st.image("images/Armas/Defensivas/Escudo de energía.jpg", caption="**Escudo de energía**")
        st.image("images/Armas/Defensivas/Placas de titanio.jpg", caption="**Placas de titanio**")
    
    with col2:
    
        st.image("images/Armas/Defensivas/Barreras de energía pulsante.jpg", caption="**Barreras de energía pulsante**")
        st.image("images/Armas/Defensivas/Campo eléctrico disipador.jpg", caption="**Campo eléctrico disipador**")
        st.image("images/Armas/Defensivas/Escudo óptico reforzado.jpg", caption="**Escudo óptico reforzado**")
        st.image("images/Armas/Defensivas/Revestimiento anti-impactos avanzado.jpg", caption="**Revestimiento anti-impactos avanzado**")
        st.image("images/Armas/Defensivas/Sistema de evasión automática.jpg", caption="**Sistema de evasión automática**")
    
    with col3:
    
        st.image("images/Armas/Defensivas/Blindaje óseo sintético.jpg", caption="**Blindaje óseo sintético**")
        st.image("images/Armas/Defensivas/Campo magnético protector.jpg", caption="**Campo magnético protector**")
        st.image("images/Armas/Defensivas/Placas de carburo endurecido.jpg", caption="**Placas de carburo endurecido**")
        st.image("images/Armas/Defensivas/Sistema de absorción cinética.jpg", caption="**Sistema de absorción cinética**")

with tab3:
    
    st.subheader(":green[Soporte]", text_alignment = "center", anchor = None)
    
    st.write("\n")
    
    col1,col2 = st.columns(2, gap="medium", vertical_alignment="top")
    
    with col1:
        
        st.image("images/Armas/Soporte/Detector de energía enemiga.jpg", caption="**Detector de energía enemiga**")
        st.image("images/Armas/Soporte/Radar de proximidad.jpg", caption="**Radar de proximidad**")
        st.image("images/Armas/Soporte/Sistema de cámaras HD.jpg", caption="**Sistema de cámaras HD**")
    
    with col2:
    
        st.image("images/Armas/Soporte/Drones de reconocimiento.jpg", caption="**Drones de reconocimiento**")
        st.image("images/Armas/Soporte/Sensores ópticos avanzados.jpg", caption="**Sensores ópticos avanzados**")
        
with tab4:
    
    st.subheader(":yellow[Especial]", text_alignment = "center", anchor = None)
    
    st.write("\n")
    
    col1,col2 = st.columns(2, gap="medium", vertical_alignment="top")
    
    with col1:
        
        st.image("images/Armas/Especial/Generador de niebla.jpg", caption="**Generador de niebla**")
        st.image("images/Armas/Especial/Iluminación UV.jpg", caption="**Iluminación UV**")
    
    with col2:
    
        st.image("images/Armas/Especial/Iluminación infrarroja.jpg", caption="**Iluminación infrarroja**")
        st.image("images/Armas/Especial/Sistema de hologramas distractores.jpg", caption="**Sistema de hologramas distractores**")
    
st.divider()

st.subheader(
    body ="Coming soon...",
    text_alignment="center",
    anchor = False
    )