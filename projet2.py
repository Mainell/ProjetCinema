# Importation des bibliothèques nécessaires

import streamlit as st
#from streamlit_option_menu import option_menu

#import pandas as pd

# Importation du dataset

#dataset_cinema = st.file_uploader("DFnettoye.csv", type="csv")

# Vérifier si un fichier a été téléchargé
#if dataset_cinema is not None:
    # Lire le fichier CSV avec Pandas
    #df = pd.read_csv(dataset_cinema)

    # Afficher les premières lignes du dataset
    #st.write("Aperçu du dataset :")
    #st.dataframe(df)

# Ajout d'un fond sonore
st.audio("mediavision.mp4", format="audio/mpeg")

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

# Création d'un menu permettant de choisir entre deux stratégies de choix de film

#selection = option_menu(

            #menu_title=None,

            #options = ["Choix d'un acteur que vous appréciez", "Choix du genre et de la période du film"]

        #)

# Stratégie n°1 : choix de l'acteur
#if selection == "Choix d'un acteur que vous appréciez":

    st.markdown(
    """
    <h2 style="color: white; text-align: center;">Commencez par nous dire quel est l'acteur du film que vous aimeriez voir...</h2>
    """, unsafe_allow_html=True
    )

#def rechercher_films_par_acteur(df, acteur):
  #films = df[df['primaryName'].str.contains(acteur, case=False, na=False)]
  #if films.empty:
    #return f"Aucun film trouvé pour l'acteur '{acteur}'."
  #return films[['primaryTitle','primaryName']]

#acteur_recherche = input("Entrez le nom d'un acteur: ")
#films_trouves = rechercher_films_par_acteur(df, acteur_recherche)

#if isinstance(films_trouves, str):
    #print(films_trouves)
#else:
    #print(f"L'acteur a joué dans les films suivants :")
    #for index,row in films_trouves.iterrows():
        #print(f"- {row['primaryTitle']} ({row['primaryName'].split(',')[:3]})")

    #base_image = "https://image.tmdb.org/t/p/w500" # taille standard de l'image
    #poster = base_image + first_movie['poster_path']
    #print(poster)

# Stratégie n°2 : choix du genre et de la période du film
#elif selection == "Choix du genre et de la période du film":

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



    st.write("\n\n")
    st.write('_____')


# Ajout d'un bouton pour le fun, visible sur n'importe quelle page du menu


col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    if st.button("Clique ici si tu as aimé notre application !"):
        st.markdown(''':yellow_heart: :rainbow[Merciiii ! A très bientôt !] :yellow_heart:''')

with col3:
    st.write(' ')
