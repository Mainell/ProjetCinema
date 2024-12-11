# Importation des bibliothèques nécessaires

import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Importation du dataset

df = pd.read_csv("DFnettoye.csv")


# Ajout d'un fond sonore

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    #if st.button("Lancer le son"):
    st.audio("mediavision.mp3", format="audio/mpeg", autoplay= True)

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
st.write("juste un test")
st.markdown(page_element, unsafe_allow_html=True)


# Création d'un menu permettant d'accéder à la page d'accueil ou d'accéder à deux stratégies différentes de choix du film

option = st.sidebar.selectbox("Quelle page de notre application souhaiteriez-vous consulter ?", ["Accueil", "Choix par acteur", "Choix par genre et par période"])

if option == "Accueil":
    # Page d'Accueil
    # Ajout d'un mot de bienvenue 
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
        #df[df["genres"].str.contains("Documentary")].sort_values(by='averageRating').head(5)['primaryTitle']

    with col3:
        st.write(' ')

    # Ajout de quelques documentaires conseillés car thème 2025 du festival cinéma d'Aubusson

    col1, col2, col3 = st.columns(3)
    recoaccueil = df[df['genres'].str.contains("Documentary")].sort_values(by='averageRating').sample(6)

    with col1:
        for i, j in recoaccueil.iloc[0:2].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL = base_image + j['poster_path']
            st.image(URL)
            st.write(f"- {j['primaryTitle']} - ({int(j['startYear'])})\n"
                     f" - Genres : {j['genre_unique']}\n"
                     f" - Durée : {j['runtimeMinutes']} minutes\n"
                     f" - Note moyenne : {j['averageRating']}\n")  
    with col2:
        for i, j in recoaccueil.iloc[2:4].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL = base_image + j['poster_path']
            st.image(URL)
            st.write(f"- {j['primaryTitle']} - ({int(j['startYear'])})\n"
                     f" - Genres : {j['genre_unique']}\n"
                     f" - Durée : {j['runtimeMinutes']} minutes\n"
                     f" - Note moyenne : {j['averageRating']}\n")
    with col3:
        for i, j in recoaccueil.iloc[4:6].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL = base_image + j['poster_path']
            st.image(URL)
            st.write(f"- {j['primaryTitle']} - ({int(j['startYear'])})\n"
                     f" - Genres : {j['genre_unique']}\n"
                     f" - Durée : {j['runtimeMinutes']} minutes\n"
                     f" - Note moyenne : {j['averageRating']}\n")


elif option == "Choix par acteur":
    # Deuxième page : choix par acteur
    st.markdown(
    """
    <h2 style="color: white; text-align: center;">Commencez par choisir un acteur.</h2>
    """, unsafe_allow_html=True
    )

    # st.dataframe(df)

    acteur =  st.text_input("Entrez le nom d'un acteur:")

    col1, col2, col3 = st.columns(3)

    with col1:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)]
        for index, row in films_acteur.iloc[0:2].iterrows():
            acteurs_principaux = ", ".join(row['primaryName'].split(", ")[:3])
            base_image = "https://image.tmdb.org/t/p/w500"
            URL = base_image + row['poster_path']
            st.image(URL)
            st.write(f"- {row['primaryTitle']} - ({int(row['startYear'])})\n"
                     f" - Genres : {row['genre_unique']}\n"
                     f" - Durée : {row['runtimeMinutes']} minutes\n"
                     f" - Note moyenne : {row['averageRating']}\n")  
    with col2:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)]
        for index, row in films_acteur.iloc[2:4].iterrows():
            acteurs_principaux = ", ".join(row['primaryName'].split(", ")[:3])
            base_image = "https://image.tmdb.org/t/p/w500"
            URL = base_image + row['poster_path']
            st.image(URL)
            st.write(f"- {row['primaryTitle']} - ({int(row['startYear'])})\n"
                     f" - Genres : {row['genre_unique']}\n"
                     f" - Durée : {row['runtimeMinutes']} minutes\n"
                     f" - Note moyenne : {row['averageRating']}\n")  
    with col3:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)]
        for index, row in films_acteur.iloc[4:6].iterrows():
            acteurs_principaux = ", ".join(row['primaryName'].split(", ")[:3])
            base_image = "https://image.tmdb.org/t/p/w500"
            URL = base_image + row['poster_path']
            st.image(URL)
            st.write(f"- {row['primaryTitle']} - ({int(row['startYear'])})\n"
                     f" - Genres : {row['genre_unique']}\n"
                     f" - Durée : {row['runtimeMinutes']} minutes\n"
                     f" - Note moyenne : {row['averageRating']}\n")  

    # def rechercher_films_par_acteur(df, acteur):
        # films = df[df['primaryName'].str.contains(acteur, case=False, na=False)]
        # if films.empty:
            # return f"Aucun film trouvé pour l'acteur '{acteur}'."
        # return films[['primaryTitle','primaryName']]

    # films_acteur = rechercher_films_par_acteur(df,acteur)
    # st.write(f"Films avec l'acteur/actrice '{acteur}':")
    # for index, row in films_acteur.iterrows():
        # acteurs_principaux = ", ".join(row['primaryName'].split(", ")[:3])
    
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
    # Troisième page : choix par genre et par période

    st.markdown(
    """
    <h2 style="color: white; text-align: center;"> Hey ! Ici vous allez pouvoir choisir un genre et une période pour votre film ✨ </h2>
    """, unsafe_allow_html=True
    )

    st.write("\n\n")


    genres = {
        'Drame': 0,
        'Crime': 1,
        'Comédie': 2,
        'Action': 3,
        'Aventure': 4,
        'Biographie': 5,
        'Romance': 6,
        'Fantaisie': 7,
        'Musical': 8,
        'Horreur': 9,
        'Mystère': 10,
        'Science-fiction': 11,
        'Animation': 12,
        'Documentaire': 13,
        'Western': 14,
        'Musique': 15,
        'Famille': 16,
        'Thriller': 17,
        'Guerre': 18,
        'Adulte': 19,
        'Histoire': 20}

    
    #choix_genre = st.radio(" ", options=list(genres.keys() ) )
    #genre_value = genres[choix_genre]
    #st.write(f"Vous avez choisi le genre '{choix_genre}' : très bon choix !")

    startyear, endyear = st.select_slider("Choisissez une date de début et une date de fin pour la période de votre film",
                                            options=range(1930, 2025),
                                            value=(1930, 2024))
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:

        st.write("La période que vous avez choisie commence en", startyear, "et se termine en", endyear)

        X = df[['startYear','genre_facto']]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        model = NearestNeighbors(n_neighbors=3, metric="euclidean")
        model.fit(X_scaled)

        genre_selection = st.selectbox("Choisissez un genre :", list(genres.keys()))
        genre_facto = genres[genre_selection]


        if st.button("Lancer la recherche"):
            recom = []
            for i in range(startyear, endyear + 1):
                criteres = pd.DataFrame([[i, genre_facto]], columns=['startYear', 'genre_facto'])
                criteres_scaled = scaler.transform(criteres)
                distance, indice = model.kneighbors(criteres_scaled)
                reco = df.iloc[indice[0]].copy()
                reco['Distance'] = distance[0]
                reco = reco[(reco['startYear'] >= startyear) & (reco['startYear'] <= endyear)]
                recom.append(reco)

            recom_final = pd.concat(recom).drop_duplicates(subset=['primaryTitle', 'startYear'])
            recom_final = recom_final.rename(columns={
                'primaryTitle': 'Titre',
                'startYear': 'Année',
                'genres': 'Genres',
                'runtimeMinutes': 'Durée (minutes)',
                'averageRating': 'Note moyenne'}).sort_values(["Distance", "Note moyenne"], ascending=[True, False]) 
    
        st.markdown("<h3 style='color: white;'>Top 5 recommandations :</h3>", unsafe_allow_html=True)
        if recom_final.empty:
            st.write("Aucun film trouvé pour les critères sélectionnés.")
        else:
            for i, j in recom_final.head(5).iterrows():
                st.write(
                    f"- {j['Titre']} - ({int(j['Année'])})\n"
                    f"  - Genres : {j['Genres']}\n"
                    f"  - Durée : {j['Durée (minutes)']} minutes\n"
                    f"  - Note moyenne : {j['Note moyenne']}\n")
                base_image = "https://image.tmdb.org/t/p/w500"
                URL = base_image + j['poster_path']
                st.image(URL) 

        # Pour finir, ajoutr d'un bouton pour recuueillir l'avis utilisateur
        if st.button("Clique ici si tu as aimé notre application !"):
            st.markdown(''':yellow_heart: :rainbow[Merciiii ! A très bientôt !] :yellow_heart:''')

    with col3:
        st.write(' ')



    st.write("\n\n")
    st.write('_____')
