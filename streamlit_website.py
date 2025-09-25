# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="pagina fitnness",
    page_icon=":dolphin:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)




pg = st.navigation(["portada.py","recetas.py","Kobrish nadadora.py","Eduardo Cisternas.py","acondicionamiento fisico.py","quienes somos.py"])
pg.run()