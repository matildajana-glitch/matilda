import streamlit as st

st.set_page_config(
    page_title="Este es mi sitio",
    page_icon=":sweat_drops:"
    )

st.title("Bienvenido a  la biografia de Kristel Köbrich ")
st.badge("Cuenta de alto rendimiento", color="red", icon=":material/done_outline:")
st.write("Este es un sitio web  para personas que realmente les importa el deporte")

st.divider()

st.header("Nadadora", divider=True)
col1, col2 = st.columns(2)
col1.write("Kristel Köbrich alcanza histórico registro en Mundial de Singapur y fue la mejor latina en 1500 metros ")
col2.write("Kristel kobrich")
col1.write("Apodo(s)La Cobra,NacimientoSantiago, Chile · 9 de agosto de 1985 (40 años),Nacionalidad(es)Chilena,Altura1,71 m,Peso60 k,DeporteNatación,EntrenadorDaniel F. Garimaldiel y de la selección de Chile ")
col1.write(
"""La nadadora chilena Kristel Köbrich sigue escribiendo con letras doradas su historia en el deporte, esta vez con una destacada participación en el Mundial de Singapur 2025.

La santiaguina, de 39 años, debutó este lunes en los 1500 metros libres, donde terminó como la mejor latinoamericana y top 15. Hizo 16:22.66 y culminó en el lugar 14.

En el puesto 18 remató la brasileña Gabrielle Rocanto, mientras que su compatriota Leticia Fassina Romao finalizó en el puesto 20. Más atrás, en la casilla 22 apareció la argentina Delfina Din,Eso no es todo, ya que la mujer récord completó su décimo tercera participación en campeonatos mundiales, lo que es récord absoluto en el planeta. """
)

col2.image("plata.jpg   ", caption=" nadar es lo maximo")
col2.image("dorada.jpg", caption="entrena cada dia")

col2.video("https://youtu.be/S7PbrsYbCcM?si=NYsthm_zzyM0Ukrj")