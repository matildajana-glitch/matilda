import streamlit as st

st.set_page_config(
    page_title="Este es mi sitio",
    page_icon=":sweat_drops:"
    )

st.title("como afecta el acondicionamiento fisico en deportistas de alto rendimiento")
st.badge("Cuenta de alto rendimiento", color="red", icon=":material/done_outline:")
st.write("Este es un sitio web  para personas que realmente les importa el deporte")

st.divider()

st.header("deportes", divider=True)
col1, col2 = st.columns(2)
col1.write("Mejora del rendimiento: Un buen acondicionamiento físico permite al deportista rendir al máximo de sus capacidades. Aumenta la fuerza, la resistencia, la velocidad y la agilidad, lo que se traduce en un mejor desempeño en su disciplina. ")
col2.write("Prevención de lesiones: Un cuerpo bien acondicionado es menos propenso a sufrir lesiones. Los músculos, tendones y ligamentos más fuertes y flexibles pueden soportar mejor el estrés del entrenamiento y la competición, reduciendo el riesgo de esguinces, desgarros y otras lesiones.")
col1.write("Recuperación más rápida: El acondicionamiento físico adecuado mejora la capacidad del cuerpo para recuperarse después de un esfuerzo intenso. Esto significa que el deportista puede entrenar con más frecuencia y con mayor intensidad sin experimentar una fatiga excesiva. ")
col1.write(
"""Mayor longevidad en el deporte: Los deportistas con un buen acondicionamiento físico suelen tener carreras deportivas más largas, ya que su cuerpo está mejor preparado para soportar las exigencias del deporte a largo plazo ,acontinuacion adjunto audio con musica para entrenar con motivacion. """
)

col2.image("correr.jpeg", caption=" sigue haciendo deporte siempre ")
col2.image("fisico.jpg", caption="entrena cada dia")

col2.video("https://www.youtube.com/watch?v=JnDu110SBN0&list=PLn7X7_tj-QEcuRfDEkVsUNbU4g9LoIYx-")
col2.audio("dont-talk-315229.mp3")