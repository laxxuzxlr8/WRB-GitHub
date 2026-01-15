import streamlit as st
import sys
sys.path.append(r"https://github.com/laxxuzxlr8/WRB-GitHub/blob/main")
from core import mostrar_texto

# --- #: Sección acerca de :# --- #

st.subheader("🥊¿Qué es la WRB?")

texto_info_1 = "La World Robot Boxing (WRB) es la máxima arena de combate donde la ingeniería se convierte en espectáculo. En este circuito global, robots de última generación se enfrentan en duelos electrizantes que combinan fuerza bruta, precisión táctica y tecnología de vanguardia. Cada combate es más que una pelea: es una batalla por la supremacía entre titanes de acero, donde los puños hidráulicos chocan con escudos de energía y las estrategias se ejecutan al milisegundo."
mostrar_texto(texto_info_1)

st.write("\n")

st.image(
    image="https://github.com/laxxuzxlr8/WRB-GitHub/blob/main/images/pelea_robots.png"
    )

st.write("\n")

texto_info_2 = "La WRB no es solo un deporte, es una cultura. Las gradas rugen con fanáticos que siguen a sus máquinas favoritas como si fueran leyendas vivas. Los equipos se preparan con recursos limitados, eligiendo cuidadosamente armas, sensores y sistemas de defensa, sabiendo que una mala combinación puede significar la derrota. Aquí, cada robot tiene una historia, cada combate tiene consecuencias, y cada victoria se graba en el metal."
mostrar_texto(texto_info_2)

st.divider()

# --- #: Secció puntos clave :# --- #

st.subheader("✅ Puntos clave de la WRB")

puntos_a_favor = """
- Peleas épicas: choques espectaculares entre titanes de acero que combinan fuerza y estrategia por alcanzar la victoria.

- Variedad de robots y armas: diseños únicos y equipamiento diverso que hacen cada combate impredecible.

- Escenarios complejos: arenas dinámicas con obstáculos y efectos que cambian el rumbo de la pelea.

- Modalidades desafiantes: duelos individuales, batallas por equipos y formatos especiales que elevan la emoción.

"""

with st.expander(label="Lo mejor de lo mejor en tecnología robótica:"):
    mostrar_texto(puntos_a_favor)

st.divider()

# --- #: Sección info adicional :# --- #

st.write("\n")
col1,col2,col3 = st.columns([1.1,0.8,1.1], gap="small", vertical_alignment="top")

with col1: 
    texto_final ="Bienvenido al corazón del acero. Aquí no hay segundas oportunidades. Solo circuitos quemados, gloria mecánica y el rugido de la multitud que ansía ver quién se queda con el mayor de los trofeos: la copa CiberBoxing."         
    mostrar_texto(texto_final)

with col2:
    st.image("https://github.com/laxxuzxlr8/WRB-GitHub/blob/main/images/ciberboxing.png")

with col3:
    texto_copa = "Si quiere conocer más acerca de este mundo y del robot boxeador más famoso de la WRB, puedes ver la película que inspira esta WEB: Gigantes de acero:"    
    mostrar_texto(texto_copa)
    
    st.link_button("Pulsa aquí", url="https://www.youtube.com/watch?v=DebFX7MC0vE", use_container_width=True)