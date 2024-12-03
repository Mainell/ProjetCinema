# Importation des bibliothèques nécessaires

import streamlit as st

# Ajout d'un fond sonore
st.audio("feu.mp3", format="audio/mpeg")

# Ajout d'un fond d'écran
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://lafibre.info/images/smileys/201004_Warm_lights_by_Max_Barners.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Titre de l'application : mot de bienvenue !
st.markdown(
    """
    <h1 style="color: white; text-align: center;">Bienvenue sur l'application de recommandations</h1>
    <h2 style="color: orange; text-align: center;">Offerte par votre cinéma ! </h2>
    """, unsafe_allow_html=True
)

st.write("\n\n")

# Ajout du logo de l'agence Multimedia-Creuse, au centre de trois colonnes

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image("logo.png")

with col3:
    st.write(' ')

# Première partie : prise en compte du genre du film

st.markdown(
    """
    <h2 style="color: white; text-align: center;">Commencez par nous dire quel genre de film vous aimeriez voir...</h2>
    """, unsafe_allow_html=True
)
st.radio("  ", ['Comédie', 'Aventure', 'Thriller', 'Romance', 'Documentaire', 'Dessin animé'])

st.write("\n\n")

# Deuxième partie : prise en compte de la date de production du film

st.markdown(
    """
    <h2 style="color: white; text-align: center;">... Et ensuite, un film de quelle période vous aimeriez regarder !</h2>
    """, unsafe_allow_html=True
)

start_year, end_year = st.select_slider(
    "   ", options=[
        "1930",
        "1940",
        "1950",
        "1960",
        "1970",
        "1980",
        "1990",
        "2000",
        "2010",
        "2020",
        "2024"],
    value=("1930", "2024"),
)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.write("La période que vous avez choisie commence en", start_year, "et se termine en", end_year)

with col3:
    st.write(' ')



st.write("\n\n")
st.write('_____')


# Ajout d'un bouton pour le fun


col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    if st.button("Clique ici si tu as aimé notre application !"):
        st.markdown(''':yellow_heart: :rainbow[Merciiii ! A très bientôt !] :yellow_heart:''')

with col3:
    st.write(' ')
