
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-purple.svg)
![License](https://img.shields.io/badge/License-CC-green.svg)

# ¡World Robot Boxing!

## Tema Seleccionado

**Planificador de combates entre Robots de la WRB.**

## Tabla de Contenidos
- [Descripción](#descripción-del-proyecto)
- [Características](#características-principales)
- [Funciones](#funciones-auxiliares)
- [Restricciones](#restricciones-de-la-wrb)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Estructura](#estructura-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Licencia y Agradecimientos Especiales](#licencia-y-agradecimientos-especiales)

## Descripción del Proyecto

¡El Deporte más famoso del Futuro ya está aquí! El combate entre Robots siempre ha sido uno de los deseos más ambiciosos del ser humano: Metal vs Metal, un hito inalcanzable decían algunos excéntricos de los últimos tiempos. Pero gracias a **@laxxuzxlr8** y a su Proyecto estrella: La **World Robot Boxing**(**WRB**), ahora es posible organizar estos asaltos legendarios entre **Gigantes de Acero**. Con una amplia gama de Robots, Armas, Arenas y Restricciones, esta aplicación Web te permitirá organizar Combates inolvidables a tú manera, almacenándolos en nuestro **Sistema de Almacenamiento Json** para que no te pierdas ninguna presentación de tu Combatiente favorito.

## Características Principales

Esta aplicación Web cuenta con varios Módulos que te permitirán:

*   **Ver Información de la WRB**: Conoce acerca de la WRB, qué es y todo lo que puede llegar a ofrecer.
*   **Organizar Combates**: ¡El suelo tiembla ante la dominación del Metal! Organiza combates personalizados entre Robots de tu preferencia, con armas de todo tipo de calibre y restricciones específicas establecidas por este Sistema. Selecciona, entre las opciones disponibles, de manera rápida y sin colisiones entre Combates y Recursos, una configuración que mejor se ajuste a tus gustos: Fecha, Arena, Modo, Equipos, Control, así como el Patrocinador encargado de gestionar el encuentro planificado. 
*   **Listar Combates Programados**: Revisa el listado de todos los combates organizados hasta el momento, así como todas sus especificaciones y recursos que requiere.
*   **Eliminar un Combate**: La aplicación Web tiene un sistema de borrado fácil y rápido para que descartes todo tipo de encuentros que ya no sean de tu interés.
*   **Ver Robots del Ranking Mundial**: Descubre cuáles son los Robots más exitosos de este deporte mediante una serie de imágenes de ellos.
*   **Ver Armas y Accesorios de la WRB**: Navega a través del catálogo de armas y accesorios de la WRB para que conozcas con qué combinar a tus robots favoritos.

## Funciones Auxiliares

Este proyecto cuenta también con algunas funciones auxiliares que apoyan el código de la Aplicación Web:

*   **Recomendación de Hueco disponible**: Ten referencia del próximo día disponible para la organización de un combate en la WRB.
*   **Repartición de Recursos**: El sistema reconoce los recursos empleados en el día seleccionado y muestra solo los recursos disponibles para poder organizar otro combate.
*   **Panel de Previsualización de Equipos**: Previsualiza en tiempo real cómo están quedando los equipos formados y modifica los establecidos hasta el momento.
*   **Comprobación de Datos Necesarios**: Automáticamente el sistema reconoce si faltan campos por llenar antes de confirmar la organización de un combate y los da a conocer.
*   **Confirmación y Cancelación del Combate**: La aplicación Web cuenta con botones de Confirmación, para comprobar la integridad de los datos necesarios y Cancelación, para borrar algunos datos entrados, como la distribución de los equipos formados. 
*   **Verificación de disponibilidad de Células de Energía**: Ante la confirmación de un evento, el sistema calcula la disponibilidad y el requerimiento de C/E pre-establecido en la base de datos de la Aplicación Web.
*   **Controlador de Eventos Completados**: Al iniciar la app, todo evento programado, que se haya realizado hasta la fecha actual, es eliminado de la base de datos del sistema de manera automática.
*   **Sistema de Ayuda**: Cada menú de la aplicación cuenta con un panel de ayuda explicando para que es cada campo de entrada.


## Restricciones de la WRB

Como parte de la organización de combates, la WRB ha establecido un conjunto de restricciones, que la aplicación Web hace cumplir, para una mejor planificación de estos:

### Restricción de Co-requisito

*   **Regla**: Un robot requiere de una cantidad pre-establecida de Células de Energía para poder combatir.\
    **Explicación**: Se ha desarrollado un Sistema de Células de Energía en el cual cada robot depende de una cantidad fija de estas células para su óptimo y completo funcionamiento, durante todo el evento.
    
    **Sistema de Células de Energía**:
      
      | Robots | C/E | Robots | C/E | Robots | C/E | Robots | C/E | Robots | C/E |
      | :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: |
      | Albino | 375 | Ambush | 410 | Atom | 350 | Axelrod | 400 | Bash | 430 |
      | Blacktop | 395 | Blue Bot | 415 | Bricks | 440 | Fatboy | 480 | Gambit | 365 |
      | Gridlock | 425 | HollowJack | 385 | Metro | 420 | Midas | 400 | Nitro | 420 |
      | Noisy Boy | 395 | Shogun | 410 | Six Shooter | 390 | Tackle | 435 | Tri-Tip | 470 |
      | Twin Cities | 435 | Vanda | 490 | Visualizer | 325 | Wheeled Bot | 415 | Zeus | 550 |

*   **Regla**: Un Robot requiere de dos armas, una para cada brazo, para ser válido.\
    **Explicación**: Para que los combates sean más emocionantes y variados, cada robot debe estar equipado, obligatoriamente, con dos armas diferentes, posibilitando una mayor dificultad de su control.
    
    **Armamento**:
    
    | Arma-Accesorio | Tipo | Arma-Accesorio | Tipo | Arma-Accesorio | Tipo |
    | :--- | :---: | :--- | :---: | :--- | :---: |
    | Aplastador neumático | Ofensivo | Cañón de microondas | Ofensivo | Cañón de plasma de baja potencia | Ofensivo |
    | Cañón sónico | Ofensivo | Cañón láser | Ofensivo | Cuchilla guillotina vertical | Ofensivo |
    | Cuchillas retráctiles de tungsteno | Ofensivo | Electroshock | Ofensivo | Garra prensil aplastante | Ofensivo |
    | Lanzador de proyectiles metálicos | Ofensivo | Lanzallamas | Ofensivo | Lanza-arpón motorizado | Ofensivo |
    | Lanza-chispas de arco eléctrico | Ofensivo | Martillo hidráulico | Ofensivo | Martillo rotatorio de impacto | Ofensivo |
    | Maza electromagnática | Ofensivo | Misiles de corto alcance | Ofensivo | Motosierra | Ofensivo |
    | Puños reforzados | Ofensivo | Sierra de cadena doble | Ofensivo | Taladro percutor industrial | Ofensivo |
    | Absorción de impactos | Defensivo | Barreras de energía pulsante | Defensivo | Blindaje óseo sintético | Defensivo |
    | Blindaje reforzado | Defensivo | Campo eléctrico disipador | Defensivo | Campo magnético protector | Defensivo |
    | Escudo de energía | Defensivo | Escudo óptico reforzado | Defensivo | Placas de carburo endurecido | Defensivo |
    | Placas de titanio | Defensivo | Revestimiento anti-impactos avanzado | Defensivo | Sistema de absorción cinética | Defensivo |
    | Sistema de evasión automática | Defensivo | Detector de energía enemiga | Soporte | Drones de reconocimiento | Soporte |
    | Radar de proximidad | Soporte | Sensores ópticos avanzados | Soporte | Sistema de cámaras HD | Soporte |
    | Generador de niebla | Especial | Iluminación infrarroja | Especial | Iluminación UV | Especial |
    | Sistema de hologramas distractores | Especial | --- | --- | --- | --- |   

### Restricción de Exclusión Mutua

*   **Regla**: Diferentes tipos de armas no pueden coexistir con otras.\
    **Explicación**: Por razones de incompatibilidad entre armas, ciertas combinaciones de armamento no pueden establecerse en un mismo robot.\
    
    
    **Combinaciones**:
    * **Combinación**: Lanzallamas, Sensores ópticos avanzados.\
      **Razón**: El fuego bloquea la visión de los sensores.
        
    * **Combinación**: Cañón láser, Generador de niebla.\
      **Razón**: La niebla impide la precisión del láser.
        
    * **Combinación**: Martillo hidráulico, Escudo de energía.\
      **Razón**: El escudo absorbe el impacto, no pueden coexistir.
        
    * **Combinación**: Electroshock, Campo magnético protector.\
      **Razón**: El campo anula la descarga eléctrica.
        
    * **Combinación**: Blindaje reforzado, Sistema de evasión     automática.\
      **Razón**: El blindaje pesado impide la agilidad.
        
    * **Combinación**: Placas de titanio, Absorción de impactos.\
      **Razón**: Ambos ocupan el mismo sistema estructural.
        
    * **Combinación**: Drones de reconocimiento, Iluminación infrarroja.\
      **Razón**: La luz IR interfiere con los drones.
        
    * **Combinación**: Iluminación UV, Iluminación infrarroja.\
      **Razón**: Solo puede usarse un tipo de iluminación a la vez.
    
    * **Combinación**: Maza electromagnética, Campo magnético protector.\
      **Razón**: Ambos generan campos que se anulan entre sí dentro del mismo robot.
    
    * **Combinación**: Lanzador de proyectiles metálicos, Placas de carburo endurecido.\
      **Razón**: Las placas desvían los proyectiles al salir, causando fallos internos.
    
    * **Combinación**: Cuchilla guillotina vertical, Sistema de evasión automática.\
      **Razón**: El movimiento evasivo impide la estabilidad necesaria para la guillotina.
    
    * **Combinación**: Garra prensil aplastante, Escudo óptico reforzado.\
      **Razón**: La garra no puede operar sin obstruir el campo visual del escudo.
    
    * **Combinación**: Lanza-chispas de arco eléctrico, Campo eléctrico disipador.\
      **Razón**: El campo disipador neutraliza el arco eléctrico del arma.
    
    * **Combinación**: Sierra de cadena doble, Blindaje óseo sintético.\
      **Razón**: El blindaje desprende residuos que atascan la doble cadena.
    
    * **Combinación**: Cañón sónico, Detector de energía enemiga.\
      **Razón**: Las ondas sónicas saturan los sensores del detector.

### Otras Restricciones

*   **Regla**: Las arenas se requieren durante 24 horas.\
    **Explicación**: Durante la gestión de eventos, es necesario preparar las arenas para la realización del combate, por lo que no se pueden programar diversos combates en una misma arena, el mismo día.

*   **Regla**: Las células de energía se cargan durante una noche completa.\
    **Explicación**: El buen funcionamiento de un robot depende de la totalidad de carga de sus células de energía, por lo que estas deben estar en perfecto estado ante cada combate.
    En otras palabras, si una célula es usada un día, no puede ser usada hasta el próximo día.

*   **Regla**: Todos los campos son obligatorios.\
    **Explicación**: La validez de un combate depende del llenado correcto de todos sus campos. Para una mayor organización del Proyecto, es obligatoria la entrada de todos los datos del evento.

## Requisitos

Asegurece de tener instalado en su sistema:
*   **Python 3.8 o superior**
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
    
## Estructura del Proyecto

Visualización de la estructura de los archivos del Proyecto:

```
WRB-GitHub/
├── data/                           # Carpeta de archivos json (base de datos de la Aplicación Web)
│   ├── inventario.json             # Registro del inventario de recursos de la WRB
│   └── combates.json               # Registro de combates planificados de la WRB
├── images/                         # Carpeta de imágenes de la aplicación Web
├── pages/                          # Carpeta de páginas de la aplicación Web
│   ├── acerca_de.py                # Página de información de la WRB
│   ├── organizar_combate.py        # Página para organizar combates en la WRB
│   ├── combates_organizados.py     # Página para listar combates programados de la WRB
│   ├── robots.py                   # Página de Ranking Mundial de robots de la WRB
│   └── armas.py                    # Página de catálogo de armas y accesorios
├── core.py                         # Algunas funciones de la aplicación Web
├── main.py                         # Archivo principal de la aplicación Web
├── README.md                       # Este archivo
└── requirements.txt                # Lista de dependencias para instalación fácil
```

## Tecnologías Utilizadas

Lenguaje de Programación y Librerías utilizadas para la creación de esta Web:

*   **[Streamlit](https://streamlit.io/)**: Framework para crear aplicaciones web interactivas en Python de manera rápida.
*   **[Pandas](https://pandas.pydata.org/)**: Biblioteca para manipulación y análisis de datos, ideal para gestionar listas de héroes y combates.
*   **[Python](https://www.python.org/)**: Lenguaje de programación principal.

## Licencia y Agradecimientos Especiales

Este proyecto fue creado como Primer Proyecto Evaluativo para la Carrera de Ciencias de la Computación de la Universidad de la Habana; 1er año, Curso: 2025-2026.

**Agradecimiento especial a [ClaudiaHdezPerez](https://github.com/ClaudiaHdezPerez) por amadrinar este Proyecto.**

Además, este proyecto fue inspirado por el mundo de **Gigantes de Acero**. Si te gusta el lore de esta gran historia puedes buscar información en su Wiki Oficial:
* [Fandom Gigantes de Acero](https://gigantes-de-acero.fandom.com/es/wiki/Wiki_Gigantes_de_Acero)

También puedes ver La película oficial protagonizada por **Hugh Jackman**, una historia llena de pasión y éxitos:
* [Gigantes de Acero - Película (2011)](https://www.youtube.com/watch?v=DebFX7MC0vE) 

---

**Made with 💜 by [laxxuzxlr8](https://github.com/laxxuzxlr8)**