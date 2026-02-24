import streamlit as st

st.set_page_config(layout="wide", page_title="CV Alonso Mercado")

# ---- CSS PARA JUSTIFICAR Y AGRANDAR TEXTO ----
st.markdown("""
<style>
.justified-text {
    text-align: justify;
    font-size: 20px;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

st.title("Currículum Vitae – Alonso Mercado")

pagina = st.sidebar.radio(
    "Secciones",
    ["Presentación", "Información Personal", "Formación Académica", "Experiencia", "Habilidades"]
)

# ---------------- PRESENTACIÓN ----------------
if pagina == "Presentación":
    st.header("Perfil Profesional")
    st.markdown("""
    <div class="justified-text">
    Ingeniero Civil Industrial titulado de la Universidad Técnica Federico Santa María.  
    Me especializo en análisis cuantitativo, modelamiento predictivo y desarrollo de soluciones basadas en datos.  
    Tengo especial interés en finanzas, econometría, optimización y machine learning aplicado a la toma de decisiones estratégicas.  
    Me caracterizo por una fuerte orientación analítica, pensamiento estructurado y capacidad para transformar datos en información accionable.  
    </div>
    """, unsafe_allow_html=True)

# ---------------- INFORMACIÓN PERSONAL ----------------
elif pagina == "Información Personal":
    st.header("Información Personal")
    st.markdown("""
    <div class="justified-text">
    <b> Nombre: </b> Alonso Simón Mercado Rojel <br> 
    <b> Profesión:</b> Ingeniero Civil Industrial  <br>
    <b> Nacionalidad:</b> Chilena  <br>
    <b> Ciudad de residencia:</b> Valparaíso, Chile  <br>
    <b> Teléfono:</b> +56 9 8807 9161  <br>
    <b> Correo:</b> alonsosimon.m.r@gmail.com <br>
    <a href="https://www.linkedin.com/in/alonso-mercado-rojel-35118b2b2?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BvSYZZ2lMSHKOzAz49muM6g%3D%3D" target="_blank"><b>Perfil de LinkedIn</b></a>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FORMACIÓN ----------------
elif pagina == "Formación Académica":
    st.header("Formación Académica")
    st.markdown("""
    <div class="justified-text">
    <b>Universidad Técnica Federico Santa María – Casa Central Valparaíso</b>   
                 
    Ingeniería Civil Industrial  
    2020 – 2025  

    • Asignaturas de Especialización: Finanzas II, Gestión de Inversiones y Uso de Software para la Ingeniería Industrial  
    • Trabajo de Título: Evaluación Comparativa de modelos GARCH y GARCH-LSTM Incorporando el Índice VIX para la predicción de volatilidad en ETFS del sector energético de EE. UU.  

    <b>Cursos Udemy</b>  
    • Especialista en Deep-learning en Python con Pytorch  
    • Especialista en Ciencia de Datos con Python  
    2025  
    </div>
    """, unsafe_allow_html=True)


# ---------------- EXPERIENCIA ----------------
elif pagina == "Experiencia":
    st.subheader("Práctica Profesional – KeyProcess SPA")
    st.markdown("""
<div class="justified-text">

Empresa especializada en recuperación de minerales en relaves y soluciones tecnológicas para la minería.  

La práctica profesional se realizó en <a href="https://www.key-process.com/" target="_blank"><b>KeyProcess SPA</b></a>, donde desarrollé dashboards interactivos para análisis financiero y operacional, automaticé reportes en línea utilizando Python y herramientas Office, apoyé en la gestión de operaciones y análisis de costos, y adquirí experiencia en el uso del portal SAP Ariba para gestión de proveedores.
La práctica tuvo una duración de 320 horas.
</div>
""", unsafe_allow_html=True)


    st.subheader("Práctica Industrial – Dirección de Transformación Digital, USM")
    st.markdown("""
<div class="justified-text">

Durante la práctica industrial en la <a href="https://transformaciondigital.usm.cl/dtd/" target="_blank"><b>Dirección de Transformación Digital</b></a> de la Universidad Técnica Federico Santa María, elaboré reportes estratégicos en Power BI, participé en la digitalización y consolidación de bases de datos institucionales y apoyé procesos de transformación digital.
La práctica tuvo una duración de 320 horas.
</div>
""", unsafe_allow_html=True)

    st.header("Experiencia Académica – Ayudantías")

    st.markdown("""
    <div class="justified-text">

    <b> Gestión de Operaciones II – USM (2025)</b>  
    • Diseño y evaluación de tareas  
    • Apoyo en modelamiento de problemas de optimización  

    <b> Econometría – USM (2024–2025) </b>  
    • Clases de cátedra y creación de material  
    • Corrección de certámenes y guías  

    <b> Macroeconomía – USM (2024) </b>  
    • Clases de cátedra y creación de material  
    • Corrección de certámenes y guías  

    <b> Microeconomía – USM (2022–2023) </b>  
    • Clases de cátedra, creación de material y correción de evaluaciones  
    • Corrección de certámenes y guías.  
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
<div class="justified-text">
<b> Referencias </b><br>
KeyProcess: mbastias@keyflot.cl<br>
Dirección de Transformación Digital USM: mauricio.saldivia@usm.cl<br>
Prof. Econometría: bernardo.pincheira@usm.cl<br>
Prof. Gestión de Operaciones: monica.lopezc@usm.cl
</div>
""", unsafe_allow_html=True)

# ---------------- HABILIDADES ----------------
elif pagina == "Habilidades":
    st.header("Habilidades Técnicas")

    st.markdown("""
<div class="justified-text">
<b> Programación:</b> Python (diferentes librerías, desde manipulación de datos hasta creación de modelos de Machine Learning), MySQL y R. <br>                   
<b> Visualización:</b> Power BI y Streamlit (Python). <br>  
<b> Idiomas:</b> Inglés B1.
</div>
""", unsafe_allow_html=True)



