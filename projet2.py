# Importation des bibliothèques nécessaires

import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Importation du dataset

df = pd.read_csv("dfnettoye_titrefr.csv")


# Ajout d'un fond sonore

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.audio("mediavision.mp3", format="audio/mpeg", autoplay= False)

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
        st.markdown(
        """
        <h3 style="color: white; text-align: center;">Voici une suggestion de documentaires...</h3>
        """, unsafe_allow_html=True
        )
        st.write(' ')

    with col2:
        st.image("logo.png")

    with col3:
        st.markdown(
        """
        <h3 style="color: white; text-align: center;">... en prévision des festivals du cinéma | 2025 </h3>
        """, unsafe_allow_html=True
        )
        st.write(' ')

    st.write("\n\n")
    st.write('_____')

    # Ajout de quelques documentaires conseillés car thème récurrent des festivals cinéma

    col1, col2, col3 = st.columns(3)
    recoaccueil = df[df['genres'].str.contains("Documentary")].sort_values(by='averageRating', ascending=False).sample(6)

    with col1:
        for i, j in recoaccueil.iloc[0:2].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + j['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + j['tconst']
            regions = [x.strip("'")for x in j['region'].split(", ")]
            titres = [x.strip("'")for x in j['title'].split(", ")]
            if len(regions)<len(titres):
                regions += ['\\N']*(len(titres)-len(regions))
            elif len(regions)>len(titres):
                titres += ['']*(len(regions)-len(titres))
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {j['genre_unique']}\n"
                     f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {j['averageRating']}\n")
    with col2:
        for i, j in recoaccueil.iloc[2:4].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + j['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + j['tconst']
            regions = [x.strip("'")for x in j['region'].split(", ")]
            titres = [x.strip("'")for x in j['title'].split(", ")]
            if len(regions)<len(titres):
                regions += ['\\N']*(len(titres)-len(regions))
            elif len(regions)>len(titres):
                titres += ['']*(len(regions)-len(titres))
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {j['genre_unique']}\n"
                     f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {j['averageRating']}\n")
    with col3:
        for i, j in recoaccueil.iloc[4:6].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + j['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + j['tconst']
            regions = [x.strip("'")for x in j['region'].split(", ")]
            titres = [x.strip("'")for x in j['title'].split(", ")]
            if len(regions)<len(titres):
                regions += ['\\N']*(len(titres)-len(regions))
            elif len(regions)>len(titres):
                titres += ['']*(len(regions)-len(titres))
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {j['genre_unique']}\n"
                     f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {j['averageRating']}\n")


elif option == "Choix par acteur":
    # Deuxième page : choix par acteur
    st.markdown(
    """
    <h3 style="color: white; text-align: center;">Sur cette page vous allez accéder à une sélection de films en choisissant un acteur !</h3>
    """, unsafe_allow_html=True
    )

    st.write("\n\n")
    st.write('_____')

    acteur =  st.text_input("Entrez le nom d'un acteur:")

    col1, col2, col3 = st.columns(3)

    with col1:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)].sort_values(by='averageRating',ascending=False)
        for index, row in films_acteur.iloc[0:2].iterrows():
            acteurs_principaux = ", ".join(row['primaryName'].split(", ")[:3])
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + row['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + row['tconst']
            regions = [x.strip("'")for x in row['region'].split(", ")]
            titres = [x.strip("'")for x in row['title'].split(", ")]
            if len(regions)<len(titres):
                regions += ['\\N']*(len(titres)-len(regions))
            elif len(regions)>len(titres):
                titres += ['']*(len(regions)-len(titres))
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(row['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {row['genre_unique']}\n"
                     f"  - ⌛ Durée : {int(row['runtimeMinutes']//60)}h {int(row['runtimeMinutes']-((row['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {row['averageRating']}\n")

    with col2:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)].sort_values(by='averageRating', ascending=False)
        for index, row in films_acteur.iloc[2:4].iterrows():
            acteurs_principaux = ", ".join(row['primaryName'].split(", ")[:3])
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + row['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + row['tconst']
            regions = [x.strip("'")for x in row['region'].split(", ")]
            titres = [x.strip("'")for x in row['title'].split(", ")]
            if len(regions)<len(titres):
                regions += ['\\N']*(len(titres)-len(regions))
            elif len(regions)>len(titres):
                titres += ['']*(len(regions)-len(titres))
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(row['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {row['genre_unique']}\n"
                     f"  - ⌛ Durée : {int(row['runtimeMinutes']//60)}h {int(row['runtimeMinutes']-((row['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {row['averageRating']}\n")
    with col3:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)].sort_values(by='averageRating', ascending=False)
        for index, row in films_acteur.iloc[4:6].iterrows():
            acteurs_principaux = ", ".join(row['primaryName'].split(", ")[:3])
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + row['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + row['tconst']
            regions = [x.strip("'")for x in row['region'].split(", ")]
            titres = [x.strip("'")for x in row['title'].split(", ")]
            if len(regions)<len(titres):
                regions += ['\\N']*(len(titres)-len(regions))
            elif len(regions)>len(titres):
                titres += ['']*(len(regions)-len(titres))
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(row['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {row['genre_unique']}\n"
                     f"  - ⌛ Durée : {int(row['runtimeMinutes']//60)}h {int(row['runtimeMinutes']-((row['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {row['averageRating']}\n")
    
    st.write("\n\n")
    st.write('_____')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:
        st.write(' ')

    with col3:
        st.write(' ')



    st.write("\n\n")

        

else : 
    # Troisième page : choix par genre et par période

    st.markdown(
    """
    <h2 style="color: white; text-align: center;"> Hey ! Ici vous allez pouvoir choisir un genre et une période pour votre film ✨ </h2>
    """, unsafe_allow_html=True
    )

    st.write('_____')
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
        'Horreur': 9,
        'Mystère': 10,
        'Science-fiction': 11,
        'Animation': 12,
        'Documentaire': 13,
        'Western': 14,
        'Famille': 16,
        'Thriller': 17,
        'Guerre': 18,
        'Histoire': 20}

    startyear, endyear = st.select_slider("Choisissez une date de début et une date de fin pour la période de votre film",
                                            options=range(1930, 2025),
                                            value=(1930, 2024))
    #st.write("La période que vous avez choisie commence en", startyear, "et se termine en", endyear)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')


    with col2:
        X = df[['startYear','genre_facto']]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        model = NearestNeighbors(n_neighbors=3, metric="euclidean")
        model.fit(X_scaled)

        genre_selection = st.selectbox("Choisissez un genre :", list(genres.keys()))
        genre_facto = genres[genre_selection]
        recom_final = pd.DataFrame()

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

        st.write('_____')
        st.write(' ')
        st.markdown("<h3 style='color: orange; text-align: center;'>Top 3 des recommandations:</h3>", unsafe_allow_html=True)
        st.write("\n\n")


    with col3:
        st.write(' ')
    

    col1, col2, col3 = st.columns(3)
    with col1:
        if recom_final.empty:
            st.write(" ")
        else:
            for i, j in recom_final.iloc[0:1].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if len(regions)<len(titres):
                  regions += ['\\N']*(len(titres)-len(regions))
                elif len(regions)>len(titres):
                  titres += ['']*(len(regions)-len(titres))
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr=titres[indexfr].strip("['[\"").replace('"',"")
                else: titrefr=titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['Année'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['genre_unique']}\n"
                        f"  - ⌛ Durée : {int(j['Durée (minutes)']//60)}h {int(j['Durée (minutes)']-((j['Durée (minutes)']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['Note moyenne']}\n")
        st.write(' ')

    with col2:
        if recom_final.empty:
            st.write("Choisissez une période et un genre ! Si rien ne s'affiche après avoir appuyé sur le bouton 'Lancer la recherche', c'est qu'aucun film n'a été trouvé pour les crtières sélectionnés.")
        else:
            for i, j in recom_final.iloc[1:2].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if len(regions)<len(titres):
                  regions += ['\\N']*(len(titres)-len(regions))
                elif len(regions)>len(titres):
                  titres += ['']*(len(regions)-len(titres))
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr=titres[indexfr].strip("['[\"").replace('"',"")
                else: titrefr=titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['Année'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['genre_unique']}\n"
                        f"  - ⌛ Durée : {int(j['Durée (minutes)']//60)}h {int(j['Durée (minutes)']-((j['Durée (minutes)']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['Note moyenne']}\n")
        st.write(' ')

    with col3:
        if recom_final.empty:
            st.write(" ")
        else:
            for i, j in recom_final.iloc[2:3].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if len(regions)<len(titres):
                  regions += ['\\N']*(len(titres)-len(regions))
                elif len(regions)>len(titres):
                  titres += ['']*(len(regions)-len(titres))
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr=titres[indexfr].strip("['[\"").replace('"',"")
                else: titrefr=titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['Année'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['genre_unique']}\n"
                        f"  - ⌛ Durée : {int(j['Durée (minutes)']//60)}h {int(j['Durée (minutes)']-((j['Durée (minutes)']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['Note moyenne']}\n")
        st.write(' ')


    
    st.write("\n\n")
    st.write('_____')
