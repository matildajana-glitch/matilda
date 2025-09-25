import streamlit as st

st.set_page_config(
    page_title="Este es mi sitio",
    page_icon=":sweat_drops:"
    )

st.title("Bienvenido a  la biografia de Eduardo")
st.badge("Cuenta de alto rendimiento", color="red", icon=":material/done_outline:")
st.write("Este es un sitio web  para personas que realmente les importa el deporte")

st.divider()

st.header("Nadador", divider=True)
col1, col2 = st.columns(2)
col1.write("Eduardo Cisternas, sumó una nueva medalla de plata para nuestro país con una marca de 03:49:40, en los 400 metros libre, bajando 5 segundos su tiempo de presentación y rompiendo el récord nacional en esta disciplina,Tras este triunfo, Chile suma, hasta ahora, un total de 10 medallas en el primer día de competencia: 5 de oro, 3 de plata y 2 de bronce,Con este resultado, nuestro país se ubica en el segundo lugar del medallero, justo después de Brasil, que acumula 15 preseas en lo que va de la competencia")
col2.write("Eduardo cisternas")
col1.write("Nacimiento:Santiago de Chile (Chile) · 10 de enero de 2004,Nacionalidad:(es)Chilena,Altura:1.81 m,Peso72 kg,Deporte: Natación,ClubStade Francais,Nombre completo:Eduardo Alberto Cisternas gomez")
col1.write(
"""Una brillante tarde tuvo Eduardo Cisternas en los Juegos Panamericanos Junior de Asunción 2025, donde en la final de los doscientos metros libre se quedó con la medalla de plata y registró un nuevo récord nacional absoluto Durante esta tarde el nadador chileno Eduardo Cisterna disputó la final de los 200m libre en piscina larga de los Juegos Panamericanos Junior de Asunción 2025.
En una lucha codo a codo con el brasileño Stephan Steverink el chileno se quedó con el segundo lugar de la prueba con un crono de 1:47.99 (+0.76) consiguiendo así la medalla de plata para Chile.
El ganador fue el brasileño Stephan Steverink con 1:47.23, mientras que el argentino Matías Santiso cerró el podio con 1:50.03
Cisternas no solo consiguió un tremendo segundo lugar, además estableció un nuevo récord nacional absoluto en los 200m libre, batiendo su propia marca de 1.49.47 realizada este año en el marco del Campeonato Nacional de Categorías de Invierno."""
)

col2.image("paginaweb.png   ", caption=" nadar es lo maximo")
col2.image("social-eduardo-cisternas-jjoo-ok.png", caption="entrena cada dia")

col2.video("https://youtu.be/KGfBr-KySi8?si=M6WAKGCz_uNUZRLB")