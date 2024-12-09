# Importation des bibliothèques nécessaires

import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd

# Importation du dataset

df = pd.read_csv("DFnettoye.csv")


# Ajout d'un fond sonore

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    #if st.button("Lancer le son"):
    st.audio("mediavision.mp4", format="audio/mpeg")

with col3:
    st.write(' ')

# Ajout d'un fond d'écran
page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://lafibre.info/images/smileys/201004_Warm_lights_by_Max_Barners.jpg");
  background-size: cover;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)


# Création d'un menu permettant d'accéder à la page d'accueil ou d'accéder à deux stratégies différentes de choix du film

option = st.sidebar.selectbox("Quelle page de notre application souhaiteriez-vous consulter ?", ["Accueil", "Choix par acteur", "Choix par genre et par période"])

if option == "Accueil":

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

elif option == "Choix par acteur":
    st.markdown(
    """
    <h2 style="color: white; text-align: center;">Commencez par choisir un acteur.</h2>
    """, unsafe_allow_html=True
    )

    st.dataframe(df)

    acteur =  st.text_input("Entrez le nom d'un acteur:")

    def rechercher_films_par_acteur(df, acteur):
        films = df[df['primaryName'].str.contains(acteur, case=False, na=False)]
        if films.empty:
            return f"Aucun film trouvé pour l'acteur '{acteur}'."
        return films[['primaryTitle','primaryName']]

    films_acteur = rechercher_films_par_acteur(df,acteur)
    st.write(f"Films avec l'acteur/actrice '{acteur}':")
    for index, row in films_acteur.iterrows():
        acteurs_principaux = ", ".join(row['primaryName'].split(", ")[:3])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:
        if st.button("Clique ici si tu as aimé notre application !"):
            st.markdown(''':yellow_heart: :rainbow[Merciiii ! A très bientôt !] :yellow_heart:''')

    with col3:
        st.write(' ')



    st.write("\n\n")
    st.write('_____')

        

else : 
    # Première partie : prise en compte du genre du film

    st.markdown(
    """
    <h2 style="color: white; text-align: center;">Commencez par nous dire quel genre de film vous aimeriez voir...</h2>
    """, unsafe_allow_html=True
    )

    st.radio("  ", ['Drame', 'Comédie', 'Documentaire', 'Crime', 'Action','Aventure', 'Biographie', 'Horreur', 'Dessin animé', 'Thriller', 'Romance', 'Famille', 'Science-Fiction', 'Musical', 'Western', 'Adult', 'Music', 'Guerre', 'Histoire'])

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
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:
        if st.button("Clique ici si tu as aimé notre application !"):
            st.markdown(''':yellow_heart: :rainbow[Merciiii ! A très bientôt !] :yellow_heart:''')

    with col3:
        st.write(' ')



    st.write("\n\n")
    st.write('_____')
