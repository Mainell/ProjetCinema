# Importation des bibliothèques nécessaires
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='auto', target='fr')

# Importation du dataset
df = pd.read_csv("df_avecgenretrad.csv")

# Ajout d'un fond sonore
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.audio("mediavision.mp3", format="audio/mpeg", autoplay = False)
with col3:
    st.write(' ')

# Ajout d'un fond d'écran
page_element="""<style>[data-testid="stAppViewContainer"]{background-image: url("https://lafibre.info/images/smileys/201004_Warm_lights_by_Max_Barners.jpg");
  background-size: cover;}</style>"""
st.markdown(page_element, unsafe_allow_html=True)

# Création d'un menu permettant d'accéder à la page d'accueil ou d'accéder à deux stratégies différentes de choix du film
option = st.sidebar.selectbox("Quelle page de notre application souhaiteriez-vous consulter ?", ["Accueil", "Choix par acteur", "Choix par genre et par période", "Sélection à partir d'un film"])
if option == "Accueil":
    # Première page: page d'accueil
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
        st.markdown("""<h3 style="color: white; text-align: center;">Voici une suggestion de documentaires...</h3>
        """, unsafe_allow_html=True)
        st.write(' ')

    with col2:
        st.image("logo.png")

    with col3:
        st.markdown("""<h3 style="color: white; text-align: center;">... en prévision des festivals du cinéma | 2025 </h3>
        """, unsafe_allow_html=True)
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
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {j['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(j['overview']) or len(j['overview'])>4998:
                    st.write("Aucun résumé disponible.")
                else: st.write(translator.translate(j['overview']))

    with col2:
        for i, j in recoaccueil.iloc[2:4].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + j['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + j['tconst']
            regions = [x.strip("'")for x in j['region'].split(", ")]
            titres = [x.strip("'")for x in j['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {j['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(j['overview']) or len(j['overview'])>4998:
                    st.write("Aucun résumé disponible.")
                else: st.write(translator.translate(j['overview']))

    with col3:
        for i, j in recoaccueil.iloc[4:6].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + j['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + j['tconst']
            regions = [x.strip("'")for x in j['region'].split(", ")]
            titres = [x.strip("'")for x in j['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {j['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(j['overview']) or len(j['overview'])>4998:
                    st.write("Aucun résumé disponible.")
                else: st.write(translator.translate(j['overview']))

# Deuxième page : choix par acteur
elif option == "Choix par acteur":
    st.markdown("""<h3 style="color: white; text-align: center;">Sur cette page vous allez accéder à une sélection de films en choisissant un acteur !</h3>
    """, unsafe_allow_html=True)
    st.write("\n\n")

    acteur =  st.text_input("Entrez le nom d'un acteur:")

    st.write('_____')
    st.markdown("""<h5 style="color: white; text-align: center;">En attendant votre choix, nous vous proposons les films les mieux notés de notre base de données.</h5>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)].sort_values(by='averageRating',ascending=False)
        for index, row in films_acteur.iloc[0:2].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + row['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + row['tconst']
            regions = [x.strip("'")for x in row['region'].split(", ")]
            titres = [x.strip("'")for x in row['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(row['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {row['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(row['runtimeMinutes']//60)}h {int(row['runtimeMinutes']-((row['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {row['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(row['overview']) or len(row['overview'])>4998:
                    st.write("Aucun résumé disponible.")
                else: st.write(translator.translate(row['overview']))

    with col2:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)].sort_values(by='averageRating', ascending=False)
        for index, row in films_acteur.iloc[2:4].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + row['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + row['tconst']
            regions = [x.strip("'")for x in row['region'].split(", ")]
            titres = [x.strip("'")for x in row['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(row['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {row['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(row['runtimeMinutes']//60)}h {int(row['runtimeMinutes']-((row['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {row['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(row['overview']) or len(row['overview'])>4998:
                    st.write("Aucun résumé disponible.")
                else: st.write(translator.translate(row['overview']))

    with col3:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)].sort_values(by='averageRating', ascending=False)
        for index, row in films_acteur.iloc[4:6].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + row['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + row['tconst']
            regions = [x.strip("'")for x in row['region'].split(", ")]
            titres = [x.strip("'")for x in row['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr=titres[indexfr].strip("['[\"").replace('"',"")
            else: titrefr=titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(row['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {row['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(row['runtimeMinutes']//60)}h {int(row['runtimeMinutes']-((row['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {row['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(row['overview']) or len(row['overview'])>4998:
                    st.write("Aucun résumé disponible.")
                else: st.write(translator.translate(row['overview']))

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

# Troisième page : choix par genre et par période
elif option == "Choix par genre et par période" :
    st.markdown("""<h2 style="color: white; text-align: center;"> Hey ! Ici vous allez pouvoir choisir un genre et une période pour votre film ✨ </h2>
    """, unsafe_allow_html=True)

    st.write('_____')
    st.write("\n\n")

    genres = {
        'Drame': 0,'Crime': 1,'Comédie': 2,'Action': 3,'Aventure': 4,
        'Biographie': 5,'Romance': 6,'Fantaisie': 7,'Horreur': 9,
        'Mystère': 10,'Science-fiction': 11,'Animation': 12,
        'Documentaire': 13,'Western': 14,'Famille': 16,'Thriller': 17,
        'Guerre': 18,'Histoire': 20}

    startyear, endyear = st.select_slider("Choisissez une date de début et une date de fin pour la période de votre film",
                                            options=range(1930, 2025),
                                            value=(1930, 2024))

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
            recom_final = recom_final.sort_values(["Distance", "averageRating"], ascending=[True, False])

        st.write(' ')
        st.markdown("<h3 style='color: orange; text-align: center;'>Top 6 des recommandations</h3>", unsafe_allow_html=True)
        st.write("\n\n")

    with col3:
        st.write(' ')

    col1, col2, col3 = st.columns(3)
    with col1:
        if recom_final.empty:
            st.write(" ")
        else:
            for i, j in recom_final.iloc[0:2].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr=titres[indexfr].strip("['[\"").replace('"',"")
                else: titrefr=titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                        f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                with st.expander("📜 Lire le résumé"):
                    if pd.isna(j['overview']) or len(j['overview'])>4998:
                        st.write("Aucun résumé disponible.")
                    else: st.write(translator.translate(j['overview']))
        st.write(' ')

    with col2:
        if recom_final.empty:
            st.markdown("<h5 style='color: white; text-align: center;'>Choisissez une période et un genre ci-dessus !</h5>", unsafe_allow_html=True)

        else:
            for i, j in recom_final.iloc[2:4].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr=titres[indexfr].strip("['[\"").replace('"',"")
                else: titrefr=titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                        f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                with st.expander("📜 Lire le résumé"):
                    if pd.isna(j['overview']) or len(j['overview'])>4998:
                        st.write("Aucun résumé disponible.")
                    else: st.write(translator.translate(j['overview']))

        st.write(' ')

    with col3:
        if recom_final.empty:
            st.write(" ")
        else:
            for i, j in recom_final.iloc[4:6].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr=titres[indexfr].strip("['[\"").replace('"',"")
                else: titrefr=titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                        f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                with st.expander("📜 Lire le résumé"):
                    if pd.isna(j['overview']) or len(j['overview'])>4998:
                        st.write("Aucun résumé disponible.")
                    else: st.write(translator.translate(j['overview']))

        st.write(' ')

    st.write("\n\n")
    st.write('_____')

# Quatrième page : sélection à partir d'un film
else :

    # Visuel avec liste déroulante
    with st.form("form 1"):
        st.subheader("Une sélection de trois films à partir d'un film apprécié")

        # Importation de nouvelles bibliothèques (vérifier utilité & supprimer doublons)
        import unicodedata
        import numpy as np
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.preprocessing import StandardScaler, RobustScaler
        from sklearn.model_selection import train_test_split

        # Vérifier si nécessaire d'importer à nouveau le dataframe
        #df = pd.read_csv("df_avecgenretrad.csv")

        # Normalisation des données numériques
        scaled_features = df.copy()
        colonnes_num = ['genre_facto']
        features = scaled_features[colonnes_num]
        scaler = RobustScaler().fit(features.values)
        features = scaler.transform(features.values)
        scaled_features[colonnes_num] = features

        # Choix des colonnes utilisées pour l'algorithme de KNN
        scaled_features = scaled_features[['primaryTitle', 'titre_fr', 'genre_facto', 'averageRating', 'numVotes']]

        # Variables X et y
        X_bis = scaled_features[['genre_facto', 'averageRating', 'numVotes']]
        y_bis = scaled_features['primaryTitle']

        # Sélection de 3 films pour le test
        knn = KNeighborsClassifier(n_neighbors=4, weights='distance')
        knn.fit(X_bis, y_bis)

        # Indices des films les plus proches récupérés
        distances, indices = knn.kneighbors(X_bis)

        df_liste_vf = df['titre_fr'].apply(lambda x:x.strip("['[\"")).tolist()
        df_liste_vo = df['primaryTitle'].apply(lambda x:x.strip("['[\"")).tolist()
        df_liste = df_liste_vf + df_liste_vo
        df_liste = list(set(df_liste))
        df_liste.insert(0, '')

        st.write('Quel film souhaiteriez-vous prendre comme référence ?')
        film_select = st.selectbox('', df_liste)

        film_select = scaled_features[np.where(scaled_features['primaryTitle'].str.contains(film_select,case=False), True,False)|
               np.where(scaled_features['titre_fr'].str.contains(film_select,case=False), True,False)]

        film_select_string = film_select.iloc[0,0]

        propositions = knn.kneighbors(scaled_features.loc[scaled_features['primaryTitle'] == film_select_string, ['genre_facto', 'averageRating', 'numVotes']])

        final_proposition = propositions[1][0]
        final_proposition = final_proposition.tolist()

        prop = df.iloc[final_proposition]

        # Ordre de l'agencement des colonnes dans le dataframe affiché
        prop = prop[['titre_fr', 'primaryTitle', 'startYear', 'runtimeMinutes','averageRating', 'genre_facto','poster_path', 'tconst', 'region', 'title','Genre_trad','overview']]
        # prop = prop[['titre_fr', 'primaryTitle', 'startYear', 'runtimeMinutes','averageRating', 'genre_facto']]
        prop = prop.iloc[1:4,:]

        if st.form_submit_button():
            st.write('Voici le top 3 des films recommandés à partir du film sélectionné: ')

        col1, col2, col3 = st.columns(3)
        with col1:

            for i, j in prop.iloc[0:1].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr=titres[indexfr].strip("['[\"").replace('"',"")
                else: titrefr=titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                        f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                with st.expander("📜 Lire le résumé"):
                    if pd.isna(j['overview']) or len(j['overview'])>4998:
                        st.write("Aucun résumé disponible.")
                    else: st.write(translator.translate(j['overview']))

        with col2:

            for i, j in prop.iloc[1:2].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr=titres[indexfr].strip("['[\"").replace('"',"")
                else: titrefr=titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                        f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                with st.expander("📜 Lire le résumé"):
                    if pd.isna(j['overview']) or len(j['overview'])>4998:
                        st.write("Aucun résumé disponible.")
                    else: st.write(translator.translate(j['overview']))

        with col3:

            for i, j in prop.iloc[2:3].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr=titres[indexfr].strip("['[\"").replace('"',"")
                else: titrefr=titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                        f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                with st.expander("📜 Lire le résumé"):
                    if pd.isna(j['overview']) or len(j['overview'])>4998:
                        st.write("Aucun résumé disponible.")
                    else: st.write(translator.translate(j['overview']))
