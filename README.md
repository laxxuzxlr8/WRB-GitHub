
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-purple.svg)
![License](https://img.shields.io/badge/License-CC-green.svg)

# 🤖 ¡World Robot Boxing! 🥊

## Tema Seleccionado
**Planificador de combates entre Robots de la WRB.**

## Tabla de Contenidos
- [Descripción](#-descripción-del-proyecto)
- [Características](#-características-principales)
- [Funciones](#-funciones-auxiliares)
- [Restricciones](#-restricciones-de-la-wrb)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Estructura](#-estructura-del-proyecto)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Licencia y Agradecimientos Especiales](#-licencia)

## 📖 Descripción del Proyecto
¡El Deporte más famoso del Futuro ya está aquí! El combate entre Robots siempre ha sido uno de los deseos más ambiciosos del ser humano: Metal vs Metal, un hito inalcanzable decían algunos excéntricos de los últimos tiempos. Pero gracias a **@laxxuzxlr8** y a su Proyecto estrella: La **World Robot Boxing**(**WRB**), ahora es posible organizar estos asaltos legendarios entre **Gigantes de Acero**. Con una amplia gama de Robots, Armas, Arenas y Restricciones, esta aplicación Web te permitirá organizar Combates inolvidables a tú manera, almacenándolos en nuestro **Sistema de Almacenamiento Json** para que no te pierdas ninguna presentación de tu Combatiente favorito.

## ✅ Características Principales

Esta aplicación Web cuenta con varios Módulos que te permitirán:

*   **🏟️ Ver Información de la WRB**: Conoce acerca de la WRB, qué es y todo lo que puede llegar a ofrecer.
*   **⚔️ Organizar Combates**: ¡El suelo tiembla ante la dominación del Metal! Organiza combates personalizados entre Robots de tu preferencia, con armas de todo tipo de calibre y restricciones específicas establecidas por este Sistema. Selecciona, entre las opciones disponibles, de manera rápida y sin colisiones entre Combates y Recursos, una configuración que mejor se ajuste a tus gustos: Fecha, Arena, Modo, Equipos, Control, así como el Patrocinador encargado de gestionar el encuentro planificado. 
*   **📋 Listar Combates Programados**: Revisa el listado de todos los combates organizados hasta el momento, así como todas sus especificaciones y recursos que requiere.
*   **🗑️ Eliminar un Combate**: La aplicación Web tiene un sistema de borrado fácil y rápido para que descartes todo tipo de encuentros que ya no sean de tu interés.
*   **🤖 Ver Robots del Ranking Mundial**: Descubre cuáles son los Robots más exitosos de este deporte mediante una serie de imágenes de ellos.
*   🗡 **Ver Armas y Accesorios de la WRB**: Navega a través del catálogo de armas y accesorios de la WRB para que conozcas con qué combinar a tus robots favoritos.

## 👾 Funciones Auxiliares

Este proyecto cuenta también con varias funciones auxiliares que apoyan el código de la aplicación Web:

*   **📅 Recomendación de Hueco disponible**: Ten referencia del próximo día disponible para la organización de un combate en la WRB.
*   **📦 Repartición de Recursos**: El sistema reconoce los recursos empleados en el día seleccionado y muestra solo los recursos disponibles para poder organizar otro combate.
*   🖥 **Panel de Previsualización de Equipos**: Previsualiza en tiempo real como están quedando los equipos formados en el combate.
*   **📜 Comprobación de Datos Necesarios**: Automáticamente el sistema reconoce si faltan campos por llenar antes de confirmar la organización de un combate y los da a conocer.
*   **✔️ Confirmación y Cancelación del Combate**: La aplicación Web cuenta con botones de Confirmación, para comprobar la integridad de los datos necesarios y Cancelación, para borrar algunos datos entrados, como la distribución de los equipos formados. 
*   **ℹ️ Sistema de Ayuda**: Cada menú de la aplicación cuenta con un panel de ayuda explicando para que es cada campo de entrada.

## 🛑 Restricciones de la WRB

Como parte de la organización de combates, la WRB ha establecido un conjunto de restricciones, que la aplicación Web hace cumplir, para una mejor planificación de estos:

### Restricción de Co-requisito

*   **Regla**: Un Robot requiere de dos armas, una para cada brazo, para ser válido.  
    **Explicación**: Para que los combates sean más emocionantes y variados, cada robot debe estar equipado, obligatoriamente, con dos armas diferentes, posibilitando una mayor dificultad de su control.

### Restricción de Exclusión Mutua

*   **Regla**: Diferentes tipos de armas no pueden coexistir con otras.\
    **Explicación**: Por razones de incompatibilidad entre armas, ciertas combinaciones de armamento no pueden establecerse en un mismo robot. Estas combinaciones son:

    * **Combinación**: Lanzallamas, Sensores ópticos avanzados.\
      **Razón**: El fuego bloquea la visión de los sensores.
        
    * **Combinación**: Cañón láser, Generador de niebla.\
      **Razón**: La niebla impide la precisión del láser.
        
    * **Combinación**: Martillo hidráulico, Escudo de energía.\
      **Razón**: El escudo absorbe el impacto, no pueden coexistir.
        
    * **Combinación**: Electroshock, Campo magnético protector.\
      **Razón**: El campo anula la descarga eléctrica.
        
    * **Combinación**: Blindaje reforzado, Sistema de evasión automática.\
      **Razón**: El blindaje pesado impide la agilidad.
        
    * **Combinación**: Placas de titanio, Absorción de impactos.\
      **Razón**: Ambos ocupan el mismo sistema estructural.
        
    * **Combinación**: Drones de reconocimiento, Iluminación infrarroja.\
      **Razón**: La luz IR interfiere con los drones.
        
    * **Combinación**: Iluminación UV, Iluminación infrarroja.\
      **Razón**: Solo puede usarse un tipo de iluminación a la vez.
        
### Otras Restricciones

*   **Regla**: Las arenas se requieren durante 24 horas.\
    **Explicación**: Durante la gestión de eventos, es necesario preparar las arenas para la realización del combate, por lo que no se pueden programar diversos combates en una misma arena, el mismo día.

*   **Regla**: Todos los campos son obligatorios.\
    **Explicación**: La validez de un combate depende del llenado correcto de todos sus campos. Para una mayor organización del Proyecto, es obligatoria la entrada de todos los datos del evento.

## Requisitos

Asegurece de tener instalado en su sistema:
*   **Python 3.7 o superior**
*   **Git**
*   **pip** (generalmente viene con Python)

## Instalación y Ejecución

Para la Instalación y Ejecución de esta aplicación Web siga las indicaciones siguientes en cualquier terminal:

1.  **Clonar el Repositorio**
    
    ```bash
    git clone https://github.com/laxxuzxlr8/WRB-GitHub.git
    cd WRB-GitHub
    ```

2.  **Crear y Activar un Entorno Virtual (Recomendado)**
    
    *   **En Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    *   **En macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instalar las Dependencias**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la Aplicación**

    ```bash
    streamlit run main.py
    ```
    
## 📁 Estructura del Proyecto

```
WRB-GitHub/
├── main.py                         # Archivo principal de la aplicación Web
├── core.py                         # Algunas funciones de la aplicación Web
├── requirements.txt                # Lista de dependencias para instalación fácil
├── data/                           # Carpeta de archivos json (datos de la Aplicación Web)
│   ├── inventario.json             # Registro del inventario de recursos de la WRB
│   └── combates.json               # Registro de combates planificados de la WRB
├── images/                         # Carpeta de imágenes de la aplicación Web
├── pages/                          # Carpeta de páginas de la aplicación Web
│   ├── acerca_de.py                # Página de información de la WRB
│   ├── organizar_combate.py        # Página para organizar combates en la WRB
│   ├── combates_organizados.py     # Página para listar combates programados de la WRB
│   ├── robots.py                   # Página de Ranking Mundial de robots de la WRB
│   └── armas.py                    # Página de catálogo de armas y accesorios
└── README.md                       # Este archivo
```

## 🦾 Tecnologías Utilizadas

*   **[Streamlit](https://streamlit.io/)**: Framework para crear aplicaciones web interactivas en Python de manera rápida.
*   **[Pandas](https://pandas.pydata.org/)**: Biblioteca para manipulación y análisis de datos, ideal para gestionar listas de héroes y combates.
*   **Python**: Lenguaje de programación principal.

## 📄 Licencia y Agradecimientos Especiales

Este proyecto fue creado como Primer Proyecto Evaluativo para la Carrera de Ciencias de la Computación de la Universidad de la Habana; 1er año, Curso: 2025-2026.

**Agradecimiento especial a [ClaudiaHdezPerez](https://github.com/ClaudiaHdezPerez) por amadrinar este Proyecto.**

Además, este proyecto fue inspirado por el mundo de **Gigantes de Acero**. Si te gusta el lore de esta gran historia puedes buscar información en su Wiki:
* [Fandom Gigantes de Acero](https://gigantes-de-acero.fandom.com/es/wiki/Wiki_Gigantes_de_Acero)

También puedes ver La película oficial protagonizada por **Hugh Jackman**, una historia llena de pasión y éxitos:
* [Gigantes de Acero - Película (2011)](https://www.youtube.com/watch?v=DebFX7MC0vE) 

---

**Made with 💜 by [laxxuzxlr8](https://github.com/laxxuzxlr8)**